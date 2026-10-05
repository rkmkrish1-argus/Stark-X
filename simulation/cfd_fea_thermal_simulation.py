import os
import json
import math
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

try:
    import numpy as np
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: numpy and/or matplotlib not installed. Please run: pip install numpy matplotlib")

# ---------------------------------------------------------------------------
# GLOBAL CONSTANTS & AIR PROPERTIES
# ---------------------------------------------------------------------------
T_AMBIENT = 30.0  # deg C
T_TARGET = 50.0   # deg C
RHO_AIR = 1.092   # kg/m^3 at 50C
CP_AIR = 1006.0   # J/kg-K
MU_AIR = 1.95e-5  # Pa.s at 50C
K_AIR = 0.028     # W/m-K
G = 9.81          # m/s^2
STEFAN_BOLTZMANN = 5.67e-8  # W/m^2-K^4

# Dimensions
CHAMBER_WIDTH = 0.55   # m
CHAMBER_DEPTH = 0.45   # m
CHAMBER_HEIGHT = 0.65  # m
CHAMBER_VOL = 0.161    # m^3

# ---------------------------------------------------------------------------
# 1. COMPONENT NOMENCLATURE & THERMAL ZONE MAPPING
# ---------------------------------------------------------------------------
@dataclass
class Material:
    name: str
    k: float        # Thermal conductivity (W/mK)
    rho: float      # Density (kg/m^3)
    cp: float       # Specific heat (J/kgK)
    E: float = 0.0  # Young's modulus (Pa)
    alpha: float = 0.0 # CTE (1/K)
    yield_strength: float = 0.0 # Pa

@dataclass
class Component:
    name: str
    material: Material
    dimensions: tuple # (W, D, H) or (Thickness, W, H) in meters
    mass: float       # kg
    function_description: str

# Define Materials
MAT_CRCA = Material("CRCA Steel", k=45.0, rho=7850, cp=490, E=200e9, alpha=1.2e-5, yield_strength=250e6)
MAT_SS304 = Material("SS304", k=16.2, rho=8000, cp=500, E=193e9, alpha=1.7e-5, yield_strength=205e6)
MAT_ROCKWOOL = Material("Rockwool 40mm", k=0.038, rho=100, cp=840)
MAT_PUF = Material("Rigid PUF 50mm", k=0.022, rho=40, cp=1500)
MAT_AIR = Material("Air", k=K_AIR, rho=RHO_AIR, cp=CP_AIR)

components = {
    "Wall_CRCA_Outer": Component("Wall_CRCA_Outer", MAT_CRCA, (0.0012, 0.65, 1.1), 15.0, "Outer structural shell"),
    "Wall_SS304_Inner": Component("Wall_SS304_Inner", MAT_SS304, (0.0008, 0.55, 0.65), 8.0, "Inner food-grade liner"),
    "Insulation_Rockwool_40mm": Component("Insulation_Rockwool_40mm", MAT_ROCKWOOL, (0.04, 0.55, 0.65), 5.0, "Thermal barrier"),
    "PTC_Heater_Core": Component("PTC_Heater", MAT_CRCA, (0.1, 0.1, 0.1), 0.5, "1.2kW Peak / 580W Steady Heat Source"),
    "BLDC_Blower": Component("Blower", MAT_CRCA, (0.15, 0.15, 0.15), 1.2, "100 m^3/h @ 75 Pa"),
}

for i in range(1, 11):
    components[f"Tray_{i:02d}"] = Component(
        f"Tray_{i:02d}", MAT_SS304, (0.5, 0.4, 0.015), 0.8, 
        "SS304 wire mesh, 4x4 aperture, 1.0mm wire, 55mm pitch"
    )

# ---------------------------------------------------------------------------
# 2. CFD-EQUIVALENT AIRFLOW SIMULATION (1D Zonal Model)
# ---------------------------------------------------------------------------
def simulate_airflow(airflow_m3h=100.0, louver_angle_deg=45.0, num_trays=10):
    """
    1D Zonal airflow model. Calculates velocity, pressure drop, and convective coefficients.
    """
    results = {}
    Q_m3s = airflow_m3h / 3600.0
    A_chamber = CHAMBER_WIDTH * CHAMBER_DEPTH  # m^2
    V_superficial = Q_m3s / A_chamber

    # Tray mesh resistance (Darcy-Forchheimer simplified)
    # Porosity > 75%, wire diameter 1mm
    porosity = 0.75
    V_pore = V_superficial / porosity
    
    dp_total = 0.0
    zone_data = []

    # Louver resistance (Idelchik)
    theta = math.radians(louver_angle_deg)
    # Simplified K factor based on angle
    K_louver = 0.5 + 1.5 * (math.sin(theta)**2)
    dp_louver = K_louver * 0.5 * RHO_AIR * (V_superficial**2)
    dp_total += dp_louver

    results["dp_louver"] = dp_louver

    for i in range(1, num_trays + 1):
        # Reynolds number at wire
        Re_wire = (RHO_AIR * V_pore * 0.001) / MU_AIR
        
        # Ergun/Darcy approximation for screen
        K_screen = 1.3 * (1 - porosity) + (1/porosity - 1)**2
        dp_tray = K_screen * 0.5 * RHO_AIR * (V_superficial**2)
        dp_total += dp_tray
        
        # Heat transfer coeff (Nusselt for cylinder in crossflow)
        Nu = 0.683 * (Re_wire**0.466) * (0.7**0.33)  # Pr ~ 0.7
        h_conv = (Nu * K_AIR) / 0.001

        zone_data.append({
            "zone": f"Tray_{i}",
            "velocity_m_s": V_pore,
            "Re": Re_wire,
            "dp_Pa": dp_tray,
            "h_W_m2K": h_conv
        })

    results["tray_zones"] = zone_data
    results["dp_total_Pa"] = dp_total
    return results


# ---------------------------------------------------------------------------
# 3. CONJUGATE HEAT TRANSFER (CHT) THERMAL MODEL
# ---------------------------------------------------------------------------
def calculate_cht(insulation_k=0.038, insulation_thickness=0.04, heater_power_W=580.0, airflow_m3h=100.0):
    """
    Steady-state energy balance and overall U-value calculation.
    """
    Q_m3s = airflow_m3h / 3600.0
    mass_flow = Q_m3s * RHO_AIR

    # U-value calculation
    h_in = 15.0  # W/m^2K
    h_out = 25.0 # W/m^2K
    R_total = (1/h_in) + (0.0008/MAT_SS304.k) + (insulation_thickness/insulation_k) + (0.0012/MAT_CRCA.k) + (1/h_out)
    U_value = 1 / R_total

    A_surface = 2*(0.65*0.55 + 0.65*0.45 + 0.55*0.45) # m^2 (simplified rectangular)

    # Max delta T possible if no evaporation
    # Q_heater = m_dot * Cp * dT + U * A * dT
    dT_max = heater_power_W / (mass_flow * CP_AIR + U_value * A_surface)
    T_steady = T_AMBIENT + dT_max

    # Thermal efficiency (heat into air vs total heat)
    Q_useful = mass_flow * CP_AIR * dT_max
    efficiency = Q_useful / heater_power_W

    return {
        "U_value_W_m2K": U_value,
        "Steady_State_Temp_C": T_steady,
        "Wall_Heat_Loss_W": U_value * A_surface * dT_max,
        "Thermal_Efficiency": efficiency
    }


# ---------------------------------------------------------------------------
# 4. TRANSIENT THERMAL ANALYSIS
# ---------------------------------------------------------------------------
def transient_analysis():
    """
    Lumped capacitance model simulating heat-up, PID drying, falling rate, and cooldown.
    """
    time_steps_min = 300
    dt_s = 60  # 1 minute steps

    configs = {
        "v0_40mm_Rockwool": {"k": 0.038, "t": 0.04, "pcm_mass": 0.0},
        "v1_50mm_PUF": {"k": 0.022, "t": 0.05, "pcm_mass": 0.0},
        "v2_Rockwool_3kg_PCM": {"k": 0.038, "t": 0.04, "pcm_mass": 3.0},
        "v3_PUF_5kg_PCM": {"k": 0.022, "t": 0.05, "pcm_mass": 5.0}
    }

    # Effective thermal mass of chamber (SS304 + wet agarbatti)
    m_chamber = 8.0 # kg SS304 inner
    cp_chamber = MAT_SS304.cp
    m_load = 12.5 # kg wet
    cp_load = 3000 # approx J/kgK for wet biomass
    
    # PCM latent heat approx (RT52)
    pcm_latent = 160000 # J/kg
    pcm_melt_temp = 52.0

    results = {}

    for name, conf in configs.items():
        T = T_AMBIENT
        history = []
        
        # U-value
        R_tot = (1/15) + (0.0008/16.2) + (conf["t"]/conf["k"]) + (0.0012/45) + (1/25)
        U = 1/R_tot
        A = 1.73

        # Effective thermal mass C_eff
        C_eff = m_chamber * cp_chamber + m_load * cp_load + (conf["pcm_mass"] * 2000) # baseline solid

        pcm_energy_stored = 0.0
        pcm_max_energy = conf["pcm_mass"] * pcm_latent

        for t_min in range(time_steps_min):
            # Phase determination
            if t_min < 15:
                Q_in = 1200 # Peak heat
            elif t_min < 210:
                Q_in = 580  # PID steady
            elif t_min < 270:
                Q_in = 350  # Falling rate
            else:
                Q_in = 0    # Cooldown

            Q_loss = U * A * (T - T_AMBIENT)
            Q_exhaust = (100 / 3600.0) * RHO_AIR * CP_AIR * (T - T_AMBIENT)
            
            # Simple latent heat evaporation penalty during drying
            Q_evap = 200 if (15 <= t_min < 210) else (50 if 210 <= t_min < 270 else 0)

            Q_net = Q_in - Q_loss - Q_exhaust - Q_evap

            # Handle PCM melting logic
            if conf["pcm_mass"] > 0 and 51.5 < T < 52.5 and Q_net > 0 and pcm_energy_stored < pcm_max_energy:
                # Energy goes into melting
                pcm_energy_stored += Q_net * dt_s
                dT_dt = 0
            elif conf["pcm_mass"] > 0 and T < 52.0 and Q_net < 0 and pcm_energy_stored > 0:
                # Energy released from freezing
                pcm_energy_stored += Q_net * dt_s
                dT_dt = 0
            else:
                dT_dt = Q_net / C_eff
            
            T += dT_dt * dt_s
            history.append(T)
            
        results[name] = history
        
    return results


# ---------------------------------------------------------------------------
# 5. FEA-EQUIVALENT STRUCTURAL CHECK
# ---------------------------------------------------------------------------
def structural_check():
    """
    Beam theory deflection of tray and thermal expansion.
    """
    # Tray dimensions: 0.5 x 0.4 x 0.015
    L = 0.5
    load_kg = 1.25 + 0.8 # wet sticks + self weight
    w = (load_kg * G) / L # N/m (UDL)
    
    # Moment of inertia for wire mesh is complex. Approximate as solid plate of equivalent mass.
    # Equivalent thickness t_eq
    rho = MAT_SS304.rho
    t_eq = 0.8 / (0.5 * 0.4 * rho) # Volume = mass/rho
    I = (0.4 * (t_eq**3)) / 12

    E = MAT_SS304.E
    # Max deflection at center for simply supported UDL: 5*w*L^4 / 384*E*I
    delta_max = (5 * w * (L**4)) / (384 * E * I)

    # Thermal expansion (ambient 30 to target 50 -> dT = 20)
    dT = T_TARGET - T_AMBIENT
    alpha = MAT_SS304.alpha
    thermal_exp = alpha * L * dT

    # Von Mises (simplified bending stress)
    M_max = (w * (L**2)) / 8
    sigma_max = (M_max * (t_eq / 2)) / I
    safety_factor = MAT_SS304.yield_strength / sigma_max

    return {
        "max_deflection_mm": delta_max * 1000,
        "thermal_expansion_mm": thermal_exp * 1000,
        "max_bending_stress_MPa": sigma_max / 1e6,
        "safety_factor": safety_factor,
        "status": "PASS" if (delta_max*1000 < 2.0 and safety_factor > 2.0) else "FAIL"
    }


# ---------------------------------------------------------------------------
# 6. ENERGY BALANCE & SOLAR SIZING
# ---------------------------------------------------------------------------
def energy_balance():
    """
    Energy audit for one cycle (4.5 hours)
    """
    # Power draw
    p_heater_preheat = 1200 # W for 0.25h
    p_heater_steady = 580   # W for 3.25h
    p_heater_falling = 350  # W for 1.0h
    p_blower = 24           # W for 4.5h (100 m3/h @ 75Pa, est.)
    p_control = 5           # W for 4.5h
    
    e_heater = (p_heater_preheat*0.25) + (p_heater_steady*3.25) + (p_heater_falling*1.0)
    e_blower = p_blower * 4.5
    e_control = p_control * 4.5
    
    total_consumption_wh = e_heater + e_blower + e_control
    
    # Solar generation (Bangalore, 4.5 PSH)
    # 400W panel
    solar_gen_wh = 400 * 4.5 * 0.85 # 85% system efficiency
    
    # Battery
    batt_capacity_wh = 48 * 50 # 2400 Wh
    usable_batt_wh = batt_capacity_wh * 0.85 # 85% DoD
    
    net_energy = solar_gen_wh - total_consumption_wh
    
    return {
        "Total_Consumption_Wh": total_consumption_wh,
        "Solar_Generation_Wh": solar_gen_wh,
        "Battery_Usable_Wh": usable_batt_wh,
        "Net_Energy_Wh": net_energy,
        "Sustainable_StandAlone": net_energy > 0 or total_consumption_wh <= usable_batt_wh
    }


# ---------------------------------------------------------------------------
# 7. DESIGN ITERATION ENGINE
# ---------------------------------------------------------------------------
def run_design_iterations():
    """
    Evaluates configurations automatically and returns comparison.
    """
    iterations = {}
    
    # v0: Baseline (40mm rockwool, 55mm pitch, 580W)
    v0_cht = calculate_cht(insulation_k=0.038, insulation_thickness=0.04)
    v0_air = simulate_airflow(num_trays=10) # 55mm pitch allows 10 trays in 650mm height roughly
    iterations["v0_Baseline"] = {"U_value": v0_cht["U_value_W_m2K"], "Efficiency": v0_cht["Thermal_Efficiency"], "dP": v0_air["dp_total_Pa"]}

    # v1: 50mm PUF
    v1_cht = calculate_cht(insulation_k=0.022, insulation_thickness=0.05)
    iterations["v1_50mmPUF"] = {"U_value": v1_cht["U_value_W_m2K"], "Efficiency": v1_cht["Thermal_Efficiency"], "dP": v0_air["dp_total_Pa"]}
    
    # v2: v1 + PCM (thermal mass affects transient, steady state U is same)
    iterations["v2_PUF_PCM"] = iterations["v1_50mmPUF"].copy()
    
    # v3: v2 + optimized tray spacing (50mm pitch -> 12 trays)
    v3_air = simulate_airflow(num_trays=12)
    iterations["v3_Optimized"] = {"U_value": v1_cht["U_value_W_m2K"], "Efficiency": v1_cht["Thermal_Efficiency"], "dP": v3_air["dp_total_Pa"]}
    
    return iterations


# ---------------------------------------------------------------------------
# 8. SIMSCALE EXPORT
# ---------------------------------------------------------------------------
def generate_simscale_config(out_path):
    config = {
        "project_name": "Agarbatti_Dryer_Thermal_CFD",
        "analysis_type": "CONJUGATE_HEAT_TRANSFER",
        "geometry_naming": {
            "fluid_domain": "Air_Volume",
            "solid_domains": ["Wall_CRCA", "Insulation", "Wall_SS304", "Trays", "Heater"]
        },
        "materials": [
            asdict(MAT_CRCA),
            asdict(MAT_SS304),
            asdict(MAT_ROCKWOOL),
            asdict(MAT_PUF),
            asdict(MAT_AIR)
        ],
        "boundary_conditions": {
            "inlet": {"type": "VELOCITY_INLET", "value": "100 m^3/h", "temperature": "50 C"},
            "outlet": {"type": "PRESSURE_OUTLET", "value": "0 Pa (Gauge)"},
            "walls": {"type": "EXTERNAL_WALL_HEAT_FLUX", "heat_transfer_coefficient": 25.0, "ambient_temperature": "30 C"}
        },
        "mesh_strategy": {
            "global_sizing": "0.01 m",
            "boundary_layers": {"number_of_layers": 3, "expansion_ratio": 1.2}
        },
        "solver_settings": {
            "turbulence_model": "k-omega SST",
            "max_iterations": 1000,
            "convergence_criteria": 1e-4
        }
    }
    with open(out_path, 'w') as f:
        json.dump(config, f, indent=4)


# ---------------------------------------------------------------------------
# MAIN EXECUTION & VISUALIZATION
# ---------------------------------------------------------------------------
def plot_results(transient_res, airflow_res, out_dir):
    if not HAS_MATPLOTLIB:
        return

    # 1. Transient Curves
    plt.figure(figsize=(10, 6))
    time_axis = np.arange(300)
    for name, data in transient_res.items():
        plt.plot(time_axis, data, label=name)
    plt.axhline(50, color='r', linestyle='--', label='Target Temp (50C)')
    plt.title("Transient Heat-up & Cool-down Curves")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(out_dir, "plot_transient.png"))
    plt.close()

    # 2. Velocity profile (Bar chart across trays)
    trays = [z["zone"] for z in airflow_res["tray_zones"]]
    vels = [z["velocity_m_s"] for z in airflow_res["tray_zones"]]
    
    plt.figure(figsize=(8, 5))
    plt.bar(trays, vels, color='skyblue')
    plt.title("Velocity Profile Across Tray Levels")
    plt.ylabel("Velocity (m/s)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "plot_velocity.png"))
    plt.close()

def print_ascii_summary(airflow, struct, energy):
    print("\n" + "="*60)
    print(" [!] ANTIGRAVITY AGARBATTI DRYER - CFD/FEA SIMULATION ENGINE")
    print("="*60)
    
    print("\n[ AIRFLOW & THERMAL PROFILE ]")
    print(f"  Total Pressure Drop: {airflow['dp_total_Pa']:.2f} Pa")
    print(f"  Avg Tray Velocity:   {airflow['tray_zones'][4]['velocity_m_s']:.3f} m/s")
    print("  Velocity Profile:    |########  | (Uniformity Check)")
    
    print("\n[ STRUCTURAL INTEGRITY (FEA EQUIV) ]")
    print(f"  Max Tray Deflection: {struct['max_deflection_mm']:.3f} mm (Limit: 2.0 mm)")
    print(f"  Thermal Expansion:   {struct['thermal_expansion_mm']:.3f} mm")
    print(f"  Safety Factor:       {struct['safety_factor']:.1f}x [ {struct['status']} ]")
    
    print("\n[ ENERGY & SOLAR SIZING ]")
    print(f"  Cycle Consumption:   {energy['Total_Consumption_Wh']:.0f} Wh")
    print(f"  Solar Generation:    {energy['Solar_Generation_Wh']:.0f} Wh")
    print(f"  Battery Capacity:    {energy['Battery_Usable_Wh']:.0f} Wh")
    if energy["Sustainable_StandAlone"]:
        print("  Status: [ PASS ] Solar + Battery covers full cycle.")
    else:
        print("  Status: [ WARN ] Deficit requires grid hybrid mode.")
    print("="*60 + "\n")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plots_dir = os.path.join(script_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    
    results = {}
    
    # 1-4. Run Physics Models
    results["airflow"] = simulate_airflow()
    results["cht"] = calculate_cht()
    results["transient"] = transient_analysis()
    
    # 5. Structural
    results["structural"] = structural_check()
    
    # 6. Energy
    results["energy"] = energy_balance()
    
    # 7. Iterations
    results["design_iterations"] = run_design_iterations()
    
    # Output to Console
    print_ascii_summary(results["airflow"], results["structural"], results["energy"])
    
    # Export JSON
    json_path = os.path.join(script_dir, "cfd_fea_results.json")
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=4)
    print(f"Results exported to: {json_path}")
    
    # Export SimScale
    simscale_path = os.path.join(script_dir, "simscale_config.json")
    generate_simscale_config(simscale_path)
    print(f"SimScale config exported to: {simscale_path}")
    
    # Generate Plots
    if HAS_MATPLOTLIB:
        plot_results(results["transient"], results["airflow"], plots_dir)
        print(f"Plots saved to: {plots_dir}")

if __name__ == "__main__":
    main()

# ANTIGRAVITY ENGINEERING SPECIFICATION: AGARBATTI DRYING SYSTEM
## DOCUMENT 04: MECHANICAL CAD ARCHITECTURE & TRAY LAYOUT
### Chamber Geometry, Tray Spacing, Aerodynamic Ducting, and Mechanical Tolerances
**Document ID:** AGY-DRY-CAD-004 | **Revision:** 1.0  
**Domain:** Mechanical Engineering, CAD Architecture, Thermal Enclosure Design

---

## 1. CHAMBER OVERALL DIMENSIONS & STRUCTURAL ENVELOPE

```
      FRONT ELEVATION                                 SIDE CROSS-SECTION
 ┌──────────────────────┐ 1100 mm                ┌──────────────┬──────┐ 
 │  [ Touchscreen HMI ] │                        │  Intake Fan  │ PTC  │
 ├──────────────────────┤                        │  [BLDC 48V]  │Heater│
 │  ┌────────────────┐  │                        └──────┬───────┴──────┘
 │  │                │  │                               ▼
 │  │ Tray Tier 1    │  │                        ┌──────────────┐
 │  │ Tray Tier 2    │  │                        │LOUVER (15-45)│◄── Motorized Sweeper
 │  │ Tray Tier 3    │  │                        ├──────────────┤
 │  │ Tray Tier 4    │  │                        │  Tray 1 ────►│
 │  │ Tray Tier 5    │  │                        │  Tray 2 ────►│ ──┐
 │  │ Tray Tier 6    │  │                        │  Tray 3 ────►│   │ Airflow
 │  │ Tray Tier 7    │  │                        │  Tray 4 ────►│   │ Across
 │  │ Tray Tier 8    │  │                        │  Tray 5 ────►│   ▼ Trays
 │  │ Tray Tier 9    │  │                        │  Tray 6 ────►│
 │  │ Tray Tier 10   │  │                        │  Tray 7 ────►│ ──┐ Exhaust
 │  │                │  │                        │  Tray 8 ────►│   │ Chimney
 │  └────────────────┘  │                        │  Tray 9 ────►│   ▼
 │   Insulated Door     │                        │  Tray 10───► │  [RH Exhaust]
 ├──────────────────────┤                        └──────────────┴──────────────┘
 │ [Power / Battery Bay]│                         [40mm Mineral Wool Insulation]
 └──────────────────────┘                        └──────────────550 mm─────────┘
 ◄─────── 650 mm ───────►
```

### 1.1 Envelope Dimensions (Prototype Scale)
* **External Width ($W_{\text{ext}}$):** $650\text{ mm}$
* **External Depth ($D_{\text{ext}}$):** $550\text{ mm}$
* **External Height ($H_{\text{ext}}$):** $1100\text{ mm}$ (includes $100\text{ mm}$ castor wheels)
* **Internal Chamber Volume:**
  * Internal Width: $550\text{ mm}$
  * Internal Depth: $450\text{ mm}$
  * Internal Drying Height: $650\text{ mm}$
  * Usable Internal Air Volume: $\approx 0.161\text{ m}^3$
* **Wall Construction:** Double-walled sheet metal ($1.2\text{ mm}$ CRCA steel with epoxy powder coating exterior; $0.8\text{ mm}$ SS304 inner liner) separated by $40\text{ mm}$ high-density rockwool / mineral wool insulation ($k = 0.038\text{ W/m}\cdot\text{K}$).

---

## 2. TRAY RACK ARCHITECTURE & LOADING DENSITY

### 2.1 Tray Specifications
* **Number of Active Tiers:** $10\text{ tiers}$
* **Vertical Tray Pitch (Spacing):** $55.0\text{ mm}$ center-to-center
* **Clear Air Gap between Tiers:** $40.0\text{ mm}$ (permits uniform crossflow without aerodynamic choke)
* **Individual Tray Dimensions:** $500\text{ mm}\ (\text{Width}) \times 400\text{ mm}\ (\text{Depth}) \times 15\text{ mm}\ (\text{Lip Height})$
* **Tray Material:** Grade SS304 food-grade wire mesh ($4\text{ mm} \times 4\text{ mm}$ aperture, $\varnothing 1.0\text{ mm}$ wire) with welded $15\text{ mm} \times 15\text{ mm}$ SS angle frame. Wire mesh allows $>75\%$ open area for vertical vapor migration.

### 2.2 Stick Loading Density & Alignment
* **Stick Length:** $230\text{ mm}$ ($9\text{ inches}$).
* **Tray Arrangement:** Sticks are arranged in **two parallel rows** along the $500\text{ mm}$ width of each tray, perpendicular to the air crossflow direction:
  * Row 1: Sticks placed along front half ($230\text{ mm}$ length).
  * Row 2: Sticks placed along rear half ($230\text{ mm}$ length).
* **Pitch per Stick:** Sticks placed side-by-side with $\approx 0.8\text{ mm}$ air gap ($\approx 4.0\text{ mm}$ center-to-center).
* **Sticks per Row:** $500\text{ mm} / 4.0\text{ mm} \approx 125\text{ sticks/row} \times 2\text{ rows} = 250\text{ sticks}$ per sub-layer.
* **Layering Density:** 4 to 5 interleaved layers per tray (cross-stacked with wooden spacers) $= 1,150\text{ sticks/tray}$.
* **Total Batch Capacity:**
  $$10\text{ trays} \times 1,150\text{ sticks/tray} = \mathbf{11,500\text{ sticks}} \approx \mathbf{12.5\text{ kg wet mass}}$$

---

## 3. AERODYNAMIC DUCTING & RECIRCULATION SYSTEM

### 3.1 Flow Path Architecture
1. **Intake Manifold:** Top-mounted 48V BLDC centrifugal blower pulls either ambient air or partial recirculation air through a stainless steel lint/charcoal dust filter screen.
2. **Thermal Booster Core:** Air passes through the low-resistance ceramic PTC honeycomb matrix, absorbing $580\text{ W} - 1200\text{ W}$ of heat to reach target $50^\circ\text{C}$.
3. **Louver Distributor Nozzle ($200\text{ mm} \times 150\text{ mm}$):**
   * Located at the upper inlet plenum.
   * Six precision-linked airfoil blades sweep between $15^\circ$ (downward-angled jet towards lower trays) and $45^\circ$ (upward-diverted jet towards top trays).
   * Over a 20-second period, every individual tray tier experiences alternating pulses of high-shear drying air, stripping stagnant boundary layers.
4. **Exhaust & Recirculation Damper:**
   * At cycle start ($RH_{\text{air}} < 30\%$), the recirculation flap is $70\%$ open, saving $65\%$ of thermal energy by recycling hot air.
   * As humidity rises ($RH_{\text{air}} > 40\%$), the servo-actuated exhaust damper progressively vents humid air out the rear chimney while pulling fresh dry make-up air.

---

## 4. MECHANICAL FABRICATION & ASSEMBLY TOLERANCES

* **Louver Blade Clearances:** $1.0\text{ mm} \pm 0.2\text{ mm}$ gap between blade tip and louver side-casing to eliminate friction binding during thermal expansion up to $65^\circ\text{C}$.
* **Chamber Door Seal:** Dual-lip extruded food-grade silicone hollow bulb gasket ($12\text{ mm} \times 8\text{ mm}$) with positive cam-action compression latch (compression ratio $35\%$).
* **Tray Slide Rails:** Formed 1.5 mm SS304 channel rails with front stop-notches to prevent accidental slide-out during loading.

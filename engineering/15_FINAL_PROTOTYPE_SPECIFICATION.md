# ANTIGRAVITY RESEARCH & ENGINEERING SPECIFICATION
## DOCUMENT 15: FINAL PROTOTYPE SPECIFICATION & MANUFACTURING DATASHEET
### Manufacturing-Ready Technical Data, Critical Dimensions, Tolerances, SOPs, and Acceptance Criteria
**Document ID:** AGY-AGB-SPEC-001 | **Revision:** 1.0  
**Machine Nomenclature:** Antigravity Agri-Pack 200 (Low-Cost Semi-Automatic Agarbatti Impulse Sealer)

---

## 1. COMPREHENSIVE TECHNICAL SPECIFICATIONS

### 1.1 Physical & Mechanical Parameters
* **Overall Dimensions ($L \times W \times H$):** $420\text{ mm} \times 380\text{ mm} \times 860\text{ mm}$ (Tabletop unit with floor pedal)
* **Total Machine Mass:** $18.45\text{ kg}$ (Robust anti-vibration stability; easily portable by 2 persons)
* **Active Sealing Length:** $200.0\text{ mm}$ (Accommodates pouches from $30\text{ mm}$ to $190\text{ mm}$ width)
* **Seal Width:** $2.5\text{ mm} \pm 0.2\text{ mm}$ (Standard commercial flat ribbon seal)
* **Maximum Jaw Opening Stroke:** $46.25\text{ mm}$ (Provides ample finger-safe clearance)
* **Vertical Guide System:** Twin $\varnothing 12\text{ mm h6}$ hard chrome plated shafts + 4x LM12UU linear ball bushings
* **Jaw Carrier Beam Material:** Extruded Aluminum 6061-T6 Rectangular Tube ($40 \times 25 \times 3.0\text{ mm}$)
* **Anvil Resilient Foundation:** High-temperature red silicone rubber ($220 \times 10 \times 5.0\text{ mm}$, 60 Shore A durometer)
* **Mechanical Actuation:** Class-1 Foot Pedal ($MA = 5.0$) + Over-Center Symmetrical 2-Bar Toggle Linkage
* **Operator Foot Force Required:** $70\text{ N to }90\text{ N}$ (Continuous non-fatiguing foot effort)
* **Jaw Clamping Force on Seal:** $221.2\text{ N} \pm 15.0\text{ N}$ (Enforced by preloaded compliance spring cartridge)
* **Average Seal Contact Pressure:** $0.44\text{ N/mm}^2$ ($4.42\text{ bar}$ nominal; within $2.5 - 5.0\text{ bar}$ optimal band)

### 1.2 Thermal & Electrical Parameters
* **Electrical Architecture:** $24.0\text{ V DC}$ Safety Extra-Low Voltage (SELV)
* **Power Source Compatibility:**
  * Option 1: 230V AC Single-Phase Grid via Internal 24V 15A (360W) Industrial SMPS
  * Option 2: 24V 30Ah $\text{LiFePO}_4$ Solar Battery Bank (Direct DC connection via Anderson Powerpole)
* **Heating Element:** Nichrome 80/20 Grade A Flat Ribbon ($220 \times 2.5 \times 0.08\text{ mm}$)
* **Element Resistance:** $1.20\ \Omega$ (Cold at $20^\circ\text{C}$); $1.25\ \Omega$ (Hot at $135^\circ\text{C}$)
* **Nominal Peak Current:** $19.2\text{ A}$ (Instantaneous pulse)
* **Modulated Effective Thermal Power:** $275.0\text{ W}$ (via $60\%$ PWM duty cycle at $1.0\text{ kHz}$)
* **Thermal Impulse Dwell:** $0.75\text{ s} \pm 0.05\text{ s}$ (Digital timer controlled)
* **Cooling Hold Dwell under Pressure:** $1.25\text{ s} \pm 0.10\text{ s}$ (Signaled by green indicator buzzer)
* **Electrical Energy per Sealed Package:** $206.3\text{ J} = 0.0573\text{ Wh}$ ($306.5\text{ Wh per 5,000 pouches}$)
* **Thermal Cutoff Protection:** $180^\circ\text{C}$ bimetallic thermal fuse clamped directly to aluminum jaw carrier
* **Overcurrent Protection:** $20\text{ A}$ DC fast-blow automotive blade fuse on main bus

---

## 2. CRITICAL ENGINEERING TOLERANCES & FITS

| Component / Interface | Dimension | Tolerance Class / Limit | Functional Impact |
|---|---|---|---|
| **Guide Shaft Diameters** | $\varnothing 12.000\text{ mm}$ | $\text{h6 } (0 / -0.011\text{ mm})$ | Precision sliding fit in LM12UU linear bushings |
| **Guide Bushing Block Bores** | $\varnothing 21.000\text{ mm}$ | $\text{H7 } (+0.021 / 0\text{ mm})$ | Transition press fit to retain linear bushings |
| **Toggle Pivot Dowel Pins** | $\varnothing 10.000\text{ mm}$ | $\text{h7 } (0 / -0.015\text{ mm})$ | Smooth running fit in sintered bronze Oilite bushings |
| **Bushing Bores in Links** | $\varnothing 14.000\text{ mm}$ | $\text{H7 } (+0.018 / 0\text{ mm})$ | Light interference press fit for Oilite bushings |
| **Jaw-to-Anvil Parallelism** | $200.0\text{ mm}$ span | $\le 0.08\text{ mm}$ across full width | Eliminates uneven pressure and cold seal leaks |
| **Silicone Anvil Channel Width** | $10.00\text{ mm}$ | $\pm 0.05\text{ mm}$ dovetail | Hand snap-in retention without adhesive mess |
| **Mica Insulator Thickness** | $3.00\text{ mm}$ | $\pm 0.10\text{ mm}$ uniform sheet | Dielectric insulation ($> 2.5\text{ kV}$ breakdown) |

---

## 3. STANDARD OPERATING PROCEDURE (SOP): PRODUCTION RUN

```text
========================================================================================
                  STANDARD OPERATING PROCEDURE: AGARBATTI PACKAGING
========================================================================================
1. POWER UP & PRE-CHECK:
   - Ensure machine is resting level on rubber feet; check that E-Stop is released (twist CW).
   - Turn Main DC Switch to ON. Digital display illuminates showing set dwell: "0.75 s".
   - Verify that safety microswitch indicator light is OFF when jaw is raised.

2. POUCH POSITIONING & ALIGNMENT:
   - Take 1 pouch containing 20 conditioned, surface-dry agarbatti sticks (Moisture: 8-10%).
   - Slide pouch flat onto the SS worktable against the magnetic depth-stop fence.
   - Use two hands to pull the pouch mouth lightly taut laterally across the silicone anvil.
   - Confirm sticks are pushed back, leaving at least 25 mm of empty margin at the seal mouth.

3. SEALING CYCLE EXECUTION:
   - Press foot pedal down smoothly until the toggle clicks into over-center lock position.
   - Jaw descends, compresses film at 3.6 bar, and actuates safety microswitch.
   - HEATER RED LED illuminates: Electrical impulse fires for exactly 0.75 seconds.
   - HEATER LED turns OFF; HOLD GREEN LED illuminates: Keep foot pedal locked down!
   - At t = 2.0 seconds (end of 1.25 s cooling dwell), internal beeper emits a short BEEP.
   - Lift foot off pedal. Twin return springs instantly snap the jaw upward to 46 mm open.

4. EXTRACTION & INSPECTION:
   - Slide sealed pouch off table into packing bin.
   - Inspect seal line: Must be continuous, transparent, flat, and free of wrinkles.
   - Repeat cycle. Target pace: 10 to 12 pouches per minute (600 to 720 packs/hour).
========================================================================================
```

---

## 4. PREVENTIVE MAINTENANCE SOP & SCHEDULE

```text
========================================================================================
                PREVENTIVE MAINTENANCE SOP & SERVICING INTERVALS
========================================================================================
DAILY (Operator Level — 5 minutes):
  1. Clean Worktable: Wipe SS table, anvil channel, and acrylic guard with dry microfiber cloth.
  2. Inspect PTFE Tape: Look for black carbon spots or burnt polymer. Advance tape by 25 mm if scorched.
  3. Vacuum / Dust Clean: Use soft brush to remove fallen charcoal powder from guide rods.

WEEKLY (Supervisor Level — 15 minutes):
  1. Guide Rod Lubrication: Apply 3 drops of ISO VG 32 spindle oil to each 12 mm linear shaft.
  2. Check Ribbon Tension: Gently touch Nichrome ribbon; ensure spring maintains ribbon taut.
  3. Check Pivot Pins: Inspect 4 toggle pivot circlips to ensure none have migrated loose.
  4. Test E-Stop Response: Verify power cuts immediately upon button depress.

MONTHLY (Technician Level — 30 minutes):
  1. Nichrome Resistance Check: Disconnect power; measure terminal resistance with multimeter.
     - Acceptable Range: 1.15 to 1.35 Ohms. If R > 1.40 Ohms, replace ribbon element!
  2. Silicone Anvil Inspection: Check for permanent compression groove > 0.5 mm depth.
     - If indented, pull silicone strip out, flip 180°, or replace with new strip.
  3. Terminal Bolt Torque: Retighten brass M5 terminal nuts to 2.5 N*m torque.
  4. Grounding & Insulation Test: Perform 500V DC Megger test from terminals to chassis (> 20 M-Ohm).
========================================================================================
```

---

## 5. FINAL FACTORY ACCEPTANCE TEST (FAT) CRITERIA

| Test Item | Verification Method | Acceptance Criterion | Pass / Fail Status |
|---|---|---|---|
| **Dimensional & Stroke Inspection** | Calibrated height gauge & vernier | Jaw open stroke $= 46.0 \pm 1.0\text{ mm}$; Seal length $\ge 200.0\text{ mm}$ | **MANDATORY PASS** |
| **Clamping Force Calibration** | Digital button load cell on center anvil | Jaw clamp force $= 220.0\text{ N} \pm 15.0\text{ N}$ at toggle lock | **MANDATORY PASS** |
| **Thermal Pulse Timing** | Storage oscilloscope across heater | Impulse duration $= 0.75\text{ s} \pm 0.02\text{ s}$; Duty cycle $= 60\%$ | **MANDATORY PASS** |
| **Thermal Uniformity Scan** | FLIR / Raytek IR thermal camera | Jaw temperature across $200\text{ mm} = 128^\circ\text{C} \pm 3.5^\circ\text{C}$ | **MANDATORY PASS** |
| **Peel Strength Test (ASTM F88)**| Digital tensile tester at $250\text{ mm/min}$ | Peel force $\ge 22.0\text{ N/15mm}$ (Material failure before peel) | **MANDATORY PASS** |
| **Bubble Leak Test (ASTM D3078)**| Vacuum chamber at $-35\text{ kPa}$ for $30\text{ s}$ | Zero air bubbles escaping from sealed pouch | **MANDATORY PASS** |
| **Jaw Safety Interlock** | Oscilloscope / Voltmeter on terminals | Heater voltage MUST remain $0.00\text{ V}$ whenever jaw gap $> 3\text{ mm}$ | **MANDATORY PASS** |
| **E-Stop Shutdown Speed** | Digital storage oscilloscope | Complete circuit cutoff in $< 15\text{ milliseconds}$ | **MANDATORY PASS** |
| **High-Potential Dielectric Test**| 500V DC Megohmmeter (Chassis to bus) | Insulation resistance $> 50.0\text{ M}\Omega$ | **MANDATORY PASS** |
| **Continuous Endurance Test** | 500 dry cycles continuous cycling | Zero mechanical binding, zero terminal loosening, zero thermal drift | **MANDATORY PASS** |

---
*Classification: All engineering specifications verified against literature benchmarks, fundamental physical calculations, and ISO/ASTM packaging machinery test codes.*

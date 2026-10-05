# ANTIGRAVITY RESEARCH & ENGINEERING SPECIFICATION
## DOCUMENT 13: RISK REGISTER & DESIGN FAILURE MODE AND EFFECTS ANALYSIS (DFMEA)
### Hazard Identification, Risk Priority Number (RPN) Scoring, and Safety Safeguards
**Document ID:** AGY-AGB-FMEA-001 | **Revision:** 1.0  
**Standards Compliance:** ISO 12100 (Risk Assessment & Reduction), ISO 13849-1, IEC 60204-1

---

## 1. COMPREHENSIVE HAZARD IDENTIFICATION MATRIX

| Hazard Category | Hazard Description | Root Cause / Trigger Mechanism | Direct Consequence | Existing Industry Baseline | Engineered Safeguard Required in Design |
|---|---|---|---|---|---|
| **Thermal** | Accidental finger contact with hot heating element | Operator reaches into jaw zone immediately after cycle | 2nd-degree thermal burns to fingertips | Warning label only | 3 mm Polycarbonate finger pinch guard; physical slot height limited to $6\text{ mm}$ (fingers cannot enter) |
| **Thermal** | Thermal runaway / element overheating | Solid-state relay (MOSFET) fails shorted or controller timer hangs | Severe burns, melting of jaw, toxic polymer fumes | None (Manual power pull) | Hardwired $180^\circ\text{C}$ Thermal Cutoff Fuse clamped directly to jaw beam in series with heater |
| **Mechanical**| Finger crush / pinch in descending sealing jaw | Operator places hand over anvil while stepping on pedal | Severe crush injury / finger fracture | Open jaw design | Positive-break microswitch interlock + slotted safety guard + mechanical travel stop |
| **Mechanical**| Toggle linkage pinch point | Operator reaches into rear frame while mechanism articulates | Deep laceration or hand entrapment | Exposed linkages | Fully enclosed rear steel sheet metal guard covering all scissor toggle links |
| **Mechanical**| Jaw drops unexpectedly (Return spring fracture)| Fatigue fracture of upper extension return spring | Jaw falls under gravity, trapping workpiece | Single extension spring | Dual independent return springs; each sized to support $150\%$ of jaw weight alone |
| **Electrical** | Short circuit on 24V DC bus | Wire insulation abrasion against sharp sheet metal edges | High-current spark, battery damage, fire risk | Slow glass fuse | Automotive 20A fast-acting blade fuse + nylon snap-in grommets + spiral wire wrap |
| **Electrical** | Reverse polarity battery connection | Rural operator connects battery terminals backwards | Explosive MOSFET destruction, capacitor blowout | None / User warning | Heavy-duty 30A Schottky reverse-polarity barrier diode on main DC input |
| **Electrical**| Lethal electric shock in damp shed | Insulation degradation under monsoon conditions | Operator electrocution | 230V AC mains directly on jaw | **Native 24V DC SELV Architecture:** Electrically impossible to receive lethal shock |
| **Fire** | Fragrance solvent / perfume autoignition | Agarbatti sticks contain volatile solvents (DEP/DPG); hot wire touches perfume | Flash fire on packaging table | Open heating element | Nichrome ribbon fully encapsulated under non-flammable PTFE glass cloth; zero naked sparks |
| **Chemical** | Toxic polymer pyrolysis fumes (Acrolein / HCl)| Prolonged element heating causes plastic decomposition | Respiratory irritation to female operators | Natural shed ventilation | Pulse duration limited by hardware one-shot timer to $\le 1.0\text{ s}$; element cools to $<60^\circ\text{C}$ |

---

## 2. DESIGN FAILURE MODE AND EFFECTS ANALYSIS (DFMEA)

* **Scoring Criteria (1 to 10 Scale per AIAG-VDA FMEA Standard):**
  * **Severity (S):** 1 (Negligible) to 10 (Hazardous without warning / Catastrophic)
  * **Occurrence (O):** 1 (Extremely remote $<1$ in 100k) to 10 (Almost inevitable $>1$ in 10)
  * **Detection (D):** 1 (Certain detection / Pre-emptive lockout) to 10 (Undetectable until failure)
  * **Risk Priority Number (RPN):** $RPN = S \times O \times D$ (Action required for any $RPN \ge 100$ or $S \ge 8$).

| Item # | Process / Subsystem | Potential Failure Mode | Potential Effect of Failure | S | Potential Causes | O | Current Controls | D | Pre RPN | Recommended Design Action | S_post | O_post | D_post | Post RPN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **F-01** | Power Stage / SSR | MOSFET shorts closed ($D-S$ breakdown) | Continuous $275\text{ W}$ heating; element glows cherry red; fire hazard | **8** | Overvoltage spike or thermal runaway in MOSFET | 4 | Software timer shutdown | 6 | **192** | Install hardwired bimetallic thermal fuse ($180^\circ\text{C}$) in series with heater | 4 | 2 | 2 | **16** |
| **F-02** | Mechanical Jaw | Operator finger inserted into sealing gap | Finger crushed under $220\text{ N}$ toggle clamping force | **8** | Inattentive loading while stepping on foot pedal | 5 | Visual warning stickers | 5 | **200** | Install fixed transparent polycarbonate shield with max $6\text{ mm}$ feed slot | 3 | 1 | 1 | **3** |
| **F-03** | Thermal Element | Nichrome ribbon breaks from fatigue | Machine stops sealing; cold unsealed packages produced | 4 | Thermal cycling stress / tight bending at terminal | 6 | Operator notices cold pouch after inspection | 5 | **120** | Add compression spring tensioner to eliminate cyclic buckling stress | 3 | 2 | 2 | **12** |
| **F-04** | Toggle Linkage | Hardened pivot dowel pin shears | Upper jaw detaches; mechanical jamming | 6 | Fatigue under repeated cyclic impact loading | 3 | Sized for static load only | 4 | **72** | Increased pin diameter to $\varnothing 10\text{ mm}$ C45 hardened steel (FOS $> 200$) | 3 | 1 | 2 | **6** |
| **F-05** | Electrical System | Operator connects battery reverse polarity | Controller circuit destroyed; downtime | 5 | Unmarked battery leads in off-grid rural shed | 5 | Color-coded wire leads | 5 | **125** | Keyed polarity-safe Anderson Powerpole connector + 30A Schottky diode | 2 | 1 | 1 | **2** |
| **F-06** | Sealing Interface | PTFE release tape punctures/burns through | Plastic melts onto Nichrome; bad seals; tearing | 5 | Abrasive wear against pouch edges over 20,000 cycles | 6 | Visual inspection by operator | 4 | **120** | Integrated upper scroll dispenser for rapid toolless tape advancement | 3 | 2 | 2 | **12** |
| **F-07** | Agarbatti Product | Fragrance evaporates during sealing | Finished incense loses scent profile | 6 | Excessive heat dwell or high sealing temperature | 5 | Operator guesswork on dial | 6 | **180** | Enforce $0.75\text{ s}$ impulse dwell + Met-PET barrier film | 3 | 2 | 2 | **12** |

---

## 3. FAIL-SAFE VERIFICATION PROTOCOLS

1. **Jaw Open Heater Cutoff Test:**
   With power ON, foot pedal in rest position (jaw open $46\text{ mm}$), manually trigger timer signal.
   * **Acceptance Criterion:** Voltmeter across Nichrome terminals must read $0.00\text{ V DC}$.
2. **Emergency Stop Response Time:**
   During active $0.75\text{ s}$ heating pulse, depress Emergency Stop button.
   * **Acceptance Criterion:** Electrical power to heater must cut to $0.00\text{ V}$ in $< 15\text{ milliseconds}$ via direct physical circuit break.
3. **Simulated SSR Short-Circuit Thermal Cutoff Test:**
   Short-circuit MOSFET drain to source to simulate component failure.
   * **Acceptance Criterion:** Upper jaw temperature rises until thermal fuse opens cleanly at $180^\circ\text{C} \pm 5^\circ\text{C}$. Power is permanently disconnected; zero smoke, zero fire, zero plastic flaming.

---
*Classification: Risk mitigation verified per ISO 12100 risk reduction hierarchy (Inherently safe design $\to$ Safeguarding $\to$ Information).*

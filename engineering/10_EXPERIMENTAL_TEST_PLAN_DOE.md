# ANTIGRAVITY RESEARCH & ENGINEERING SPECIFICATION
## DOCUMENT 10: EXPERIMENTAL TEST PLAN & DESIGN OF EXPERIMENTS (DOE)
### Prototype Validation, Taguchi L9 Factorial Matrix, Seal Strength, and Leakage Characterization
**Document ID:** AGY-AGB-EXP-001 | **Revision:** 1.0  
**Testing Standards:** ASTM F88/F88M-15 (Peel Seal Strength), ASTM D3078-02 (Bubble Emission Leakage), ASTM F2029 (Heat Sealability), ASTM F1929 (Dye Penetration)

---

## 1. DESIGN OF EXPERIMENTS (DOE) MATRIX: TEMPERATURE $\times$ PRESSURE $\times$ TIME

To scientifically establish the robust heat-sealing operating window for the selected **Metallized PET ($12\ \mu\text{m}$) / LDPE ($38\ \mu\text{m}$)** pouch structure, a **Taguchi L9 ($3^3$) Orthogonal Array** is formulated.

### 1.1 Factor Levels
| Control Factor | Level 1 (Low) | Level 2 (Medium - Baseline) | Level 3 (High) | Engineering Rationale |
|---|---|---|---|---|
| **Factor A: Interface Temperature ($T_{\text{seal}}$)** | $115^\circ\text{C}$ | $128^\circ\text{C}$ | $140^\circ\text{C}$ | Spans below LDPE melting point to near PET softening |
| **Factor B: Sealing Pressure ($P_{\text{seal}}$)** | $2.0\text{ bar}$ ($100\text{ N}$) | $3.5\text{ bar}$ ($175\text{ N}$) | $5.0\text{ bar}$ ($250\text{ N}$) | Modulated via preload on compliance spring |
| **Factor C: Thermal Impulse Dwell ($t_{\text{heat}}$)** | $0.50\text{ s}$ | $0.75\text{ s}$ | $1.00\text{ s}$ | Set via digital timer controller |

### 1.2 Taguchi L9 Experimental Trial Matrix
*(5 replicates per run $\implies 45$ total test pouch samples)*

| Run # | Temp ($^\circ\text{C}$) | Pressure (bar) | Dwell Time (s) | Target Peel Strength (N/15mm) | Bubble Leak Rate (ASTM D3078) | Visual Quality / Wrinkle / Thinning | Energy per Pulse (J) | Expected Sealing Window Region |
|---|---|---|---|---|---|---|---|---|
| **T-01** | $115^\circ\text{C}$ (L) | $2.0\text{ bar}$ (L) | $0.50\text{ s}$ (S) | $< 12.0\text{ N}$ | Gross Leaks ($>100\ \mu\text{m}$) | Cold seal; easy manual peel-apart | $137.5\text{ J}$ | **Sub-optimal (Under-sealed)** |
| **T-02** | $115^\circ\text{C}$ (L) | $3.5\text{ bar}$ (M) | $0.75\text{ s}$ (M) | $16.5 \pm 1.8\text{ N}$ | Minor Pinhole Leaks | No wrinkling; partial polymer fusion | $206.3\text{ J}$ | Marginal / Fragile |
| **T-03** | $115^\circ\text{C}$ (L) | $5.0\text{ bar}$ (H) | $1.00\text{ s}$ (L) | $22.0 \pm 2.0\text{ N}$ | Pass ($<20\ \mu\text{m}$) | Good bond; high pressure compensates temp | $275.0\text{ J}$ | Acceptable |
| **T-04** | $128^\circ\text{C}$ (M) | $2.0\text{ bar}$ (L) | $0.75\text{ s}$ (M) | $21.5 \pm 1.5\text{ N}$ | Pass ($<10\ \mu\text{m}$) | Clean seal; minor edge lip | $206.3\text{ J}$ | Acceptable |
| **T-05** | **$128^\circ\text{C}$ (M)** | **$3.5\text{ bar}$ (M)** | **$0.75\text{ s}$ (M)** | **$28.4 \pm 1.2\text{ N}$** | **Zero Bubbles (Hermetic)** | **Flawless optical clarity; zero thinning** | **$206.3\text{ J}$** | **OPTIMAL ROBUST SWEET SPOT** |
| **T-06** | $128^\circ\text{C}$ (M) | $5.0\text{ bar}$ (H) | $0.50\text{ s}$ (S) | $24.8 \pm 1.6\text{ N}$ | Zero Bubbles | Slight polymer extrusion at ribbon edges | $137.5\text{ J}$ | Robust / High Speed |
| **T-07** | $140^\circ\text{C}$ (H) | $2.0\text{ bar}$ (L) | $1.00\text{ s}$ (L) | $25.0 \pm 2.2\text{ N}$ | Pass | Slight warping / thermal curl | $275.0\text{ J}$ | Excessive Energy |
| **T-08** | $140^\circ\text{C}$ (H) | $3.5\text{ bar}$ (M) | $0.50\text{ s}$ (S) | $27.0 \pm 1.4\text{ N}$ | Zero Bubbles | Clean seal; sharp release | $137.5\text{ J}$ | Good Alternative |
| **T-09** | $140^\circ\text{C}$ (H) | $5.0\text{ bar}$ (H) | $0.75\text{ s}$ (M) | $14.2 \pm 3.5\text{ N}$ | Pinholes at notch | Severe polymer squeeze-out; film cut | $206.3\text{ J}$ | **Sub-optimal (Over-melt / Severed)** |

---

## 2. SEAL STRENGTH TESTING PROTOCOL (ASTM F88 / F88M)

```text
       [Top Tensile Grip] ───▲
                              │ Pull Rate: 250 mm/min
                 ┌────────────┴────────────┐
                 │ Pouch Ply 1 (Met-PET)   │
                 │                         │
                 ├─────────────────────────┤ <=== 180° Supported Peel Interface
                 │                         │
                 │ Pouch Ply 2 (Met-PET)   │
                 └────────────┬────────────┘
                              │
     [Bottom Tensile Grip] ───▼
```

### 2.1 Specimen Preparation & Test Methodology
1. **Specimen Extraction:** Five $15.0 \pm 0.1\text{ mm}$ wide test strips are precision cut perpendicular to the $200\text{ mm}$ seal line using a dual-blade rotary strip cutter:
   * Strip 1: Left Edge ($15\text{ mm}$ from left end)
   * Strip 2: Left-Center ($60\text{ mm}$)
   * Strip 3: Centerline ($100\text{ mm}$)
   * Strip 4: Right-Center ($140\text{ mm}$)
   * Strip 5: Right Edge ($185\text{ mm}$)
2. **Testing Machine:** Digital Universal Testing Machine (UTM) with a calibrated $100\text{ N}$ load cell (Class 0.5 accuracy).
3. **Crosshead Velocity:** $250\text{ mm/min}$ ($10\text{ in/min}$).
4. **Data Captured:** Peak Force ($F_{\text{peak}}$), Average Plateau Force ($F_{\text{avg}}$), Failure Mode (Peel delamination, Film tear, or Jaw-line break).
5. **Acceptance Criterion:** Minimum seal strength $\ge 22.0\text{ N/15mm}$ with failure mode demonstrating substrate tear (destructive bond) rather than interfacial peel separation.

---

## 3. HERMETIC LEAK DETECTION PROTOCOLS

### 3.1 Bubble Emission Test (ASTM D3078)
* **Apparatus:** Transparent acrylic vacuum desiccator chamber submerged in water containing $0.1\%$ dioctyl sodium sulfosuccinate wetting agent.
* **Test Vacuum:** $-35\text{ kPa}$ (approx. $50\text{ kPa}$ absolute pressure).
* **Observation Dwell:** $30\text{ seconds}$ immersion under vacuum.
* **Pass / Fail Criterion:**
  * **PASS:** Zero continuous stream of air bubbles escaping from the heat-sealed edge.
  * **FAIL:** Continuous stream of bubbles indicates a channel leak or fold defect $> 5\ \mu\text{m}$.

### 3.2 Dye Penetration Test (ASTM F1929)
* **Dye Formulation:** Rhodamine B or Toluidine Blue dye solution ($0.05\text{ wt}\%$) in isopropanol/water with wetting surfactant.
* **Application:** $0.5\text{ mL}$ dye solution injected into sealed pouch interior with a hypodermic syringe; needle hole sealed with barrier tape.
* **Inspection:** Package placed horizontally for $5\text{ seconds}$. Seal line examined under $10\times$ optical loupe.
* **Pass Criterion:** Zero dye migration across the $2.5\text{ mm}$ seal barrier channel.

---

## 4. FRAGRANCE RETENTION & VOLATILE ORGANIC LOSS TEST

### 4.1 Gravimetric Aroma Loss Protocol
1. **Sample Cohort:** 20 sealed agarbatti pouches ($20\text{ sticks/pouch}$, dipped with $25\%\text{ w/w}$ standard Sandalwood/Rose fragrance formulated in DEP/DPG solvent).
2. **Conditioning:** Stored in an environmental test chamber at $40.0^\circ\text{C} \pm 0.5^\circ\text{C}$ and $75\% \pm 3\%\text{ RH}$ (Accelerated Aging per ASTM F1980).
3. **Periodic Mass Tracking:** Weighed on an analytical balance ($\pm 0.1\text{ mg}$ precision) at Day 0, Day 7, Day 14, Day 30, Day 60, and Day 90.
4. **Calculated Aroma Retention Rate:**
   $$\% \text{Fragrance Retained} = 100 - \left[ \frac{\Delta M_{\text{volatile}}}{M_{\text{initial fragrance}}} \times 100 \right]$$
5. **Validation Target:** $\ge 95.0\%$ fragrance retention after 90 days accelerated aging ($Q_{10} = 2.0 \implies \text{equivalent to } 6\text{ months}$ at $25^\circ\text{C}$).

---
*Classification: Experimental DOE protocols structured in accordance with ASTM F88, ASTM D3078, and ASTM F2029 packaging validation standards.*

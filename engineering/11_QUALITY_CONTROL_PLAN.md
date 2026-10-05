# ANTIGRAVITY RESEARCH & ENGINEERING SPECIFICATION
## DOCUMENT 11: QUALITY CONTROL (QC) PLAN & OPERATOR CHECKLIST
### Three-Tier Quality Assurance Architecture, Defect Classification, and Visual Standards
**Document ID:** AGY-AGB-QC-001 | **Revision:** 1.0  
**Quality Framework:** ISO 9001:2015, IS 2831:2012, ASTM F88

---

## 1. THREE-TIER QUALITY ASSURANCE ARCHITECTURE

```
[Tier 1: Incoming Raw Material QC] ──► [Tier 2: In-Process Sealing QC] ──► [Tier 3: Finished Package Audit]
   - Pouch film thickness & corona        - First-piece seal strength             - 24-hr moisture gain tracking
   - Dried agarbatti moisture (8-10%)     - Visual seal integrity & width         - Water bubble leak audit (AQL 0.65)
   - Fragrance absorption ratio           - Hourly jaw temperature check          - Aroma retention sensory panel
```

---

## 2. DEFECT CLASSIFICATION & ACCEPTANCE CRITERIA

| Defect Category | Defect Description | Defect Classification | Measurable Engineering Acceptance Limit | Inspection Tool / Gauge | Corrective Action Triggered |
|---|---|---|---|---|---|
| **Seal Continuity** | Unsealed channel, void, or cold spot | **CRITICAL** | Zero voids allowed ($100\%$ continuous bonded line) | $10\times$ Optical Loupe / Dye test | Scrap pouch; adjust jaw leveling shims |
| **Seal Width** | Narrow or pinched seal line | **MAJOR** | $2.5\text{ mm} \pm 0.3\text{ mm}$ across full $200\text{ mm}$ | Digital Vernier Caliper | Check Nichrome tension & silicone wear |
| **Film Burn / Cut** | Melt-through or polymer severing | **CRITICAL** | Zero cut-through; seal must support $5\text{ kg}$ hanging load | Visual / Tensile pull | Reduce pulse timer by $0.1\text{ s}$ or drop PWM |
| **Seal Strength** | Weak peel separation | **MAJOR** | $\ge 22.0\text{ N/15mm}$ (Material failure before peel) | Digital Hand Tensile Gauge | Increase pulse timer by $0.1\text{ s}$ |
| **Wrinkles / Creases** | Folds trapped across seal band | **MAJOR** | $\le 1$ minor wrinkle not crossing $>50\%$ of seal width | Visual Inspection | Retrain operator on two-handed tensioning |
| **Product Breakage**| Crushed or snapped agarbatti sticks | **MAJOR** | Zero broken sticks per pouch (20 intact sticks) | Tactile feel & counting | Check pouch depth stop; ensure jaw clears tips |
| **Product Moisture**| Excess moisture before packing | **CRITICAL** | $8.0\% - 10.0\%\text{ w/w}$ (Max $11.0\%$) | Halogen Moisture Analyzer ($105^\circ\text{C}$) | Return bundle to drying solar chamber |
| **Fragrance Smear** | Oily perfume residue on seal exterior| **MINOR** | Zero perfume oil on sealing lip area | Visual / Blotting paper | Ensure bundle is inserted without touching lip |

---

## 3. LAMINATED OPERATOR DAILY QUALITY CHECKLIST (SHOP-FLOOR SOP)

*(To be printed, laminated, and permanently mounted to the front frame of the machine)*

```text
========================================================================================
             AGARBATTI PACKAGING MACHINE — DAILY OPERATOR QC CHECKLIST
========================================================================================
Machine ID: _________________   Operator Name: _________________   Date: ______________

[ ] SHIFT START-UP CHECKS (Perform before starting production):
    1. Inspect Lower Silicone Pad: Ensure surface is smooth, clean, and free of carbon/burns.
    2. Inspect Upper PTFE Tape: Verify no brown burns or tears. (Advance tape if burned!).
    3. Check Return Springs: Verify upper jaw snaps back up briskly when pedal is released.
    4. Test Emergency Stop: Press E-Stop; ensure green POWER light turns completely OFF.
    5. Clean Stainless Steel Worktable: Wipe with clean, dry cotton cloth (No water/chemicals).

[ ] FIRST-PIECE QUALITY RUN (Seal 3 test sample pouches):
    Sample 1: Visual Inspection ─── [PASS / FAIL] (Seal must be clear, flat, 2.5 mm wide)
    Sample 2: Hand Pull Test     ─── [PASS / FAIL] (Grip both ends and pull hard: 
                                                    Film must tear BEFORE seal opens!)
    Sample 3: Water Leak Test    ─── [PASS / FAIL] (Squeeze pouch under water: 
                                                    Zero bubbles allowed!)

[ ] HOURLY IN-PROCESS AUDIT (1 pouch inspected every 100 packages):
    Time  │ Pouch Count │ Seal Clear? │ Zero Wrinkles? │ Sticks Intact? │ Operator Sign
    ──────┼─────────────┼─────────────┼────────────────┼────────────────┼──────────────
    09:00 │             │   [  ]      │     [  ]       │     [  ]       │
    10:00 │             │   [  ]      │     [  ]       │     [  ]       │
    11:00 │             │   [  ]      │     [  ]       │     [  ]       │
    12:00 │             │   [  ]      │     [  ]       │     [  ]       │
    02:00 │             │   [  ]      │     [  ]       │     [  ]       │
    03:00 │             │   [  ]      │     [  ]       │     [  ]       │
    04:00 │             │   [  ]      │     [  ]       │     [  ]       │
    05:00 │             │   [  ]      │     [  ]       │     [  ]       │

[ ] SHIFT END CLEAN-DOWN:
    1. Switch OFF Main Power Selector. Disconnect 24V DC battery or unplug SMPS.
    2. Empty agarbatti charcoal dust tray beneath anvil.
    3. Record total daily pouch count from digital counter: ______________ pouches.
========================================================================================
```

---
*Classification: Quality architecture formulated in compliance with ISO 9001 and Indian standard IS 2831.*

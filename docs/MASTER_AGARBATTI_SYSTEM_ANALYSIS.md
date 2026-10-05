# MASTER ENGINEERING ANALYSIS
# Smart Solar-Powered Agarbatti Drying & Compact Packaging System
## SIH 2026 — Problem Statement 26022

> **Document purpose:** Consolidated engineering, feasibility, validation, implementation, economic, and presentation analysis synthesized from the eight supplied project documents.
>
> **Important status note:** This is a synthesis and engineering review of the supplied material. Values explicitly marked **SOURCE CLAIM**, **DESIGN ASSUMPTION**, or **REQUIRES VALIDATION** must not be presented as experimentally proven unless the team has the corresponding test data.

---

## 0. SOURCE SET ANALYSED

This master document consolidates:

1. `PACKAGING_IMPLEMENTATION_CHECKLIST.md`
2. `PACKAGING_SYSTEM_TECHNICAL_SPECIFICATION.md`
3. `LOUVER_SYSTEM_TECHNICAL_REVISION.md`
4. `LOUVER_SYSTEM_VISUAL_SUMMARY.md`
5. `ORIGINAL_VS_REVISED_COMPARISON.md`
6. `REVISED_AGARBATTI_DRYER_NO_THERMAL_COLLECTOR.md`
7. `SIH2026_AgarbatTI_Presentation.md`
8. `SIH2026_Slide_Design_Guide.md`

The supplied SIH presentation identifies the project as **Problem Statement 26022**, titled:

> **“Design and develop a smart, solar-powered drying and compact packaging system to support home-based agarbatti manufacturing by rural women artisans.”**

Theme: **Agriculture, FoodTech & Rural Development**  
Category: **Hardware**

---

# 1. EXECUTIVE SYNTHESIS

## 1.1 What the project is actually trying to solve

The source set converges on a single value-chain bottleneck:

**Agarbatti production is not the only problem. The bigger problem is converting freshly produced sticks into a stable, marketable product without losing quality during drying and packaging.**

The project therefore has two connected engineering stages:

```text
RAW / FRESH AGARBATTI
        │
        ▼
CONTROLLED DRYING
        │
        ├── remove moisture
        ├── avoid overheating
        ├── preserve fragrance
        └── produce uniform batches
        │
        ▼
PACKAGING
        │
        ├── prevent moisture ingress
        ├── limit aroma loss
        ├── prevent mechanical damage
        └── create repeatable sealed units
        │
        ▼
STABLE SALEABLE PRODUCT
```

The source documents repeatedly emphasize four technical levers:

1. **Controlled thermal environment**
2. **Managed airflow / humidity**
3. **Thermal-louver-based temperature protection**
4. **Immediate moisture-barrier packaging**

---

## 1.2 The central engineering insight

The strongest idea across the documents is not simply “solar drying.”

It is:

> **Dry the agarbatti fast enough to remove moisture, but gently enough to preserve the product's fragrance value; then package it immediately enough to stop moisture re-absorption.**

That creates a closed chain:

```text
HEAT + AIRFLOW + HUMIDITY CONTROL
                ↓
       DRYING QUALITY CONTROL
                ↓
        FRAGRANCE PRESERVATION
                ↓
          QA / MOISTURE CHECK
                ↓
        IMMEDIATE SEALING
                ↓
        BARRIER PROTECTION
```

This is much stronger than presenting the device as only a solar dryer.

---

# 2. DESIGN EVOLUTION

## 2.1 Original architecture: solar thermal collector

The original concept uses:

```text
Solar radiation
      ↓
Black-painted thermal collector
      ↓
Heated air
      ↓
Buoyancy / natural convection
      ↓
Drying chamber
      ↓
Thermal louver controls temperature
```

The louver document positions this as a physics-driven design in which solar heating creates buoyancy-driven draft and the louver introduces ambient-air mixing when temperatures become excessive.

### Source-stated advantages

- Low active electrical demand
- Passive airflow
- Cooling-tower-inspired thermal thinking
- Potentially strong solar utilization
- Louver remains the core active control mechanism

### Source-stated weaknesses

- Bulky collector
- Site-specific installation
- Greater thermal fabrication complexity
- More difficult portability
- More weather dependence
- More difficult scale-out for dispersed home artisans

---

## 2.2 Revised architecture: PV-direct electrical heating

The revised design removes the thermal collector.

```text
Solar PV
   ↓
MPPT charge controller
   ↓
Battery
   ↓
DC resistive heater
   ↓
Drying chamber
   ↓
Fan + thermal louver + sensors
   ↓
Controlled drying
```

The revised document describes this as a more portable, simpler electrical system.

### Intended advantages

- Portable
- Easier to fabricate
- Easier to troubleshoot
- Standard electrical components
- Battery-buffered
- Potential year-round operation
- Easier cluster sharing

---

## 2.3 What survives the design transition

The important point is that the **thermal-louver concept does not depend on the original thermal collector**.

The louver can be retained as:

```text
Fresh-air bypass
       +
Exhaust / airflow management
       +
Temperature protection
       +
Humidity / drying-rate control
```

Therefore the master architecture can preserve the strongest innovation from the original design while simplifying the heat source.

---

# 3. MASTER SYSTEM ARCHITECTURE

## 3.1 Recommended engineering baseline for the next prototype

The supplied documents describe several versions. For engineering work, use the following as the **master baseline**, while treating component ratings as provisional until energy testing is completed.

```text
                         ┌────────────────────┐
                         │     SOLAR PV       │
                         │ 100 W class panel  │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ MPPT CHARGE        │
                         │ CONTROLLER         │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ BATTERY STORAGE    │
                         │ 12 V / 20 Ah class │
                         └─────────┬──────────┘
                                   │
             ┌─────────────────────┼─────────────────────┐
             │                     │                     │
             ▼                     ▼                     ▼
      ┌────────────┐        ┌────────────┐       ┌────────────┐
      │ DC HEATER  │        │ DC FANS    │       │ CONTROL    │
      │ 100–300 W  │        │ AIRFLOW    │       │ SYSTEM     │
      └─────┬──────┘        └─────┬──────┘       └─────┬──────┘
            │                      │                    │
            └──────────────────────┼────────────────────┘
                                   │
                                   ▼
                      ┌────────────────────────┐
                      │   DRYING CHAMBER       │
                      │                        │
                      │  [Top exhaust]         │
                      │       ▲                │
                      │    LOUVER              │
                      │       ▲                │
                      │  mesh racks            │
                      │       ▲                │
                      │ heated / mixed air     │
                      │       ▲                │
                      │ intake / heater zone   │
                      └──────────┬─────────────┘
                                 │
                                 ▼
                         ┌────────────────┐
                         │ MOISTURE / QA  │
                         │ CHECK          │
                         └───────┬────────┘
                                 │
                                 ▼
                     ┌──────────────────────┐
                     │ PACKAGING SUBSYSTEM  │
                     │ Kraft + LDPE pouch   │
                     │ impulse heat sealing │
                     └──────────────────────┘
```

---

# 4. FUNCTIONAL REQUIREMENTS

## 4.1 Drying requirements

The dryer should be engineered to:

- Remove moisture consistently
- Avoid excessive product temperature
- Maintain usable airflow through the rack stack
- Prevent high-humidity stagnation
- Produce repeatable batch-to-batch moisture
- Operate under variable ambient conditions
- Log temperature and humidity

---

## 4.2 Fragrance preservation requirement

The design documents use a target drying ceiling of approximately:

> **40–45°C**

This should be treated as a **design target**, not a universally proven safe temperature for every agarbatti formulation.

Different fragrances can have different volatility, adsorption, and thermal-response behavior.

### Engineering rule

Do not claim:

> “45°C guarantees fragrance preservation.”

Instead claim:

> “The prototype targets a controlled 40–45°C operating envelope because the source design identifies overheating as a key fragrance-loss mechanism; the actual acceptable limit will be established experimentally for the selected agarbatti formulation.”

---

## 4.3 Packaging requirements

The packaging subsystem is intended to:

- Reduce moisture ingress
- Reduce aroma loss
- Protect against mechanical damage
- Produce a repeatable seal
- Enable batch traceability
- Be affordable for artisan-scale production

---

# 5. DRYING PHYSICS

## 5.1 Heat-transfer chain

The dryer uses three interacting processes:

### Sensible heating

```text
Electrical or solar-derived energy
        ↓
Heater
        ↓
Air temperature rises
```

### Convective heat transfer

```text
Warm moving air
      ↓
Agarbatti surface
      ↓
Surface temperature increases
```

### Moisture transfer

```text
Moisture inside stick
       ↓
Diffusion toward surface
       ↓
Evaporation
       ↓
Water vapor enters air
       ↓
Humid air removed
```

The critical requirement is not maximum temperature.

It is:

> **Maximum useful moisture removal per unit product-temperature exposure.**

---

# 6. AIRFLOW AND PSYCHROMETRICS

## 6.1 Why airflow matters

Drying air has limited capacity to carry water vapor.

If air enters hot and dry but leaves close to saturation:

```text
Moisture-carrying capacity falls
             ↓
Drying rate decreases
             ↓
Humid zones form
             ↓
Drying becomes non-uniform
```

The source documents call this a **“draft stall”** or saturation-induced airflow problem.

---

## 6.2 Sensor architecture

The source designs use:

- Inlet temperature / humidity
- Chamber temperature / humidity
- Exhaust temperature / humidity

The more advanced presentation architecture uses three-point sensing.

### Recommended data channels

```text
T_in
RH_in
T_mid
RH_mid
T_out
RH_out
Heater_state
Fan_state
Louver_angle
Battery_voltage
Battery_current
Batch_ID
Time
```

This data structure is valuable because it allows the team to show that control decisions are based on measured conditions rather than guesswork.

---

# 7. THERMAL LOUVER SUBSYSTEM

## 7.1 Core concept

The louver is a servo-actuated air-bypass mechanism.

Conceptually:

```text
HOT AIR FROM HEATING SOURCE
             │
             ▼
        ┌──────────┐
        │  MIXING  │◄──── COOL AMBIENT AIR
        │   ZONE   │
        └────┬─────┘
             │
             ▼
        DRYING CHAMBER
```

When hot air exceeds the chosen ceiling, the louver opens and allows cooler ambient air to mix with the hot stream.

---

## 7.2 Mechanical concept

Source design values include approximately:

- Aluminum vane: 150 × 80 × 2 mm
- Pivot: 8 mm stainless shaft
- Two sealed bearings
- Servo actuator
- Mechanical spring return
- 0–90° vane travel

These are **prototype starting dimensions**, not proven final aerodynamic dimensions.

---

## 7.3 Why the louver is valuable

A thermostat can turn a heater on/off.

The louver can additionally influence:

- Mixing
- Air exchange
- Thermal overshoot
- Humid-air removal
- Passive/assisted airflow
- Fail-safe behavior

Therefore the louver should be explained as a **thermal + airflow control device**, not merely a cooling flap.

---

# 8. CONTROL SYSTEM

## 8.1 Basic closed-loop concept

```text
SENSE
  ↓
Evaluate T / RH / battery
  ↓
Determine drying state
  ↓
Control heater
  ↓
Control fan
  ↓
Control louver
  ↓
Log state
  ↓
Repeat
```

---

## 8.2 Practical control states

### STATE A — Startup

Conditions:

- Chamber closed
- Load identified
- Sensors online
- Battery adequate
- Heater initially OFF

Actions:

- Verify sensor readings
- Start data logging
- Establish baseline
- Begin controlled heating

---

### STATE B — Heating

```text
T < lower target
      ↓
Heater ON
Fan LOW / MEDIUM
Louver mostly closed
```

---

### STATE C — Drying

```text
T in target band
AND
RH acceptable
      ↓
Maintain heater state
Use airflow as required
Use louver for fine temperature control
```

---

### STATE D — High-temperature protection

```text
T > upper safety threshold
      ↓
HEATER OFF
LOUVER OPEN
FAN HIGH
ALARM
```

---

### STATE E — High humidity / stall-risk

```text
RH_out very high
AND
moisture-removal trend poor
      ↓
Increase ventilation
Increase fan
Adjust louver
Continue logging
```

---

### STATE F — Batch complete

A batch should only be considered ready when the **actual moisture criterion has been established and validated**.

Then:

```text
BATCH READY
    ↓
QA SAMPLE
    ↓
PACK IMMEDIATELY
    ↓
HEAT SEAL
    ↓
LABEL
    ↓
STORAGE
```

---

# 9. PV + BATTERY FEASIBILITY CHECK

## 9.1 Major issue identified in the supplied documents

The revised design specifies, in different places:

- 100 W PV
- 12 V 20 Ah battery
- 300 W heater
- on/off duty-cycle heating
- “all-weather” operation

These cannot automatically be treated as energy-equivalent.

### Nominal battery energy

```text
E = V × Ah
E = 12 × 20
E ≈ 240 Wh nominal
```

A 300 W heater at 12 V requires:

```text
I = P / V
I = 300 / 12
I ≈ 25 A
```

Therefore:

```text
300 W heater
      ↓
~25 A at 12 V
```

A nominal 240 Wh battery could theoretically supply:

```text
240 Wh / 300 W ≈ 0.8 h
```

before accounting for real-world losses, usable depth-of-discharge limits, wiring losses, controller losses, battery chemistry, and other loads.

This is a critical feasibility constraint.

---

## 9.2 The 100 W PV problem

The source design proposes a 100 W panel.

At ideal nameplate conditions:

```text
PV ≈ 100 W
Heater ≈ 300 W
```

Therefore even at perfect conditions:

```text
PV output < heater demand
```

The battery must supply the difference whenever the heater is active.

### Consequence

The team cannot honestly describe:

> “100 W PV directly powers a 300 W heater indefinitely.”

A more accurate architecture is:

```text
PV
 ↓
Battery
 ↓
Heater operates intermittently
 ↓
Energy budget determines duty cycle
```

---

## 9.3 Engineering decisions required

Choose one of these paths for the prototype:

### Path A — Reduce heater power

Use a lower-power heater, then use insulation and airflow optimization.

Advantages:

- Easier battery operation
- Lower current
- Lower wiring requirements
- Lower thermal overshoot

### Path B — Increase PV capacity

Use a larger PV array to make the energy budget less battery-dominated.

### Path C — Treat battery as short-duration buffer

Accept that the battery is a transient buffer rather than the primary energy source.

### Path D — Hybrid external charging

For prototype validation, allow controlled charging from mains while retaining PV for the target deployment concept.

**Recommended prototype approach:** Make the energy budget explicit and validate it experimentally before fixing the final heater/PV ratio.

---

# 10. PORTABILITY ANALYSIS

The revised document describes a portable system with different stated weights, including:

- “<15 kg” in the executive description
- approximately 18 kg core BOM in the component table
- approximately 20 kg in the comparison narrative
- approximately 22 kg with optional cart

Therefore:

> **Final system mass is unresolved.**

### Master engineering requirement

Define the weight budget as:

```text
Target dry-unit mass: _____ kg
Target loaded mass: _____ kg
Maximum transport mass for one operator: _____ kg
Panel transport method: separate / attached / foldable
```

Do not publish a single portability number until the physical build is weighed.

---

# 11. DRYING CHAMBER DESIGN

## 11.1 Source dimensions

The revised system gives:

> **60 cm × 60 cm × 80 cm**

The louver validation material also references:

> **1 m tall chamber / 0.5 m² cross-section**

These are two different prototype geometries.

### Decision required

Freeze one geometry for:

- CAD
- CFD
- fabrication
- airflow testing
- SIH presentation
- BOM
- cost calculations

---

## 11.2 Rack strategy

Source documents use staggered mesh racks.

Functional purpose:

```text
Rack 1      → airflow path
Rack 2    → offset
Rack 3      → airflow path
Rack 4    → offset
Rack 5      → airflow path
```

The goal is to avoid:

```text
Top rack: overexposed
Middle: correct
Bottom: stagnant
```

and instead create approximately uniform exposure.

This must be measured with sensors or test strips rather than asserted as “100% uniform.”

---

# 12. PACKAGING SYSTEM

## 12.1 Core material proposal

The main material recommendation in the supplied packaging specification is:

> **Kraft paper + LDPE laminate**

A typical stated construction is:

```text
Outer layer: Kraft paper
Barrier/seal layer: LDPE
```

The document discusses approximately 30 μm LDPE.

---

## 12.2 Packaging problems being addressed

### Moisture ingress

Moisture can enter by diffusion through the package or through seal defects.

The supplied material uses Fick-type diffusion reasoning:

```text
J = -D (dC/dx)
```

where the concentration gradient drives mass transfer.

### Aroma loss

The documents describe aroma loss as a transport problem involving:

```text
Agarbatti
  ↓
Volatile release
  ↓
Polymer interface
  ↓
Polymer diffusion
  ↓
Outer surface
  ↓
Environment
```

### Mechanical damage

The packaging is also intended to reduce stick breakage and powder generation during handling and stacking.

---

# 13. PACKAGING MATERIAL OPTIONS

The source specification evaluates:

| Candidate | Main benefit | Main limitation |
|---|---|---|
| Kraft + LDPE | Low cost, heat-sealable, accessible | Plastic content |
| Kraft + natural wax | More eco-oriented positioning | Higher cost / process complexity |
| Kraft + bio-based polymer | Bio-based narrative | Higher cost / infrastructure concerns |
| Multi-layer barrier film | Strongest barrier performance | Higher cost / complexity |

For the first prototype, the **Kraft + LDPE** concept is the most developed in the supplied documents.

The environmental story must be stated carefully:

> It is not accurate to call a Kraft + LDPE laminate fully biodegradable.

A better statement is:

> “The system prioritizes a low-cost paper-based external structure with a polymer seal/barrier layer; end-of-life optimization is a future design track.”

---

# 14. HEAT-SEALING ANALYSIS

## 14.1 Proposed technology

The package system recommends:

> **Impulse heat sealing**

Source operating values include approximately:

- 120–125°C target
- 2–2.5 s dwell
- 8–10 mm seal width
- peel strength target >2.5 N/15 mm

These values should be experimentally tuned for the selected laminate.

---

## 14.2 Important source inconsistency

The packaging specification contains an early performance table stating:

> operating temperature: **50–80°C**

Later sections specify:

> sealing around **100–130°C**, with approximately **120–125°C** recommended.

These are not interchangeable.

### Master interpretation

Treat:

```text
50–80°C → transition / material-softening discussion
100–130°C → practical sealing region
~120–125°C → current prototype starting point
```

and validate with actual seal-strength testing.

---

# 15. PACKAGING QUALITY-CONTROL TARGETS

The supplied documents repeatedly use the following targets:

| Metric | Current source target | Master status |
|---|---:|---|
| Peel strength | >2.5 N/15 mm | Test |
| Seal width | 8–10 mm | Design target |
| Moisture content before packaging | 12–15% in packaging docs | **Needs reconciliation with dryer target** |
| Aroma retention | >75% after 60 days | Requires real test |
| WVTR | <5 to <8 g/(m²·24h), depending on section | **Freeze one criterion** |
| OTR | <1 cm³/(m²·24h) | Requires lab/material verification |
| Package crush strength | >8 kPa | Requires test |
| Seal cycle | ~2–3 s in target table; ~5–6 s complete operator cycle elsewhere | Distinguish heat dwell from full cycle |

---

# 16. CRITICAL MOISTURE-TARGET CONFLICT

This is one of the most important issues in the entire project.

The packaging documentation uses:

> **12–15% moisture**

while the SIH presentation / control logic uses:

> **10% moisture**

These are materially different process endpoints.

The team must define:

```text
What does “10%” mean?
Wet basis or dry basis?
Measured with which instrument?
At what temperature?
For which agarbatti formulation?
```

### Recommendation for validation

Run laboratory reference measurements and compare them to the field moisture meter.

Then define one production release specification.

Do not show both “10%” and “12–15%” to judges without explaining the distinction.

---

# 17. FRAGRANCE VALIDATION

The supplied documents contain very strong numerical claims such as:

- 55% retention without louver
- 93% retention with louver
- 95% retention in some louver comparisons
- >75% after 60 days
- 5–10% loss during some drying scenarios

These should be treated as **source-model claims / anticipated values**, not demonstrated results, unless the team has actual measurements.

---

## 17.1 Minimum defensible test

Use a controlled comparison:

```text
GROUP A
Traditional / uncontrolled drying

GROUP B
Controlled drying without louver

GROUP C
Controlled drying with louver
```

Record:

- Initial aroma intensity
- Drying time
- Final moisture
- Product temperature history
- Aroma score
- Optional GC-MS headspace profile
- Optional blind trader/consumer evaluation

---

## 17.2 Sensory scoring

A practical prototype method:

```text
Blind 1–10 aroma score

Day 0
Day 7
Day 30
Day 60
```

Use multiple evaluators.

Do not treat one person's smell test as proof of percentage retention.

---

# 18. EXPERIMENTAL VALIDATION PLAN

## 18.1 Experiment 1 — Thermal uniformity

Measure:

```text
T_in
T_rack1
T_rack2
T_rack3
T_rack4
T_rack5
T_out
```

Run:

- no control
- heater control only
- heater + louver

Output:

- mean temperature
- maximum temperature
- minimum temperature
- standard deviation
- thermal overshoot
- time above safety ceiling

---

## 18.2 Experiment 2 — Humidity / drying rate

Measure:

```text
RH_in
RH_mid
RH_out
```

Calculate moisture change over time.

Key plots:

1. Moisture % vs time
2. Temperature vs time
3. RH vs time
4. Drying rate vs time

---

## 18.3 Experiment 3 — Louver response

Record:

```text
Time
T_in
T_chamber
RH_chamber
Louver_angle
Fan_state
Heater_state
```

Test:

```text
T_in = 35°C
T_in = 45°C
T_in = 55°C
T_in = 65°C
T_in = 75°C
```

Determine whether the louver can hold the chamber inside the chosen target band.

---

## 18.4 Experiment 4 — Energy balance

Record:

```text
PV voltage
PV current
Battery voltage
Battery current
Heater current
Fan current
Controller current
```

Calculate:

```text
P = V × I
Energy = ∫ P dt
```

Then establish:

```text
Wh required per kg of agarbatti dried
```

This number is more valuable than simply saying “solar-powered.”

---

## 18.5 Experiment 5 — Drying performance

Compare:

| Method | Drying time | Final moisture | Temperature exposure | Aroma score |
|---|---:|---:|---:|---:|
| Traditional | measure | measure | measure | measure |
| Dryer, no louver | measure | measure | measure | measure |
| Dryer + louver | measure | measure | measure | measure |

---

## 18.6 Experiment 6 — Packaging

Test:

### Seal quality

- seal width
- visual uniformity
- peel force

### Barrier

- WVTR if laboratory access exists
- practical moisture-ingress test if lab access does not exist

### Storage

Store samples under controlled humidity and compare:

```text
Day 0
Day 7
Day 30
Day 60
```

---

# 19. PACKAGING ECONOMICS — RECONCILIATION

The packaging document contains two different economic narratives.

### Narrative A — very low material package cost

The material-selection section states approximately:

> ₹2–3 per package

### Narrative B — all-in operating cost

The detailed cost model gives:

> **₹10.64 per package**

including:

- film
- printing
- thread
- labor
- depreciation
- overhead
- waste

These are not necessarily contradictory if clearly labeled.

### Correct way to explain them

```text
Barrier package material cost
        ≠
Total packaging operating cost
```

For SIH, use an explicit cost stack:

```text
Material
+ printing
+ labor
+ sealing
+ QA
+ waste
+ overhead
= all-in packaging cost
```

---

# 20. PACKAGING COST CONTRADICTION

The packaging document states:

- cotton thread about ₹0.50 per bundle in one section
- ₹5 per bundle in another

This is a factor-of-ten mismatch.

This must be corrected before presenting the economic model.

---

# 21. FULL SYSTEM ECONOMICS

The dryer documents contain several system-cost figures:

- ~₹24,500 baseline BOM in one SIH presentation
- ~₹26,500 revised core system
- ~₹28,500 revised system with optional cart
- ~₹29,500 original thermal-collector system
- ~₹31,000 / ₹32,000 retail figures in presentation variants

### Master rule

Do not present all of these simultaneously.

Create a single official costing sheet:

```text
Prototype BOM
Production BOM
Retail price
Subsidy assumption
Artisan purchase price
```

and give each a date/version.

---

# 22. ECONOMIC MODEL — CORRECT STRUCTURE

## 22.1 Per-artisan economics

The source documents attempt to link:

```text
Better drying
    ↓
Less rejection
    ↓
Better grade
    ↓
Better selling price
    ↓
Higher income
```

This is directionally logical, but the exact source figures such as:

- ₹18/kg
- ₹32/kg
- ₹28–35/kg
- +40–60%
- +₹2,500–3,500/month

must be validated with real buyer/trader data.

---

## 22.2 What should be measured

For each batch:

```text
Input mass
Good output mass
Rejected mass
Drying time
Final moisture
Fragrance score
Selling grade
Selling price
Packaging cost
Energy consumed
Labor time
```

Then compute actual contribution margin.

---

# 23. SCALABILITY ANALYSIS

The documents repeatedly reference:

> **1,850 artisans across 37 clusters / 5 states**

This should be treated as a **deployment scenario**, not proof that the system is already deployed at that scale.

The master scaling model should distinguish:

### Level 1 — laboratory

1 prototype

### Level 2 — pilot

5–10 dryers

### Level 3 — cluster

20–50 artisans

### Level 4 — multi-cluster

hundreds to thousands of users

At each level measure:

- maintenance rate
- downtime
- operator training hours
- spare-parts consumption
- real energy cost
- real income change
- adoption friction

---

# 24. SAFETY ARCHITECTURE

This system combines:

- DC battery current
- resistive heating
- moving fan
- servo mechanism
- hot sealing element
- flammable aromatic material

Therefore safety is not optional.

## 24.1 Electrical protection

Include:

- main fuse
- branch fuse for heater
- correctly rated wire gauge
- proper connectors
- strain relief
- battery protection
- over-current protection
- reverse-polarity protection
- protected enclosure for live terminals

---

## 24.2 Thermal protection

Use at least two layers:

```text
Software temperature control
        +
Independent hardware thermal cutoff
```

Never rely on Arduino software as the only safety mechanism.

---

## 24.3 Fire risk

The chamber contains combustible material and volatile fragrance compounds.

The prototype should therefore establish:

- maximum product temperature
- maximum heater surface temperature
- clearance from heater
- airflow path
- automatic heater shutdown
- emergency stop
- safe post-fault behavior

---

# 25. LOUVER FAILURE MODES

## Failure: Servo jam

Response:

```text
Detect temperature rise
        ↓
Heater OFF
        ↓
Fan HIGH if safe
        ↓
Alarm
        ↓
Manual inspection
```

---

## Failure: Microcontroller crash

Use a watchdog.

Independent high-temperature cutoff remains active.

---

## Failure: Louver stuck closed

Risk:

- temperature may increase

Mitigation:

- independent over-temperature cutoff

---

## Failure: Louver stuck open

Risk:

- drying may become slower

Mitigation:

- detect low temperature
- increase heater state if energy available

This is a **graceful-degradation** design principle.

---

# 26. PACKAGING FAILURE MODES

## Weak seal

Potential causes:

- insufficient heat
- insufficient dwell
- poor pressure
- contamination
- wrinkles
- incorrect film construction

---

## Burnt seal

Potential causes:

- excessive temperature
- excessive dwell
- excessive pressure
- incompatible film

---

## Moisture ingress despite good seals

Potential causes:

- barrier film inadequate
- laminate defects
- puncture
- storage humidity
- package geometry

The implementation guide correctly emphasizes distinguishing **seal failure** from **barrier failure**.

---

# 27. IMPLEMENTATION ROADMAP

## Phase 1 — Architecture freeze

Deliverables:

- one chamber geometry
- one heater rating
- one PV rating
- one battery chemistry
- one louver design
- one packaging material
- one moisture target

---

## Phase 2 — Mechanical prototype

Build:

- chamber
- racks
- louver
- heater duct
- fan mount
- packaging station

Deliverable:

> Complete dry mechanical prototype.

---

## Phase 3 — Electrical prototype

Integrate:

- PV
- controller
- battery
- heater
- fans
- sensors
- Arduino
- protection devices

Deliverable:

> Safe powered system without product.

---

## Phase 4 — Control integration

Implement:

- temperature hysteresis
- humidity logic
- louver control
- over-temperature protection
- watchdog
- data logging

Deliverable:

> Stable closed-loop operation.

---

## Phase 5 — Dummy-load validation

Measure:

- thermal uniformity
- humidity behavior
- energy consumption
- louver response
- battery autonomy

Deliverable:

> Engineering data set.

---

## Phase 6 — Real agarbatti testing

Use controlled batches.

Measure:

- moisture
- drying time
- aroma
- appearance
- breakage
- repeatability

Deliverable:

> Validated drying performance.

---

## Phase 7 — Packaging integration

Measure:

- seal time
- peel strength
- leak rate
- material cost
- operator time

Deliverable:

> Dry → QA → Pack → Seal workflow.

---

## Phase 8 — Pilot

Run repeated batches with actual users.

Measure:

- ease of use
- downtime
- training time
- maintenance
- acceptance
- economics

---

# 28. SIH PRESENTATION MASTER STORY

The supplied presentation and design guide strongly favor an evaluator flow built around:

```text
Problem
   ↓
Root cause
   ↓
System architecture
   ↓
Innovation
   ↓
Feasibility
   ↓
Measured impact
   ↓
Scalability
```

---

## Slide 1 — Administrative correctness

Show:

- PS ID 26022
- exact title
- theme
- category
- team details

Avoid changing the official title.

---

## Slide 2 — The problem and the system

Core statement:

> **The bottleneck is not simply production; it is drying and packaging without sacrificing product quality.**

Visual:

```text
Fresh sticks
   ↓
Weather-dependent drying
   ↓
Overheating / humidity / inconsistency
   ↓
Fragrance + quality loss
   ↓
Moisture re-absorption during manual packaging
   ↓
Lower-value product
```

Then:

```text
SMART CONTROLLED DRYING
+
LOUVER
+
IMMEDIATE BARRIER PACKAGING
```

---

## Slide 3 — Technical architecture

Show one clean architecture diagram.

Must include:

- energy source
- controller
- heater
- sensors
- fan
- louver
- chamber
- logging
- packaging

---

## Slide 4 — Feasibility

Use four dimensions:

### Technical

Can it be built from available components?

### Financial

What is the realistic BOM and operating cost?

### Market

Who uses it and why would they adopt it?

### Operational

Can an artisan run it safely with minimal training?

---

## Slide 5 — Impact

Do not lead with unsupported percentage claims.

Lead with measurable engineering variables:

```text
Drying time
Moisture consistency
Maximum product temperature
Fragrance score
Breakage rate
Packaging defect rate
Energy per kg
Cost per kg
```

Then convert those into economic outcomes after validation.

---

## Slide 6 — Research

Organize references into:

- drying thermodynamics
- psychrometrics
- agarbatti / fragrance science
- barrier packaging
- heat sealing
- solar energy
- rural deployment
- government context

Do not present invented or unverified references.

---

# 29. JUDGE-DEFENSE POSITION

## Q: Why not just use a conventional electric dryer?

Answer structure:

```text
Conventional dryer
      ↓
heat + airflow

Our system
      ↓
heat + airflow + moisture-state monitoring
      ↓
temperature protection
      ↓
fragrance-oriented control
      ↓
immediate barrier packaging
```

The distinction must be demonstrated experimentally.

---

## Q: Why does the louver matter if you already have a thermostat?

Answer:

> The thermostat controls heat input. The louver additionally controls the air stream by changing the mixture of hot and ambient air, so it can influence both temperature and ventilation.

Then show data.

---

## Q: Can 100 W solar run a 300 W heater continuously?

Correct answer:

> No, not continuously. The current concept relies on duty cycling and battery buffering. We are therefore validating the actual energy balance and may resize the heater, PV array, or battery based on measured Wh/kg drying demand.

This is a much stronger engineering answer than pretending the numbers are already compatible.

---

## Q: Is the 93% fragrance-retention number experimentally proven?

Correct answer:

> It is a design/reference claim in our current documentation. The prototype validation will establish the measured retention under a defined test protocol.

---

## Q: Why use Kraft + LDPE?

Answer:

- low-cost
- locally manufacturable
- compatible with impulse sealing
- paper exterior improves handling/branding
- polymer layer provides the sealing/barrier function

Then acknowledge end-of-life limitations honestly.

---

# 30. MASTER DATA LOG FORMAT

Each batch should produce one machine-readable row set.

```csv
batch_id,
date,
ambient_temp,
ambient_rh,
inlet_temp,
inlet_rh,
mid_temp,
mid_rh,
outlet_temp,
outlet_rh,
louver_angle,
fan_pwm,
heater_state,
battery_voltage,
battery_current,
pv_voltage,
pv_current,
initial_mass,
final_mass,
initial_moisture,
final_moisture,
drying_time_min,
aroma_score_day0,
aroma_score_day7,
aroma_score_day30,
aroma_score_day60,
breakage_count,
packaging_defects,
seal_peel_force,
package_material_batch
```

This dataset becomes the foundation for:

- engineering plots
- SIH evidence
- troubleshooting
- future ML optimization
- quality assurance
- lifecycle economics

---

# 31. WHAT THE TEAM SHOULD PROVE

The project becomes technically persuasive when it can demonstrate these six things:

## Proof 1 — Temperature control

```text
Target range
vs.
measured chamber temperature
```

## Proof 2 — Uniform drying

```text
Rack-to-rack moisture variation
```

## Proof 3 — Moisture removal

```text
Moisture %
vs.
time
```

## Proof 4 — Fragrance preservation

```text
Aroma / chemical retention
vs.
control
```

## Proof 5 — Energy feasibility

```text
Wh/kg
PV generation
battery behavior
```

## Proof 6 — Packaging retention

```text
seal strength
moisture ingress
storage performance
```

---

# 32. CONTRADICTION / CLEAN-UP REGISTER

This section is mandatory before any external submission.

| Issue | Source variants | Why it matters | Action |
|---|---|---|---|
| PV size | 50 W vs 100 W | Changes energy model | Freeze one |
| Heater power | 300 W | High battery current | Validate or resize |
| Battery | 20 Ah variants | Runtime changes | Freeze chemistry + usable Wh |
| System mass | <15, 18, 20, 22 kg | Portability claim | Weigh prototype |
| Chamber size | 60×60×80 cm vs 1 m tall / 0.5 m² | Airflow/CAD mismatch | Freeze geometry |
| Moisture endpoint | 10% vs 12–15% | Product release ambiguity | Validate measurement method |
| Packaging WVTR | <5 vs <8 | Material qualification | Freeze criterion |
| Seal temperature | 50–80 vs 100–130 / 120–125 | Process inconsistency | Separate transition vs sealing range |
| Seal cycle | 2–3 s vs ~5–6 s | Throughput mismatch | Define dwell vs total cycle |
| Thread cost | ₹0.50 vs ₹5 | Economic model error | Correct source |
| Package material cost | ₹2–3 vs ₹6 film component | Cost-definition ambiguity | Define material vs all-in |
| Aroma retention | 75%, 93%, 95%, 55% control | Risk of overclaiming | Replace with measured results |
| Income impact | Multiple ₹/kg and monthly figures | Depends on market data | Treat as scenario only |
| Scale | 1,850 artisans | Deployment scenario, not demonstrated deployment | Label as target |
| “First” / “only” claims | Repeated in presentation | Requires literature/patent search | Verify before public use |

---

# 33. CLAIM MATURITY MATRIX

Use the following rule for all presentation language.

### GREEN — safe as design fact

Examples:

- “The prototype includes a servo-driven louver.”
- “The system logs temperature and humidity.”
- “The package uses a heat-sealed polymer barrier concept.”

### YELLOW — design target

Examples:

- “We target 40–45°C.”
- “We target >2.5 N/15 mm peel strength.”
- “We target a specific moisture endpoint.”

### RED — must have evidence

Examples:

- “93% fragrance retention.”
- “60% higher income.”
- “100% uniform drying.”
- “Zero fungal growth.”
- “First system of its kind.”
- “Validated by CFD.”
- “All-weather operation.”
- “1,850-artisan deployment feasibility.”

---

# 34. FINAL MASTER DESIGN PHILOSOPHY

The project should be presented as:

> **A controlled post-production quality system for agarbatti, not merely a solar dryer.**

Its value chain is:

```text
                 ENERGY
                   │
                   ▼
            ┌─────────────┐
            │ CONTROLLED  │
            │    HEAT     │
            └──────┬──────┘
                   │
        ┌──────────▼──────────┐
        │   AIRFLOW + RH      │
        │   MANAGEMENT        │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │ THERMAL LOUVER      │
        │ OVERHEAT PROTECTION │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │ UNIFORM DRYING      │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │ MOISTURE + QA       │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │ BARRIER PACKAGING   │
        │ + HEAT SEAL         │
        └──────────┬──────────┘
                   │
                   ▼
          STABLE SALEABLE
             AGARBATTI
```

The strongest engineering narrative is therefore:

> **Control moisture without overheating. Preserve quality before packaging. Lock that quality in after drying. Measure the whole chain.**

---

# 35. IMMEDIATE ENGINEERING CHECKLIST

Before final SIH submission, the team should freeze and verify:

- [ ] Final chamber dimensions
- [ ] Final chamber mass
- [ ] Final rack count
- [ ] Final heater power
- [ ] Final PV size
- [ ] Final battery chemistry and usable Wh
- [ ] Current draw of heater and fans
- [ ] Fuse ratings
- [ ] Independent thermal cutoff
- [ ] Final sensor configuration
- [ ] Final louver geometry
- [ ] Final control algorithm
- [ ] Moisture measurement method
- [ ] Final moisture acceptance criterion
- [ ] Final packaging material
- [ ] WVTR specification
- [ ] Seal temperature
- [ ] Seal dwell time
- [ ] Peel-strength test method
- [ ] Actual packaging material cost
- [ ] Actual total BOM
- [ ] Actual measured drying time
- [ ] Actual energy per kg
- [ ] Actual aroma test protocol
- [ ] Actual validation data
- [ ] Evidence for all “first / only / unique” claims

---

# 36. ONE-SENTENCE PROJECT DEFINITION

> **A portable smart agarbatti post-production system that controls drying temperature, airflow and humidity to protect product quality, then immediately creates a repeatable moisture-barrier seal so the value gained during drying is not lost in storage.**

---

# 37. DOCUMENT STATUS

**Status:** Master synthesis / engineering review  
**Basis:** Eight supplied project documents  
**Purpose:** Single reference for architecture, prototype, validation, economics, implementation, and SIH communication  
**Critical next step:** Freeze the conflicting engineering parameters and replace projected performance numbers with measured prototype data.

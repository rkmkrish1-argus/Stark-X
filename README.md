# ⚡ Stark-X — Smart Solar-Powered Agarbatti Drying Chamber

> **SIH 2026 | Problem Statement: PS 26022**  
> Team Project: Smart Thermal Drying with Dynamic Louver Control & Fragrance Retention

---

## 🌟 Overview

**Stark-X** (also known as **AgarDry**) is an innovative, off-grid solar-powered Agarbatti (incense stick) drying system designed for Small and Micro Enterprise (SME) and Self Help Group (SHG) manufacturers in rural India.

Traditional sun-drying of agarbatti is slow, weather-dependent, and causes fragrance loss. Stark-X replaces this with a **controlled thermal chamber** that:

- 🌞 Harnesses solar energy through an **insulated polycarbonate chamber**
- 🔁 Actively manages temperature and humidity via **dynamic thermal louvers** (0°–30° actuation)
- 💨 Controls airflow using **PWM-modulated fans** for optimal moisture evacuation
- 🌸 Minimizes **fragrance loss** by maintaining precise drying conditions (≤ 48°C)
- 📡 Operates fully **off-grid** with a 24V DC power architecture

---

## 📁 Repository Contents

| File / Folder | Description |
|---|---|
| `dryer_digital_twin.html` | Interactive Canvas-based Digital Twin simulation of the drying chamber |
| `agarbatti_louver_flow_system.png` | Thermal louver airflow system diagram |
| `Power Section Module Wiring Diagram.pdf` | Complete 24V DC electrical wiring diagram |
| `VID 1.mp4` | Prototype demonstration / concept video |
| `README.md` | This file |

---

## 🖥️ Digital Twin Simulation

The `dryer_digital_twin.html` file is a **fully self-contained, offline-capable** HTML5 simulation:

- **Lumped Thermal Physics Model** — Real-time temperature, humidity, and moisture kinetics
- **Dynamic Louver Angle Control** — Slide louvers from 0° (closed) to 30° (open) to control airflow
- **PWM Fan Speed Control** — Humidity evacuation rate control
- **Real-Time Plotting** — Moisture content vs. time and drying chamber temperature
- **Solar Insolation Slider** — Simulate variable cloud cover and time-of-day effects
- **Dark/Light Mode** — Professional UI with responsive layout

▶ **Just open `dryer_digital_twin.html` in any modern browser — no installation required.**

---

## 🔗 Related Repositories

| Repository | Purpose |
|---|---|
| [Stark-X](https://github.com/rkmkrish1-argus/Stark-X) | ← **This Repo** — Main hardware, simulation, CAD & assets |
| [Stark-X WebPrototype](https://github.com/rkmkrish1-argus/Stark-X_-WebPrototype) | Live web prototype & GitHub Pages deployment |

---

## ⚙️ System Architecture

```
Solar Radiation
      │
      ▼
┌─────────────────────────────┐
│  Polycarbonate Solar Chamber │ ← Passive heating via GHE
│  (Insulated double-wall)     │
│                              │
│  ┌─────────────────────┐    │
│  │  Agarbatti Drying    │    │ ← Temp held ≤ 48°C
│  │  Trays (Stacked)     │    │   RH evacuated by fan
│  └─────────────────────┘    │
│                              │
│  [Thermal Louvers 0°–30°] ←─┼─── PWM Servo / Manual
│  [PWM Exhaust Fan]      ←───┼─── 24V DC Controller
│  [Temp/RH Sensors]      ←───┘
└─────────────────────────────┘
         │
    [24V Battery Bank] ← Solar Panel → Charge Controller
```

---

## 📐 Key Engineering Parameters

| Parameter | Value |
|---|---|
| Target drying temperature | ≤ 48°C |
| Louver actuation range | 0° – 30° |
| Power architecture | 24V DC |
| Chamber material | Twinwall polycarbonate |
| Target moisture reduction | ≥ 35% → ≤ 12% MC |
| Operation mode | Off-grid, solar-only |

---

## 👥 Team & Context

- **Competition:** Smart India Hackathon 2026 (SIH 2026)
- **Problem Statement:** PS 26022 — Smart Solar-Powered Agarbatti Drying
- **GitHub Account:** [rkmkrish1-argus](https://github.com/rkmkrish1-argus)

---

*Built with engineering rigor, simulation-first design, and a mission to empower rural artisans.* 🙏

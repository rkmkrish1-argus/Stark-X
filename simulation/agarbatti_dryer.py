"""
Parametric CAD model: Solar agarbatti dryer with thermal louver system
Run:   python agarbatti_dryer.py --angle 30
Sweep: python agarbatti_dryer.py --sweep      (makes 15/30/45 deg versions)
Outputs (in ./output):
  dryer_assembly_<angle>.step  -> full machine (open in Fusion 360 / SolidWorks)
  dryer_fluid_<angle>.step     -> simplified air volume (import to SimScale / ANSYS)
  louver_only_<angle>.step     -> louver module alone (fast CFD test)
Units: millimetres. X = width (left intake -> right exhaust), Y = depth (front = -Y), Z = up.
"""
import argparse, os, math
import cadquery as cq

# ------------------------------------------------------------------ PARAMETERS
P = dict(
    W=600, D=500, H=600,          # chamber outer width / depth / height
    wall=20,                      # insulated wall thickness
    base_h=100,                   # control-panel plinth height
    n_trays=5, tray_gap=85, tray_t=6, tray_margin=40, tray_first_z=60,
    hole=8, hole_pitch=20,        # tray perforations
    # louver modules
    louver_w=240, louver_h=300, louver_depth=60, n_blades=6, blade_t=3,
    louver_angle=30,              # blade tilt from horizontal (deg): 0 = fully open, ~75 = closed
    # fans (square PWM fans)
    fan=120, fan_t=25,
    # solar panel
    pv_l=700, pv_w=450, pv_t=30, pv_tilt=20,
    # side units
    batt=(250, 300, 200), sealer=(300, 250, 220),
)

def box(x, y, z, cx=0, cy=0, cz=0):
    """Box centred at (cx,cy,cz)."""
    return cq.Workplane("XY").box(x, y, z).translate((cx, cy, cz))

# ------------------------------------------------------------------ LOUVER MODULE
def louver_module(p, angle):
    """Louver built with flow along +X. Returns (frame, blades) centred at origin."""
    d, w, h = p["louver_depth"], p["louver_w"], p["louver_h"]
    t = 8  # frame thickness
    frame = box(d, w, h).cut(box(d + 2, w - 2 * t, h - 2 * t))
    blades = None
    pitch = (h - 2 * t) / p["n_blades"]
    blade_chord = pitch * 1.25          # slight overlap when closed
    for i in range(p["n_blades"]):
        z = -h / 2 + t + pitch * (i + 0.5)
        b = (box(blade_chord, w - 2 * t, p["blade_t"])
             .rotate((0, 0, 0), (0, 1, 0), -angle)
             .translate((0, 0, z)))
        blades = b if blades is None else blades.union(b)
    return frame, blades

def fan_unit(p):
    f, th = p["fan"], p["fan_t"]
    body = box(th, f, f).cut(
        cq.Workplane("YZ").circle(f * 0.45).extrude(th + 2).translate((-th / 2 - 1, 0, 0)))
    hub = cq.Workplane("YZ").circle(f * 0.18).extrude(th * 0.8).translate((-th * 0.4, 0, 0))
    blades = None
    for k in range(7):
        bl = (box(th * 0.6, f * 0.34, 3, 0, f * 0.27, 0)
              .rotate((0, 0, 0), (1, 0, 0), 25)
              .rotate((0, 0, 0), (1, 0, 0), k * 360 / 7))
        blades = bl if blades is None else blades.union(bl)
    return body, hub.union(blades)

# ------------------------------------------------------------------ MAIN BUILD
def build(angle):
    p = P.copy(); p["louver_angle"] = angle
    W, D, H, wl, bh = p["W"], p["D"], p["H"], p["wall"], p["base_h"]
    zc = bh + H / 2                                   # chamber centre height
    asm = cq.Assembly(name="agarbatti_dryer")
    green, steel, glass = (0.05, 0.28, 0.15), (0.75, 0.77, 0.8), (0.6, 0.85, 1.0)

    # --- base plinth + knob/LED panel
    base = box(W, D, bh, 0, 0, bh / 2)
    asm.add(base, name="base", color=cq.Color(*green, 1))
    for i, c in enumerate([(1, 0, 0), (0, 0.8, 0), (1, 0.6, 0)]):
        led = cq.Workplane("XZ").circle(8).extrude(6).translate((60 + 45 * i, -D / 2, bh / 2))
        asm.add(led, name=f"led{i}", color=cq.Color(*c, 1))
    knob = cq.Workplane("XZ").circle(22).extrude(20).translate((-40, -D / 2, bh / 2))
    asm.add(knob, name="knob", color=cq.Color(0.1, 0.1, 0.1, 1))
    for sx in (-1, 1):
        for sy in (-1, 1):
            foot = cq.Workplane("XY").circle(18).extrude(12).translate((sx * (W / 2 - 40), sy * (D / 2 - 40), -12))
            asm.add(foot, name=f"foot{sx}{sy}", color=cq.Color(0.1, 0.1, 0.1, 1))

    # --- chamber shell (front open), with wall openings for intake/exhaust
    shell = box(W, D, H, 0, 0, zc).cut(box(W - 2 * wl, D - wl, H - 2 * wl, 0, -wl / 2 - 0.5, zc))
    lw, lh = p["louver_w"] - 16, p["louver_h"] - 16
    z_in, z_out = bh + H * 0.42, bh + H * 0.62
    shell = shell.cut(box(wl + 2, lw, lh, -W / 2 + wl / 2, 0, z_in))
    shell = shell.cut(box(wl + 2, lw, lh, W / 2 - wl / 2, 0, z_out))
    asm.add(shell, name="chamber", color=cq.Color(*green, 1))

    # --- door frame + glass
    dw, dh = W - 2 * wl, H - 2 * wl
    door = box(dw, 12, dh, 0, -D / 2 - 6, zc).cut(box(dw - 60, 14, dh - 60, 0, -D / 2 - 6, zc))
    asm.add(door, name="door_frame", color=cq.Color(*steel, 1))
    asm.add(box(dw - 56, 4, dh - 56, 0, -D / 2 - 6, zc), name="door_glass", color=cq.Color(*glass, 0.3))
    handle = box(14, 14, 160, W / 2 - 45, -D / 2 - 25, zc)
    asm.add(handle, name="handle", color=cq.Color(0.1, 0.1, 0.1, 1))

    # --- trays (perforated) + side rails
    tw, td = W - 2 * wl - 2 * p["tray_margin"] / 2, D - wl - 2 * p["tray_margin"]
    pts = [(x, y)
           for x in [i * p["hole_pitch"] - tw / 2 + 25 for i in range(int(tw // p["hole_pitch"]) - 1)]
           for y in [j * p["hole_pitch"] - td / 2 + 25 for j in range(int(td // p["hole_pitch"]) - 1)]]
    tray = box(tw, td, p["tray_t"]).cut(
        cq.Workplane("XY").pushPoints(pts).circle(p["hole"] / 2).extrude(p["tray_t"] + 2)
        .translate((0, 0, -p["tray_t"] / 2 - 1)))
    for i in range(p["n_trays"]):
        z = bh + wl + p["tray_first_z"] + i * p["tray_gap"]
        asm.add(tray.translate((0, -wl / 2, z)), name=f"tray{i+1}", color=cq.Color(*steel, 1))
        for s in (-1, 1):
            asm.add(box(10, td, 8, s * (tw / 2 + 5), -wl / 2, z - 7), name=f"rail{i+1}_{s}",
                    color=cq.Color(*steel, 1))

    # --- heater coil (top of chamber) + sensor stick
    heater = (cq.Workplane("YZ").circle(9).extrude(W - 2 * wl - 80)
              .translate((-(W - 2 * wl - 80) / 2, 0, bh + H - wl - 45)))
    asm.add(heater, name="heater_coil", color=cq.Color(1, 0.35, 0.05, 1))
    asm.add(cq.Workplane("XY").circle(6).extrude(90).translate((W / 2 - 80, 0, bh + H - wl - 130)),
            name="sensor_TRH", color=cq.Color(0.9, 0.9, 0.9, 1))

    # --- intake side (left): louver + fan + baffle duct
    frame, blades = louver_module(p, angle)
    fan_body, fan_rotor = fan_unit(p)
    ld = p["louver_depth"]
    x_l = -W / 2 - ld / 2
    asm.add(frame.translate((x_l, 0, z_in)), name="intake_louver_frame", color=cq.Color(*steel, 1))
    asm.add(blades.translate((x_l, 0, z_in)), name="intake_louver_blades", color=cq.Color(0.85, 0.87, 0.9, 1))
    x_f = -W / 2 + wl + p["fan_t"] / 2 + 5
    asm.add(fan_body.translate((x_f, 0, z_in)), name="intake_fan", color=cq.Color(0.1, 0.1, 0.1, 1))
    asm.add(fan_rotor.translate((x_f, 0, z_in)), name="intake_fan_rotor", color=cq.Color(0.2, 0.2, 0.2, 1))
    baffle = box(60, D - 2 * wl - 40, 6, -W / 2 + wl + 80, 0, bh + H - wl - 20)   # air baffle / duct plate
    asm.add(baffle, name="air_baffle", color=cq.Color(*steel, 1))

    # --- exhaust side (right): fan + louver
    x_r = W / 2 + ld / 2
    asm.add(frame.translate((x_r, 0, z_out)), name="exhaust_louver_frame", color=cq.Color(*steel, 1))
    asm.add(blades.translate((x_r, 0, z_out)), name="exhaust_louver_blades", color=cq.Color(0.85, 0.87, 0.9, 1))
    x_f2 = W / 2 - wl - p["fan_t"] / 2 - 5
    asm.add(fan_body.translate((x_f2, 0, z_out)), name="exhaust_fan", color=cq.Color(0.1, 0.1, 0.1, 1))
    asm.add(fan_rotor.translate((x_f2, 0, z_out)), name="exhaust_fan_rotor", color=cq.Color(0.2, 0.2, 0.2, 1))

    # --- solar panel on tilted stand
    pv = (box(p["pv_l"], p["pv_w"], p["pv_t"])
          .rotate((0, 0, 0), (1, 0, 0), p["pv_tilt"])
          .translate((0, 0, bh + H + 130)))
    asm.add(pv, name="solar_panel", color=cq.Color(0.05, 0.1, 0.35, 1))
    for s in (-1, 1):
        leg = box(12, 12, 130, s * 250, 20, bh + H + 65)
        asm.add(leg, name=f"pv_leg{s}", color=cq.Color(*steel, 1))

    # --- battery box (left of base) and sealer (right of base)
    bx, by, bz = p["batt"]
    asm.add(box(bx, by, bz, -W / 2 - bx / 2 + 30, 0, bz / 2), name="battery_box", color=cq.Color(*green, 1))
    sx, sy, sz = p["sealer"]
    asm.add(box(sx, sy, sz, W / 2 + sx / 2 - 10, 0, sz / 2), name="sealer_body", color=cq.Color(*green, 1))
    roller = cq.Workplane("XZ").circle(28).extrude(sy - 40).translate((W / 2 + sx / 2, sy / 2 - 20, sz + 28))
    asm.add(roller, name="sealer_roller", color=cq.Color(0.8, 0.5, 0.2, 1))

    # --- simplified fluid domain for CFD (air volume only)
    inner = box(W - 2 * wl, D - wl, H - 2 * wl, 0, -wl / 2, zc)
    duct_in = box(wl + ld, lw, lh, -W / 2 - ld / 2 + wl / 2, 0, z_in)
    duct_out = box(wl + ld, lw, lh, W / 2 + ld / 2 - wl / 2, 0, z_out)
    fluid = inner.union(duct_in).union(duct_out)

    # --- louver-only test article (fast CFD): louver in a 500 mm straight duct
    lf, lb = louver_module(p, angle)
    louver_only = lf.union(lb)

    return asm, fluid, louver_only, p

def export(angle, outdir="output"):
    os.makedirs(outdir, exist_ok=True)
    asm, fluid, lv, p = build(angle)
    asm.save(f"{outdir}/dryer_assembly_{angle}.step")
    cq.exporters.export(fluid, f"{outdir}/dryer_fluid_{angle}.step")
    cq.exporters.export(lv, f"{outdir}/louver_only_{angle}.step")
    # quick free-area estimate: open face area after blades (projection) -> feeds your 1D model
    pitch = (p["louver_h"] - 16) / p["n_blades"]
    open_frac = max(0.0, 1 - (pitch * 1.25 * math.sin(math.radians(angle))) / pitch)
    print(f"[{angle:>2} deg] exported. Approx. free-area fraction ~ {open_frac:.2f} "
          f"(geometric estimate only; get real dP from CFD).")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--angle", type=float, default=30)
    ap.add_argument("--sweep", action="store_true")
    a = ap.parse_args()
    for ang in ([15, 30, 45] if a.sweep else [a.angle]):
        export(ang)

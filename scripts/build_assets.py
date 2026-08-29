#!/usr/bin/env python3
"""Regenerate the SVG assets for the profile overview.

    python3 scripts/build_assets.py

Every asset is drawn twice, once for light mode and once for dark mode.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from draw import (ANIM, DARK, LIGHT, MONO, SANS, arrow, chip, circle, corner_ticks, delay,
                  draw_line, esc, head, line, path, r, rect, text, tw)
import repos as R

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
CARDS = os.path.join(ASSETS, "cards")

MONTHS = {"Mar": "March", "Apr": "April", "May": "May", "Jul": "July", "Aug": "August"}
N = len(R.REPOS)


def dcolor(P, repo):
    return P["div"][R.DIVISION_INDEX[repo["div"]]]


def dname(repo):
    return R.DIVISIONS[R.DIVISION_INDEX[repo["div"]]][1]


# ----------------------------------------------------------------- emblems
def emblem(kind, P):
    a, ln, sf = P["accent"], P["border"], P["surface"]
    nd = P["line"]
    o = []
    if kind == "federated":
        cx = cy = 42
        for i in range(6):
            ang = math.radians(-90 + i * 60)
            x, y = cx + 32 * math.cos(ang), cy + 32 * math.sin(ang)
            o.append(line(cx, cy, x, y, ln))
            o.append(circle(x, y, 5, fill=sf, stroke=nd, sw=1.3))
            if i in (1, 4):
                o.append(circle(x, y, 5, fill=a))
        o.append(path("M42 26 l14 5 v12 c0 8 -6 13 -14 16 c-8 -3 -14 -8 -14 -16 v-12 z",
                      fill=sf, stroke=a, sw=1.7))
        o.append(path("M36 42 l4 4 l9 -9", stroke=a, sw=1.7))
    elif kind == "shield-check":
        o.append(path("M42 8 l26 10 v22 c0 17 -11 27 -26 34 c-15 -7 -26 -17 -26 -34 v-22 z",
                      fill=sf, stroke=nd, sw=1.4))
        o.append(path("M30 42 l8 9 l17 -20", stroke=a, sw=2.1))
        for i, y in enumerate((20, 30, 40)):
            o.append(line(4, y + 14, 12, y + 14, ln))
    elif kind == "shield-loop":
        o.append(path("M42 8 l26 10 v22 c0 17 -11 27 -26 34 c-15 -7 -26 -17 -26 -34 v-22 z",
                      fill=sf, stroke=nd, sw=1.4))
        o.append(path("M31 44 a11 11 0 1 1 4 8", stroke=a, sw=1.9))
        o.append(path("M31 36 v8 h8", stroke=a, sw=1.9))
        o.append(circle(42, 44, 3, fill=a))
    elif kind == "airgap":
        for gx, filled in ((14, False), (66, True)):
            for dy in (-16, 0, 16):
                o.append(circle(gx, 42 + dy, 5, fill=a if filled and dy == 0 else sf,
                                stroke=nd, sw=1.3))
            o.append(line(gx, 26, gx, 58, ln))
        o.append(line(42, 12, 42, 72, a, sw=1.6, dash="4 5", opacity=0.85))
        o.append(line(19, 42, 32, 42, ln))
        o.append(line(52, 42, 61, 42, ln))
    elif kind == "recover":
        o.append(path("M20 52 a24 24 0 1 1 9 17", stroke=nd, sw=1.5))
        o.append(path("M20 40 v12 h12", stroke=a, sw=1.8))
        for i, h in enumerate((10, 18, 26)):
            o.append(rect(32 + i * 11, 56 - h, 7, h, fill=a if i == 2 else sf,
                          stroke=nd if i != 2 else None, rx=1.5))
    return "<g transform=\"translate(24,22)\">" + "".join(o) + "</g>"


EMBLEM = {
    "Sentinel-FL": ("federated", "a ring of six federated nodes around a shield"),
    "Actionguard-CI": ("shield-check", "a shield carrying a verification tick"),
    "Actionguard-Autoaudit": ("shield-loop", "a shield around a remediation loop"),
    "Airgap-noc-Copilot": ("airgap", "two node clusters split by a dashed air gap"),
    "RecoverOS": ("recover", "a recovery loop lifting three rising bars"),
}


# -------------------------------------------------------------------- card
def card(repo, P):
    W, H = 1200, 128
    kind, emblem_desc = EMBLEM[repo["name"]]
    exp = f"EXP-{repo['n']:02d}"
    desc = (f"Specimen plate for experiment {repo['n']}, {repo['label']}. "
            f"Division: {dname(repo)}. Primary language: {repo['lang']}. "
            f"Emblem: {emblem_desc}. Pipeline: " + ", then ".join(repo["pipeline"]) + ".")
    o = [head(W, H, f"{exp} {repo['label']}", desc)]
    a = dcolor(P, repo)
    o.append(rect(0, 0, W, H, fill=P["bg"]))
    o.append(rect(1, 1, W - 2, H - 2, fill=P["panel"], stroke=P["border"], rx=10))
    o.append(rect(1, 1, 4, H - 2, fill=a, rx=2))
    o.append(rect(3, 1, 2, H - 2, fill=a))
    o.append(f'<g class="fi" style="animation-delay:0.05s">{emblem(kind, P)}</g>')
    o.append(line(116, 24, 116, 104, P["border"]))

    o.append(text(130, 34, exp, 10, a, 700, mono=True, ls=2))
    tick = 130 + tw(exp, 10, mono=True, ls=2) + 12
    o.append(line(tick, 22, tick, 36, P["line"]))
    o.append(text(tick + 14, 34, dname(repo).upper(), 9, P["mute"], 600, mono=True, ls=1.8))
    o.append(text(130, 66, repo["label"], 21, P["ink"], 600))
    o.append(text(130, 88, repo["blurb"], 12.5, P["mid"]))

    x = 130
    for label in [repo["lang"]] + ([repo["licence"]] if repo["licence"] else []):
        s, w = chip(x, 100, label, P)
        o.append(s)
        x += w + 6

    # pipeline
    px0, px1 = 560, 1172
    o.append(text(px0, 34, "PIPELINE", 8.5, P["mute"], 600, mono=True, ls=1.8))
    o.append(circle(px0 - 9, 64, 2.4, fill=a))
    widths = [tw(s, 10) + 20 for s in repo["pipeline"]]
    gap = (px1 - px0 - sum(widths)) / (len(widths) - 1)
    x = px0
    for i, (label, w) in enumerate(zip(repo["pipeline"], widths)):
        o.append(rect(x, 52, w, 24, fill=P["surface"], stroke=P["border"], rx=5))
        o.append(text(x + w / 2, 67.5, label, 10, P["ink"], anchor="middle"))
        x += w
        if i < len(widths) - 1:
            o.append(line(x + 3, 64, x + gap - 7, 64, P["line"]))
            o.append(arrow(x + gap - 8, 64, a))
            x += gap
    o.append(corner_ticks(W, H, P, inset=12))
    return "".join(o) + "</svg>"


# -------------------------------------------------------------------- hero
def hero(P):
    W, H = 1200, 580
    desc = (f"Title card. The question: what happens when the model is wrong? "
            f"{N} experiments arranged on a ring in five divisions -- autonomous agents, "
            f"grounded retrieval, perception and vision, systems and simulation, security and "
            f"assurance -- joined by the technologies they share. Readouts: {N} experiments, "
            f"5 divisions, 6 months, 1 live deployment.")
    o = [head(W, H, "Tayab Ahamed N -- AI Research and Engineering Lab", desc)]
    o.append(rect(0, 0, W, H, fill=P["bg"]))
    o.append('<g class="fu">')
    o.append(text(56, 62, "TAYAB AHAMED N", 11, P["ink"], 700, mono=True, ls=3.4))
    o.append(line(208, 52, 208, 66, P["line"]))
    o.append(text(224, 62, "AI RESEARCH AND ENGINEERING LAB", 10, P["mute"], 600, mono=True, ls=2.4))
    o.append(text(1144, 62, "EST 2026", 10, P["mute"], 600, anchor="end", mono=True, ls=2.4))
    o.append("</g>")
    o.append(line(56, 84, 1144, 84, P["border"]))

    o.append('<g class="fu" style="animation-delay:0.06s">')
    for i, ln in enumerate(("What happens", "when the model", "is wrong?")):
        o.append(text(56, 168 + i * 52, ln, 42, P["ink"], 600))
    o.append("</g>")
    o.append('<g class="fu" style="animation-delay:0.12s">')
    for i, ln in enumerate((
            f"{N} experiments in five divisions. Each one takes a single",
            "question into a different domain: what the system does when",
            "the model is uncertain, unavailable or simply wrong.")):
        o.append(text(56, 330 + i * 22, ln, 13.5, P["mid"]))
    o.append("</g>")

    stats = [(str(N), "EXPERIMENTS"), ("5", "DIVISIONS"), ("6", "MONTHS"), ("1", "LIVE DEPLOYMENT")]
    o.append(line(56, 420, 560, 420, P["border"]))
    x = 56
    for i, (val, label) in enumerate(stats):
        o.append(text(x, 466, val, 30, P["ink"], 600))
        o.append(text(x, 490, label, 8.5, P["mute"], 600, mono=True, ls=1.6))
        x += max(tw(label, 8.5, mono=True, ls=1.6), 60) + 28

    # ring
    cx, cy, rad = 880, 300, 168
    o.append('<g class="fi" style="animation-delay:0.3s">')
    o.append(circle(cx, cy, rad, stroke=P["border"], sw=1))
    o.append(circle(cx, cy, rad - 46, stroke=P["border"], sw=1, opacity=0.5))
    pts = []
    order = sorted(R.REPOS, key=lambda q: (R.DIVISION_INDEX[q["div"]], q["n"]))
    for i, repo in enumerate(order):
        ang = math.radians(-90 + i * 360.0 / N)
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang), repo))
    # chords between repositories sharing two or more technologies
    k = 0
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            shared = set(pts[i][2]["tech"]) & set(pts[j][2]["tech"])
            if len(shared) >= 3:
                o.append(draw_line(pts[i][0], pts[i][1], pts[j][0], pts[j][1], P["line"],
                                   opacity=0.55, d=0.45 + k * 0.03))
                k += 1
    for i, (x0, y0, repo) in enumerate(pts):
        o.append('<g class="fu" style="%s">' % delay(0.5 + i * 0.035))
        o.append(circle(x0, y0, 6.5, fill=P["surface"], stroke=dcolor(P, repo), sw=1.6))
        o.append(circle(x0, y0, 3, fill=dcolor(P, repo)))
        o.append("</g>")
    o.append(circle(cx, cy, 3.2, fill=P["accent"]))
    o.append(circle(cx, cy, 3.2, fill=P["accent"], cls="pu"))
    o.append("</g>")

    # legend, two columns under the ring
    lx = [660, 900]
    for i, (key, name, _q) in enumerate(R.DIVISIONS):
        col, row = i % 2, i // 2
        x0 = lx[col]
        y0 = 508 + row * 22
        o.append(circle(x0, y0 - 3.5, 3.4, fill=P["div"][i]))
        o.append(text(x0 + 10, y0, name, 10.5, P["mid"]))
    o.append(corner_ticks(W, H, P, inset=18))
    return "".join(o) + "</svg>"


# ---------------------------------------------------------------- registry
def registry(P):
    rows = sorted(R.REPOS, key=lambda q: q["n"])
    rh = 30
    W = 1200
    H = 150 + rh * len(rows) + 44
    desc = (f"A numbered register of {N} experiments, 001 to {N:03d}, each with its division, "
            "derived state, primary language and month of creation. State is derived: deployed "
            "means a public URL exists, open means an OSI licence, prototype means neither.")
    o = [head(W, H, "Experiment registry", desc)]
    o.append(rect(0, 0, W, H, fill=P["bg"]))
    o.append(text(56, 54, "EXPERIMENT REGISTRY", 10, P["mute"], 600, mono=True, ls=3))
    o.append(text(56, 88, "Everything, in order", 26, P["ink"], 600))
    o.append(text(1144, 88, f"{N:03d} / {N:03d}", 26, P["mute"], 300, anchor="end"))
    cols = ((56, "NO"), (132, "EXPERIMENT"), (486, "DIVISION"), (760, "STATE"),
            (900, "LANGUAGE"), (1040, "OPENED"))
    for x, label in cols:
        o.append(text(x, 118, label, 8, P["mute"], 600, mono=True, ls=1.8))
    o.append(line(56, 132, 1144, 132, P["border"]))
    y = 132
    for ri, repo in enumerate(rows):
        yc = y + rh / 2 + 4
        o.append('<g class="fu" style="%s">' % delay(0.06 + ri * 0.035))
        o.append(text(56, yc, f"{repo['n']:03d}", 10.5, P["mute"], 400, mono=True))
        o.append(text(132, yc, repo["label"], 13.5, P["ink"], 500))
        nx = 132 + tw(repo["label"], 13.5, ls=0) + 14
        o.append(text(nx, yc, repo["blurb"].lower(), 10.5, P["mute"]))
        o.append(circle(486, yc - 4, 3.2, fill=dcolor(P, repo)))
        o.append(text(496, yc, dname(repo), 11.5, P["mid"]))
        st = R.state(repo)
        col = {"deployed": P["accent"], "open": P["mid"], "prototype": P["mute"]}[st]
        s, _w = chip(760, y + 6, st, P, size=9.5, h=18,
                     fill=P["panel"], stroke=P["border"], color=col)
        o.append(s)
        o.append(text(900, yc, repo["lang"], 11.5, P["mid"]))
        o.append(text(1040, yc, f"{MONTHS[repo['month']]} 2026", 11.5, P["mute"]))
        o.append("</g>")
        y += rh
        o.append(line(56, y, 1144, y, P["border"], opacity=0.75))
    o.append(text(56, y + 30, "State is derived from the repository itself, not claimed.",
                  10.5, P["mute"]))
    o.append(corner_ticks(W, H, P, inset=18))
    return "".join(o) + "</svg>"


# ----------------------------------------------------------------- lab map
def lab_map(P):
    W = 1200
    cw, gap = 344, 28
    panel_h = 268
    H = 128 + panel_h * 2 + gap + 40
    groups = R.by_division()
    desc = "The " + str(N) + " repositories arranged as five research divisions. " + " ".join(
        f"Division {i+1:02d} {name.lower()}: " + ", ".join(x["label"] for x in items) + "."
        for i, (_k, name, _q, items) in enumerate(groups))
    o = [head(W, H, "Lab map: five research divisions", desc)]
    o.append(rect(0, 0, W, H, fill=P["bg"]))
    o.append(text(56, 46, "LAB MAP", 10.5, P["mute"], 600, mono=True, ls=3.2))
    o.append(text(56, 74, "Five divisions. Seventeen experiments.", 17, P["ink"], 600))
    o.append(text(56, 96, "Grouped by the question the work is asking, not by language.", 12.5, P["mid"]))
    o.append(line(56, 112, 1144, 112, P["border"]))
    for i, (_key, name, question, items) in enumerate(groups):
        col, row = i % 3, i // 3
        x = 56 + col * (cw + gap)
        y = 132 + row * (panel_h + gap)
        c = P["div"][i]
        o.append('<g class="fu" style="%s">' % delay(0.08 + i * 0.09))
        o.append(rect(x, y, cw, 3, fill=c, rx=1.5))
        o.append(text(x, y + 26, f"DIVISION {i+1:02d}", 9, P["mute"], 600, mono=True, ls=1.8))
        o.append(text(x, y + 46, name, 14.5, P["ink"], 600))
        for j, ln in enumerate(question):
            o.append(text(x, y + 66 + j * 15, ln, 11.5, P["mid"]))
        by = y + 96
        bh = panel_h - 96 - 8
        o.append(rect(x, by, cw, bh, fill=P["panel"], stroke=P["border"], rx=8))
        o.append(rect(x, by + 12, 2.5, bh - 24, fill=c, rx=1.25))
        for j, repo in enumerate(items):
            ry = by + 26 + j * 30
            o.append(text(x + 16, ry, f"{repo['n']:02d}", 8.5, P["mute"], 600, mono=True, ls=1.4))
            o.append(text(x + 42, ry, repo["label"], 12.5, P["ink"], 500))
            o.append(text(x + 42, ry + 14, repo["blurb"], 10, P["mute"]))
        o.append("</g>")
    return "".join(o) + "</svg>"


# ---------------------------------------------------------------- timeline
PHASES = [
    ("MARCH", "Tools first",
     "A forensics engine, a repo auditor, a detector and a deployment platform. "
     "Instruments before experiments."),
    ("APRIL", "Applied systems",
     "Simulation, sensing and orchestration. The instruments get pointed at real domains."),
    ("MAY", "Rigour",
     "Attribution, refusal and self-observability become requirements, not extras."),
    ("JULY", "Grounded and hardened",
     "Retrieval that cites, plus three systems whose whole job is proving a pipeline is intact."),
    ("AUGUST", "Bounded autonomy",
     "Agents that act on money and on networks, under policy, offline, with an audit trail."),
]
PHASE_MONTH = ["Mar", "Apr", "May", "Jul", "Aug"]


def wrap(s, size, max_w, limit=None):
    words, lines, cur = s.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if tw(trial, size) > max_w and cur:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines[:limit] if limit else lines


def timeline(P):
    W, H = 1200, 476
    desc = (f"A timeline of {N} repositories created between March and August 2026, in five "
            "phases: tools first in March, applied systems in April, rigour in May, grounded "
            "and hardened in July, and bounded autonomy in August.")
    o = [head(W, H, "Research log, March to August 2026", desc)]
    o.append(rect(0, 0, W, H, fill=P["bg"]))
    o.append('<g class="fu">')
    o.append(text(56, 46, "RESEARCH LOG", 10.5, P["mute"], 600, mono=True, ls=3.2))
    o.append(text(56, 74, "Six months", 17, P["ink"], 600))
    o.append(text(56, 96, f"{N} repositories, in the order they were created.", 12.5, P["mid"]))
    o.append("</g>")
    cw = (1088 - 4 * 16) / 5
    for i, (month, title, body) in enumerate(PHASES):
        x = 56 + i * (cw + 16)
        count = sum(1 for q in R.REPOS if q["month"] == PHASE_MONTH[i])
        o.append('<g class="fu" style="%s">' % delay(0.08 + i * 0.09))
        o.append(rect(x, 124, cw, 150, fill=P["panel"], stroke=P["border"], rx=8))
        o.append(rect(x, 124, cw, 2.5, fill=P["accent2"], rx=1.25, opacity=0.4 + i * 0.14))
        o.append(text(x + 16, 152, f"PHASE {i+1:02d}  \u00b7  {month}", 8.5, P["mute"], 600,
                      mono=True, ls=1.6))
        o.append(text(x + 16, 174, title, 13, P["ink"], 600))
        for j, ln in enumerate(wrap(body, 10.5, cw - 32, 5)):
            o.append(text(x + 16, 196 + j * 14, ln, 10.5, P["mid"]))
        o.append(line(x + 16, 246, x + cw - 16, 246, P["border"]))
        o.append(text(x + 16, 262, f"{count} repositories", 9.5, P["mute"]))
        o.append("</g>")

    # spine: labels alternate above and below so seventeen names have room to breathe
    sy = 384
    x0, x1 = 64, 1136
    o.append(draw_line(x0 - 8, sy, x1 + 8, sy, P["border"], d=0.4))
    step = (x1 - x0) / (N - 1)
    for i, repo in enumerate(sorted(R.REPOS, key=lambda q: q["n"])):
        x = x0 + i * step
        c = dcolor(P, repo)
        up = i % 2 == 0
        o.append('<g class="fu" style="%s">' % delay(0.55 + i * 0.04))
        o.append(line(x, sy - (26 if up else 0), x, sy + (0 if up else 26), P["line"]))
        o.append(circle(x, sy, 4.5, fill=P["surface"], stroke=c, sw=1.6))
        o.append(circle(x, sy, 2, fill=c))
        ty = sy - 36 if up else sy + 46
        o.append(text(x, ty, repo["label"], 10, P["ink"], 500, anchor="middle"))
        o.append(text(x, ty + (-12 if up else 12), f"{repo['n']:02d}", 8.5, P["mute"], 600,
                      anchor="middle", mono=True, ls=1))
        o.append("</g>")
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------- stack
def stack(P):
    W = 1200
    lx, cx0, right = 56, 216, 1144
    rows = []
    y = 104
    for role, items in R.STACK:
        x, first_y = cx0, y
        lines = 1
        placed = []
        for label in items:
            w = tw(label, 12.5) + 20
            if x + w > right:
                x = cx0
                y += 34
                lines += 1
            placed.append((x, y, w, label))
            x += w + 8
        rows.append((role, first_y, placed))
        y += 34 + 12
    H = y + 20
    desc = (f"Technologies used across the {N} repositories, grouped by role: languages, models, "
            "retrieval, services, interface, perception, assurance, data and runtime. Language "
            "entries show how many repositories use that language as their primary language.")
    o = [head(W, H, "Instrument inventory", desc)]
    o.append(rect(0, 0, W, H, fill=P["bg"]))
    o.append(text(56, 44, "INSTRUMENT INVENTORY", 10.5, P["mute"], 600, mono=True, ls=3.2))
    o.append(text(56, 68, "Everything below appears in at least one repository.", 13, P["mid"]))
    o.append(line(56, 84, 1144, 84, P["border"]))
    for gi, (role, ry, placed) in enumerate(rows):
        o.append('<g class="fu" style="%s">' % delay(0.06 + gi * 0.07))
        o.append(text(lx, ry + 17, role, 9.5, P["mid"], 600, mono=True, ls=2))
        for x, y0, w, label in placed:
            o.append(rect(x, y0, w, 26, fill=P["panel"], stroke=P["border"], rx=6))
            o.append(text(x + 10, y0 + 17.4, label, 12.5, P["ink"]))
        o.append("</g>")
        last_y = max(p[1] for p in placed)
        o.append(line(56, last_y + 39, 1144, last_y + 39, P["border"]))
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------- atlas
TECH_MIN = 3   # a technology joins the map once three repositories use it


def _relax(nodes, iterations=260):
    """Push overlapping centre nodes apart, keeping them near their home angle."""
    for _ in range(iterations):
        moved = False
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                a, b = nodes[i], nodes[j]
                dx, dy = b["x"] - a["x"], b["y"] - a["y"]
                min_x = (a["w"] + b["w"]) / 2 + 18
                min_y = 44
                if abs(dx) < min_x and abs(dy) < min_y:
                    moved = True
                    push = (min_y - abs(dy)) / 2 + 0.5
                    if dy >= 0:
                        a["y"] -= push
                        b["y"] += push
                    else:
                        a["y"] += push
                        b["y"] -= push
        if not moved:
            break
    return nodes


def atlas(P):
    W, H = 1200, 900
    cx, cy = 600, 528
    ring = 292

    counts = {}
    for repo in R.REPOS:
        for t in repo["tech"]:
            counts[t] = counts.get(t, 0) + 1
    shared = sorted([kv for kv in counts.items() if kv[1] >= TECH_MIN],
                    key=lambda kv: (-kv[1], kv[0]))
    top = ", ".join(f"{k} in {v} repositories" for k, v in shared[:3])
    desc = (f"A knowledge graph of the whole laboratory. The {N} repositories sit on an outer "
            "ring, grouped into five divisions. Every technology shared by three or more of them "
            "floats in the centre, joined by a line to each repository that uses it. The most "
            f"shared are {top}.")
    o = [head(W, H, "Technology atlas", desc)]
    o.append(rect(0, 0, W, H, fill=P["bg"]))
    o.append('<g class="fu">')
    o.append(text(56, 58, "TECHNOLOGY ATLAS", 10, P["mute"], 600, mono=True, ls=3))
    o.append(text(56, 96, f"What the {N} share", 30, P["ink"], 600))
    o.append(text(56, 122, "Every technology used by three or more repositories, joined to each "
                           "repository that uses it.", 13, P["mid"]))
    o.append("</g>")
    x = 56
    for i, (_k, name, _q) in enumerate(R.DIVISIONS):
        o.append('<g class="fu" style="%s">' % delay(0.1 + i * 0.05))
        o.append(circle(x, 154, 3.4, fill=P["div"][i]))
        o.append(text(x + 10, 157.5, name, 10, P["mid"]))
        o.append("</g>")
        x += tw(name, 10) + 42
    o.append(draw_line(56, 178, 1144, 178, P["border"], d=0.1))

    # outer ring: one node per repository
    order = sorted(R.REPOS, key=lambda q: (R.DIVISION_INDEX[q["div"]], q["n"]))
    pos = {}
    for i, repo in enumerate(order):
        ang = math.radians(-90 + i * 360.0 / N)
        pos[repo["name"]] = (cx + ring * math.cos(ang), cy + ring * math.sin(ang), ang)
    o.append(circle(cx, cy, ring, stroke=P["border"], sw=1, opacity=0.9))

    # centre: one node per shared technology, placed near the repositories using it
    users = {k: [q for q in R.REPOS if k in q["tech"]] for k, _v in shared}
    hi = shared[0][1]
    nodes = []
    for k, v in shared:
        angs = [pos[q["name"]][2] for q in users[k]]
        mx = sum(math.cos(a) for a in angs) / len(angs)
        my = sum(math.sin(a) for a in angs) / len(angs)
        ang = math.atan2(my, mx)
        pull = 0.3 + 0.7 * (hi - v) / max(1, hi - TECH_MIN)
        rad = 44 + 148 * pull
        nodes.append(dict(k=k, v=v, x=cx + rad * math.cos(ang), y=cy + rad * math.sin(ang),
                          w=tw(k, 10.5) + 26))
    _relax(nodes)

    # edges: repository -> technology
    e = 0
    o.append('<g class="fi" style="%s">' % delay(0.24))
    for nd in nodes:
        for q in users[nd["k"]]:
            rx, ry, _a = pos[q["name"]]
            o.append(draw_line(nd["x"], nd["y"], rx, ry, dcolor(P, q), sw=1,
                               opacity=0.45, d=0.3 + e * 0.012))
            e += 1
    o.append("</g>")

    # technology nodes on top of their edges
    for i, nd in enumerate(nodes):
        o.append('<g class="fu" style="%s">' % delay(0.42 + i * 0.03))
        rad = 3.4 + nd["v"] * 0.42
        o.append(circle(nd["x"], nd["y"], rad + 5.5, fill=P["bg"], opacity=0.92))
        o.append(circle(nd["x"], nd["y"], rad, fill=P["ink"], opacity=0.82))
        lw = tw(nd["k"], 10.5)
        o.append(rect(nd["x"] - lw / 2 - 5, nd["y"] + 9, lw + 10, 15, fill=P["bg"],
                      rx=4, opacity=0.92))
        o.append(text(nd["x"], nd["y"] + 20, nd["k"], 10.5, P["ink"], 500, anchor="middle"))
        o.append(text(nd["x"], nd["y"] + 31, f"\u00b7{nd['v']}", 8.5, P["mute"], 600,
                      anchor="middle", mono=True))
        o.append("</g>")

    # repository nodes and their labels
    for i, repo in enumerate(order):
        x0, y0, ang = pos[repo["name"]]
        c = dcolor(P, repo)
        o.append('<g class="fu" style="%s">' % delay(0.18 + i * 0.03))
        o.append(circle(x0, y0, 7, fill=P["surface"], stroke=c, sw=1.7))
        o.append(circle(x0, y0, 3.2, fill=c))
        lx0 = cx + (ring + 18) * math.cos(ang)
        ly0 = cy + (ring + 18) * math.sin(ang) + 4
        anchor = "start" if math.cos(ang) > 0.08 else ("end" if math.cos(ang) < -0.08 else "middle")
        if anchor == "middle":
            ly0 += 8 if math.sin(ang) > 0 else -8
        o.append(text(lx0, ly0, repo["label"], 11.5, P["ink"], 500, anchor=anchor))
        o.append(text(lx0, ly0 + 14, f"EXP-{repo['n']:02d}", 8.5, P["mute"], 600, anchor=anchor,
                      mono=True, ls=1.2))
        o.append("</g>")

    o.append(circle(cx, cy, 2.6, fill=P["accent"]))
    o.append(circle(cx, cy, 2.6, fill=P["accent"], cls="pu"))
    return "".join(o) + "</svg>"


# --------------------------------------------------------------- substrate
def substrate(P):
    W = 1200
    rows = R.LAYERS
    top = 268
    rh = 34
    H = top + rh * len(rows) + 84
    order = sorted(R.REPOS, key=lambda q: q["n"])
    desc = (f"A matrix of {len(rows)} shared layers against the {N} repositories. A filled cell "
            "means that repository uses that layer. The layers are "
            + ", ".join(n.lower() for _k, n in rows) + ".")
    o = [head(W, H, "Repository relationship matrix", desc)]
    o.append(rect(0, 0, W, H, fill=P["bg"]))
    o.append(text(56, 46, "REPOSITORY RELATIONSHIPS", 10.5, P["mute"], 600, mono=True, ls=3.2))
    o.append(text(56, 74, "What the systems share", 17, P["ink"], 600))
    o.append(text(56, 96, "A filled cell means the repository uses that layer. Read across for who "
                          "shares a decision;", 12.5, P["mid"]))
    o.append(text(56, 113, "read down for what a system is made of.", 12.5, P["mid"]))
    x0, x1 = 372, 1144
    step = (x1 - x0) / (N - 1)
    for i, repo in enumerate(order):
        x = x0 + i * step
        o.append("<g transform=\"translate(%s,%s) rotate(-52)\">%s</g>" % (
            r(x + 4), top - 26, text(0, 0, repo["label"], 10, P["mid"])))
        o.append(text(x, H - 46, f"{repo['n']:02d}", 8.5, P["mute"], anchor="middle", mono=True))
        o.append(rect(x - 9, H - 38, 18, 2.5, fill=dcolor(P, repo), rx=1.25))
    y = top
    for li, (key, name) in enumerate(rows):
        o.append('<g class="fu" style="%s">' % delay(0.1 + li * 0.06))
        o.append(text(340, y + 4, name, 11.5, P["ink"], anchor="end"))
        o.append(line(x0 - 20, y - 13, 1160, y - 13, P["border"], opacity=0.7))
        for i, repo in enumerate(order):
            x = x0 + i * step
            if key in repo["layers"]:
                o.append(circle(x, y, 5, fill=dcolor(P, repo)))
            else:
                o.append(circle(x, y, 3, fill=P["panel2"], stroke=P["border"], sw=1))
        count = sum(1 for q in order if key in q["layers"])
        o.append(text(1176, y + 4, str(count), 10, P["mute"], anchor="end", mono=True))
        o.append("</g>")
        y += rh
    o.append(line(x0 - 20, y - 13, 1160, y - 13, P["border"], opacity=0.7))
    return "".join(o) + "</svg>"


# -------------------------------------------------------------------- main
def write(name, builder, folder=ASSETS):
    os.makedirs(folder, exist_ok=True)
    for suffix, P in (("", LIGHT), ("-dark", DARK)):
        p = os.path.join(folder, f"{name}{suffix}.svg")
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(builder(P))
        print("wrote", os.path.relpath(p, ROOT))


def main():
    write("hero", hero)
    write("registry", registry)
    write("lab-map", lab_map)
    write("timeline", timeline)
    write("stack", stack)
    write("atlas", atlas)
    write("substrate", substrate)
    for repo in R.REPOS:
        if repo["name"] in EMBLEM:
            write(f"card-{repo['name']}", lambda P, q=repo: card(q, P), folder=CARDS)


if __name__ == "__main__":
    main()

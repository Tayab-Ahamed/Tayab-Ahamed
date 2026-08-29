"""Tiny SVG writer. No dependencies: the standard library draws everything."""

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

ANIM = (
    "<style>.fu{animation:fu .75s cubic-bezier(.16,.84,.44,1) both}"
    "@keyframes fu{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}"
    ".fi{animation:fi .9s ease both}@keyframes fi{from{opacity:0}to{opacity:1}}"
    ".dr{animation:dr 1.5s cubic-bezier(.4,0,.2,1) both}"
    "@keyframes dr{from{stroke-dashoffset:var(--L)}to{stroke-dashoffset:0}}"
    ".pu{transform-box:fill-box;transform-origin:center;animation:pu 3.4s ease-in-out infinite}"
    "@keyframes pu{0%,100%{opacity:.14;transform:scale(1)}50%{opacity:.42;transform:scale(1.85)}}"
    "@media(prefers-reduced-motion:reduce){.fu,.fi,.dr,.pu{animation:none!important}}</style>"
)

LIGHT = dict(
    bg="#FFFFFF", panel="#FAFAF9", panel2="#F3F3F1", border="#E3E3E0", line="#D4D4D0",
    ink="#171715", mid="#63635D", mute="#9C9C95", accent="#3D7DE8", accent2="#2F6FD0",
    surface="#FFFFFF",
    div=["#3D7DE8", "#4F8F6C", "#B07C34", "#7E6EAF", "#3F8C97"],
)
DARK = dict(
    bg="#0C0C0B", panel="#131312", panel2="#1B1B19", border="#282826", line="#37372F",
    ink="#F4F4F1", mid="#A0A099", mute="#6A6A63", accent="#6BA3F0", accent2="#6BA3F0",
    surface="#0C0C0B",
    div=["#6BA3F0", "#74B491", "#D3A45F", "#A292D0", "#6FB3BE"],
)

_NARROW = set("iljtIf.,;:'!|()[]{} ")
_WIDE = set("MWmw@")


def tw(s, size, mono=False, ls=0.0):
    """Approximate rendered text width in px."""
    if not s:
        return 0.0
    if mono:
        return len(s) * (size * 0.6 + ls) - ls
    total = 0.0
    for ch in s:
        if ch in _NARROW:
            f = 0.31
        elif ch in _WIDE:
            f = 0.86
        elif ch.isupper() or ch.isdigit():
            f = 0.63
        else:
            f = 0.535
        total += size * f + ls
    return total - ls


def _cs(cls=None, style=None):
    """Render optional class and inline style attributes."""
    c = f' class="{cls}"' if cls else ""
    y = f' style="{style}"' if style else ""
    return c + y


def delay(seconds):
    """An animation-delay inline style, rounded to avoid float noise."""
    return f"animation-delay:{round(seconds, 3)}s"


def draw_line(x1, y1, x2, y2, stroke="#D4D4D0", sw=1, opacity=None, d=0.0):
    """A line that draws itself in, left to right, on load."""
    import math as _m
    L = round(_m.hypot(x2 - x1, y2 - y1), 2)
    return line(x1, y1, x2, y2, stroke, sw, opacity, dash=L, cls="dr",
                style=f"--L:{L};{delay(d)}")


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def head(w, h, title, desc, anim=True):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
        f'height="{h}" role="img" aria-labelledby="t d" font-family="{SANS}">'
        f'<title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc>'
        + (ANIM if anim else "")
    )


def text(x, y, s, size=12, fill="#171715", weight=400, anchor=None, mono=False, ls=None,
         opacity=None, cls=None, style=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    m = f' font-family="{MONO}"' if mono else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<text x="{r(x)}" y="{r(y)}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}"{a}{m}{l}{o}{_cs(cls, style)}>{esc(s)}</text>')


def rect(x, y, w, h, fill="none", stroke=None, rx=0, sw=1, opacity=None, cls=None,
         style=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<rect x="{r(x)}" y="{r(y)}" width="{r(w)}" height="{r(h)}" rx="{rx}" '
            f'fill="{fill}"{s}{o}{_cs(cls, style)}/>')


def line(x1, y1, x2, y2, stroke="#D4D4D0", sw=1, opacity=None, dash=None, cls=None,
         style=None):
    o = f' opacity="{opacity}"' if opacity is not None else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{r(x1)}" y1="{r(y1)}" x2="{r(x2)}" y2="{r(y2)}" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linecap="butt"{o}{d}{_cs(cls, style)}/>')


def circle(cx, cy, rad, fill="none", stroke=None, sw=1, opacity=None, cls=None,
           style=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return f'<circle cx="{r(cx)}" cy="{r(cy)}" r="{r(rad)}" fill="{fill}"{s}{o}{_cs(cls, style)}/>'


def path(d, fill="none", stroke=None, sw=1, opacity=None, dash=None, cls=None,
         style=None):
    s = f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}"{s}{o}{da}{_cs(cls, style)}/>'


def chip(x, y, label, P, size=10, h=18, pad=8, fill=None, stroke=None, color=None):
    w = tw(label, size) + pad * 2
    out = rect(x, y, w, h, fill=fill or P["panel2"], stroke=stroke or P["border"], rx=h / 2)
    out += text(x + pad, y + h / 2 + size * 0.35, label, size, color or P["mute"])
    return out, w


def arrow(x, y, color, size=4):
    return path(f"M{r(x)} {r(y - size * 0.8)} l{size} {r(size * 0.8)} l-{size} {r(size * 0.8)}",
                stroke=color, sw=1.3)


def corner_ticks(w, h, P, inset=14, size=7):
    o = []
    for cx, sx in ((w - inset, -1), ):
        for cy, sy in ((inset, 1), (h - inset, -1)):
            o.append(line(cx, cy, cx + sx * size, cy, P["line"], opacity=0.7))
            o.append(line(cx, cy, cx, cy + sy * size, P["line"], opacity=0.7))
    return "".join(o)


def r(v):
    if isinstance(v, str):
        return v
    v = round(float(v), 2)
    return int(v) if v == int(v) else v

# Design system

The whole profile is drawn by `scripts/theme.py`. There is no CSS framework, no
icon set, no font file and no third-party package. Every shape is a string of
SVG written by hand.

---

## Principle

**Instrument, not poster.** Everything is styled like laboratory equipment:
hairlines, registration marks, monospace instrument labels, restrained colour
used only to carry meaning. Nothing is decorative. If a mark on the page does
not encode a fact, it is deleted.

The reference points are Linear's density, Stripe's typographic discipline and
the visual grammar of mission-control telemetry. Not cyberpunk, not neon, not
gradient-heavy.

---

## Colour

Two palettes, same token names, so every generator is theme-agnostic &mdash; it
asks for `c["ink2"]`, never for a hex value.

| Token | Light | Dark | Used for |
|---|---|---|---|
| `canvas` | `#FFFFFF` | `#0C0C0B` | page background |
| `panel` | `#FAFAF9` | `#131312` | cards, alternating matrix rows |
| `panel2` | `#F3F3F1` | `#1B1B19` | chips inside panels |
| `hairline` | `#E3E3E0` | `#282826` | borders, empty matrix cells |
| `rule` | `#D4D4D0` | `#37372F` | axes, ticks, registration marks |
| `ink` | `#171715` | `#F4F4F1` | primary text |
| `ink2` | `#63635D` | `#A0A099` | secondary text |
| `ink3` | `#9C9C95` | `#6A6A63` | instrument labels, captions |
| `accent` | `#2F6FD0` | `#6BA3F0` | the single accent |
| `grid` | `#EFEFEC` | `#181816` | month gridlines |

The dark canvas is `#0C0C0B`, slightly darker than GitHub's `#0d1117`, so assets
read as deliberately inset rather than accidentally mismatched.

### Division colours

Four hues, one per research division. These are the **only** colours that carry
meaning, and they are the only colours in the profile besides the accent.

| Division | Light | Dark |
|---|---|---|
| D1 Autonomous Agents | `#3D7DE8` | `#6BA3F0` |
| D2 Grounded Retrieval | `#4F8F6C` | `#7FBF9C` |
| D3 Perception and Vision | `#B07C34` | `#D6A45A` |
| D4 Systems and Simulation | `#7E6EAF` | `#A796D8` |

Each was lightened for dark mode rather than reused, so contrast against
`#0C0C0B` stays legible.

---

## Type

System stacks only. No web font is downloaded, which is most of the reason the
profile loads instantly.

```
sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif
mono: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace
```

| Role | Size | Weight | Treatment |
|---|---|---|---|
| Hero wordmark | 31 | 600 / 300 | two weights, one line each |
| Section heading | 17 | 600 | &mdash; |
| Instrument label | 8.5&ndash;10.5 | 400 | mono, uppercase, 1.5&ndash;3.6 tracking |
| Body | 10.5&ndash;13 | 400 | `ink2` |
| Caption | 10 | 400 | `ink3` |

Uppercase mono with wide tracking is the signature. It is used for every label
that names a thing rather than saying something.

---

## Measuring text without a font engine

The generators need to know how wide a string will be &mdash; to wrap paragraphs,
size pills and pack timeline labels &mdash; but there is no font loaded and no
layout engine available.

`theme.text_w()` estimates advance width by classifying characters:

| Class | Factor of font size |
|---|---|
| space | 0.280 |
| narrow `iljtfIr.,:;'\|!()[]{}-` | 0.300 |
| wide `mwMW@%` | 0.880 |
| uppercase and digits | 0.665 |
| everything else | 0.540 |
| any monospace character | 0.601 |

It is approximate, so every layout that depends on it is built with slack: pills
get 20px of padding, wrapped text gets a 32px margin inside its card, and the
timeline requires a 10px gap before reusing a row. That tolerance is why the
layouts survive being off by a few percent.

---

## Primitives

`theme.py` exposes the vocabulary every generator draws with:

| Function | Purpose |
|---|---|
| `svg_open` / `svg_close` | document wrapper, emits `role="img"` plus `<title>` and `<desc>` |
| `rect`, `line`, `path`, `circle` | shapes |
| `text` | text node, with `mono`, `anchor`, `tracking`, `weight` |
| `label` | uppercase mono instrument label |
| `pill` | rounded chip; returns markup **and** its width so callers can flow them |
| `crosshair`, `corner`, `grid` | registration marks and gridlines |
| `esc` | escapes `& < > "` |
| `write` | writes a file |

### Two rules that are not optional

**Escape every text node.** An earlier version escaped `&` for pill contents but
not for row labels, so a group called "AI & ML" emitted a raw ampersand and the
file stopped being valid XML. `esc()` now centralises this and every text
primitive calls it. `build_all.py` re-parses all 38 files at the end of every
build specifically to catch this class of mistake.

**Trim floats.** `_n()` strips trailing zeros from coordinates. Across thousands
of shapes this is a meaningful share of the file size.

---

## Layout

- Canvas width is always **1200**, which is GitHub's README content width at
  desktop. Height varies per asset and is computed from content, never hardcoded.
- Horizontal padding is **56**, except on project cards where it is **28**.
- Corner registration marks are inset **28** from the edge.
- Cards use an **8px** radius, pills **5&ndash;6px**.

Mobile behaviour comes free: each asset is one `<img>` with `width="100%"`, and
SVG scales without reflowing. Nothing is sized in pixels in the Markdown.

---

## Accessibility

- Every SVG carries `role="img"`, `aria-labelledby`, a `<title>` and a `<desc>`
  that describes the data, not the picture.
- Every `<img>` in the README carries alt text of its own.
- All body copy is real Markdown. Nothing that a reader needs is trapped inside
  an image &mdash; the images are the visualisation layer, not the content layer.
- Colour is never the only channel. Divisions carry a colour, but also a code
  (D1&ndash;D4), a title and a position.
- No animation, so nothing to disable and nothing that restarts on scroll.

---

## Dark mode

GitHub honours `prefers-color-scheme` inside `<picture>`:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img alt="..." src="assets/hero.svg" width="100%">
</picture>
```

Every asset ships as a light/dark pair generated from the same code path with a
different palette dict, so the two versions can never drift apart in layout.

---

## Cost

| | |
|---|---|
| Assets | 38 SVG files |
| Total weight | ~400 KB uncompressed, ~3&ndash;20 KB each |
| Fonts downloaded | none |
| Scripts executed | none |
| Third-party requests | none |
| Build dependencies | none |

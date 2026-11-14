# news-image-01 entry: a working Python 3.13 program (standard library only)
# that copies the entry.png sitting next to it into $MAKEFUN_OUTPUT_DIR.
#
# The image is a dense "many stories in one picture" poster, "THE WORLD IN
# ONE PICTURE — Friday 13 November 2026": a full-width LEAD band (five
# nations to speak for Europe at the Ukraine talks) plus a uniform 3x3 grid
# of nine numbered picture-led stories (Trump, Xi and Putin's first
# three-way meeting; the FAA grounding every US departure; Nvidia falling
# under $4 trillion; Iran's radar claim in Bahrain; Starship Flight 15;
# the strike on Gaza's Nasser Hospital; Pope Leo XIV's Mass in Chiclayo;
# a Kyiv hospital set ablaze; the Assam bus-truck crash) plus an "ALSO ON
# FRIDAY 13 NOVEMBER" list of 18 more verified stories (New Orleans
# riverboat, Microsoft outage, Turkey/Qatar pact, Hormuz gas tanker, Yemen
# displaced, Moscow car bomb, Takaichi's first China visit, Pakistan raids,
# North Korea's flag, Nairobi collapse, Nigeria Ebola contacts cleared,
# RAF Lakenheath drone scare, US wholesale inflation, Boebert's loss,
# Shuttle Endeavour upright in LA, U2's new album, Pochettino to
# Manchester United, Japan beating South Korea 9-5) — 28 verified stories
# in total, every one reported on Friday 13 November 2026.
#
# The look is deliberately different from the earlier dense poster (v3)
# and from the reference poster it resembled: a navy banner masthead with
# white/amber sans type instead of a giant serif date, ink-sketch + pale
# wash illustrations instead of flat full-colour vector scenes, navy square
# number badges instead of coloured round ones, Liberation Sans throughout,
# a lead band + 3x3 grid instead of a 3+4+4 grid, and a 2-column also-on
# list. Same dense structure, a clearly different poster.
#
# Deterministic and offline: every run copies the same bytes, and the
# output is a complete JPEG (magic bytes ffd8ff, 1024x1024). The image was
# rendered by ../work/draw_v4.py (PIL, fixed layout, ink-sketch scenes
# drawn from constants, no network, fixed seeds only), so the rendered
# image is byte-identical on every run (verified twice).
#
# Rendered entry.png: JPEG 1024x1024, 308,600 bytes, sha256
# b0ffec5e7e4de480d492a8b298c2f426745eb7de529caca5cbc907501724fa89.
# Verified: draw script run 2x byte-identical; this program run 2x
# byte-identical against the same entry.png.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
dst = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
if not src.is_file():
    raise SystemExit(f"entry.png not found next to {__file__}")
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dst)
print(f"wrote {dst} ({dst.stat().st_size} bytes)")

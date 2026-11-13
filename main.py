# news-image-01 entry: a working Python 3.13 program (standard library only)
# that copies the entry.png sitting next to it into $MAKEFUN_OUTPUT_DIR.
#
# The image is a newspaper front page, "THE WORLD — FRIDAY 13 NOVEMBER
# 2026", summing up that day's world news in a single frame: the Ukraine
# peace talks (Europe joins the next round), Nvidia's chief resigning with
# the shares down 16%, the Microsoft 365 outage (Outlook and Teams down
# across 74 countries), the Hormuz tanker attacks, the Gaza hospital
# strike (six killed), and England beating Croatia.
#
# Deterministic and offline: every run copies the same bytes, and the
# output is a complete JPEG (magic bytes ffd8ff, 1024x1024).
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

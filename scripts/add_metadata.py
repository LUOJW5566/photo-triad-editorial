#!/usr/bin/env python3
"""Add the exact date and theme to a generated lower panel."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


DATE_RE = re.compile(r"^[0-9]{2} [A-Z]{3} [0-9]{4}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_panel", type=Path)
    parser.add_argument("output_panel", type=Path)
    parser.add_argument("--date", required=True, help="Exact date: DD MON YYYY")
    parser.add_argument("--theme", required=True, help="One to three words")
    parser.add_argument("--font", type=Path, help="Optional TrueType font")
    return parser.parse_args()


def choose_font(explicit: Path | None, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        explicit,
        Path(r"C:\Windows\Fonts\BASKVILL.TTF"),
        Path(r"C:\Windows\Fonts\georgia.ttf"),
        Path(r"C:\Windows\Fonts\times.ttf"),
        Path(r"C:\Windows\Fonts\arial.ttf"),
    ]
    for candidate in candidates:
        if candidate and candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def main() -> None:
    args = parse_args()
    if not args.input_panel.is_file():
        raise FileNotFoundError(f"Input panel not found: {args.input_panel}")
    if not DATE_RE.fullmatch(args.date):
        raise ValueError("date must match DD MON YYYY, for example 27 AUG 2026")
    theme = " ".join(args.theme.split())
    if not theme or len(theme.split()) > 3 or "\n" in args.theme or "\r" in args.theme:
        raise ValueError("theme must contain one to three words and no line breaks")

    panel = Image.open(args.input_panel).convert("RGB")
    draw = ImageDraw.Draw(panel)
    margin_x = max(24, round(panel.width * 0.06))
    margin_y = max(24, round(panel.height * 0.055))
    font_size = max(18, min(52, round(panel.width * 0.029)))
    font = choose_font(args.font, font_size)
    line_gap = max(8, round(font_size * 0.32))
    fill = (40, 45, 42)

    date_box = draw.textbbox((0, 0), args.date, font=font)
    theme_box = draw.textbbox((0, 0), theme, font=font)
    theme_y = panel.height - margin_y - (theme_box[3] - theme_box[1])
    date_y = theme_y - line_gap - (date_box[3] - date_box[1])
    draw.text((margin_x, date_y), args.date, font=font, fill=fill)
    draw.text((margin_x, theme_y), theme, font=font, fill=fill)

    args.output_panel.parent.mkdir(parents=True, exist_ok=True)
    panel.save(args.output_panel, format="PNG", optimize=True)
    print(f"ANNOTATED_PANEL={args.output_panel.resolve()}")
    print(f"SIZE={panel.width}x{panel.height}")
    print(f"DATE={args.date}")
    print(f"THEME={theme}")


if __name__ == "__main__":
    main()



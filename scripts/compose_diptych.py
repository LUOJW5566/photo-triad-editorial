#!/usr/bin/env python3
"""Compose an untouched RGB photograph above an annotated lower panel."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("photo", type=Path)
    parser.add_argument("annotated_panel", type=Path)
    parser.add_argument("output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.photo.is_file():
        raise FileNotFoundError(f"Photo not found: {args.photo}")
    if not args.annotated_panel.is_file():
        raise FileNotFoundError(f"Annotated panel not found: {args.annotated_panel}")

    photo = Image.open(args.photo).convert("RGB")
    panel = Image.open(args.annotated_panel).convert("RGB")
    if photo.width <= 0 or photo.height <= 0 or panel.width <= 0 or panel.height <= 0:
        raise ValueError("photo and panel must have positive dimensions")

    scale = photo.width / panel.width
    panel_size = (photo.width, max(1, round(panel.height * scale)))
    if panel.size != panel_size:
        panel = panel.resize(panel_size, Image.Resampling.LANCZOS)

    final = Image.new("RGB", (photo.width, photo.height + panel.height))
    final.paste(photo, (0, 0))
    final.paste(panel, (0, photo.height))

    # Verify the documentary region before writing the output.
    if final.crop((0, 0, photo.width, photo.height)).tobytes() != photo.tobytes():
        raise RuntimeError("photo pixel preservation check failed")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    final.save(args.output, format="PNG", optimize=True)
    print(f"FINAL_COMPOSITE={args.output.resolve()}")
    print(f"SIZE={final.width}x{final.height}")
    print(f"PHOTO_SIZE={photo.width}x{photo.height}")
    print(f"PANEL_SIZE={panel.width}x{panel.height}")
    print("PHOTO_PIXELS_PRESERVED=True")


if __name__ == "__main__":
    main()



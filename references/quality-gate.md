# Quality Gate

Inspect the final image at full size and thumbnail size. Return it only when all applicable checks pass.

## Source and composition

- One uploaded photograph is the sole content source.
- The upper photo remains the main documentary evidence: subject, scene identity, major spatial relationships, light direction, brightest region, and emotional temperature are intact.
- The work is one vertical diptych with a direct, clean join.
- The lower panel is one continuous composition, not three mini-panels or a before/after comparison.
- The lower motif is deliberately placed, normally 30–45% of panel width and no more than 30% of panel height, with approximately 65–85% quiet space.
- The raw panel, annotated panel, and final composite exist as three separate files.
- The final composite's upper region matches the original photograph pixel-for-pixel after conversion to RGB; only the lower panel may be resized to match the photo width.

## Triad integration

- Isometric structure is visible through a small number of source-justified axes, planes, intervals, or stepped depth relationships.
- 3D volume is visible through restrained layering, occlusion, extrusion, contact, or material separation.
- Pixel language is visible through coarse blocks, stepped edges, broken contours, or selective loss of detail.
- The three roles describe the same source-derived motif and share one light direction, palette hierarchy, and spatial logic.
- None of the three roles becomes a generic grid, glossy CGI render, or uniform pixel filter.

## Source evidence and palette

- Every major mark maps to a named source fact.
- The dominant subject or relationship remains primary.
- Minor objects, surface noise, tiny text, readable faces, hidden anatomy, and unsupported symbols are omitted.
- Colors come from the photograph and retain its temperature/value hierarchy.
- No invented neon, random accent, decorative symmetry, or unrelated object competes with the source.

## Surface and text

- The lower field is clean, low-chroma, continuous, and spacious.
- No hard pasted rectangle, frame, shadow, tape, divider ornament, gradient, glow, haze, stain, uncontrolled grain, or dirty paper effect appears.
- Text is absent unless allowed; when allowed, exactly two small lower-left items appear: `DD MON YYYY` and a 1–3 word theme.
- No extra title, caption, number, location, logo, signature, or watermark appears.

## Pipeline integrity

- `RAW_PANEL` contains no generated or deterministic text.
- `ANNOTATED_PANEL` differs from `RAW_PANEL` only by the exact lower-left date and theme plus the deterministic text rendering.
- `FINAL_COMPOSITE` is created by `scripts/compose_diptych.py` from the original photo and `ANNOTATED_PANEL`, never by asking the image model to redraw the complete diptych.
- The returned paths are explicitly labelled `RAW_PANEL`, `ANNOTATED_PANEL`, and `FINAL_COMPOSITE`.

## Revision decision

If a check fails, identify the single failed variable and revise only that variable. Do not compensate for a weak source mapping by adding decoration, text, stronger color, or more detail. If the upper photograph has been substantially changed, restart from the original upload.


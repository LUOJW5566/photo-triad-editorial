---
name: photo-triad-editorial
description: Create a source-faithful vertical photo-and-abstraction diptych from one uploaded photograph, with a spacious lower panel that unifies isometric structure, restrained 3D volume, and coarse pixel marks. Use when the user asks for photo abstraction, visual memory, isometric/3D/pixel reinterpretation, or an editorial image with generous negative space. Do not use for unrelated 3D renders, generic pixel art, or photo editing without an abstraction panel.
---

# Photo Triad Editorial

Create a three-artifact vertical editorial workflow from one uploaded photograph. The photograph is the factual source; the lower panel is a new abstraction of its visual relationships. The default language is a single continuous fusion of **isometric structure + restrained 3D volume + coarse pixel articulation**, not three unrelated filters and not three separate variants.

## Invocation and output contract

- Trigger when the user supplies a photograph and asks for an abstract diptych, isometric reinterpretation, 3D/pixel photo abstraction, visual memory, or a related editorial composition.
- If the user gives no explicit mode, use `fuse`: preserve the photograph as the upper evidence area and generate one lower abstract panel.
- Produce and return these three purposeful artifacts when the user asks to validate or run the workflow: (1) the raw generated lower panel with no generated text, (2) the same lower panel after deterministic Python date/theme annotation, and (3) the final deterministic composite containing the original photograph above the annotated panel. The final composite is the primary deliverable, but the two intermediate images must remain available.
- Keep the upper photograph as the dominant documentary evidence. Do not generatively redraw it in the default mode. Only make restrained proportional placement or the minimum crop required by the chosen composition.
- Use the uploaded photograph as the only content source. Other images, if available, are style references only and must never contribute subjects, objects, colors, or arrangements.
- Add only two small lower-left text items when the user has not prohibited text: a factual date in `DD MON YYYY` format and a 1–3 word theme. Generate neither item with the image model. Add them only with `scripts/add_metadata.py`. Do not add titles, labels, numbers, location names, logos, signatures, captions, or watermarks.

## Three-artifact pipeline

Use the built-in image-generation tool only for the raw lower panel. Do not ask it to create the complete diptych and do not use it to render typography.

1. Lock the uploaded photograph as `USER_PHOTO` and inspect it as the sole content source.
2. Generate `RAW_PANEL` as a complete lower-panel image only. It must contain the clean background and the source-derived fused triad motif, but no text of any kind.
3. Run:

   ```text
   python scripts/add_metadata.py RAW_PANEL ANNOTATED_PANEL --date "DD MON YYYY" --theme "THEME"
   ```

   This creates the second artifact without changing the panel dimensions or visual content outside the lower-left metadata area.

4. Run:

   ```text
   python scripts/compose_diptych.py USER_PHOTO ANNOTATED_PANEL FINAL_COMPOSITE
   ```

   This creates the third artifact. The script keeps the original photograph at its native pixel dimensions and places the annotated panel below it, scaling only the panel when necessary to match the photo width.
5. Return all three paths, clearly labelled `RAW_PANEL`, `ANNOTATED_PANEL`, and `FINAL_COMPOSITE`. Never return an image-model full-diptych result in place of the deterministic composite.

If either script fails, stop at that stage and report the failed artifact. Do not silently substitute a generated full composite.

## Core method

Run this sequence internally and do not print the analysis inside the artwork:

`OBSERVE → SELECT EVIDENCE → MAP RELATIONSHIPS → ABSTRACT → FUSE → AUDIT`

1. **Observe:** identify the dominant subject or relationship, foreground/midground/background, major masses, axes, direction of light, brightest area, depth order, repeated rhythm, material cues, color roles, and useful negative space.
2. **Select evidence:** retain the 3–6 facts that make this photograph distinctive. Prefer position, scale, direction, count groups, overlap, rhythm, and color hierarchy over surface detail.
3. **Map relationships:** use [references/source-to-mark-mapping.md](references/source-to-mark-mapping.md) to convert each retained fact into a small number of marks. Every major mark must have a named source fact.
4. **Abstract:** remove incidental texture, tiny objects, literal outlines, readable faces, decorative signage, and low-information background detail. Preserve enough evidence for the result to recall this specific photograph rather than a generic subject.
5. **Fuse:** build one lower panel in which isometric structure, 3D volume, and pixel articulation cooperate. Keep the panel spacious and source-derived.
6. **Audit:** use [references/quality-gate.md](references/quality-gate.md). Correct only the failed variable and inspect again.

## Composition

- Use one vertical upper/lower diptych with a clean, direct join and no hard pasted card, frame, shadow, tape, divider ornament, or mockup background. The join is produced by `scripts/compose_diptych.py`, not by the image model.
- Adapt the split to the source instead of forcing equal halves:
  - landscape or horizontally extended source: photo about 40–52% of final height;
  - vertical architecture/person/tall subject: photo about 55–68%;
  - near-square or balanced source: photo about 48–58%.
- Let the lower panel occupy the remaining height, adjusting within about 8% when needed for visual balance.
- Preserve the source's aspect ratio and primary subject. Do not crop away the defining evidence just to meet a fixed canvas ratio.
- Use one continuous, low-chroma, near-uniform lower field. Default to a clean neutral ivory/off-white field with strong contrast against the derived marks. Keep roughly 65–85% of the lower panel visually quiet.
- Place the abstract motif in the lower-middle or in a deliberate asymmetric position supported by the source's visual weight or negative space. Avoid dead-center placement by habit.
- The motif normally occupies about 30–45% of the lower-panel width and no more than 30% of its height. A source-born road, horizon, bridge, or crowd may extend wider while remaining shallow and sparse.

## The unified triad language

Use all three languages in one coherent motif. They are roles, not independent effects:

- **Isometric:** establish a limited spatial skeleton through oblique axes, planes, stepped depth, repeated intervals, or an orthographic-like arrangement. Use only axes justified by the source; never add technical grids, unexplained diagrams, or decorative perspective lines.
- **3D:** give selected masses restrained volume through layered planes, occlusion, extrusion, contact, and one coherent light direction. Use matte or softly controlled surfaces, not glossy CGI, dramatic lens effects, or invented physical detail.
- **Pixel:** quantize contours and surfaces into coarse blocks, stepped edges, broken segments, and selectively missing information. Use large low-frequency blocks; never use a full-frame pixel filter, tiny sprite detail, anti-aliased micro-tracing, or dense dithering.

Choose one primary mark family and at most two supporting families. Suitable combinations include:

- primary: stepped isometric planes; support: volumetric overlap + coarse pixel erosion;
- primary: layered 3D masses; support: oblique structural axes + block clusters;
- primary: segmented pixel bands; support: shallow isometric planes + one restrained volume cue.

Do not make every mark equally explicit. The structure should read first as a sparse editorial abstraction, then recall the photograph on closer inspection.

## Source fidelity and color

- Keep the upper photo's subject identity, major composition, light direction, brightest region, emotional temperature, and key color relationships.
- Do not reconstruct concealed faces, bodies, architecture, or objects that are not visible in the source.
- People become simple irregular masses or short vertical forms; never draw facial features, separate limbs, or costume detail.
- Distinctive architecture receives only one to three identity cues: a mass, opening, roofline, taper, arch, or rhythm.
- Extract a compact palette from the photograph: one field/neutral role, one dark structural role, one light role, one or two subject midtones, and at most one small high-chroma accent when it truly exists in the source.
- Preserve the source's luminance and temperature hierarchy. Never add fashionable neon, unsupported complementary colors, generic cyberpunk color, or an accent solely for decoration.

## Text and date behavior

- Default to no title and no explanatory copy.
- If text is allowed or requested, place only the date and one short theme together in the lower-left of the abstract panel, small and secondary to the image.
- Use the user-supplied date/theme when provided. Otherwise use the artwork creation date in `DD MON YYYY` and derive a quiet 1–3 word theme from a visible source fact.
- Render text deterministically with `scripts/add_metadata.py`. Never ask the image model to invent typography and never use OCR-like generated text as the final metadata.

## Rejection and revision rules

Reject or regenerate the lower panel when it is a uniform filter, a miniature redraw, a generic isometric diagram, a generic 3D render, or unrelated pixel art. Also reject when:

- the upper photo is substantially redrawn, replaced, recolored, or made unrecognizable;
- the lower panel contains unsupported objects, symbols, perspective grids, decorative geometry, or colors;
- isometric, 3D, and pixel cues appear as three disconnected treatments rather than one fused construction;
- the motif fills the panel, destroys the intended negative space, or becomes a hard-edged pasted rectangle;
- the panel uses gradients, glow, heavy shadows, dirty texture, haze, excessive grain, or uncontrolled paper aging;
- more than the permitted date and theme appear as text;
- the abstract panel cannot be explained as a short list of source fact → visual mark mappings.

Revise only the failed variable: source fidelity, evidence selection, spatial mapping, triad integration, scale, palette, surface cleanliness, or text restraint.

## Supporting references

- Read [references/personal-style.md](references/personal-style.md) for the user's editorial tone, hierarchy, color restraint, and negative-space preferences.
- Read [references/source-to-mark-mapping.md](references/source-to-mark-mapping.md) before generating the lower panel.
- Read [references/quality-gate.md](references/quality-gate.md) before returning the finished image.
- Use [scripts/add_metadata.py](scripts/add_metadata.py) for the annotated lower panel and [scripts/compose_diptych.py](scripts/compose_diptych.py) for the final composite.


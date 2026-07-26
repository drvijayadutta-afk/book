# KDP Interior — Illustrated Beta

`My-First-Money-Adventure-KDP-Interior-DRAFT.pdf` is a **paperback interior** file formatted to Amazon KDP's technical spec — reader-facing content only (no illustration prompts, interactive questions, or production notes visible on the page) — with real illustrations and a designed, polished layout, not placeholder boxes or plain text-on-white.

## What's in this version

- **All 24 story pages are illustrated** with original flat-vector scenes (not photos or AI-generated raster images — hand-built SVG, rendered crisp at any size): consistent character designs for Milu, Pico, the coin, and all eight helpers across every scene, warm gradient skies, and scene-appropriate props (wheat field, bus, sewing machine, hospital room, market stall, etc.), matching the palette/character bible from the manuscript's Illustration Consistency Guide.
- **Layered, dimensional illustrations**: every character/prop that sits on the ground casts a soft radial-gradient shadow, outfits use a subtle top-light gradient instead of flat color, faces have blush cheeks and eye catchlights, the coin has a proper beveled highlight, and each scene carries a gentle vignette for depth.
- **A designed page system, not illustration-then-plain-text**: warm cream page background throughout, illustrations sit in a white matted, drop-shadowed frame (like a real picture-book plate), a small coin divider separates image from text, and story text sits in its own soft card set in a serif typeface with a colored lead-in word opening each page.
- **Visual infographics**: the Helping Chart (Page 28) is a card grid with mini helper avatars + object icons, not a plain text table; the Matching Game (Page 32) carries the same icon set. Page numbers are styled as small badges instead of plain gray text.
- A real, working single-solution maze (Page 31) and a hand-drawn line-art coloring page (Page 30).
- **A coordinated, muted storybook palette**: every helper's outfit color is now defined once (`PALETTE` / `HELPERS` in `scripts/build_kdp_interior.py`) and reused everywhere that character appears — the wheat-field scene, the market scene, the "all helpers together" page, the Helping Chart, and the Matching Game all show Farmer Ravi in the exact same sage green, not four different ad hoc greens. The old, more saturated/clashing hexes (bright yellow, hot pink, saturated blue) were replaced with muted sage/dusty-blue/plum/mustard/burnt-orange/dusty-rose tones that sit together harmoniously. Back-matter/activity pages also got their own teal accent color (headings, page-number badges, checkboxes) so they read as a distinct section from the terracotta-accented story pages.
- 32 single pages, 8.5" × 8.5" trim, no spreads, not encrypted, embedded (subset) fonts, clean minimal metadata, table rulings ≥ 0.75 pt, body text well above the 7-pt floor.

## Honest framing: this is a beta, not commissioned final art

The illustrations are original vector artwork built programmatically (see `scripts/`), styled to be warm and consistent rather than to be mistaken for a professional illustrator's finished work. Good for read-aloud testing, layout review, and getting a feel for pacing — not a substitute for final commissioned art if you want a fully polished trade-quality picture book.

## Not yet done — required before you actually upload to KDP

1. **Illustrator name** — flagged in red on the title/copyright pages. Fill in or remove the credit line. If you keep this vector art as final, credit yourself/this generator instead.
2. **Bleed rebuild, if you want art to run to the page edge** — this file is deliberately no-bleed (every scene is inset from the trim edge). If you want full-bleed spreads, the file must be regenerated at trim+bleed size (8.625" × 8.75" per KDP's bleed formula: +0.125" outside edge, +0.125" top and bottom, 0" at the spine).
3. **ISBN** — intentionally omitted from the interior. Either let KDP assign a free ISBN during title setup, or add your own once you have one.
4. Full (non-subset) font embedding is a "nice to have" per KDP's guide, not a hard requirement — subset embedding (what this file has) is standard and accepted.

## Generator

- `scripts/svgkit.py` — reusable flat-vector asset library: characters (Milu, Pico, coin, generic helper "adult" with swappable accessories), props (wheat, bus, cow, sewing machine, hospital wall, school building, market stall, furniture...), and small icon glyphs used in the infographics.
- `scripts/build_kdp_interior.py` — composes each of the 24 scenes from that library, lays out front/back matter and activities, and renders the whole thing via weasyprint. Run with `python3 scripts/build_kdp_interior.py` from the `kdp/` directory; it writes the PDF one level up.
- Story text and scene data are authored directly in the script, not derived from `manuscript/my-first-money-adventure.md` — if you edit the story, edit both places or ask to regenerate.

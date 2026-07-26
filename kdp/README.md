# KDP Interior — Illustrated Beta

`My-First-Money-Adventure-KDP-Interior-DRAFT.pdf` is a **paperback interior** file formatted to Amazon KDP's technical spec — reader-facing content only (no illustration prompts, interactive questions, or production notes visible on the page) — with real illustrations and a designed, polished layout, not placeholder boxes or plain text-on-white.

## What's in this version

- **All 24 story pages are illustrated** with original flat-vector scenes (not photos or AI-generated raster images — hand-built SVG, rendered crisp at any size): consistent character designs for Milu, Pico, the coin, and all eight helpers across every scene, gradient skies, and scene-appropriate props (wheat field, bus, sewing machine, hospital room, market stall, etc.).
- **Color-psychology palette, tuned for ages 3-5, not muted adult pastels**: preschoolers engage more with bright, saturated color than the softer tones adults tend to prefer. Every character's hue is chosen for what it should make a small child feel — green for Farmer Ravi (growth, safety), blue for Driver Joseph (calm, dependable), purple for Teacher Fatima (imagination), gold for Tailor Suresh (cheer), white for Doctor Ananya (gentleness), orange for Builder Karim (energy), pink for Shopkeeper Meena (warmth). Milu herself is a vivid coral-red (the "follow me" color) and Pico a bright sky blue (a calm, trustworthy companion color that doesn't compete with her). Documented with the reasoning inline in `PALETTE`/`HELPERS` in `scripts/build_kdp_interior.py`.
- **Richer gradients throughout**: 3-stop sky gradients (not flat 2-color fades), a beveled/highlighted coin, soft top-light gradients on every outfit, a rainbow gradient "picture-book plate" frame around every story illustration, and a gradient text card.
- **A layout built around the picture, the way young-reader books are laid out**: every story illustration now bleeds to the full page edge (not inset in a margin) so the art dominates the page instead of sharing it with whitespace, story text is bigger (16.5pt) and sits in its own card below, and the page number moved off the picture into a small badge in the divider so nothing sits on top of the art.
- **Visual infographics**: the Helping Chart (Page 28) is a card grid with mini helper avatars + object icons, not a plain text table; the Matching Game (Page 32) carries the same icon set.
- A real, working single-solution maze (Page 31) and a hand-drawn line-art coloring page (Page 30).
- Every helper's outfit color is defined once and reused everywhere that character appears (the wheat-field scene, the market scene, the "all helpers together" page, the Helping Chart, the Matching Game) — no more drift between an ad hoc hex in one scene and a different one in another. Back-matter/activity pages keep their own teal accent so they read as a distinct section from the terracotta-accented story pages.
- 32 single pages, 8.5" × 8.5" trim, not encrypted, embedded (subset) fonts, clean minimal metadata, table rulings ≥ 0.75 pt, body text well above the 7-pt floor.

## Honest framing: this is a beta, not commissioned final art

The illustrations are original vector artwork built programmatically (see `scripts/`), styled to be warm and consistent rather than to be mistaken for a professional illustrator's finished work. Good for read-aloud testing, layout review, and getting a feel for pacing — not a substitute for final commissioned art if you want a fully polished trade-quality picture book.

## Not yet done — required before you actually upload to KDP

1. **Illustrator name** — flagged in red on the title/copyright pages. Fill in or remove the credit line. If you keep this vector art as final, credit yourself/this generator instead.
2. **This file now visually bleeds but is sized at trim only (8.5"×8.5"), not trim+bleed** — story illustrations intentionally run to the page edge for a bigger, more immersive image, but the physical page is still exactly 8.5"×8.5" with no extra overhang. For actual print, KDP needs the page built at trim+bleed size (8.625"×8.75" — +0.125" outside edge, +0.125" top/bottom, 0" at the spine) with the same art extending past that new edge, so ordinary manufacturing trim tolerance can't leave a thin white sliver. Rebuilding at that size is a straightforward change to `@page` and the illustration viewBoxes in `scripts/build_kdp_interior.py`, not a redesign.
3. **ISBN** — intentionally omitted from the interior. Either let KDP assign a free ISBN during title setup, or add your own once you have one.
4. Full (non-subset) font embedding is a "nice to have" per KDP's guide, not a hard requirement — subset embedding (what this file has) is standard and accepted.

## Generator

- `scripts/svgkit.py` — reusable flat-vector asset library: characters (Milu, Pico, coin, generic helper "adult" with swappable accessories), props (wheat, bus, cow, sewing machine, hospital wall, school building, market stall, furniture...), and small icon glyphs used in the infographics.
- `scripts/build_kdp_interior.py` — composes each of the 24 scenes from that library, lays out front/back matter and activities, and renders the whole thing via weasyprint. Run with `python3 scripts/build_kdp_interior.py` from the `kdp/` directory; it writes the PDF one level up.
- Story text and scene data are authored directly in the script, not derived from `manuscript/my-first-money-adventure.md` — if you edit the story, edit both places or ask to regenerate.

# KDP Interior — Draft

`My-First-Money-Adventure-KDP-Interior-DRAFT.pdf` is a **paperback interior** file formatted to Amazon KDP's technical spec — reader-facing content only (no illustration prompts, interactive questions, or production notes visible on the page).

## What's already correct

- 32 single pages (even count), 8.5" × 8.5" trim, no spreads
- No bleed (illustration boxes are inset from the edge — see "Not yet done" below)
- Not encrypted, no forms/annotations, minimal clean metadata (Title + Author only)
- Fonts embedded (subset)
- Body text set well above the 7-pt legibility floor
- Table/line rulings are ≥ 0.75 pt
- A real, working single-solution maze (Page 31) and a simple line-art coloring page (Page 30), built as vector art — not placeholders

## Not yet done — required before you actually upload to KDP

1. **Illustrator name** — flagged in red on the title/copyright pages. Fill in or remove the credit line.
2. **Real illustrations** — every dashed gray box on the 24 story pages (`ILLUSTRATION PLACEHOLDER`) is a stand-in. KDP will reject a book with visible placeholder boxes; these must be replaced with final art from an illustrator (see `manuscript/my-first-money-adventure.md` → Appendix B, the Illustration Consistency Guide, for the character bible/palette/lighting rules to hand them).
3. **Bleed rebuild, if your final art bleeds to the page edge** — this draft is deliberately no-bleed. If the illustrator's final pages have color/art running off the trim edge, the file must be regenerated at trim+bleed size (8.625" × 8.75" per KDP's bleed formula: +0.125" outside edge, +0.125" top and bottom, 0" at the spine) before upload.
4. **ISBN** — intentionally omitted from the interior. Either let KDP assign a free ISBN during title setup, or add your own once you have one.
5. Full (non-subset) font embedding is a "nice to have" per KDP's guide, not a hard requirement — subset embedding (what this file has) is standard and accepted.

## Generator

Built by `build_kdp_interior.py` (weasyprint) from data authored directly in that script — not derived from the manuscript markdown, so if you edit the story text, edit both places or ask to regenerate.

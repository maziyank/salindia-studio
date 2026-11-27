<!-- ppt-master-schema: design-spec/v1 -->
# Brutalism Field Guide - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | brutalism_field_guide |
| Canvas Format | ppt169, 1280 × 720 px |
| Page Count | 16 |
| Primary Language | en |
| Target Audience | English-reading adults with a general interest in architecture and cities — they recognise the concrete buildings but do not know where the style came from, what its architects believed, or why it was hated and then loved again |
| Communication Intent | Explain first — make the origin of the word, the material logic, and the ethic traceable; then inform completely about the figures, buildings and the demolition-versus-listing record; finally reframe the reader's judgement of the style without arguing them into liking it |
| Desired Audience Outcome | The reader can say where "new brutalism" came from, name the material logic behind béton brut, name three canonical buildings and their architects, explain both the backlash and the revival, and look at a concrete building with an informed rather than a reflexive reaction |
| Core Message / Ask / Action | Brutalism was an ethic before it was a look: show the structure, show the material as found — and that honesty is exactly what made it both hated and, fifty years on, worth saving |
| Delivery Context | Reader-led. A self-standing English briefing read on screen at desk distance; no live presenter. Secondary use as a leave-behind reference for an architecture reading group |
| Artifact Afterlife | Reference and reuse — kept, re-read, and shared; every claim traceable to the single cited source page |
| Reading Mode | text |
| Content Strategy | Balanced. Re-architect the encyclopedia article into a story arc — origin, ethic, buildings, reckoning, revival — while keeping every fact, name, date and quotation exactly as the source states them. Add no fact the source does not carry; where a figure is missing, say so on the page rather than estimating |
| Design Style | Brutalist editorial newspaper carrying a narrative arc — a field guide printed on newsprint: masthead numerals, irregular column widths, heavy rules, one inverted focal cell per spread, halftone documentary photography |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — workflow default (proactive Stage-2 value `true`) |
| Custom Animations | enabled — explicit user instruction: at least two Morph pairs plus entrance motion |
| Narration Audio | disabled — final Stage-2 proactive policy |
| Created Date | 2026-09-04 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | ppt169 |
| Dimensions | 1280 × 720 px |
| viewBox | `0 0 1280 720` |
| Margins | 48 px left/right, 40 px top, 44 px bottom |
| Content Area | x 48–1232, y 40–676 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Visual style**: custom
- **Mode References**: narrative
- **Mode Behavior**: Run one arc across five parts — a house in Uppsala gets a name (situation), the name hardens into an ethic (rising stake), the ethic becomes hundreds of public buildings (payoff), the public turns on them and the wrecking balls arrive (reversal), then the style is listed, reprinted and rebuilt (resolution). Titles read as beats that advance the story, never as topic labels. Each part opens on a visibly reset page and the two evidence tables land as the story's factual floor, not as an appendix.
- **Visual Style References**: brutalist
- **Visual Style Behavior**: Newsprint field guide. Irregular two-, three-, and four-column measures on one 12-column ruleset, mixed within a page; ink hairline column dividers and 6–10 px full-bleed rule bars slicing sections; a masthead numeral set at 120 px that crosses column rules and carries the page identity; one grid cell per page inverted to solid ink with paper-light type as the focal cell; a single rotated stamp box (2–4°) breaking the grid at one deliberate point on the anchor pages; `rx="0"` everywhere, no shadow, no gradient except a halftone `<pattern>` dot field used as printed texture. Photography enters only as high-contrast duotone or halftone, cropped hard into a ruled box. Colour is punctuation — the spot red appears at most twice per page, on a masthead rule or one key figure.
- **Theme**: A printed field guide to raw concrete: the page is built the way the buildings were — structure exposed, grid visible, nothing smoothed. Recurring motif: the **masthead numeral**, an oversized page number set in the display face, crossing the top rule; its continuity job is to number the field guide like plates in a printed manual, and it varies in position and scale by page rhythm.
- **Tone**: Reportorial, dry, unsentimental — a critic's field notes rather than an advocate's brochure.

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F2F0EA | Newsprint paper field, every page |
| Secondary background | #E2DFD5 | Grey stock for boxed columns, sidebars, table banding |
| Primary | #14110F | Ink — rules, masthead numerals, headline type, inverted focal cells |
| Accent | #C8331E | Spot red punctuation — one masthead rule, key figure, or stamp box per page |
| Secondary accent | #6E6A62 | Weathered concrete grey — halftone duotone shadow, secondary rules, quiet fills |
| Body text | #1C1A17 | Column body type on paper |
| Secondary text | #55514A | Captions, annotations, source lines, footnotes |
| Divider | #9A958B | Hairline column dividers, table rules lighter than the section bars |

Additional anchored neutral roles: `surface` #E2DFD5 (boxed column lift, identical to secondary background by design), `grid` #C9C5BA (halftone dot field and table hairlines), `scrim` #14110F at plan-level meaning "ink scrim under type over a photograph", `block-shade` #D8D4C8 (one step off the paper field for print-fill blocks).

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | Display sans, poster-black weight; the headline collision this style needs | Arial Black | — | Arial Black |
| Body | Transitional serif with lining figures; column body at small size, tight leading | Cambria | — | Cambria |
| Cover title | Poster-black at cover scale — the display word that opens the guide | Arial Black | — | Arial Black |
| Display numeral | The masthead numeral crossing the top rule on every page | Arial Black | — | Arial Black |
| Subtitle | Serif, not black — a quiet second line under a black headline | Cambria | — | Cambria |
| Lead | Serif at reading weight — the page's primary claim | Cambria | — | Cambria |
| Data | Monospace figures, table columns, years, heights, counts | Consolas | — | Consolas |
| Annotation | Monospace small — captions, credits, source lines | Consolas | — | Consolas |
| Table body | Monospace agate — the cell text of the two full-width record tables | Consolas | — | Consolas |
| Footnote | Monospace smallest — page numbers and licence lines | Consolas | — | Consolas |

- **Title stack**: Arial Black
- **Body stack**: Cambria
- **Cover title stack**: Arial Black
- **Display numeral stack**: Arial Black
- **Subtitle stack**: Cambria
- **Lead stack**: Cambria
- **Data stack**: Consolas
- **Annotation stack**: Consolas
- **Table body stack**: Consolas
- **Footnote stack**: Consolas
- **Role rationale**: `Cover title` and `Display numeral` separate the 80 px cover word and the 120 px masthead numeral from ordinary page titles so neither oversized carrier depends on the Executor display exception; `Subtitle` and `Lead` are pinned to the serif so a black headline is never followed by a second black line; `Data`, `Annotation`, and `Footnote` give the two native tables, every year, height and count, the photo credits and the page numbers a monospace column the serif body cannot supply; `Table body` is the agate cell size the two full-width record tables need to carry every named architect and building without dropping one, and it recurs on both table pages.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 20 |
| Title | 36 |
| Subtitle | 26 |
| Annotation | 16 |
| Cover title | 80 |
| Lead | 24 |
| Display numeral | 120 |
| Data | 22 |
| Table body | 16 |
| Footnote | 12 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: Attention enters at the masthead numeral or the top rule bar, drops to the headline set flush left, then reads down the widest column; the inverted focal cell catches the eye once per page and holds the page's single hardest fact.
- **Composition tendency**: Irregular column measures over a 12-column ruleset — a page may run 5+7, 4+4+4, 3+6+3, or 8+4 — never the same split on adjacent pages. Full-bleed rule bars mark section changes. Photographs are cropped into ruled boxes that sit on column lines, never floated.
- **Cross-page continuity**: The masthead numeral recurs on every page and is the deck's continuity carrier; the top rule bar recurs at a stable weight; the inverted focal cell recurs once per page and moves. Part openers reset visibly by giving the numeral the full left column.
- **Spacing posture**: Dense by default with deliberate breathing at the two part-reset beats and the closing.
- **Spacing anchors**: page margin 48 px; block gap 24 px; column gutter 20 px; corner radius 0 px; body leading 30 px.

## VI. Icon Usage Specification

- **Primary bundled library**: chunk-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| chunk-filled/building | A named building, structure, or canonical work |
| chunk-filled/block-quote | A pull quote lifted from an architect or critic |
| chunk-filled/calendar | A dated event in the timeline of the style |
| chunk-filled/trash | Demolition and loss |
| chunk-filled/bookmark | Listing, protection, preservation |
| chunk-filled/globe | International spread of the style |
| chunk-filled/hammer | Material, construction, and fabric |
| chunk-filled/user | A named architect or critic |
| chunk-filled/book | A published book, essay, or citation |
| chunk-filled/link | An external source reference |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P09 | table | record_table | One row per country with its named brutalist architects and the works the source attributes to them |
| P13 | table | record_table | One row per building with its architect, year of loss or listing, and the source-stated outcome |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| src_beton_brut.jpg | 5358×3572 | 1.50 | Cover field — the raw concrete surface the whole guide is about | Source | not placed | adaptive | web | Sourced | Board-marked or shuttered raw concrete façade of a brutalist building, frontal or steeply angled, strong directional daylight raking the surface so the formwork grain reads; quiet upper-left region for the masthead; no people, no sky-dominant framing | none | — |
| cover_beton_brut_duo.png | 1000×667 | 1.50 | Cover — the concrete field, printed | image | Cropped hard into a ruled square box holding the right third of the cover while the display word runs across it; the photograph is the page's only tonal mass | adaptive | web | Sourced | Derived from src_beton_brut.jpg; treatment=contrast 1.35 then duotone #14110F/#F2F0EA then fit 1000x1000 | none | — |
| src_boston_city_hall.jpg | 4080×3060 | 1.33 | Evidence for the page on exposing a building's inner workings | Source | not placed | no-crop | web | Sourced | Boston City Hall, Boston, USA — exterior showing the projecting upper volumes over the recessed base, so the differently shaped projections that mark the special rooms behind them are legible; daylight, whole building in frame | none | — |
| boston_city_hall_half.png | 900×675 | 1.33 | The building whose outside announces its inside | image | Sits in a ruled box on the narrow column beside the argument, with the projecting volumes aligned to a column rule so the page grid and the building's grid rhyme | no-crop | web | Sourced | Derived from src_boston_city_hall.jpg; treatment=contrast 1.4 then duotone #14110F/#E2DFD5 then fit 900x900 | none | — |
| src_demolition.jpg | 6000×4000 | 1.50 | The reckoning — a brutalist block coming down | Source | not placed | adaptive | web | Sourced | A concrete tower block or slab mid-demolition or partly collapsed, dust and exposed floor plates visible; documentary, unromantic, wide enough to read the structure being destroyed | none | — |
| demolition_mono.png | 1000×667 | 1.50 | The page where the public verdict becomes physical | image | Full-width band across the lower half of the page, cropped to a letterbox so the falling structure runs against the horizontal rules; the inverted focal cell sits directly above it | adaptive | web | Sourced | Derived from src_demolition.jpg; treatment=contrast 1.5 then duotone #14110F/#C9C5BA then fit 1000x1000 | none | — |
| src_ningbo_museum.jpg | 5472×3648 | 1.50 | The revival — neobrutalism built | Source | not placed | no-crop | web | Sourced | Ningbo Museum, Ningbo, China, by Wang Shu — exterior wall showing the monumental mass and its textured recycled surface; daylight, whole façade section in frame | none | — |
| ningbo_museum_duo.png | 900×600 | 1.50 | Proof the ethic outlived the movement | image | Ruled box on the right column facing the neobrutalism argument, cropped to the wall itself so the surface texture, not the skyline, is what the reader sees | no-crop | web | Sourced | Derived from src_ningbo_museum.jpg; treatment=contrast 1.3 then duotone #14110F/#E2DFD5 then fit 900x900 | none | — |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: Conversational narration grounded in the final SVG of each page — bridge from the previous beat, name what the reader is looking at, add the connective reasoning the dense columns cannot carry, and never introduce a fact absent from the page or the source article. Quotations stay verbatim; the two NO DATA gaps are named as gaps.
- **Total duration**: approximately 16–20 minutes at a reading pace of about 70–80 seconds per page
- **Notes style**: conversational
- **Presentation purpose**: Explain the origin, material logic and ethic of brutalism, inform completely about its architects, buildings and the demolition-versus-listing record, and leave the reader able to judge a concrete building on the terms the style set for itself

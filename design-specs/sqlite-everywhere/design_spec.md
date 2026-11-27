<!-- ppt-master-schema: design-spec/v1 -->
# SQLite Everywhere - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | sqlite_everywhere_ppt169_20261024 |
| Canvas Format | ppt169 — PPT 16:9, 1280×720 |
| Page Count | 12 |
| Primary Language | en |
| Target Audience | Software engineers at an internal technical sharing session; they write SQL and run client/server databases, and may think of SQLite as a toy or test-only store |
| Communication Intent | Explain why SQLite is the most deployed database: first the deployment evidence, then the mechanism (in-process architecture, layer stack, B-tree pages, rollback journal vs WAL), then the trust factors (testing culture, public-domain license); finish by teaching the official when-to-use / when-not-to-use judgment |
| Desired Audience Outcome | Engineers can describe SQLite's layer stack and the rollback-journal vs WAL trade-off, and can apply sqlite.org's checklist to decide when SQLite fits and when a client/server engine is the better choice |
| Core Message / Ask / Action | SQLite is everywhere because it competes with fopen(), not with Oracle: an in-process, zero-configuration, single-file engine, verified by test code 590× the size of the library and free of any license |
| Delivery Context | Presenter-led engineering tech talk (about 20 minutes, projected); secondary: the deck is shared afterwards as a reference |
| Artifact Afterlife | Shared reference deck for the team; sources cited on page so readers can follow up on sqlite.org |
| Reading Mode | balanced |
| Content Strategy | balanced default (content_divergence left blank): re-architect the official sqlite.org pages into one teaching arc, keeping every figure exactly as published |
| Design Style | Custom "Drafting Sheet" — engineering blueprint schematic on dark paper (direction 0 of 3, selected) |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — explicit user instruction (dogfood brief: Speaker Notes=true) |
| Custom Animations | enabled — explicit user instruction (dogfood brief: Custom Animations=true, objects scope, adjacent-page Morph at least twice) |
| Narration Audio | disabled — explicit user instruction (dogfood brief: Narration Audio=false) |
| Created Date | 2026-10-24 |

Confirmation surface: the user explicitly delegated both confirmation gates to the agent. Stage 1 decided `free_design` (no template intent, no supplied workspace root). Stage 2 authored three directions — 0 "Drafting Sheet" (dark blueprint schematic, Bahnschrift + Segoe UI + Consolas, contrast pairing), 1 "Datasheet" (white-paper data-journalism grid, Arial throughout + Consolas, concord pairing, signal-red accent), 2 "Terminal" (near-black dark-tech, phosphor green, Consolas-led headings) — and selected 0 because the content is mostly architecture, page anatomy, and process diagrams that read most naturally as annotated engineering drawings. `design_spec_depth: brief`.

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 64 px left/right, 48 px top, 40 px bottom |
| Content Area | x 64–1216, y 48–680 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional, pyramid
- **Mode Behavior**: Open with the conclusion-level evidence (it is everywhere, here is why that is plausible), then teach the mechanism top-down through the layer stack in ordered, annotated steps where each page explains one layer or one mechanism; close with the trust factors and a decision checklist the engineer can apply. Titles state what the page teaches.
- **Visual style**: custom
- **Visual Style References**: blueprint
- **Visual Style Behavior**: Each page is a sheet from one engineering drawing set: deep navy paper with a faint 32 px grid, all structure drawn in thin single-weight pale-cyan line work (1.25–2 px, square or 2 px corners), components as outlined boxes with mono component codes, connectors with arrowheads and dimension lines, leader-line annotations instead of cards; one amber spot accent marks the current layer, key path, or hero number per page; a small drawing-sheet title block (sheet number, source page) anchors the lower-right corner of every content page. Depth comes from isometric layering and line weight, never shadows.
- **Theme**: SQLite as an engineered object laid open on the drafting table — one file, one library, one stack of layers
- **Tone**: precise, calm, quietly confident; technical without hype

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #0B1F3A | Blueprint paper field on every page |
| Secondary background | #11294B | Panel lift, title block, table header fills |
| Primary | #8CC4EE | Schematic line work, frames, connectors, icons |
| Accent | #FFB547 | Single spot highlight: current layer, key path, hero number |
| Secondary accent | #5ED3C4 | Second semantic lane (WAL / "works well" side) when a page contrasts two mechanisms |
| Body text | #EAF2FB | Titles and body copy |
| Secondary text | #9FB6CF | Captions, annotations, source lines |
| Divider | #2D4C74 | Rules, table borders, hairlines |
| Grid | #16305A | Faint background grid lattice |
| Negative | #FF7A6B | "Use client/server instead" / failure markers |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: blueprint
- **Image Rendering Behavior**: Technical blueprint line drawing on deep navy paper: crisp uniform pale-cyan strokes, isometric axonometric projection, faint grid at very low opacity, a single amber highlight on the focal element. No shading, no texture, no glow halos, no painterly marks; reads like a draftsman's exploded-assembly sheet.
- **Visual**: an exploded isometric drawing of one database file opened into stacked fixed-size pages, with leader lines and blank callout tags
- **Mood**: precise and calm, like an exploded-view sheet in a machinist's manual

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | DIN-like engineering sans, slightly condensed | Bahnschrift | — | sans-serif |
| Body | Neutral humanist sans | Segoe UI | — | sans-serif |
| Code | Monospace for component names, file names, API calls, coordinates | Consolas | — | monospace |

- **Title stack**: Bahnschrift, sans-serif
- **Body stack**: Segoe UI, sans-serif
- **Code stack**: Consolas, monospace
- **Display stack**: Bahnschrift, sans-serif
- **Hero stack**: Bahnschrift, sans-serif
- **Role rationale**: `code` carries every component code, source file name, and API symbol the blueprint style labels in mono; `display` keeps hero numerals in the title family.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 22 |
| Title | 40 |
| Subtitle | 28 |
| Lead | 26 |
| Annotation | 16 |
| Footnote | 13 |
| Code | 17 |
| Kicker | 15 |
| Cover Title | 76 |
| Hero | 112 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: kicker (sheet code) → title → the drawing → annotations → source line; the eye lands on the amber element first
- **Composition tendency**: the schematic is the layout — one dominant drawing per page with copy hung on leader lines or set in a narrow side column; comparisons as two lanes of the same drawing
- **Cross-page continuity**: a recurring layer-stack rail (eight labelled bands from Interface to OS Interface) appears on the architecture pages and its amber marker moves as the explanation descends; the drawing-sheet title block recurs on every content page
- **Spacing posture**: variable by page rhythm — dense diagram pages, one breathing page (P10), open anchors
- **Spacing anchors**: page margin 64 px · block gap 24 px · column gutter 32 px · corner radius 2 px · body leading 1.4

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 1.5
- **Brand-logo library**: simple-icons (real platforms and products named by sqlite.org/mostdeployed and the SQLite mark itself)

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/database.svg | |
| icons/tabler-outline/file.svg | |
| icons/tabler-outline/server.svg | |
| icons/tabler-outline/device-mobile.svg | |
| icons/tabler-outline/device-desktop.svg | |
| icons/tabler-outline/device-tv.svg | |
| icons/tabler-outline/car.svg | |
| icons/tabler-outline/browser.svg | |
| icons/tabler-outline/code.svg | |
| icons/tabler-outline/binary.svg | |
| icons/tabler-outline/stack-2.svg | |
| icons/tabler-outline/lock.svg | |
| icons/tabler-outline/shield-check.svg | |
| icons/tabler-outline/bug.svg | |
| icons/tabler-outline/test-pipe.svg | |
| icons/tabler-outline/license.svg | |
| icons/tabler-outline/network.svg | |
| icons/tabler-outline/users.svg | |
| icons/tabler-outline/bolt.svg | |
| icons/tabler-outline/refresh.svg | |
| icons/tabler-outline/file-zip.svg | |
| icons/tabler-outline/circle-check.svg | |
| icons/tabler-outline/circle-x.svg | |
| icons/tabler-outline/alert-triangle.svg | |
| icons/tabler-outline/settings-off.svg | |
| icons/tabler-outline/certificate.svg | |
| icons/tabler-outline/cpu.svg | |
| icons/tabler-outline/world.svg | |
| icons/tabler-outline/terminal-2.svg | |
| icons/tabler-outline/feather.svg | |
| icons/simple-icons/sqlite.svg | |
| icons/simple-icons/android.svg | |
| icons/simple-icons/apple.svg | |
| icons/simple-icons/windows.svg | |
| icons/simple-icons/firefoxbrowser.svg | |
| icons/simple-icons/googlechrome.svg | |
| icons/simple-icons/safari.svg | |
| icons/simple-icons/skype.svg | |
| icons/simple-icons/itunes.svg | |
| icons/simple-icons/dropbox.svg | |
| icons/simple-icons/python.svg | |
| icons/simple-icons/php.svg | |
| icons/simple-icons/quickbooks.svg | |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P09 | table | metric_table | Compare the four independent test harnesses by size, case count, and what each one guarantees |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_file_stack.png | 2752×1536 | 16:9 | Canonical generated drawing; feeds the two placed derivatives | Source | Not placed; source for cover and closing derivatives | adaptive | ai | Generated | Exploded isometric blueprint of a single database file: a thin file slab with about eight stacked equal-size page sheets lifted above it, top sheet amber, leader lines ending in empty callout tags, a dimension line along one edge; subject in the right two-thirds, left third quiet navy paper with faint grid | none | hero_page |
| cover_file_stack_fit.jpg | 1600×893 | 16:9 | Cover hook visual: one file that is a whole database | Illustration | Full-bleed drawing field; the exploded file sits in the right two-thirds while the left third stays quiet paper for the native title block; the empty callout tags may receive native mono labels | adaptive | ai | Generated | Derived from cover_file_stack.png; treatment=fit 1600x900; | none | hero_page |
| closing_file_stack_dim.jpg | 1600×893 | 16:9 | Closing field: the same drawing receded behind the final takeaway | Illustration | Full-bleed receded field under a dark scrim; the takeaway sits on top as native text | adaptive | ai | Generated | Derived from cover_file_stack.png; treatment=brightness 0.45, blur 3, fit 1600x900; | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: explain each drawing in the order it reveals; every number comes from the cited sqlite.org page; mention the source page aloud where a number is surprising
- **Total duration**: about 20 minutes
- **Notes style**: conversational, patient engineering explainer
- **Presentation purpose**: explain why SQLite is the most deployed database, teach its architecture and journaling trade-offs, and equip engineers to decide when to use it

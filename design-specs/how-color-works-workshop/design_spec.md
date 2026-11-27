<!-- ppt-master-schema: design-spec/v1 -->
# How Color Works - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | how_color_works_ppt169_20260910 |
| Canvas Format | PPT 16:9 — 1280 × 720 |
| Page Count | 14 |
| Primary Language | en-US |
| Target Audience | Working designers, front-end developers and marketers who choose colors every week — fluent in their tools, with no formal training in optics, color science or accessibility, sceptical of "design taste" arguments, and short on time |
| Communication Intent | Teach first, then persuade: give practitioners the minimum physical and physiological model they need, get them to apply it in two live exercises, and along the way keep what is a published rule separate from what is only an inherited convention, so they stop treating the two the same way |
| Desired Audience Outcome | Each participant can say why a specific color pair fails, check it against a WCAG threshold, extract and repair a five-color palette from a real image, and explain why a rainbow ramp is the wrong default for ordered data |
| Core Message / Ask / Action | Most color decisions that feel like taste are lightness decisions — separate hue from lightness, measure the lightness, and what is left is judgement you can defend |
| Delivery Context | Primary: a presenter-led 90-minute hands-on workshop with two working exercises at the participants' own screens. Secondary: the file is handed out afterwards and re-read alone |
| Artifact Afterlife | Reused as a self-serve reference and as material another facilitator can re-run; the source links must stay clickable |
| Reading Mode | balanced |
| Content Strategy | Balanced default (no material-divergence constraint stated). The research pair is the only fact source; every external number is cited by fact id and no figure is invented |
| Design Style | Studio Worksheet — a quiet warm-paper worksheet on a strict grid, where the only saturated color on any page is the color being taught |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy (`proactive_speaker_notes: true`) |
| Custom Animations | enabled — final Stage-2 proactive policy (`proactive_custom_animations: true`); the deck teaches by building swatches and states up in order |
| Narration Audio | disabled — final Stage-2 proactive policy (`proactive_narration_audio: false`) |
| Created Date | 2026-09-10 |

- **Template Application**: Adopt the Workshop Teaching method wholesale — its objective → minimum concept → worked demonstration → guided practice → common mistake → understanding check → recap sequence orders the roster, and its claim discipline becomes a visible labelling system on the pages (RULE / CONVENTION / RECOMMENDATION / PREFERENCE). Adopt its evidence obligations: charts teach a relationship and are labelled directly on the mark, the reference card is a native editable table, exercise pages stay visually distinct from teaching pages, and the incorrect and corrected states sit in direct correspondence. Adopt its color-behavior default of a light calm field with a fixed teaching mapping for new / changed / correct / wrong that survives without color alone, and its typography character of a warm legible sans with a genuinely monospaced companion for anything the learner types or reads as a value. Depart from its preferred `sketch-notes` visual style and rendering, and from its hand-adjacent decoration density, for one reason recorded in §III: this deck's subject is color itself, so the page's own palette and texture must recede completely; a warm-paper field with a strict grid and hairline rules keeps every saturated pixel available to the demonstrated colors, and precise swatch and contrast comparisons need exact edges rather than wobbled ones. The Style's functional annotation layer — an arrow that points at something specific, a mark on the part that changed — is kept, because it is the part of that decoration budget which carries information. The Style supplies no structure or roster, so the deck stays flat free design.

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 64 px left/right, 56 px top, 56 px bottom |
| Content Area | x 64–1216, y 56–664 (1152 × 608) |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional
- **Mode Behavior**: Run the deck as one 90-minute teaching cycle rather than a topic tour: state the observable capability first, introduce each concept only at the moment it is needed to act, then demonstrate the whole task with real input and real output, hand the same task over for timed practice, show the two mistakes the learner is about to make with their actual cause, and close with a check that asks for application rather than recall. Titles say what the page teaches or what the learner does there. Every claim on a page is labelled as a rule, a convention, a recommendation or a preference, and a deliberate simplification is marked as one instead of being left to look complete.
- **Visual style**: custom
- **Visual Style References**: swiss-minimal, editorial, sketch-notes
- **Visual Style Behavior**: `swiss-minimal` owns the skeleton — a strict modular grid, flush-left alignment, exact square-cornered geometry, one large organizing plane per page and vast deliberate whitespace, strictly flat with no shadow or material. `editorial` owns the hierarchy — a kicker line above each page title, hairline rules instead of repeated cards, an asymmetric column split, and small labelled asides that carry the RULE / CONVENTION / RECOMMENDATION / PREFERENCE chips and the source lines. `sketch-notes` contributes only its functional annotation layer: a hand-weight arrow that points at one exact target, a ring around the part that changed, a short inline label next to it — never doodles, ribbons, wobbled containers or pastel blocks. The page field stays warm near-white and near-monochrome so that swatches, ramps, wheels and contrast pairs are the only saturated marks on the canvas.
- **Theme**: A studio worksheet — paper, a ruler-straight grid, ink, and the colors under examination pinned to it.
- **Tone**: Plain, unhurried, unsentimental; confident about what is measurable and honest about what is only convention.

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | `#FAF8F4` | The warm paper field of every page |
| Secondary background | `#EDE7DC` | Recessed panels: exercise blocks, reference card ground, aside tint |
| Primary | `#23201C` | Ink — page titles, rules that must read as structure, the darkest mark |
| Accent | `#A8452B` | The `new` teaching state: what is being introduced on this page; kicker rules and pointer marks |
| Secondary accent | `#3E5C6B` | The `changed` teaching state: what was just edited or repaired; hyperlink color |
| Body text | `#2E2A25` | All running text |
| Secondary text | `#6B6259` | Captions, annotations, source lines, footnotes |
| Divider | `#D8D0C3` | Hairline rules, column dividers, table borders |

Additional locked neutral and semantic tiers: `surface` `#FFFFFF` (the white card a swatch or chart sits on so a light demonstrated color still has an edge), `grid` `#E8E1D5` (chart hairlines, lighter than dividers), `positive` `#2E7D32` (the `correct` state), `negative` `#C62828` (the `wrong` state), `warning` `#F57C00` (a borderline result).

**Fixed teaching mapping, reused on every page and never re-assigned**: `new` = accent `#A8452B` plus a filled square marker; `changed` = secondary accent `#3E5C6B` plus a dashed outline on the edited element; `correct` = positive `#2E7D32` plus a check glyph and the word PASS; `wrong` = negative `#C62828` plus a cross glyph and the word FAIL. Every state carries a glyph and a word, so the deck's own status encoding survives being read by someone who cannot separate its hues — which is itself the point of P12.

**Demonstrated colors are content, not identity**: the five palette colors sampled from the P08 artwork, the hue-wheel wedges, the lightness ramp steps and the before/after contrast pairs are page-local content paint derived from the material, not palette roles, and never replace an anchor above.

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: ink-notes, editorial
- **Image Rendering Behavior**: Explanatory pen-on-paper drawing on the deck's own warm paper field. `ink-notes` owns the mark — confident medium-weight ink line work in the deck's body-text tone with a slight human wobble, flat, no shadow, no grain, backgrounds and fills left mostly empty so the line carries the explanation. `editorial` owns the composition — one dominant focal subject, deliberate alignment to invisible columns, generous negative space, and simple geometric forms rendered with editorial confidence rather than cartoon warmth. Color stays under 10% of each image and comes only from the deck's accent and secondary-accent roles, except where the drawing's own subject is light itself, where the spectrum it disperses is the subject and may be fully saturated.
- **Visual**: Ink line drawings of physical apparatus and anatomy — a prism on a bench, an eye in section, a press sheet beside a lit screen — drawn as if by a patient instructor mid-explanation, with everything not being explained left as bare paper.
- **Mood**: The margin of a good textbook: unhurried, exact, hand-made but not cute. Closest real-world analogy is a Mike Rohde sketchnote redrawn with an architect's discipline.

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | Humanist sans, warm, slightly calligraphic terminals | Trebuchet MS | — | — |
| Body | Humanist sans, open apertures, high legibility at distance | Segoe UI | — | — |
| Display | Monospaced, lining figures, exact digit widths | Consolas | — | — |
| Data | Monospaced, lining figures | Consolas | — | — |

- **Title stack**: `Trebuchet MS`
- **Body stack**: `Segoe UI`
- **Display stack**: `Consolas`
- **Data stack**: `Consolas`
- **Role rationale**: `Display` and `Data` leave the body family deliberately. Every number in this deck is a value the learner is expected to read exactly and often to type — hex triplets, contrast ratios, wavelengths, percentages — and the Style requires a genuinely monospaced companion for anything the learner types. `Display` carries the recurring hero ratios and percentages at scale; `Data` carries inline hex and ratio values inside running text and inside the reference table.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 42 |
| Subtitle | 32 |
| Annotation | 18 |
| Cover title | 72 |
| Lead | 30 |
| Display | 64 |
| Data | 22 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: A kicker line and a hairline rule at the top left establish where the page sits in the 90 minutes; the title states what happens here; attention then drops into one dominant demonstration region on the right or lower two-thirds, with the labelled claim chips and source line held at the bottom left where they never compete with the color being shown.
- **Composition tendency**: One large organizing plane or one dominant specimen region per page against wide margins; asymmetric splits rather than even columns; the demonstrated color always sits on the white `surface` tier so a pale sample still has an edge. Teaching pages keep a light two-region rhythm; the reference card and the check page may run denser under the same grid.
- **Cross-page continuity**: The kicker/rule/title lockup, the claim chips, the fixed four-state teaching mapping and the source line recur on every page. The hue wheel introduced on P05 is the same object on P06; the five sampled swatches introduced on P08 are the same five objects on P09 and are referenced again on P10. Exercise pages (P10) and the check page (P13) carry the recessed `secondary_bg` ground so a learner scanning the handout later finds them without reading.
- **Spacing posture**: Open on teaching and concept pages, deliberately denser on the reference card (P07) and the check page (P13), never uniform.
- **Spacing anchors**: page margin 64 px · block gap 32 px · column gutter 40 px · corner radius 4 px · body leading 36 px.

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| `tabler-outline/eye` | Vision, perception, what the viewer actually receives |
| `tabler-outline/bulb` | Light as a physical source; a point being introduced |
| `tabler-outline/palette` | Palette construction and color choice |
| `tabler-outline/color-swatch` | An individual sampled color, swatch handling |
| `tabler-outline/contrast` | Contrast, lightness comparison, the measurable rule |
| `tabler-outline/droplet` | Pigment, ink, subtractive mixing |
| `tabler-outline/device-desktop` | Screens, emitted light, additive mixing |
| `tabler-outline/printer` | Print output, physical reproduction |
| `tabler-outline/ruler` | Measurement, thresholds, checking a value |
| `tabler-outline/alert-triangle` | The common mistake, a warning about a tempting error |
| `tabler-outline/circle-check` | A passing result, a completed objective |
| `tabler-outline/circle-x` | A failing result |
| `tabler-outline/clock` | Timing inside the 90-minute run sheet, exercise duration |
| `tabler-outline/pencil` | Guided practice, something the learner does |
| `tabler-outline/help-circle` | The understanding check |
| `tabler-outline/link` | External tools and further reading |
| `tabler-outline/chart-bar` | Data encoding, ordered data |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | chart | column_chart | Compare where the three cone types peak along the spectrum |
| P07 | table | comparison_matrix | Look up the required contrast ratio by text class and conformance level |
| P12 | chart | horizontal_bar_chart | Compare how common each type of red-green color vision deficiency is among men |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `prism_bench.jpg` | 1920×1072 | 16:9 | Cover hook: light arriving as one beam and leaving as a spectrum | Illustration | Full-canvas field the cover title sits inside, with the dispersed spectrum band low and right so the display title keeps clean paper above and left of it | adaptive | ai | Generated | An ink line drawing of a triangular glass prism standing on a plain workbench; a single narrow beam enters from the left and leaves the far face as a widening fan of spectral color that falls across the bench surface; the bench, the prism and the beam are bare line work on the deck's paper field, and the dispersed fan is the only saturated area | none | hero_page |
| `eye_cones.png` | 1032×444 | ~2.33:1 | Show that the eye samples the spectrum with three receptors rather than measuring it | Illustration | Transparent drawing sitting in the page's right region beside the chart, its inset aligned to the chart's category axis so the three receptors and the three chart columns read as the same three things | no-crop | slice | Generated | Derived from `teaching_sheet.png`; top cell | none | local |
| `press_and_screen.png` | 800×385 | ~2.08:1 | Anchor additive and subtractive mixing to the two physical systems the learner actually ships into | Illustration | Transparent drawing along the lower band of the page, the press half sitting under the subtractive diagram and the screen half under the additive one so each drawing labels the diagram above it | no-crop | slice | Generated | Derived from `teaching_sheet.png`; bottom cell | none | local |
| `great_wave_fit.jpg` | 1400×967 | ~1.45:1 | The real specimen the demonstration palette is sampled from | Photo | Shown complete on the left of the page as the specimen under examination, with the sampled swatches building down the right against it | no-crop | web | Sourced | Derived from `great_wave.jpg`; treatment=fit 1400x970 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: Written for a facilitator running this live for the first time. Each page's notes give the transition in from the previous page, the one thing to say that the slide deliberately does not print, the question the learner is most likely to ask at that moment with its answer, and — on the two exercise-adjacent pages — the exact timing call and what to do if the room is behind. Every number stated in the notes is one already sourced on the page; the notes introduce no fact that is not in the research pair. Where the deck simplifies, the notes say what the simplification is so a facilitator asked a harder question can answer honestly.
- **Total duration**: 90 minutes total session; approximately 55 minutes of presented material across the 14 pages, with 12 minutes of guided practice at P10 and the remainder in discussion and comparison
- **Notes style**: Conversational and patient, in the instructional register — define before using, analogy then principle, signpost every transition
- **Presentation purpose**: Teach first, then persuade — deliver the minimum model, get it applied live in two exercises, and keep published rules distinct from inherited conventions

<!-- ppt-master-schema: design-spec/v1 -->
# Four-Day Week Decision Memo - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | four_day_week_memo_a4_20260910 |
| Canvas Format | A4 Print (1240×1754) |
| Page Count | 10 |
| Primary Language | en-GB |
| Target Audience | The executive committee of a 200-person UK professional-services firm — managing partner, COO, finance director, HR director and two practice heads. They know the four-day week as a headline and a recruitment talking point, not as an evidence base; they care about client service, realisation and utilisation, cost, and senior retention, and they are sceptical of advocacy numbers. |
| Communication Intent | Put a go/no-go decision in front of the committee. First establish what the public evidence actually supports and where it is weak or absent; then set out the options and their trade-offs; then ask for a decision on a bounded pilot. Argue honestly rather than persuasively — the memo must survive hostile reading and being quoted back later. |
| Desired Audience Outcome | Each member can state, unprompted, which findings are robust and which are self-reported or statistically insignificant; can name the two or three conditions that would make this fail at this firm; and can approve, reject, or defer a defined pilot with named owners, metrics and kill criteria. |
| Core Message / Ask / Action | The wellbeing case is strong, replicated and controlled; the business case is unproven rather than disproven, on the pilots' own admission; and professional services is precisely where the model has been observed to fail. So the defensible move is a six-month, redesign-first pilot on 100-80-100 in two practice groups with pre-agreed kill criteria — not a firm-wide commitment and not a compressed week. |
| Delivery Context | Primary: a reader-led A4 memo, printed and circulated as a PDF 48 hours before the committee meeting, read alone with no presenter. Secondary: the working document in a 30-minute committee discussion, annotated in the margin. No live presentation, no projection. |
| Artifact Afterlife | The decision record for this question: filed in the board pack, cited in the minutes, audited later against what was known at the time, and reused as the terms of reference if a pilot is approved. |
| Reading Mode | text (read-close; the A4 print equivalent of a document-carried deck) |
| Content Strategy | Reshape the research supplement freely into an answer-first decision argument — regroup, reframe and sequence as the committee's decision requires. Every figure keeps its source, period and basis; no figure is invented, and the only unsourced values are the pilot's own design parameters and the risk ratings, each labelled illustrative. |
| Design Style | Printed decision record — swiss-minimal grid discipline in a portrait print memo: a fixed running header and footer, a two-column measure on evidence pages, hairline rules instead of cards, one burnt-vermilion accent reserved for the answer and the recommendation, and a slate second accent reserved for counter-evidence. |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — workflow default retained; on a reader-led memo the notes carry the "if asked in the room" reasoning and the provenance of each figure, which the afterlife (minutes, later audit) needs |
| Custom Animations | enabled — explicit run instruction requiring custom animations, light entrances on the main content units only |
| Narration Audio | disabled — workflow default; there is no presenter and no recorded delivery |
| Created Date | 2026-09-10 |

- **Template Application**: Adopt the Consulting Decision style as the communication method and the design direction only — it carries no prototypes, so every page is composed freely. Take its pyramid argument flow (governing question → overall answer → key supports → page message → evidence) and its assertion-title discipline as binding on the roster; take its page-role vocabulary as the roster's spine, using executive synthesis, situation/complication/resolution, driver decomposition, current-state diagnosis, comparison/benchmark (twice — once for persistence, once for comparability), recommendation, roadmap, risk/mitigation and appendix/evidence, and omitting process/operating model because no operating flow is being decided. Keep its claim discipline literally: facts, assumptions, implications and recommendations stay semantically distinct and visibly labelled. Keep its swiss-minimal visual preference and its restrained-accent colour behaviour; keep its chart rules (direct labels, no legends or chart furniture, retained units and source lines) and its table rules (columns derived from the decision logic, aligned units and periods, colour only where it carries declared meaning). Its "minimalist-swiss" image rendering is retained as the deck's rendering identity but no image is acquired — see §III. Identity is unowned by the template, so the palette and type system below are this project's.

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | A4 Print |
| Dimensions | 1240 × 1754 |
| viewBox | `0 0 1240 1754` |
| Margins | 80 px on all four sides (≈13.5 mm at 150 dpi-equivalent print scale; 1240 px = 210 mm, so 1 mm ≈ 5.905 px) |
| Content Area | x 80–1160 (1080 wide), y 80–1674 (1594 tall); running header occupies y 80–140 and the footer rule sits at y 1620 with footer text below it, leaving a body field of y 180–1600 |

## III. Visual Theme

### Theme Style

- **Mode**: pyramid
- **Visual style**: swiss-minimal
- **Theme**: A printed decision record. The page is a document, not a slide: a fixed masthead carrying the memo title, date and page number; a strict single grid whose columns change measure but never position; hairline rules doing the work that cards and shadows would do on screen; and evidence given more ink than framing. One burnt-vermilion accent has exactly one job — it marks the answer, the recommendation, and the single decision-relevant delta on a chart — and appears nowhere else. A slate second accent has exactly one job — it marks counter-evidence, control groups and caveats — so that the reader can see the shape of the argument's honesty before reading a word.
- **Tone**: Sober, exact, unsold. Assertion titles state a judgement; annotations state a basis. Nothing is claimed more strongly than its source supports, and where the source says "not statistically significant" the page says so at the same size as the number.

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | The page. Paper, unfilled, on every page |
| Secondary background | #F2F0EB | Evidence and appendix bands, table header fills, the one tint that separates a reasoning layer |
| Primary | #16232E | Ink: assertion titles, structural rules, dominant chart marks, established findings |
| Accent | #B4471C | One job only — the answer, the recommendation, and the single decision-relevant delta on a chart |
| Secondary accent | #4A6B7C | One job only — counter-evidence, control groups, caveats, and the critical reading of a study |
| Body text | #16232E | Running body text and table cells |
| Secondary text | #5C6871 | Captions, source lines, periods, bases, fact ids |
| Divider | #D6D2C9 | Hairline rules, table borders, the evidence-margin line |
| Surface | #F7F6F3 | Panel lift where a block must sit off the paper without a card |
| Grid | #E7E3DB | Chart gridlines and internal table rules, deliberately lighter than dividers |
| Muted | #6E777E | "No measurable effect" / "not statistically significant" marks and their labels |

Evidence strength is encoded as three tints of one system rather than a rainbow: established findings in Primary, self-reported or critical readings in Secondary accent, non-significant results in Muted. Body contrast on the page field is 15.3:1; Accent 5.4:1, Secondary accent 5.8:1, Secondary text 5.9:1 and Muted 4.6:1 all clear WCAG AA at body size.

### Cross-page motif

A single vertical hairline at x=430 divides an evidence margin (labels, periods, sources, fact ids) from the argument column on every body page. On synthesis and recommendation pages the argument column crosses it; on evidence pages it does not. Its continuity job is to make the claim-to-source path visible at a glance on every page, and it is the only decoration in the deck. Executor may adjust its position or decline it per page.

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | Neutral grotesque, bold, tightly tracked — decisive without shouting | Arial | — | Arial |
| Body | Neutral grotesque, regular — economical at print measure, silent under the evidence | Arial | — | Arial |
| Display | Heavy grotesque — used only for the answer line and hero numerals so the cover has a distinct voice without a second text family | Arial Black | — | Arial Black |

- **Title stack**: Arial
- **Body stack**: Arial
- **Display stack**: Arial Black
- **Role rationale**: Title and Body deliberately concord on one grotesque — swiss-minimal and consulting-decision both derive hierarchy from weight, scale, alignment and rule-work, and a second text family would add a voice the evidence layer does not need. Display (Arial Black) is the one deliberate exception, carrying the P01 answer line and the hero numerals only. Both faces have exact per-glyph advance data in this repository's width estimator, which matters on a dense A4 page where a wrapped assertion title changes the whole page's vertical rhythm. Data, Annotation and Footnote are size roles within the Body family and add no family override.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 26 |
| Display | 84 |
| Title | 44 |
| Subtitle | 34 |
| Lead | 30 |
| Data | 22 |
| Annotation | 20 |
| Footnote | 16 |

Body is deliberately set well below the `a4` advisory band (44–58 px). That band derives from a poster-distance formula in `canvas-formats.md`; this artifact is a hand-held print memo, where 26 px on a 1240 px-wide A4 page is 4.4 mm ≈ 12.5 pt — the correct body size for print. A 51 px body would fit roughly 45 characters per full-width line and turn a nine-page argument into thirty pages.

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: Top-down and answer-first. The assertion title is read first and is always a complete judgement; the lead sentence beneath it states the basis of that judgement; the evidence block sits below or beside it and is visually subordinate but never small; the source line closes the page. Attention never has to travel back up.
- **Composition tendency**: One to three primary regions per page, stacked in the portrait direction rather than columned. Evidence pages use a narrow evidence margin (labels, period, basis, fact ids) beside a wide argument column; synthesis and recommendation pages let the argument span the full measure and breathe. At least one page sets running body text in two equal columns to test the print measure. No cards, no filled callout boxes, no elevation.
- **Cross-page continuity**: The masthead (memo title, date, page number, "Illustrative client" marker) and the footer rule recur unchanged on every page. The evidence hairline recurs on body pages. The accent's job and the slate's job never change. Section numbering runs 1–9 in the header on body pages.
- **Spacing posture**: Variable by page rhythm — `anchor` pages open, `dense` evidence pages tight but never below the body leading.
- **Spacing anchors**: page margin 80 px · block gap 40 px · column gutter 40 px · corner radius 0 px · body leading 38 px

## VI. Icon Usage Specification

- **Primary bundled library**: chunk-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| chunk-filled/checkmark | An outcome the evidence establishes |
| chunk-filled/x | An outcome the evidence refutes, or a firm that stopped |
| chunk-filled/minus | No measurable or significant effect |
| chunk-filled/triangle-exclamation | A caveat or a live risk |
| chunk-filled/circle-question | An open question or an unmeasured quantity |
| chunk-filled/arrow-trend-up | A measured increase |
| chunk-filled/arrow-trend-down | A measured decrease |
| chunk-filled/clock | Hours, period, duration |
| chunk-filled/users | Workforce, headcount, participants |
| chunk-filled/building | An organisation or participating company |
| chunk-filled/file | A report or primary source |
| chunk-filled/link | A live source reference |
| chunk-filled/flag | A decision gate |
| chunk-filled/target | A metric or kill criterion |
| chunk-filled/calendar | A phase or milestone |
| chunk-filled/coin | Cost, revenue, saving |

`chunk-filled` is chosen over the stroke library on print grounds: the icon README records that `tabler-outline`'s thin strokes weaken when printed, and this artifact's primary delivery is paper. Icons are used only where they encode a state, never as decoration or as a grid.

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P02 | chart | horizontal_bar_chart | Expose the gap between the week before and the hours actually worked after, study by study |
| P04 | chart | horizontal_bar_chart | Rank the UK 2022 pilot's measured changes and separate the significant from the not-significant |
| P05 | chart | column_chart | Compare how much of each cohort was still on reduced hours, on a stated basis and period |
| P06 | table | comparison_matrix | Set every study against the same comparability criteria for this firm |
| P09 | table | record_table | Hold the risk register: one row per risk with likelihood, impact, mitigation and owner |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

No image resource is planned. The deck's subjects are studies, magnitudes and a decision; none is an externally verifiable place, product, person or artefact the committee must recognise, so no image carries a factual or evidentiary job. The installed style's image direction ("use images only when they provide evidence, necessary context, or a causal explanation that shapes the decision … avoid atmospheric imagery that weakens the argument") makes a stock office photograph an active liability on a page whose credibility is the whole point. The `minimalist-swiss` rendering identity is retained as the deck's rendering candidate so that any later image request inherits it; it is not exercised here.

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: One note per page, written for a reader who must defend the page in the room rather than present it. Each note states the page's governing question, the provenance and period of every figure on the page, the single most likely challenge to it and the honest answer, and what the page deliberately does not claim. Notes never introduce a figure that is not on the page and never soften a caveat the page states. Facts are grounded in the imported research pair and cited by fact id.
- **Total duration**: not time-bound — this is a reader-led print memo with no presented duration; notes are sized to one screen per page (roughly 120–180 words)
- **Notes style**: formal, defensive, evidence-first
- **Presentation purpose**: Put a go/no-go decision in front of the committee — establish what the evidence supports and where it is weak, set out the options and trade-offs, and ask for a decision on a bounded pilot.

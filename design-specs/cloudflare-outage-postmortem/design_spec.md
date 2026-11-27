<!-- ppt-master-schema: design-spec/v1 -->
# Cloudflare Outage Postmortem - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | cloudflare_outage_postmortem |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 15 |
| Primary Language | en |
| Target Audience | Site-reliability and platform engineers, incident commanders, and the engineering leaders they report to, at organizations whose availability depends on Cloudflare; secondary readers are reliability reviewers who will reuse this account as a worked example of a blameless postmortem. They know what a reverse proxy and a config rollout are; they have not read the 22,000-character source post. |
| Communication Intent | Record and hand off first: establish an accurate, source-anchored account of the 18 November 2025 Cloudflare outage that can be cited without reopening the blog. Then explain the mechanism by which a database permissions change became a global HTTP 5xx event. Then align readers on which conditions persist, which corrective actions Cloudflare committed to, and which questions the published account leaves open. Never argue about fault. |
| Desired Audience Outcome | A reader who was not there can restate the trigger, the mechanism, the impact window, and the detection-versus-diagnosis gap from memory; can tell an observed fact from an inference and from an unconfirmed item; and can name both the corrective actions and what the published account does not settle. |
| Core Message / Ask / Action | A routine database permissions change at 11:05 UTC doubled a Bot Management feature file; a fixed 200-feature preallocation limit turned that oversized file into an unhandled panic in the core proxy; the failure was detected in three minutes but took nearly three hours to diagnose because a five-minute regeneration cycle made it look like an attack. The condition that made it global — internally generated configuration propagated worldwide without staged rollout or consumer-side validation — is the same condition behind the 2 July 2019 outage. |
| Delivery Context | Primary: reader-led. A written postmortem circulated asynchronously and read end to end by people who were not in the incident channel. Secondary: presented in a 30-minute incident-review meeting where the timeline and corrective-action pages are projected. |
| Artifact Afterlife | Review, audit, and archive. Individual pages — the summary, the timeline, the corrective actions — will be quoted and forwarded on their own, so each must stand alone. Reused as a structural reference for internal postmortems. |
| Reading Mode | text |
| Content Strategy | Stay close. Every number, timestamp, product name, identifier, and quoted string comes from the published Cloudflare accounts of 18 November 2025 and 2 July 2019. Nothing is estimated, rounded for effect, or supplied from outside those two documents; where the source does not state a value, the page says NO DATA or marks the item unconfirmed. Elapsed durations are arithmetic on published timestamps and are labeled as derived. |
| Design Style | Incident Postmortem method (installed Style workspace) realized as a neutral achromatic record: white field, hairline rules, a fixed left-to-right time direction, and colour reserved entirely for the four declared severity states, each always paired with a text label. |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — workflow default (no explicit user instruction; proactive Stage-2 value `true`) |
| Custom Animations | enabled — explicit user instruction: the deck must carry a hand-authored `animations.json` with at least two Morph pairs |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-05 |

- **Template Application**: The installed `incident-postmortem` Style supplies the communication method and the design defaults, and nothing else — it owns no structure, so every page is composed freely and flat. Adopted deliberately: its argument flow (facts, then interpretation, then action), its claim discipline (observed event / inferred sequence / contributing factor / hypothesis kept distinct, unconfirmed items marked, systems and roles named instead of people), its page-role vocabulary as the roster's skeleton, its evidence rules (one timestamp precision and one stated time zone throughout, native editable tables for timeline and actions, no redrawn monitoring graph presented as the record), its restraint defaults (effectively no decoration, colour only for declared severity, always with a label), and its Fallback Colour Scheme and typographic character (plain neutral sans plus a genuinely monospaced companion) — taken as identity because no Brand or Deck workspace is active. Two Style tendencies are deliberately not followed: its `digital-dashboard` image rendering and its evidence-image guidance are inert because this deck carries no images at all (the only legitimate evidence images are Cloudflare's copyrighted screenshots), and its instruction to keep monitoring graphs as captured evidence rather than redrawing them is honoured by labelling the one time-series page a schematic reconstruction rather than a record. Its Review Focus section is not activated.

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

- **Mode**: briefing
- **Visual style**: swiss-minimal
- **Theme**: A record, not a report about a record. A white field with a strict two-band grid, hairline rules instead of boxes, and a time direction that never changes: earlier is always left, later is always right, on the chart, on the timeline tables, and on the severity strip that runs across the deck. The only chromatic events on any page are the four declared severity states.
- **Tone**: Factual, unhurried, and unembarrassed. The account describes what responders could see at each moment; it never uses hindsight vocabulary and never attributes an outcome to a person.

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | Neutral ground for a factual record; every page |
| Secondary background | #F2F4F6 | Grouped regions, table banding, evidence and code blocks |
| Primary | #1F2933 | Primary text, page titles, rules, table ink |
| Accent | #B4342C | Severity `Critical` — the full impact window and the breached limit; always with its label |
| Secondary accent | #B7791F | Severity `Degraded` — partial impact, detection gap, elevated risk; graphic use only, never body text (3.7:1 on the field) |
| Body text | #1F2933 | Running body copy |
| Secondary text | #5A6673 | Captions, annotations, source lines, footnotes |
| Divider | #D7DDE3 | Hairline rules, table borders, band separators |

Two further neutral roles carry stable meaning across the deck and are locked with the palette: `surface` #F2F4F6 (panel lift, table banding) and `grid` #E8ECEF (chart hairlines, one step lighter than dividers). Two further severity roles complete the declared four-state scale: `normal` #4A5568 (pre-incident baseline and unaffected state) and `recovered` #2E7D5B (mitigation effective, service restored). Each state also carries one recurring tint used as the severity cell field in every table and nowhere else — `normal` #EDEFF2, `degraded` #FAF0DC, `critical` #F7E4E2, `recovered` #E4F0EA — so the state reads at a glance while its label stays in body ink at full contrast. The severity mapping is fixed for the whole document and every use is paired with its text label, so it survives greyscale printing.

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | Neutral grotesque; hierarchy from weight and alignment, never from containers | Arial | — | sans-serif |
| Body | Same neutral grotesque at reading weight | Arial | — | sans-serif |
| Data | Genuinely monospaced companion for timestamps, identifiers, and table time columns | Consolas | — | monospace |
| Code | Same monospace at excerpt size for the SQL fragment and the panic string | Consolas | — | monospace |
| Display | Monospaced at hero scale so a hero window or duration keeps the same figure forms as every other timestamp | Consolas | — | monospace |

- **Title stack**: Arial
- **Body stack**: Arial
- **Data stack**: Consolas
- **Code stack**: Consolas
- **Display stack**: Consolas
- **Role rationale**: The Style requires a plain neutral sans with a genuinely monospaced companion, so Title and Body concord on one family and the contrast is carried by the mono roles. `Data` recurs on six pages (every timestamp, every identifier, the time column of three tables); `Code` recurs on two (the SQL fragment and the panic line) and needs a smaller anchor than `Data` so an unwrapped log line stays on one line; `Display` recurs on three (cover, summary, detection) for the published windows and derived durations, and stays monospaced so a hero figure and a table timestamp share one digit form.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 20 |
| Title | 36 |
| Subtitle | 28 |
| Annotation | 16 |
| Lead | 26 |
| Data | 18 |
| Code | 16 |
| Display | 56 |
| Cover title | 64 |
| Footnote | 12 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: Title states what the page establishes; a single lead line carries the governing assertion; evidence sits below it in one band. The eye moves top-left to bottom-right once, with no competing focus.
- **Composition tendency**: One fact per page under a strict grid. A fixed 12-column field with a persistent left rule; timeline and chart pages give the full width to chronology; summary, systemic-condition, what-went-well, and action pages get real vertical air.
- **Cross-page continuity**: A severity strip — a thin horizontal band spanning 11:05 to 17:06 UTC, segmented into the four declared states — recurs on the pages that place a moment in the window, always at the same y and always with the same left-to-right direction, with the page's own moment marked. A hairline rule under every page title. A source line in `Annotation` at the foot of every evidence page. Pages that carry no chronology omit the strip rather than decorate with it.
- **Spacing posture**: Variable by page rhythm — anchor pages breathe, the four table pages carry real density without truncating any identifier.
- **Spacing anchors**: page margin 64 px, block gap 28 px, column gutter 32 px, corner radius 0 px, body leading 30 px.

## VI. Icon Usage Specification

- **Primary bundled library**: chunk-filled
- **Brand-logo library**: simple-icons

| Icon Path | Suitable Scenarios |
| --- | --- |
| chunk-filled/circle-minus | Severity `Normal` — baseline or unaffected state, always beside the word Normal |
| chunk-filled/triangle-exclamation | Severity `Degraded` — partial impact or detection gap, always beside the word Degraded |
| chunk-filled/circle-x | Severity `Critical` — full impact window or breached limit, always beside the word Critical |
| chunk-filled/circle-checkmark | Severity `Recovered` — mitigation effective, always beside the word Recovered |
| chunk-filled/clock | Event class: an elapsed-time fact stated as a derived duration |
| simple-icons/cloudflare | The subject organization appearing as itself on the cover and the sources page |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | table | record_table | One row per impacted product surface with the impact description published for it |
| P05 | chart | line_chart | Relative 5xx volume against the published event clock, as a schematic reconstruction |
| P06 | table | record_table | Timeline entries 11:05–13:05 UTC with status and description |
| P07 | table | record_table | Timeline entries 13:37–17:06 UTC with status and description |
| P13 | table | record_table | Published corrective actions with the factor each addresses and its unpublished owner/date/verification |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

No image resource is planned. The Style admits images only as evidence, and the only evidence images that exist for this incident are Cloudflare's copyrighted screenshots and monitoring captures, which this deck may not redistribute. Conceptual or atmospheric imagery is forbidden by the Style in a factual record. The one time-series page is therefore a native chart labelled as a schematic reconstruction, not a captured record.

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: One note per slide, grounded in that slide's final SVG and in the two published Cloudflare accounts. Notes carry the interpretation and the transitions that the page deliberately does not: why a figure is stated the way it is, which claim class each item belongs to, and what a reader should not conclude. Notes never introduce a number, timestamp, or product name that is not on the page or in the sources, and never soften an unconfirmed item into a settled one.
- **Total duration**: approximately 22–26 minutes at a measured reading pace across 15 slides
- **Notes style**: formal
- **Presentation purpose**: Record and hand off an accurate account of the 18 November 2025 Cloudflare outage, explain its mechanism, and align readers on the persisting condition, the committed actions, and the open questions.

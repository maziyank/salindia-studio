<!-- ppt-master-schema: design-spec/v1 -->
# Heatline Seed Pitch - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | Heatline Seed Pitch |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 15 |
| Primary Language | en-GB |
| Target Audience | Seed-stage investors at climate-tech and vertical-software funds — partners and associates who follow energy-transition headlines but have never seen inside an installer business |
| Communication Intent | Persuade first, then obtain a decision: establish that installer capacity, not consumer demand, is the binding constraint on residential heat-pump deployment; show that Heatline sells the planning layer that lifts it; and secure a seed round on the stated terms. Leave a diligence trail that survives the meeting. |
| Desired Audience Outcome | Investors can restate the capacity bottleneck in their own words, can tell achieved from contracted from projected in every Heatline number, and can take a first-meeting decision on the ask |
| Core Message / Ask / Action | Electrifying home heating is now limited by installer capacity, not demand. Heatline sells the capacity-planning layer that lets an installer business grow crews and throughput, and is raising a £4.2M seed round to reach that market while European policy guarantees the demand floor. |
| Delivery Context | Primary: presenter-led 15-minute seed pitch to an investment committee. Secondary: reader-led circulation inside the fund afterwards, so every page must carry its own claim without a presenter. |
| Artifact Afterlife | Diligence hand-off and internal circulation; the appendix, metric definitions and source links must survive forwarding |
| Content Strategy | Free re-architecture of the researched material into a pitch narrative. Every externally verifiable number stays sourced to `sources/heatline_pitch_research.facts.json`; every company, product, customer, traction, pipeline and financial figure is fictional and carries a visible illustrative marker on the page, not only in the notes. |
| Design Style | Field Notes — warm, high-contrast editorial page architecture with a schematic annotation layer; one ember accent reserved for evidence |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy |
| Custom Animations | enabled — final Stage-2 proactive policy (continuity-aware solution: the capacity curve and the ask are planned as visible states across adjacent pages) |
| Narration Audio | disabled — final Stage-2 proactive policy |
| Created Date | 2026-09-10 |

- **Template Application**: Adopt the investor-pitch Style as communication method and expression discipline only. Its thirteen page roles set the deck's spine in the order given, one role per page, with use of funds split onto its own page beside the ask so the ask page stays unmistakable. Its claim discipline binds: page titles are written as claims, each metric carries its definition where it first appears, achieved / contracted / pipeline / projected stay distinguishable by texture as well as colour, market size is derived bottom-up in view, and competition is compared on axes that decide purchases without naming a vendor as inferior. Its evidence obligations bind: source and date sit on the page that carries a third-party figure, and traction, unit-economics, market and financial-plan objects are authored as editable native charts and tables. Its visual defaults are candidates, not identity: the preferred dark-tech field and corporate-photo rendering are replaced by the warm editorial system recorded in §III, for the reason recorded there, while its density rule (sparse in the arc, dense only in the appendix), its restrained-decoration rule and its rare-accent rule are adopted unchanged. No prototypes, canvas or structure come from this Style; pages stay flat free design.

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
- **Mode References**: narrative, pyramid
- **Mode Behavior**: Run the investor-pitch arc as a story with one turn — the world changed, the change created a bottleneck nobody is staffed for, here is the tool that lifts it, here is the evidence it works, here is what the money buys. Inside that arc every page states its conclusion in the title as a claim and puts its evidence directly beneath, so a forwarded page argues on its own. The turn sits at the problem→solution pair and is carried by one continuing object rather than a new frame. Appendix pages drop the arc and become retrieval surfaces.
- **Visual style**: custom
- **Visual Style References**: editorial, blueprint
- **Visual Style Behavior**: A warm paper field organised by an editorial column grid and heavy horizontal hairline rules: a rule under the claim line at a fixed height on every page, a second rule closing the evidence block, and no card unless a real container is needed. Type does the work — a large statement scale for claims and hero numbers, a quiet monospace for measurements, definitions and attribution. The blueprint contribution is an annotation layer, not a field: leader lines, tick marks, dimension ticks and monospace callouts label the product mockup, the capacity curve and the market derivation, so the deck reads as engineering field notes rather than marketing. Decoration is otherwise near zero — no gradient meshes, glow, floating devices or ornamental infographics; the ember accent appears at most twice per page and only on evidence.
- **Theme**: Engineering field notes on warm paper — a hardware business argued with measurements
- **Tone**: Confident, plain-spoken, unhurried; specific where it matters and explicitly uncertain where it is

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FBF7F1 | Warm paper field; the deck's dominant surface |
| Secondary background | #EFE7DA | Recessed evidence blocks, appendix bands, table header rows |
| Primary | #16233A | Claim lines, hero numerals, rules, chart structure |
| Accent | #D65A1E | Reserved for evidence — the decisive figure, the actual series, the ask |
| Secondary accent | #2E6F5E | Achieved / verified state where it must differ from projected |
| Body text | #1F2733 | Body copy and table cells |
| Secondary text | #6B6154 | Captions, definitions, source lines, illustrative markers |
| Divider | #C9BCA8 | Hairline rules, grid lines, table borders |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: corporate-photo, editorial
- **Image Rendering Behavior**: Real editorial photography of ordinary working situations, shot in warm low-angle daylight with a shallow but honest depth of field; no studio gloss, no anonymous stock professionals, no abstract technology. The editorial contribution is framing and restraint — a single clear subject with usable quiet space on one side for type, natural colour that sits inside the deck's warm paper and deep-ink range, visible material texture in metal, brick and workwear, and no synthetic text, screens or interface anywhere in the frame.
- **Visual**: Working installers and real domestic hardware, photographed close and plainly, with one quiet region reserved for the page's claim line
- **Mood**: Early-morning trade work — the register of a good newspaper business-section photograph rather than a manufacturer brochure

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | Display grotesque / maximum weight, built for claim lines and hero numerals | Arial Black | — | sans-serif |
| Body | Humanist sans / warm, high x-height, legible on a laptop | Calibri | — | sans-serif |
| Data | Monospace / tabular figures for aligned metrics, measurements and definitions | Consolas | — | monospace |
| Display | Display grotesque / hero numerals at statement scale, sharing the Title character | Arial Black | — | sans-serif |

- **Title stack**: `Arial Black, sans-serif`
- **Body stack**: `Calibri, sans-serif`
- **Data stack**: `Consolas, monospace`
- **Display stack**: `Arial Black, sans-serif`
- **Role rationale**: `Display` shares the Title family rather than inheriting the body family, because every hero number on the why-now, ask and metric pages must carry the same grotesque weight as the claim lines. `Data` is a genuine third family — every metric table, chart annotation, unit-economics figure, definition line and illustrative marker in this deck aligns in columns and needs tabular figures, which neither Arial Black nor Calibri supplies; it also carries the blueprint annotation layer named in §III.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 42 |
| Subtitle | 32 |
| Annotation | 18 |
| Display | 108 |
| Lead | 30 |
| Data | 20 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: Claim line first at a fixed height, then the single dominant evidence object, then the quiet layer — definition, source, illustrative marker — along the bottom rule
- **Composition tendency**: One claim and one dominant element per page on a warm field; evidence blocks recessed rather than boxed; the annotation layer labels the object instead of a legend floating beside it
- **Cross-page continuity**: The claim line's fixed height and the rule beneath it recur on every page; the capacity curve is one continuing object across the problem and solution pages; the ask figure's segments become the use-of-funds bars on the following page; the ember accent recurs only where evidence sits
- **Spacing posture**: Open through the narrative arc, deliberately dense only on the competition matrix and the diligence appendix
- **Spacing anchors**: page margin 64 px, block gap 32 px, column gutter 32 px, corner radius 4 px, body leading 34 px

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-outline/tools | Installer work, field crew, service capability |
| tabler-outline/home | Residential property, the installed base |
| tabler-outline/calendar | Scheduling horizon, booking window |
| tabler-outline/users | Crew size, headcount, team |
| tabler-outline/trending-up | Growth, rising demand, expansion |
| tabler-outline/building-factory | Manufacturer channel, industry partners |
| tabler-outline/certificate | Accreditation, training, qualification |
| tabler-outline/clock | Lead time, payback period, delay |
| tabler-outline/route | Go-to-market motion, sequence of channels |
| tabler-outline/target | Milestone, target penetration, objective |
| tabler-outline/alert-triangle | Risk, exposure, constraint |
| tabler-outline/coin | Price, revenue, cost, funding |
| tabler-outline/chart-line | Metric, measured series, reporting |
| tabler-outline/file-text | Contract, document, compliance record |
| tabler-outline/flame | Heating, fossil boiler, the thing being replaced |
| tabler-outline/bolt | Electrification, the heat pump itself |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P02 | chart | column_chart | Compare EU annual heat-pump installations across 2022–2025 to show the fall and the return |
| P06 | chart | line_chart | Show the full available history of live engineer seats month by month |
| P07 | chart | waterfall_chart | Trace gross contract value down to gross contribution per customer per year |
| P08 | table | record_table | Hold each derivation stage with its seats, its arithmetic and whether it is real or illustrative |
| P09 | table | comparison_matrix | Compare the three real alternatives against the criteria that decide a purchase |
| P10 | chart | column_chart | Compare customers acquired by each go-to-market channel, including the untested one |
| P12 | chart | stacked_bar_chart | Show revenue composition by named driver across the plan, actual and projected |
| P14 | table | record_table | Itemise the use of funds with amount, share, what it buys and the milestone it reaches |
| P15 | table | metric_table | Hold each metric's definition, measurement period and system of record for diligence |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_installation_dawn.jpg | 1920×1072 | 16:9 | Cover hero: ground the deck in the physical work before any claim | Photo | Full-bleed field carrying the cover; the subject sits right of centre so the left third stays quiet under a real scrim for the title lockup | adaptive | ai | Generated | An installer in workwear kneeling beside a newly fitted outdoor air-source heat-pump unit on a gravel pad against a brick house wall, early-morning light raking across the fins, breath visible in cold air; quiet sky and wall on the left third; no text, no screens, no logos | none | hero_page |
| problem_capacity_yard.jpg | 1024×1024 | 1:1 | Problem page: make the capacity shortage a specific situation rather than a category | Photo | Editorial crop occupying the page's right column beside the capacity curve; subject faces back into the page | adaptive | ai | Generated | Two installers loading a van at a depot before dawn, a third checking a clipboard, a rack of unfitted heat-pump units waiting behind them; the emphasis is on the small crew against the size of the stock, warm sodium and daylight mixed; no text, no screens, no logos | none | local |
| solution_survey_handover.jpg | 1200×896 | 4:3 | Solution page: show the human moment the software coordinates | Photo | Supporting image below the claim line, cropped tight so the two hands and the document dominate; sits opposite the continuing curve | adaptive | ai | Generated | Close crop of an installer and a homeowner at a kitchen doorway handing over a survey sheet, radiator and pipework visible behind, warm interior daylight; hands and paper dominate the frame, faces partly out of frame; no readable text, no screens, no logos | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: Ground every note in what is visible on its own final SVG. Carry the presenter's transition into the page, the one sentence that makes the claim land, and the detail deliberately kept off the slide — the derivation behind a figure, the honest reading of a survey, the assumption most likely to be attacked. Every note that mentions a Heatline figure states that it is illustrative; every note that mentions an external figure names its source. Notes never introduce a number that is absent from the page and its facts file.
- **Total duration**: about 15 minutes for the fifteen pages, weighted toward the problem, traction and ask pages
- **Notes style**: conversational but precise — spoken sentences a founder would actually say, with the defensible version of each number ready
- **Presentation purpose**: Persuade that installer capacity is the binding constraint, then obtain a first-meeting decision on a £4.2M seed round, leaving a diligence trail that survives forwarding

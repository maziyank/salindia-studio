<!-- ppt-master-schema: design-spec/v1 -->
# ResearchStudio-Reel paper reading - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | ResearchStudio-Reel: Automate the Last Mile of Research from Paper to Poster, Video, and Blog — paper reading deck |
| Canvas Format | PPT 16:9 (1280 × 720) |
| Page Count | 18 |
| Primary Language | en-US |
| Target Audience | Researchers and research engineers at a lab meeting or reading group who know what an agent skill, a VLM judge, and a poster benchmark are, and want to judge whether the paper's claims are earned |
| Communication Intent | Walk the paper in its own constructive order — the open problem, prior work, the five-skill system, each skill's design requirements and gates, the benchmark result, its analysis, cost, limitations — so a skeptical audience can trace every conclusion back to a figure, a table, or a stated method |
| Desired Audience Outcome | The audience can state the three gaps the system targets (shared grounding, native editability, experience-level convergence), explain the staged-fill loop and why it converges, read Table 1 correctly (best aesthetics among automated systems, but lower PaperQuiz than denser systems), and name the two honest gaps the authors leave open |
| Core Message / Ask / Action | Treating the last mile as a native-editable, section-aligned workspace — one shared extractor, three editable generators, one convergence layer, each with a testable release gate — produces posters that VLM judges rate above the authors' own on aesthetics (3.56 vs 3.03) while keeping every artifact editable and cross-linked; the evaluation is proxy-bound and the pipeline cannot invent bespoke diagrams, and the deck says so |
| Delivery Context | A 25-minute presented walkthrough at a lab meeting or paper-reading group, then circulated as slides for people who missed it |
| Artifact Afterlife | Kept as the group's reference summary of the paper; figures and numbers must be quotable back to the source |
| Reading Mode | balanced |
| Content Strategy | Faithful to the single source (the arXiv v2 PDF converted to Markdown); every number, table cell, and claim is quoted from the paper; the paper's own figures are imported as evidence at original fidelity, never redrawn; observation, inference, and speculation keep the paper's wording; nothing outside the paper is added except the arXiv and project links the paper itself prints |
| Design Style | Research-talk restraint on a Swiss grid: white field, hairline rules, one claim line per page in a fixed position, figures dominant, color used only to encode condition (our Claude Code configuration, our Codex configuration, baselines, author ground truth) with the mapping fixed across every chart and table |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — workflow default (proactive policy true); notes carry the spoken explanation, the source location of every number, and transitions |
| Custom Animations | enabled — explicit user instruction (every example ships custom animations); object-level entrances plus Morph carry-overs on the recurring claim line and the pipeline figure |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-05 |

- **Template Application**: the installed academic-research Style (`templates/design_spec.style.academic-research.md`) supplies the method only: constructive order question → prior work → approach → result → interpretation with a pyramid's trace inside it; one claim per page stated where it can be checked against the figure; observation / inference / speculation kept distinct; limitations on a real page; figures imported rather than redrawn; color as a declared condition variable. Its swiss-minimal seed is adopted as the preset visual style. No prototypes, no structure; pages are free-design flat SVG.

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | top 48 / bottom 40 / left 56 / right 56 |
| Content Area | x 56–1224, y 48–680; title band y 48–120 (title + claim line), content field y 140–620, footer (source line + page number) y 656–690 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional, pyramid
- **Mode Behavior**: the deck follows the paper's constructive order — question, prior work, contribution, each skill as one teaching unit (requirements → solution → gate), then results, analysis, cost, applications, limitations, conclusion — because a research audience cannot evaluate a conclusion before its method. Inside that order every page keeps a pyramid's discipline: the title states what the page establishes (an assertion, not a section label), and the claim line under it names the exact evidence on the page that supports it. Sibling skills get parallel pages of the same shape so the audience can map them; signposts ("skill 2 of 5") orient the listener.
- **Visual style**: swiss-minimal
- **Theme**: a research talk that reads like a well-set paper: a fixed title band with the assertion in bold and one claim line beneath it, a hairline under both, the paper's own figure or a native table or chart dominating the field, the reading of that evidence in a narrow column beside it, and a footer citing the section, figure, or table of the paper the page draws from. The recurring motif is the hairline-ruled evidence frame with a small "Fig. N / Table N" caption tag; the five skills reuse one page shape so their differences read as content, not layout.
- **Tone**: precise, sober, checkable; the paper's own numbers and hedges, no added enthusiasm

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | Page field |
| Secondary background | #F3F5F8 | Table header band, requirement cards, appendix-like density blocks |
| Primary | #1B2430 | Titles, axes, author ground-truth condition, key numbers |
| Accent | #1D4ED8 | The ResearchStudio-Reel (Claude Code) condition everywhere: table row, chart series, badge, claim emphasis |
| Secondary accent | #0E9F8A | The ResearchStudio-Reel (Codex) condition everywhere |
| Body text | #2F3A48 | Body copy, table body |
| Secondary text | #6B7684 | Captions, unit lines, axis labels, footer, single-shot baseline condition |
| Divider | #C9D0D8 | Title-band hairline, table header rule, axes |
| Grid | #E6EAEF | Table row rules, chart gridlines, poster-pipeline baseline condition |
| Surface | #F3F5F8 | Evidence frame fill behind imported figures when the figure is on a white ground |
| Positive | #2E8B57 | The FULL verdict band, wins, checks |
| Warning | #E0A100 | SPARSE / SPILLAGE verdict bands, caution |
| Negative | #C0392B | EMPTY / OVERFLOW verdict bands, limitations, non-convergence |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | plain grotesque, bold, decisive assertion | Arial | Arial | sans-serif |
| Body | plain grotesque, regular, lecture-legible | Arial | Arial | sans-serif |
| Data | lining figures for tables and chart labels | Arial | Arial | sans-serif |

- **Title stack**: Arial
- **Body stack**: Arial
- **Data stack**: Arial
- **Role rationale**: one family keeps the research-talk plainness the Style asks for; `data` is the same face at a smaller size so table digits and chart labels align, and bold weight alone marks the best value per column.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 16 |
| Title | 28 |
| Subtitle | 18 |
| Lead | 20 |
| Annotation | 12 |
| Footnote | 10 |
| Display | 44 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: title assertion first, then the claim line naming the evidence, then the evidence itself (figure, table, chart), then the reading column beside it, then the footer citation
- **Composition tendency**: fixed title band; the field splits asymmetrically — evidence dominant (about two thirds) with a narrow reading column — on figure and table pages; requirement/solution pages use a two-column requirement → solution table with the pipeline figure as a band above; the five skill pages share one shape
- **Cross-page continuity**: the title band, hairline, claim line position, "Fig. N / Table N" caption tag, section signpost (top right), footer citation and page number are fixed on every content page; the condition colors never change; Morph carries the pipeline figure from P04 into P05 and the claim line across the five skill pages
- **Spacing posture**: question, contribution, conclusion pages breathing; skill, result, analysis, cost, limitation pages dense; cover and sources anchor
- **Spacing anchors**: page margin 56; block gap 24; column gutter 32; corner radius 0; body leading 22

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | table | comparison_matrix | Prior work by output type: representative systems, what they emit, what they leave open |
| P06 | table | record_table | Paper2Poster requirements A1–A5 against the solution the paper gives each |
| P07 | chart | stacked_bar_chart | The five fullRatio verdict bands as one stacked bar on the 0.60–1.20 axis |
| P08 | table | record_table | Paper2Video requirements B1–B5 against their solutions |
| P09 | table | record_table | Paper2Blog requirements C1–C5 against their solutions |
| P11 | table | comparison_matrix | Table 1: nine systems × six sub-criteria, two overalls, two PaperQuiz splits |
| P12 | chart | scatter_chart | Aesthetic overall vs PaperQuiz detail accuracy for the nine systems |
| P14 | chart | horizontal_bar_chart | Wall-clock minutes per skill subtotal from Table 4 |
| P16 | table | record_table | Five recurring failure modes L1–L5 with their mitigations |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| poster_beit.jpg | 1920x1152 | 5:3 | Cover evidence strip, left cell: a generated poster (Figure 1a) | Screenshot | `Three equal cells in one band under the title (#P3-02), each labeled with the artifact name` | no-crop | user | Existing | Figure 1a, the Paper2Poster output for the BEiT paper | none | local |
| video_frame_citransnet.jpg | 1005x567 | 16:9 | Cover evidence strip, middle cell: a talk-video frame (Figure 1b) | Screenshot | `Middle cell of the cover band` | no-crop | user | Existing | Figure 1b, a frame of the Paper2Video output for the CITransNet paper | none | local |
| blog_docx_en.jpg | 732x1332 | 11:20 | Cover evidence strip, right cell: the bilingual blog in Word (Figure 1c) | Screenshot | `Right cell of the cover band, portrait page shown complete` | no-crop | user | Existing | Figure 1c, the English Paper2Blog DOCX for the BEiT paper | none | local |
| fig2_pipeline.png | 1181x259 | 4.6:1 | Figure 2, the five-skill pipeline: one PDF in, three editable artifacts out, one shared extraction in the middle | Diagram | `Full-width band under the claim line (#P1-04); the contribution bullets sit below it` | no-crop | user | Existing | Figure 2 of the paper | none | local |
| fig3_poster_pipeline.png | 1221x379 | 3.2:1 | Figure 3, the Paper2Poster pipeline with the staged-fill loop | Diagram | `Band across the top of the field (#P1-04); the requirement table beneath` | no-crop | user | Existing | Figure 3 of the paper | none | local |
| fig4a_fill_initial.png | 343x767 | 4:9 | Figure 4a, debug overlay of the freshly composed draft | Screenshot | `Left of three equal-height panels in a sequence (#P3-06) beside the verdict-band chart` | no-crop | user | Existing | Figure 4a, Latent Diffusion Models poster, initial exploration | none | local |
| fig4b_fill_progress.png | 387x767 | 1:2 | Figure 4b, the fill loop in progress | Screenshot | `Middle panel of the sequence` | no-crop | user | Existing | Figure 4b | none | local |
| fig4c_fill_done.png | 409x767 | 8:15 | Figure 4c, the completed poster with every section FULL | Screenshot | `Right panel of the sequence` | no-crop | user | Existing | Figure 4c | none | local |
| fig5_video_pipeline.png | 1134x379 | 3:1 | Figure 5, the Paper2Video overview | Diagram | `Band across the top of the field; the requirement table beneath` | no-crop | user | Existing | Figure 5 of the paper | none | local |
| fig7_blog_pipeline.png | 1220x230 | 5.3:1 | Figure 7, the Paper2Blog pipeline | Diagram | `Band across the top of the field; the requirement table beneath` | no-crop | user | Existing | Figure 7 of the paper | none | local |
| fig9_reel_interaction.jpg | 1920x572 | 3.36:1 | Figure 9, the two Paper2Reel interaction states: hover highlights a section, double-click opens video + blog | Screenshot | `Full-width band dominating the field (#P1-04) with the reading in two columns beneath` | no-crop | user | Existing | Figure 9 of the paper | none | local |
| fig10a_author_gt.jpg | 1920x1280 | 3:2 | Figure 10, author ground-truth poster | Screenshot | `Top-left cell of a 3 × 2 small-multiples grid (#P3-04), each cell labeled with its configuration` | no-crop | user | Existing | Figure 10, top left: the human reference | none | local |
| fig10b_claude_max.jpg | 1920x1152 | 5:3 | Figure 10, Claude Code (claude-opus-4.8) at max reasoning | Screenshot | `Grid cell` | no-crop | user | Existing | Figure 10, top right per the caption | none | local |
| fig10c_claude_48.jpg | 1920x1152 | 5:3 | Figure 10, Claude Code (claude-opus-4.8) at high reasoning | Screenshot | `Grid cell` | no-crop | user | Existing | Figure 10 | none | local |
| fig10d_claude_47.jpg | 1920x1152 | 5:3 | Figure 10, Claude Code (claude-opus-4.7) | Screenshot | `Grid cell` | no-crop | user | Existing | Figure 10 | none | local |
| fig10e_claude_46.jpg | 1920x1152 | 5:3 | Figure 10, Claude Code (claude-opus-4.6) | Screenshot | `Grid cell` | no-crop | user | Existing | Figure 10 | none | local |
| fig10f_codex.jpg | 1920x1152 | 5:3 | Figure 10, Codex (gpt-5.5) | Screenshot | `Grid cell` | no-crop | user | Existing | Figure 10, bottom right | none | local |

Every image is a figure of the source paper, imported at original fidelity as evidence and never redrawn; each placement keeps the complete figure visible (`no-crop`) with a "Fig. N" caption tag and the paper's own caption sense in native text. No AI images and no web images.

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: each page's notes open with the takeaway in one sentence, then explain the evidence on the page in the order the eye reads it, name the paper section, figure, or table each number comes from, keep the paper's hedges, and close with a one-line transition to the next page; nothing outside the paper
- **Total duration**: 25 minutes (18 pages; skill and result pages about 2 minutes each, question, contribution, and conclusion pages about 1 minute)
- **Notes style**: formal
- **Presentation purpose**: walk a skeptical research audience through the paper in its own order so every conclusion can be traced to a figure, a table, or a stated method

<!-- ppt-master-schema: design-spec/v1 -->
# The Night Shelf - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | The Night Shelf — campaign pitch for Fog & Fern Books |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 13 |
| Primary Language | en-US |
| Target Audience | The owner and the four-person team of Fog & Fern Books, a fictional independent bookstore in a mid-size English-speaking city — people who know their shop and their regulars intimately, who have never commissioned a campaign before, and who will judge the work by whether it sounds like their shop rather than by advertising craft |
| Communication Intent | Persuade first, then align: make the team feel one idea and believe it came from a real truth about how people actually spend their evenings; then align them on what the late-autumn campaign is, what it asks of the shop, and what happens next. Evidence carries the opening; the idea carries the middle; production reality closes. |
| Desired Audience Outcome | The team can repeat the campaign line exactly after one hearing, can name the audience truth it rests on, and agrees to take the campaign into production for late autumn |
| Core Message / Ask / Action | The last hour of the day is the only reading time still available, and it currently belongs to a screen; "The Night Shelf" takes it back — approve the campaign for late autumn |
| Delivery Context | Presenter-led, in the shop, one meeting, roughly twenty minutes with the deck on a screen; secondary use as a leave-behind the owner reads again alone before deciding |
| Artifact Afterlife | Review and approval, then hand-off to production as the scope-of-work reference; the sources must stay checkable in the file |
| Reading Mode | presentation |
| Content Strategy | Free — no source outline exists; the argument, the campaign and the whole visual identity are invented for this pitch. Hard boundary: every externally verifiable number stays sourced to the imported facts file, and every invented client, commercial, or production figure is marked illustrative on the page where it appears. |
| Design Style | Showcase argument in a photo-editorial deck whose own voice stays quiet so the campaign's identity is the only thing with colour and character |
| AI Image Acquisition Path | auto (Path A — `image_gen.py --manifest`) |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — workflow default retained at final Stage 2 (`proactive_speaker_notes: true`) |
| Custom Animations | enabled — explicit run instruction requiring per-page custom animations, which overrides the `false` proactive default |
| Narration Audio | disabled — workflow default; no narration was requested |
| Created Date | 2026-09-10 |

- **Template Application**: Adopt the installed Creative Pitch Style wholesale as the deck's communication method and design discipline — its argument flow (audience truth → task → strategic thought → the idea → hero execution → range → identity → tone → environment → production reality → close), its one-moment-per-page message discipline, its Claim Discipline separating insight, idea, execution and production reality, its neutral-field colour behaviour, and its image direction. The Style supplies no structure, so every page is flat free design. Two Style defaults are consumed with a stated decision: the preferred `showcase` mode and `photo-editorial` visual style are kept; the preferred `editorial` image rendering is replaced by a custom rendering because `editorial` is a magazine-infographic treatment and this deck's images are night photography and printed poster artwork, not infographics.

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 72 px on all four sides; full-bleed imagery may cross them |
| Content Area | x 72–1208, y 72–648 (1136 × 576) |

## III. Visual Theme

### Theme Style

- **Mode**: showcase
- **Visual style**: photo-editorial
- **Theme**: The deck is a dark room with one light in it. The presentation's own field is night ink and stays neutral so the campaign's colours are seen accurately; the campaign supplies the only warmth. One mark recurs — a short horizontal rule with a crescent resting on it, the shelf and the night — drawn natively so it survives every scale, and it is the continuity object that carries from the idea page into the hero and from tone into environment. Creative pages carry no chrome, no page numbers and no footer; the two factual pages (production and close) switch to a paper field, which is the register shift itself.
- **Tone**: Quiet, unhurried, confident. The deck never explains a picture it has just shown.

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | `#0E0E10` | Night ink — the deck's neutral field for the whole creative arc |
| Secondary background | `#F4F1EA` | Paper — the field for the production and close pages, the visible register shift |
| Primary | `#E9C877` | Lamplight — the campaign's one light: the mark, the light source inside every image, the reading series in the chart |
| Accent | `#7FA69B` | Fern — the shop's own signature, used only on surfaces the shop owns (window, shelf talker, event) |
| Secondary accent | `#C4553F` | Ember — reserved for the thing being taken back: the screen, and the screen series in the chart |
| Body text | `#EDEAE3` | Paper-cream type on the night field |
| Secondary text | `#A29E97` | Captions, attribution, source lines, contextual annotation |
| Divider | `#2E2E33` | Hairlines and rules on the night field |
| Ink | `#141416` | Type on the paper field (production and close pages) |
| Scrim | `#08080A` | Gradient scrim stops beneath type sitting over imagery — never a whole-frame dim |
| Grid | `#3A3A40` | Chart hairlines and axis rules, lighter than dividers |

### AI Image Strategy

- **Image Rendering**: custom
- **Visual**: Photographic night interiors and streets at low key, lit by one practical warm light — a shaded lamp, a shop window, a bedside bulb — with true depth of field, real materials (paper, painted wood, glass, wet pavement, wool) and deep unlit space left genuinely dark. Inside those photographs, any surface that belongs to the campaign itself — a pasted street poster, a phone screen, a printed bookmark — is rendered as flat printed ink: two or three solid colours, stencil-cut shapes, visible halftone in the transitions, no gradient inside a printed shape. Nothing in any image contains text.
- **Mood**: The last hour before sleep, with one lamp on. The reference is the window of a bookshop seen from a cold pavement at seven in the evening, not a lifestyle catalogue.
- **Image Rendering Behavior**: Photograph the world at night and print the campaign onto it. Lines are photographic and absent except where printed artwork appears, where edges become stencil-cut and slightly misregistered. Texture is real material grain plus a halftone dot pattern confined to printed surfaces and a light film grain over the whole frame. Depth is true optical depth — a sharp foreground object, a falling-off middle ground, unlit background — while printed surfaces stay perfectly flat inside that depth. Material is paper, glass, wood and skin under a single warm source; the mood is quiet, contemplative and slightly cold outside the light.
- **Image Rendering References**: `corporate-photo` (photographic realism, optical depth of field and real material rendering), `warm-scene` (single-source golden lamplight, bloom and atmospheric falloff), `screen-print` (flat two-to-three-colour printed ink, stencil edges and halftone, applied only to campaign surfaces inside the frame)

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | Serif / bookish, high-contrast, the voice of the work itself | Georgia | — | serif |
| Body | Sans / quiet, small, the deck's own unobtrusive voice | Arial | — | sans-serif |
| Display | Sans / lining figures for numerals shown at statement scale | Arial | — | sans-serif |
| Cover title | Serif / the campaign's own voice at cover scale | Georgia | — | serif |
| Idea line | Serif / the campaign line at statement scale | Georgia | — | serif |

- **Title stack**: `Georgia, serif`
- **Body stack**: `Arial, sans-serif`
- **Display stack**: `Arial, sans-serif`
- **Cover title stack**: `Georgia, serif`
- **Idea line stack**: `Georgia, serif`
- **Role rationale**: the cover title and the campaign's idea line belong to the work's serif voice, so they take the Title family explicitly rather than inheriting the body sans. Georgia sets old-style figures whose digits sit at different heights, so every numeral shown at statement scale — the two audience-truth numbers, the chart labels, the table values — uses the Display/Arial stack instead of the Title family. Georgia titles are kept wordy for the same reason.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 30 |
| Cover title | 84 |
| Idea line | 72 |
| Display (hero numeral) | 96 |
| Title | 48 |
| Subtitle | 38 |
| Lead | 36 |
| Annotation | 24 |
| Footnote | 18 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: One thing per page arrives first and everything else is subordinate to it. On creative pages the work arrives first and the line second; on the two factual pages the title arrives first and the grid second.
- **Composition tendency**: Alternate between full-frame work with a single line of type in a quiet corner, and sparse type-only pages with generous empty ink around a short statement. Keep the framing of the work consistent — the same caption position, the same attribution scale — while the pace varies between quiet and full.
- **Cross-page continuity**: The shelf-and-crescent mark recurs at the same small scale in the same relative position on the creative pages; caption position and attribution scale never move; the hero artwork recurs three times as derived backdrops so the deck feels like one body of work. The two paper-field pages deliberately break all of it.
- **Spacing posture**: Variable — extremely open through the creative arc, tighter and plainer on production and close.
- **Spacing anchors**: page margin 72 px; block gap 32 px; column gutter 40 px; corner radius 0 px (the phone-screen mockup's rounded corners are a property of the depicted device, not a deck radius); body leading 1.45.

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| `tabler-outline/printer` | Print and out-of-home channel class on the production page |
| `tabler-outline/device-mobile` | Social and owned-digital channel class |
| `tabler-outline/building-store` | In-store and shop-window channel class |
| `tabler-outline/calendar-event` | Event and programming channel class |
| `tabler-outline/bookmark` | Take-away print collateral class |
| `tabler-outline/book` | Product and catalogue class |
| `tabler-outline/bulb` | Light and evening-programme class |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P02 | chart | grouped_bar_chart | Compare average daily minutes spent reading against minutes spent watching television, by age band, so the gap and its shape are visible at once |
| P12 | table | record_table | Hold the production scope as flat records — one deliverable per row against stable format, quantity, lead-time, rights and owner fields |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hero_night_shelf.jpg | 1920×1072 | 43:24 | The campaign's hero execution artwork — one lit shelf in a dark room | Illustration | Full-frame field on the hero page with a single line of type in the lower quiet zone; a tight vertical detail crop of the same file carries the cover | adaptive | ai | Generated | A single narrow bookshelf in an otherwise dark room, lit by one shaded lamp standing just out of frame at the left; six or seven books stand and one lies open; a window behind shows a cold blue night with fog; the right two-thirds of the frame fall away into unlit dark and must stay quiet enough to hold type. Warm light pools on the shelf edge and the open page; everything outside the pool is deep ink. | none | hero_page |
| poster_artwork.jpg | 1288×1920 | 53:79 | The campaign's street-poster artwork, shown inside a pasted poster and inside the shop window | Illustration | Sits inside a 2:3 poster crop on the range page and again, smaller and angled by context, in the window on the environment page | adaptive | ai | Generated | A printed street poster for a night reading campaign: flat two-colour ink on cream stock, a stencil-cut crescent resting on a horizontal rule occupying the upper half, a solid block of unbroken cream in the lower third left completely empty for type, visible halftone where the two inks meet, slight misregistration. No text anywhere. | none | local |
| social_artwork.jpg | 1920×1920 | 1:1 | The campaign's social post artwork, shown inside a phone screen | Illustration | Fills a rounded phone-screen crop on the range page; the empty lower band is where the native caption sits | adaptive | ai | Generated | A square social post for the same night reading campaign: the same flat two-colour printed ink language, a crescent and a shelf rule composed off-centre to the upper right, a wide empty cream band across the bottom third, halftone texture in the transition, slight misregistration. No text anywhere. | none | local |
| instore_scene.jpg | 1920×1072 | 43:24 | Environment and context — the shop window at night seen from the pavement at honest scale | Photo | Full-frame environmental field; the window occupies the right half at a realistic standing eye level, leaving the wet pavement at the left to carry type | adaptive | ai | Generated | A small independent bookshop window photographed at night from the pavement across a narrow street, at ordinary standing eye level and true scale — the window is roughly one and a half metres wide, warm light inside, books on a low display table, a blank cream poster pasted inside the glass at the right edge, wet pavement reflecting the light in the foreground, fog softening the street lamps behind the camera. Nothing in the frame contains readable text. | none | local |
| element_book.png | 600×464 | 674:521 | Campaign element — book | Illustration | Small element resting on the shelf rule in the identity system | no-crop | slice | Generated | Derived from `elements_sheet.png`; cell 1 | none | local |
| element_lamp.png | 399×627 | 7:11 | Campaign element — lamp | Illustration | The light in the identity system and in the take-away collateral | no-crop | slice | Generated | Derived from `elements_sheet.png`; cell 2 | none | local |
| element_moon.png | 483×538 | 483:538 | Campaign element — crescent | Illustration | The crescent that sits on the shelf rule wherever the element family is shown rather than drawn | no-crop | slice | Generated | Derived from `elements_sheet.png`; cell 3 | none | local |
| element_mug.png | 543×496 | 543:496 | Campaign element — mug | Illustration | Tone-and-craft page: the register of the finished work | no-crop | slice | Generated | Derived from `elements_sheet.png`; cell 4 | none | local |
| element_bookmark.png | 236×634 | 118:317 | Campaign element — printed bookmark | Illustration | The take-away carrier on the range page, shown at its own narrow ratio | no-crop | slice | Generated | Derived from `elements_sheet.png`; cell 5 | none | local |
| element_fern.png | 471×656 | 471:656 | Campaign element — fern frond, the shop's own signature | Illustration | Marks the surfaces the shop itself owns, on the identity and production pages | no-crop | slice | Generated | Derived from `elements_sheet.png`; cell 6 | none | local |
| hero_grey.jpg | 1920×1072 | 43:24 | Desaturated, dimmed backdrop for the strategic-thought page | Illustration | Recedes to a quiet field behind a single short statement | adaptive | ai | Generated | Derived from `hero_night_shelf.jpg`; treatment=grayscale + brightness reduction | none | local |
| hero_dim.jpg | 1920×1072 | 43:24 | Dimmed backdrop for the identity-exploration page | Illustration | Darkened but still recognisable, so the identity system is seen sitting on the work rather than on a swatch board | adaptive | ai | Generated | Derived from `hero_night_shelf.jpg`; treatment=brightness reduction | none | local |
| hero_blur.jpg | 1920×1072 | 43:24 | Blurred backdrop for the tone-and-craft page | Illustration | Out of focus behind foreground material, so the page reads as texture and register rather than as another execution | adaptive | ai | Generated | Derived from `hero_night_shelf.jpg`; treatment=blur | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: One short spoken passage per page grounded in that page's final SVG — what the presenter says while the page is on screen, in the order the page is read. Every page whose content includes an external number restates its source aloud; every page carrying invented client, production or commercial figures says plainly that they are illustrative and that Fog & Fern Books is a fictional client. Notes carry the explanation the creative pages deliberately keep off the slide. No note invents a fact that is not on the page or in the imported facts file.
- **Total duration**: about 18–20 minutes for 13 pages, weighted toward the idea and range pages
- **Notes style**: conversational — a person talking in a shop, not a script being read
- **Presentation purpose**: Persuade the team to feel the idea and believe its audience truth, then align them on scope and obtain approval for late autumn

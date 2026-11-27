<!-- ppt-master-schema: design-spec/v1 -->
# القهوة العربية - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | arabic_coffee_ar_ppt169_20260911 |
| Canvas Format | PPT 16:9 (ppt169) — 1280×720 |
| Page Count | 15 |
| Primary Language | ar-SA |
| Target Audience | جمهور عام يحضر محاضرة عامة باللغة العربية، دون افتراض معرفة متخصصة بتاريخ القهوة أو بملفات اليونسكو |
| Communication Intent | التعريف بالقهوة العربية أولاً بوصفها لغة ضيافة، ثم شرح رحلتها من الحبة إلى الفنجان وآداب تقديمها، ثم عرض الاعتراف الدولي بها وبيانات إنتاج البن السعودي الموثّقة |
| Desired Audience Outcome | يستطيع الحاضر أن يشرح لماذا تُعدّ القهوة رمزاً للكرم، وأن يتعرّف على مراحل التحضير وترتيب التقديم وإشارة هزّ الفنجان، وأن يميّز بين إدراج 2015 وإدراج البن الخولاني 2022، وأن يعرف أين يُزرع البن في المملكة |
| Core Message / Ask / Action | القهوة العربية ليست مشروباً فحسب، بل لغة ضيافة لكل خطوة فيها معنى؛ ولهذا صارت تراثاً إنسانياً تحميه اليونسكو ويُزرع بنّه في جبال جازان |
| Delivery Context | محاضرة عامة يقدّمها متحدث حيّاً (نحو 25 دقيقة) على شاشة عرض في قاعة؛ استخدام ثانوي: ملف يُرسل للحضور بعد المحاضرة |
| Artifact Afterlife | مرجع للحضور بعد المحاضرة مع روابط المصادر الرسمية |
| Reading Mode | balanced |
| Content Strategy | متوازن (لم يحدّد المستخدم درجة التصرّف): إعادة بناء المادة البحثية في سرد تعليمي مع الحفاظ على كل الحقائق كما وردت في مصادرها؛ الصفحات المبنية ذاتياً تُوسَم «تنظيم» |
| Design Style | اتجاه «مجلس الضيافة»: تحريري دافئ تقوده صور طبيعة صامتة منخفضة الإضاءة، ونوافذ صور على شكل قوس المجلس، وخطوط نحاسية رفيعة، وقراءة من اليمين إلى اليسار |
| AI Image Acquisition Path | auto (Path A: `image_gen.py --manifest`، الواجهة المضبوطة في `.env`) |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy (default true) |
| Custom Animations | enabled — explicit user instruction (task brief: custom `animations.json` with entrance order and ≥2 Morph pairs) |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-11 |

- **Confirmation provenance**: the user explicitly delegated confirmation («أترك لك قرارات التأكيد، اعتمد توصياتك»); Stage 1 (communication contract + free design) and Stage 2 (direction 0 of 3) were decided under the delegated branch of `confirm-surface.md` §1; no Confirm UI was launched and no UI receipt exists.
- **Numerals**: الأرقام الغربية 0–9 في كل الشرائح والملاحظات والمخطط والجدول (كما في مصادر واس ووزارة البيئة)؛ لا تُستخدم الأرقام الهندية ٠–٩.

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 72 px يميناً ويساراً، 56 px أعلى وأسفل |
| Content Area | x 72–1208، y 56–664 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: narrative, instructional
- **Mode Behavior**: يُفتتح العرض بخطاف سردي (الفنجان رسالة)، ثم يتحوّل إلى شرح تعليمي متدرّج: المعنى ← من الحبة إلى الفنجان ← آداب التقديم ← الاعتراف الدولي ← الجغرافيا والأرقام، مع عناوين تقريرية تحمل حكماً واحداً لكل صفحة، وخطوات متوازية بالبنية نفسها، وإشارات انتقال في الملاحظات.
- **Visual style**: custom
- **Visual Style References**: editorial, photo-editorial
- **Visual Style Behavior**: هيكل تحريري من اليمين إلى اليسار: مِسطرة رأسية نحاسية رفيعة على الحافة اليمنى يتدلّى منها النص، وعنوان نسخي كبير مع نص متن بلا زوائد، وكيكر صغير فوق العنوان، وأعمدة غير متساوية؛ الصور صامتة دافئة تحتلّ النصف الأيسر أو المجال الكامل، وتُقصّ في نوافذ على شكل قوس المجلس أو دائرة المقلاة؛ لا بطاقات مكرّرة ولا ظلال زخرفية، والتدرّج الوحيد ستارة لقراءة النص فوق الصورة.
- **Theme**: مجلس الضيافة — رمل دافئ، بنّ محمّص، نحاس الدلّة، وخضرة الهيل
- **Tone**: دافئ، رصين، مضياف

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F6EFE4 | مجال الصفحات الفاتح (رمل/ورق) |
| Secondary background | #EADCC6 | أشرطة وحقول ثانوية ولوحات التمييز |
| Primary | #4A2C1D | البنّ المحمّص: العناوين والحقول الداكنة والعنصر الأساسي |
| Accent | #B8862B | نحاس الدلّة: المساطر والأرقام البطولية والتمييز |
| Secondary accent | #5E7D4F | الهيل: التمييز الثانوي والسلاسل الثانية |
| Body text | #2B1D15 | نص المتن |
| Secondary text | #6E5A4C | التعليقات والمصادر والحواشي |
| Divider | #D6C3A5 | الخطوط الشعرية والحدود |
| Scrim | #1E120B | ستارة داكنة فوق الصور لقراءة النص |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: corporate-photo
- **Image Rendering Behavior**: تصوير طبيعة صامتة تحريري منخفض الإضاءة: ضوء نافذة جانبي دافئ واحد، وخلفية بنية داكنة غير مركّزة، وعمق ميدان ضحل، ومواد حقيقية (نحاس مصقول، خزف أبيض، حديد مسوّد، قماش صوف منسوج)؛ تدرّج لوني نحو البنّ المحمّص مع لمعات نحاسية ولمسة خضراء من الهيل؛ لا نص ولا شعارات ولا وجوه في أي صورة.
- **Visual**: طبيعة صامتة لأدوات القهوة (الدلّة، الفنجان، التاوة، الهيل) ومشهد مدرّجات جبلية، بالدفعة نفسها والإضاءة نفسها
- **Mood**: دفء مجلس مسائي، كصفحة مصوّرة في مجلة ثقافية عن التراث

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | نسخي كلاسيكي بتباين خطّي (serif) | Times New Roman | Times New Roman | serif |
| Body | حديث بلا زوائد، واضح على الشاشة | Segoe UI | Segoe UI | sans-serif |

- **Typography upgrade (Reference)**: بعد تأكيد تثبيت الخط على جهاز العرض يمكن استبدال خط العنوان بـ Sakkal Majalla (ميزة لغة ويندوز العربية، غير مضمونة التثبيت).
- **Title stack**: 'Times New Roman', serif
- **Body stack**: 'Segoe UI', sans-serif
- **Display stack**: 'Times New Roman', serif
- **Role rationale**: display (الأرقام البطولية والجمل البطولية في صفحات التنفّس) يستخدم عائلة العنوان النسخية نفسها ليبقى صوت العرض واحداً؛ أُضيف أثناء التنفيذ لأن القيمة الافتراضية كانت ستسقطه على خط المتن.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 26 |
| Title | 48 |
| Subtitle | 34 |
| Lead | 30 |
| Annotation | 20 |
| Footnote | 16 |
| Kicker | 20 |
| Display | 96 |
| Cover title | 120 |

- **Body anchor rationale**: 26 px بدلاً من 24 لأن ارتفاع الحروف الصغيرة في الخطوط العربية أصغر بصرياً من اللاتينية عند المقاس نفسه، والعرض في قاعة.

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: من اليمين إلى اليسار — الكيكر والعنوان عند الحافة اليمنى، ثم المتن، ثم الدليل البصري أو الصورة في الجهة اليسرى؛ التسلسلات والخطوط الزمنية تبدأ من اليمين.
- **Composition tendency**: أعمدة غير متساوية (نص ⅖ يمين، صورة أو دليل ⅗ يسار) أو مجال صورة كامل مع منطقة نص على شكل حرف L؛ مِسطرة رأسية نحاسية يتدلّى منها النص.
- **Cross-page continuity**: قوس المجلس (نافذة مقوّسة) موتيف متكرر للصور؛ دائرة المقلاة للتحميص؛ رقم كبير نحاسي لكل فصل؛ سطر مصدر بخط صغير أسفل كل صفحة واقعية.
- **Spacing posture**: متغيّر حسب إيقاع الصفحة: كثيف في صفحات الأدلة، واسع في صفحات التنفّس.
- **Spacing anchors**: هامش الصفحة 72 px؛ فجوة الكتل 32 px؛ فاصل الأعمدة 40 px؛ نصف قطر الزوايا 4 px؛ تباعد أسطر المتن 1.6

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 1.5

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/coffee.svg | القهوة والفنجان |
| icons/tabler-outline/flame.svg | التحميص والنار |
| icons/tabler-outline/seedling.svg | الشتلات والزراعة |
| icons/tabler-outline/mountain.svg | المدرجات والجبال |
| icons/tabler-outline/link.svg | روابط المصادر |
| icons/tabler-outline/world.svg | اليونسكو والاعتراف الدولي |
| icons/tabler-outline/calendar.svg | التواريخ والأعوام |
| icons/tabler-outline/users.svg | المجالس والتجمعات |
| icons/tabler-outline/sun.svg | التجفيف |
| icons/tabler-outline/droplet.svg | الغسل والنقع |
| icons/tabler-outline/hand-stop.svg | الإشارة والاكتفاء |
| icons/tabler-outline/arrow-narrow-left.svg | اتجاه التسلسل من اليمين إلى اليسار |
| icons/tabler-outline/chevron-left.svg | اتجاه الخطوات |
| icons/tabler-outline/map-pin.svg | المواقع والمحافظات |
| icons/tabler-outline/building-arch.svg | المجلس والضيافة |
| icons/tabler-outline/leaf.svg | الهيل والنكهات |
| icons/tabler-outline/certificate.svg | الإدراج والاعتراف |
| icons/tabler-outline/filter.svg | الفرز والتصفية |
| icons/tabler-outline/hourglass.svg | الوقت والمدة |
| icons/tabler-outline/external-link.svg | روابط خارجية |
| icons/tabler-outline/grain.svg | الحبوب والطحن |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P07 | table | comparison_matrix | مقارنة المناطق بدرجة التحميص والإضافات |
| P13 | chart | horizontal_bar_chart | مقارنة إنتاج البن الصافي بين المناطق الخمس |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dallah_hero.jpg | 2752×1536 | 16:9 | صورة الغلاف: الدلّة تصبّ في فنجان | Photography | نافذة مقوّسة على يسار الغلاف بجوار العنوان | adaptive | ai | Generated | دلّة نحاسية تقليدية بمنقار طويل تصبّ قهوة ذهبية فاتحة في فنجان خزفي أبيض صغير بلا مقبض، على قماش صوفي منسوج بنقوش هندسية حمراء وبيضاء؛ بخار خفيف؛ الموضوع في الثلث الأيسر ومساحة داكنة هادئة يميناً؛ لا أيدٍ ولا وجوه ولا نص | none | hero_page |
| roasting_tawa.jpg | 2048×2048 | 1:1 | التحميص: حبوب البن في التاوة | Photography | دائرة المقلاة: قصّ دائري يطابق شكل التاوة، ويتكرر صغيراً في P03 | adaptive | ai | Generated | مقلاة حديدية مستديرة واسعة (تاوة) من الأعلى بزاوية خفيفة، فيها حبوب بن تتدرّج من الأخضر الباهت إلى الأحمر فالبني، مع ملعقة تقليب طويلة (محماس) وجمر خافت تحتها؛ الموضوع في المركز لقصّ دائري؛ لا نص | none | local |
| three_dallahs.jpg | 2752×1536 | 16:9 | الدلال الثلاث بأحجام متدرجة | Photography | شريط عريض فوقه أو تحته تسميات أصلية لكل دلّة، من اليمين إلى اليسار | adaptive | ai | Generated | ثلاث دلال نحاسية متدرّجة الحجم على مصطبة خشبية داكنة: الكبرى في أقصى اليمين، والمتوسطة في الوسط، والصغرى في اليسار، مع فراغ متساوٍ بينها وخلفية داكنة؛ لا نص | none | local |
| cardamom.jpg | 1024×1024 | 1:1 | الهيل مع البن المطحون | Photography | مربّع صغير بجوار الجدول، يُقصّ في قوس | adaptive | ai | Generated | حفنة قرون هيل خضراء بعضها مفتوح تظهر بذورها السوداء، بجانب كومة صغيرة من البن المطحون الفاتح في صحن خزفي، من الأعلى، إضاءة جانبية دافئة؛ لا نص | none | local |
| finjan_hand.jpg | 1792×2400 | 3:4 | إشارة هزّ الفنجان | Photography | صورة طولية كبيرة في P09 وتظهر صغيرة داخل دائرة في P08 (الكائن نفسه يكبر بالانتقال) | adaptive | ai | Generated | يد يمنى (بلا وجه أو هوية) تمسك فنجاناً خزفياً أبيض صغيراً بلا مقبض وتهزّه بخفة يميناً ويساراً مع أثر حركة بسيط، أمام خلفية مجلس داكنة غير مركّزة؛ الموضوع في المنتصف؛ لا نص | none | local |
| terraces.jpg | 2752×1536 | 16:9 | مدرّجات البن الجبلية | Photography | مجال كامل خلفي في P11 (نسخة ثنائية اللون) ونافذة مقوّسة في P14 | adaptive | ai | Generated | مدرّجات زراعية حجرية على سفوح جبلية خضراء في الصباح الباكر، فيها شجيرات بن تحمل ثماراً حمراء، وضباب خفيف في الوادي؛ السماء في الربع العلوي هادئة؛ لا مبانٍ حديثة ولا أشخاص ولا نص | none | local |
| terraces_duo.jpg | 2752×1536 | 16:9 | خلفية ثنائية اللون لصفحة البن الخولاني | Photography | مجال كامل بستارة داكنة يميناً لقراءة الخطوات | adaptive | ai | Generated | Derived from terraces.jpg; treatment=duotone #1E120B #EADCC6; | none | local |
| dallah_hero_blur.jpg | 2752×1536 | 16:9 | خلفية صفحة الختام | Photography | مجال كامل ضبابي داكن خلف الخلاصة والروابط | adaptive | ai | Generated | Derived from dallah_hero.jpg; treatment=brightness 0.55 + blur 18; | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: ملاحظات عربية تشرح كل صفحة وتربطها بالتي تليها، تذكر المصدر والسنة لكل رقم، وتشير إلى التعارضات الموثّقة (يد الصبّ بين اليونسكو وأبوظبي؛ رقم 2024 مقابل 2025 لجازان) دون حقائق من خارج ملف الحقائق
- **Total duration**: نحو 25 دقيقة
- **Notes style**: حواري تعليمي
- **Presentation purpose**: التعريف بالقهوة العربية لغةَ ضيافة، وشرح التحضير والآداب، وعرض الاعتراف الدولي وبيانات الإنتاج

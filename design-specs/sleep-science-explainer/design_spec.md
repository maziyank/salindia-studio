<!-- ppt-master-schema: design-spec/v1 -->
# 我们为什么要睡觉 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | sleep_science_explainer_ppt43_20260910 |
| Canvas Format | PPT 4:3 (1024×768) |
| Page Count | 15 |
| Primary Language | zh-CN |
| Target Audience | 没有生物学背景的成年听众:上班族、学生家长、熬夜的人;他们知道"睡不够会难受",但没想过睡眠内部有结构,也不知道那些睡眠建议是怎么来的 |
| Communication Intent | 先解释、后说服:用一条从熟悉经验出发的链条,把"睡眠是一个有结构、有功能的主动过程"讲通;在此基础上让听众重新掂量"少睡一点没关系"这句话;全程把共识、争议、罕见特例分开 |
| Desired Audience Outcome | 听众能用自己的话说出"睡眠压力"和"生物钟"两股力量各是什么、怎么互相作用,能说出 7 小时建议的来源,并能指出"睡眠清洗大脑"目前仍有争议 |
| Core Message / Ask / Action | 睡眠不是关机,而是一段被两股力量安排好的主动工作;把它当成可以随时挪用的时间,代价是可核查的 |
| Delivery Context | 主讲人现场讲解(科普讲座 / 公司分享 / 课堂),约 25 分钟;次要用途是讲后把文件发给听众自读 |
| Artifact Afterlife | 传阅与复用:听众自读、被引用其中的数字、来源页可点开核查 |
| Reading Mode | presentation |
| Content Strategy | 事实全部来自已导入的研究对(`sources/sleep_science_research.md` 与 `.facts.json`),叙述结构自由重组;不引入未溯源数字,凡范围与估算都写明;小鼠实验不改写成人类结论 |
| Design Style | 纸层夜谈:分层剪纸的暖纸底,深夜蓝与暖橙两色各自承担固定的解释职责,每页一层新纸盖上去 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 工作流默认(final Stage-2 proactive value `true`) |
| Custom Animations | enabled — 用户在任务书中明确要求自定义动画,并要求压测原生图表的分阶段出现 |
| Narration Audio | disabled — 工作流默认 |
| Created Date | 2026-09-10 |

- **Template Application**: 采用已安装的 Science Explainer Style 的方法层:instructional 的讲解顺序、§III 的整套页面角色(熟悉的地面 → 谜题 → building block → 类比并标出失效点 → 机制 → 尺度 → 证据 → 误解 → 知识边缘 → 为什么重要 → 继续探索)、以及"每页一个想法、标题用大白话、术语首次出现处附白话释义、类比必须标出边界、图表先讲坐标轴再上数据并直接在标记上标注"的表达纪律。视觉层沿用 Style 的 paper-cut 偏好与"颜色承担固定解释职责"的规则;偏离一处:Style §VI 的 Preferred Image Rendering 写的是 `vector-illustration`,本项目改用 `paper-cut` 渲染,理由是 Style §V 已把视觉风格定为 paper-cut,而 catalog 中 paper-cut 风格的配对渲染就是 paper-cut,沿用 vector-illustration 会让插画与页面材质分裂。Style 只提供方法与视觉默认,不提供画布、结构、原型与身份,页面保持 flat 自由设计。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 4:3 |
| Dimensions | 1024 × 768 |
| viewBox | `0 0 1024 768` |
| Margins | 上下左右各 56px |
| Content Area | x: 56–968, y: 56–712(可用宽 912,可用高 656) |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Visual style**: custom
- **Mode References**: instructional
- **Mode Behavior**: 按 instructional 的分解—排序骨架讲解,但每一步都必须由上一步"欠下的问题"引出:先给共享经验,再制造谜题,之后每页只加一块必需的积木;类比页必须在同页写出类比失效的地方;结尾回到开头那个经验并重新解释它。标题写"这个想法"的白话说法,术语只在其所指之物出现之后才登场,并与白话释义同页。
- **Visual Style References**: paper-cut
- **Visual Style Behavior**: 每个元素都是一张剪下来的纸,层叠而非描边:形状用略不规则的 polygon/path 切边,层与层之间只用 8–12% 的柔影表示高度;暖纸底作为"桌面",内容纸盖在上面;跨页保留一条底部的夜色波浪纸带作为累积容器,同一元素在相邻页保持同位置以便叠加;顶层允许小块镂空口子(die-cut window)露出下层。装饰即层次,不额外加边框与图标网格。
- **Theme**: 一夜是一张张叠上去的纸:白天那张纸越叠越厚(睡眠压力),另一张纸每天准点起落(生物钟),两张纸叠在一起才决定你什么时候睡着。
- **Tone**: 温和、具体、克制;不吓唬,不许诺,不把小鼠实验说成人类结论。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FBF5E9 | 暖纸底,所有剪纸层的"桌面" |
| Secondary background | #F0E4CE | 第二层纸:分区块、图表底板、引文块 |
| Primary | #2E4A7D | 固定语义=夜 / 睡眠 / 睡眠压力(Process S);深睡 N3 也用它 |
| Accent | #E08A32 | 固定语义=光 / 清醒 / 生物钟(Process C);仅用于大色块与标记,不做小字 |
| Secondary accent | #B4553E | 固定语义=REM(做梦)与风险提示;可做正文级小字 |
| Body text | #2A2622 | 正文与标题墨色 |
| Secondary text | #5C554C | 注释、图注、脚注、来源行 |
| Divider | #D9C9AC | 纸层切边、细分隔线 |
| Surface | #FFFDF7 | 最上层纸(卡片 / 图表面板)的纸面 |
| Block shade | #E6D8BE | 纸层落影与底纹块,比 Divider 深一档 |
| Light sleep | #6E8FBF | 固定语义=浅睡 N1/N2,是 Primary 的浅一档,与深睡形成同族梯度 |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: paper-cut
- **Mood**: 温暖、可触摸、手工感——像 Eric Carle 绘本里那种用彩色卡纸剪贴出来的夜晚场景。
- **Visual**: 彩色卡纸剪贴:形状由略不规则的剪切边定义,不画轮廓线;每层纸带 10–15% 纸纹,层与层之间落 8–12% 柔影;造型极简到能一眼认出的程度,不追求写实。所有插画都要在解释一件事(容器里的水位、被挡住的接收口、方向盘上打盹的手),不出现漂浮分子、发光大脑、实验室器皿这类只标示学科不解释内容的装饰。
- **Image Rendering Behavior**: 以 paper-cut 渲染为唯一基底:线条=无轮廓,只有纸的剪切边;纹理=每张纸 12% 纸纹;深度=层间 10% 柔影,禁止渐变与投射高光;材质=哑光卡纸;情绪=暖、手作、夜晚但不阴郁。图内不出现任何文字。

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 温暖、人文的无衬线;标题可坐在剪纸横幅上 | Microsoft YaHei | Trebuchet MS | sans-serif |
| Body | 高易读的无衬线,远距离可读 | Microsoft YaHei | Verdana | sans-serif |
| Data | 数字必须是等高数字,图表刻度与英文缩写在此角色 | Microsoft YaHei | Verdana | sans-serif |

- **Title stack**: `Microsoft YaHei, Trebuchet MS, sans-serif`
- **Body stack**: `Microsoft YaHei, Verdana, sans-serif`
- **Data stack**: `Microsoft YaHei, Verdana, sans-serif`
- **Role rationale**: 中文面只用一款(微软雅黑)是有意的——讲堂后排的可读性优先于字族对比,层级由字号、字重与颜色承担;拉丁面分两支:标题走 Trebuchet MS 取其人文的暖调,正文与数据走 Verdana 取其等高数字与远距离辨识度,避免 Georgia 一类旧式数字在图表中高低不齐。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 28 |
| Title | 52 |
| Subtitle | 36 |
| Annotation | 20 |
| Cover title | 84 |
| Lead | 34 |
| Hero number | 72 |
| Footnote | 18 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 视线先落在页面唯一的那个视觉物(插画、图表或大数字),再向下读一行白话结论;标题在顶部横幅纸上,是入口不是重点。
- **Composition tendency**: 每页一个想法一个视觉;大量留白由暖纸底承担;避免卡片网格与并列多栏,除非内容本身就是并列。
- **Cross-page continuity**: 底部的夜色波浪纸带贯穿全卷,水位/曲线类元素在相邻页保持同一位置累积;颜色的语义职责全卷固定不变(蓝=睡眠压力/夜,橙=光/生物钟,赤陶=REM 与风险)。
- **Spacing posture**: breathing 为主,数据页与证据页允许 dense。
- **Spacing anchors**: 页边距 56px;块间距 32px;栏间距 40px;圆角 12px;正文行高 42px。

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-filled/moon | 夜 / 睡眠状态标记 |
| tabler-filled/sun | 白天 / 光照输入 |
| tabler-filled/mug | 咖啡因 |
| tabler-filled/clock | 时长与时刻 |
| tabler-filled/bed | 就寝 / 睡眠时段 |
| tabler-filled/alert-triangle | 风险与警示 |
| tabler-filled/book | 继续阅读的来源 |
| tabler-filled/link | 可点开的外部链接 |
| tabler-filled/droplet | 腺苷 / 水位隐喻 |
| tabler-filled/steering-wheel | 驾驶场景 |
| tabler-filled/calendar-week | 工作日与周末的节律 |
| tabler-filled/microscope | 实验与证据 |
| tabler-filled/bulb | 想法 / 结论 |
| tabler-filled/hourglass | 半衰期与流逝 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P04 | chart | donut_chart | 一夜里四个睡眠阶段各占多少 |
| P05 | chart | line_chart | 一整夜的睡眠深度如何在四到五个周期里起伏 |
| P09 | chart | line_chart | 咖啡因按约 5 小时半衰期衰减 |
| P10 | chart | horizontal_bar_chart | 各年龄段的每日建议睡眠时长区间 |
| P12 | table | comparison_matrix | 两个常见说法与实际证据的逐条对照 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_night_third.jpg | 1920x1072 | 16:9 | 封面主视觉:夜色里被剪成三段的一天,其中一段是睡眠 | Illustration | 满幅横带压在封面下半,标题压在其上方的暖纸空处 | adaptive | ai | Generated | 剪纸夜晚:一条水平的时间带被剪成三段,最左那段是深蓝的夜,城市与床的极简剪影卧在夜段里;不要文字与刻度 | none | hero_page |
| el_night_window.png | 781x765 | 781:765 | 熟悉的地面:夜里亮着的窗与一张床 | Illustration | 放在页面右侧,与左侧的白话句子并排 | no-crop | slice | Generated | 切自 sheet_elements_a.png 左上格 | none | local |
| el_water_vessel.png | 670x811 | 670:811 | 类比与机制:一个装着水的容器,水位越醒越高 | Illustration | 页面中部偏右,水位线与相邻页保持同一高度以便承接 | no-crop | slice | Generated | 切自 sheet_elements_a.png 右上格;与 el_tide_arc 同族,可在相邻页共存 | none | local |
| el_tide_arc.png | 866x609 | 866:609 | 类比:每天准点起落的潮汐弧线与太阳月亮 | Illustration | 压在容器元素之上或之侧,表示两股力量叠加 | no-crop | slice | Generated | 切自 sheet_elements_a.png 左下格 | none | local |
| el_coffee_block.png | 816x694 | 816:694 | 机制:一只杯子挡住了一个接收口 | Illustration | 与咖啡因衰减图表同页,置于图表标题一侧 | no-crop | slice | Generated | 切自 sheet_elements_a.png 右下格 | none | local |
| el_wheel_nod.png | 663x835 | 663:835 | 证据:方向盘与一只垂下的手 | Illustration | 与困倦驾驶的大数字并排,数字为主图为辅 | no-crop | slice | Generated | 切自 sheet_elements_b.png 左上格 | none | local |
| el_two_papers_question.png | 836x546 | 836:546 | 知识边缘:两张方向相反的纸并排,中间留空 | Illustration | 居中,两侧各留一段说明位 | no-crop | slice | Generated | 切自 sheet_elements_b.png 左下格 | none | local |
| el_pillow_book.png | 770x614 | 770:614 | 为什么重要 / 继续探索:枕头上摊开的一本书 | Illustration | 页面一角,安静收束 | no-crop | slice | Generated | 切自 sheet_elements_b.png 右下格 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页讲稿承担页面刻意不写的深度:术语的第二层解释、数字的口径、类比失效的补充说明、以及到下一页的过渡句("现在我们有了水位,就可以问潮汐是什么")。事实只用 `sources/sleep_science_research.facts.json` 里的条目,讲稿不得引入页面上没有的新数字;小鼠实验在讲稿里也必须说明是小鼠。
- **Total duration**: 约 25 分钟(每页 90–120 秒)
- **Notes style**: 耐心的讲解口吻:先定义后使用,先类比后原理,预判听众会问的那一句并当场回答
- **Presentation purpose**: 先解释、后说服:把睡眠讲成一个有结构、有功能的主动过程,并让听众重新掂量"少睡一点没关系"

<!-- ppt-master-schema: design-spec/v1 -->
# 光伏为什么成了最便宜的电 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 光伏为什么成了最便宜的电 |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 15 |
| Primary Language | zh-CN |
| Target Audience | 能源、电力与产业投资的决策者及其幕僚：熟悉 LCOE 这个词，但价格认知大多停在 2018–2020 年，需要在项目立项、采购与并网排序上做判断 |
| Communication Intent | 先用一句结论纠正过时的价格认知，再用结构化证据解释便宜从哪来；随后主动暴露两个反面事实——成本曲线已在 2021 年触底回升、真正的约束在电网侧；最后推动决策者把注意力和预算从"买便宜组件"转向"买可调度性与并网位置"。说服与决策在先，信息完整性在后 |
| Desired Audience Outcome | 决策者能说出成本下降的因果机制（学习率），能指出成本中心已从组件转移，能解释为什么 2021 年后 LCOE 反而上升，并接受"约束是并网与消纳而非价格"的判断，进而在下一次投资排序中把并网位置与可调度性排在组件价格之前 |
| Core Message / Ask / Action | 光伏已经是多数市场最便宜的新增电源，但它不会自动继续变便宜；决定项目价值的已经不是组件价格，而是并网位置与可调度性 |
| Delivery Context | 主要为有主讲人的 25 分钟决策会现场演示；次要为会后独立阅读的判断备忘 |
| Artifact Afterlife | 作为投资与采购排序讨论的判断依据留存，其数据口径可被直接引用与复核 |
| Reading Mode | balanced |
| Content Strategy | 无用户素材，全部事实来自导入的研究对；口径冲突并列写出，不做平均、不做跨口径换算，缺失数据写 NO DATA |
| Design Style | pyramid × swiss-minimal：结论先行的咨询式论证，配严格瑞士网格、单一强调色与大而准的排版 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 工作流默认（final Stage-2 proactive value `true`，无更晚的显式指令） |
| Custom Animations | enabled — 用户在任务书中显式要求（"自定义动画必须做：Morph ≥ 2 组且有承接物；入场按阅读路径；框架整卷一致"） |
| Narration Audio | disabled — 工作流默认（final Stage-2 proactive value `false`，用户未要求配音） |
| Created Date | 2026-09-04 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上下左右 72px（栅格外边距） |
| Content Area | x 72–1208，y 72–648（1136 × 576） |

## III. Visual Theme

### Theme Style

- **Mode**: pyramid
- **Visual style**: swiss-minimal
- **Theme**: 一张十二列栅格上的成本论证。整卷用同一套模数（12 列 × 84px 列宽 + 24px 沟槽）作为构图骨架，其中两页把栅格线本身画出来当可见结构；每页一个大而准的几何面或一个建筑尺度的数字承担视觉重量，红色只做标点。
- **Tone**: 克制、精确、不留装饰余地；语气是顾问在董事会上给判断，不是科普。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 主画面场，整卷近全白，负空间承担与内容同等的重量 |
| Secondary background | #F2F2F2 | 栅格区块底色，同时充当图表与表格的面板底（本卷不另设 surface 角色，避免两个几乎同值的灰） |
| Primary | #111111 | 近黑：标题、大几何面、主数据系列——瑞士卷里真正的"主色" |
| Accent | #C8102E | 唯一强调色：关键数字、拐点、一条 4px 规则线；用作标点而非装饰 |
| Secondary accent | #6E6E6E | 中灰：对照系列、次级数据、被比较的一方 |
| Body text | #1A1A1A | 正文与标签 |
| Secondary text | #6E6E6E | 注释、来源行、页脚、图注 |
| Divider | #D4D4D4 | 分隔规则线与表格横线 |
| Grid | #E8E8E8 | 图表网格与可见栅格模数线，比 divider 更轻 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 新怪诞体（neo-grotesque）：中性、精确、无衬线，靠字重与尺度拉开层级 | Microsoft YaHei | Arial | sans-serif |
| Body | 同一族的常规字重，小而准 | Microsoft YaHei | Arial | sans-serif |
| Display | 建筑尺度的重量级怪诞体，只承担数字与章节序号 | Arial Black | Arial Black | sans-serif |
| Numeral | 同 Display，用于章节巨大序号 | Arial Black | Arial Black | sans-serif |
| Data | 等高线性数字，保证图表刻度与表格数值可读 | Arial | Arial | sans-serif |

- **Title stack**: `"Microsoft YaHei", Arial, sans-serif`
- **Body stack**: `"Microsoft YaHei", Arial, sans-serif`
- **Display stack**: `"Arial Black", "Microsoft YaHei", sans-serif`
- **Numeral stack**: `"Arial Black", "Microsoft YaHei", sans-serif`
- **Data stack**: `Arial, "Microsoft YaHei", sans-serif`
- **Role rationale**: Display / Numeral 用 Arial Black，因为 swiss-minimal 的"建筑尺度巨大数字"是本卷反复出现的构图骨架（封面对照数、三个章节序号、五处 hero 数字），中性正文族撑不起这个角色；Data 用 Arial 领先，是因为八个原生图表与一张原生表格的刻度、数值与年份全部是拉丁数字，需要等高线性数字而不是 CJK 族的数字形。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 44 |
| Subtitle | 32 |
| Lead | 30 |
| Annotation | 18 |
| Footnote | 16 |
| Display | 96 |
| Numeral | 160 |
| Data | 20 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 每页从左上角的断言标题起读，向下或向右交给一个占版面主导的几何面（图表、表格、巨大数字）；红色标点标出这一页唯一要被记住的数值。
- **Composition tendency**: 非对称分割，内容齐同一条轴；每页恰好一个建筑尺度的元素（大几何面 / 巨大数字 / 满宽图表）；有意留出 40–60% 负空间的页与信息密集页交替。
- **Cross-page continuity**: 标题永远左上齐 x=72；一条 4px 强调色规则线在标题下方复现并按页角色变长度；章节序号用同一 Numeral 角色；页脚来源行永远在 y≈672 左齐。
- **Spacing posture**: 变化：anchor 与 breathing 页大留白，dense 页在栅格内紧凑但不越过沟槽。
- **Spacing anchors**: page margin 72px；block gap 32px；column gutter 24px；corner radius 0px（瑞士方角，圆角为 0 是本卷的身份）；body leading 36px。

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 1.5
- **Brand-logo library**: 无（内容中不出现需要真实品牌标识的公司、产品或服务）

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/solar-panel.svg | 光伏本体、发电侧主题标记 |
| icons/tabler-outline/building-factory-2.svg | 制造、产能、供应链 |
| icons/tabler-outline/battery-3.svg | 储能、电池成本 |
| icons/tabler-outline/plug-connected.svg | 并网、接入、电网连接 |
| icons/tabler-outline/clock.svg | 等待时长、排队、时间成本 |
| icons/tabler-outline/trending-down.svg | 成本下降、价格下行 |
| icons/tabler-outline/trending-up.svg | 成本回升、反向趋势 |
| icons/tabler-outline/alert-triangle.svg | 边界条件、指标免责、反面事实 |
| icons/tabler-outline/link.svg | 来源链接 |
| icons/tabler-outline/arrow-narrow-right.svg | 判断到建议的指向 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P02 | chart | line_chart | 呈现光伏 LCOE 十七年逐年变化与 2021 年拐点 |
| P03 | chart | horizontal_bar_chart | 在同一口径下比较十种新增电源的成本区间 |
| P06 | chart | area_chart | 呈现组件价格随年份塌缩的量级 |
| P09 | chart | stacked_bar_chart | 对比 2010 与 2024 年系统成本的五个分项构成 |
| P10 | chart | line_chart | 呈现储能度电成本 2020–2026 的区间走向 |
| P12 | chart | column_chart | 比较三个年份的并网中位等待时长 |
| P13 | chart | grouped_bar_chart | 比较四个欧洲市场同月负电价小时数的同比变化 |
| P14 | table | comparison_matrix | 对照四家机构 LCOE 口径的地域、补贴、单位与最新值 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页以该页的判断句开场，再用连贯散文补上支撑事实；数字口径（哪一家、哪个地域、含不含补贴、哪一年的美元）在口头讲清楚，页面上未写下的限定条件由讲述补齐；不引入源文以外的事实；百分数与货币按中文口语读法展开
- **Total duration**: 约 25 分钟，15 页平均每页 90–110 秒；anchor 与 breathing 页更短，数据页更长
- **Notes style**: 结论驱动、克制、有权威感——顾问在决策会上给判断的语气
- **Presentation purpose**: 先纠正过时的价格认知并解释成本下降的机制，再主动暴露成本曲线转向与电网侧约束，最后推动决策者把预算从组件价格转向并网位置与可调度性

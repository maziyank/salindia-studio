<!-- ppt-master-schema: design-spec/v1 -->
# 电动车增长的下一站 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 电动车增长的下一站:2026–2028 车企市场优先级决策 |
| Canvas Format | PPT 16:9 (1280 × 720) |
| Page Count | 14 |
| Primary Language | zh-CN |
| Target Audience | 整车企业的高管团队与海外业务/战略负责人;熟悉本国市场,但对各海外市场的真实增速与结构变化只有零散印象 |
| Communication Intent | 先给出判断——全球电动车的增量重心正在从欧美转向新兴市场、PHEV 是低渗透市场的破冰产品——再用 IEA 数据逐条证明,最后请管理层对 2026–2028 的市场优先级与产品组合节奏做出决定 |
| Desired Audience Outcome | 管理层接受"美国停滞、欧洲分化、新兴市场加速"三个事实判断,批准三级市场优先级和 PHEV 先行的产品节奏,并指定本季度要落实的三件事 |
| Core Message / Ask / Action | 2025 年全球电动车 2,100 万辆、渗透率 25%,但增量结构已变:美国销量首次下滑、欧洲靠英德反弹、中国之外的新兴市场增量首次超过欧洲。2026–2028 的增量投入应按"中国深耕、欧洲选点、东南亚/拉美/印度抢滩、美国守势"分级,并以 PHEV 打开低渗透市场 |
| Delivery Context | 以阅读为主的管理层讨论稿:先作为会前预读发出,会上由战略负责人逐页讲解、当场讨论;每页要能独立成立 |
| Artifact Afterlife | 作为决策记录留档,后续可按季度用同口径数据更新;数字与来源要经得起追问 |
| Reading Mode | text(文档密度:正文 14px,咨询文档惯例) |
| Content Strategy | 事实与数值全部来自导入的 IEA 工作簿;结论、分级和路线图由这些数字推导,推导公式写在备注中;不引入工作簿之外的事实 |
| Design Style | 麦肯锡式咨询决策文档:金字塔论证 + 瑞士网格的克制版式,行动标题、编号图表、每页来源行、追踪器与页码 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — workflow default (proactive policy true);备注承载推导公式与讲解口径 |
| Custom Animations | enabled — explicit user instruction(示例库要求每份示例带自定义动画);对象级动画 + Morph 承接 |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-05 |

- **Template Application**: 采用已安装的 mbb-consulting 方法模板(自 consulting-decision 继承论证方法,视觉改为文档密度惯例):答案先行的论证链(总答案 → 关键支撑 → 页面信息 → 证据)、事实/假设/推论/建议四类表述分开、每页一个行动标题;其 swiss-minimal 视觉种子在本项目扩展为咨询文档惯例(见 §III),页面为自由设计的扁平结构,不引入模板原型或原生结构。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上 56 / 下 48 / 左 56 / 右 56 |
| Content Area | x 56–1224,y 56–648;标题区 y 56–120,正文区 y 140–620,页脚(来源行 + 页码)y 656–690 |

## III. Visual Theme

### Theme Style

- **Mode**: pyramid
- **Visual style**: custom
- **Visual Style References**: swiss-minimal
- **Visual Style Behavior**: 白底黑字的咨询决策文档,取文档密度而非演示密度(正文 14px ≈ 10.5pt,与咨询公司 11–12pt 的惯例一致)。每页一个两行以内的行动标题(陈述句,写清"所以呢")顶在页首,标题下一行灰色单位/副题行,再一条深色细横线;右上角追踪器与「讨论稿」贴纸,页脚编号脚注加来源行,右下角页码;正文区左 2/3 并置两到三个证据面板(各自带加粗小标题、单位行、直接标注、CAGR 括注),右 1/3 是「关键信息」编号要点栏,图上用编号圆点 callout 与要点对应;所有面为纯平面,只用发丝线(1px 灰)和留白分隔,不用卡片、圆角、阴影、渐变;色彩只做语义:藏青为主系列与标题,电蓝只标当页要读者看的那一个数字或系列,灰色承担其余;深色满版只出现在封面与章节页;表格是细横线表,数字右对齐、等宽字体;字号层级靠字重与大小,不靠装饰。
- **Theme**: 一份把答案写在标题里的决策文档——读者只读 14 个标题就能复述结论,再往下看是逐页的证据
- **Tone**: 冷静、精确、克制;每一句都可追溯到工作簿里的一个单元格或一个公式

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 页面底色 |
| Secondary background | #F2F2F2 | 附录与表格的隔行底、章节页的浅色分区 |
| Primary | #051C2C | 标题、主系列(中国/全球)、封面与章节页满版 |
| Accent | #2251FF | 当页唯一的强调:被讨论的数字、系列或表格行 |
| Secondary accent | #8FB8FF | 次要系列(欧洲/PHEV 等)与强调色的浅阶 |
| Body text | #333333 | 正文、表格正文 |
| Secondary text | #7F7F7F | 来源行、页码、追踪器、轴标签、注释 |
| Divider | #B7B7B7 | 标题下横线、表格表头线 |
| Grid | #E3E3E3 | 图表网格线、表格隔行线 |
| Surface | #F7F7F7 | 图表底板、结论框(仅作面,无边框) |
| Negative | #B3261E | 下滑/风险的唯一警示色(美国销量下滑、风险触发) |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 无衬线 / 粗体,行动标题的权威感 | Microsoft YaHei | Arial | sans-serif |
| Body | 无衬线 / 常规,紧凑可读 | Microsoft YaHei | Arial | sans-serif |
| Data | 无衬线 / 等高数字,右对齐对位 | Arial | Arial | sans-serif |

- **Title stack**: Microsoft YaHei
- **Body stack**: Microsoft YaHei
- **Data stack**: Arial
- **Role rationale**: `data` 用于图表数值、轴标签、表格数字列和英雄数字,Arial 的等高数字在右对齐列里对位整齐;中文标签仍用 Body。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 14 |
| Title | 24 |
| Subtitle | 14 |
| Lead | 16 |
| Annotation | 12 |
| Footnote | 10 |
| Display | 40 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 先读行动标题,再读被电蓝标出的那个数字或系列,最后读图表其余部分与来源行
- **Composition tendency**: 标题区固定在页首;正文区一到三个证据区块沿 12 列网格横向排布,图表占大区块、结论要点占窄栏;结论与建议页用编号列表占满宽度
- **Cross-page continuity**: 追踪器、标题下横线、来源行、页码四件固定;图表编号连续;区域配色固定(中国藏青、欧洲次蓝、美国灰、新兴市场电蓝);Morph 承接:P03 的全球柱承接到 P04 的分区堆叠柱,P07 的新兴市场柱承接到 P10 的优先级表首行
- **Spacing posture**: 证据页 dense,结论与建议页 breathing,封面/章节/附录 anchor
- **Spacing anchors**: 页边距 48;区块间距 20;栏间距 24;圆角 0;正文行距 20

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | chart | dual_axis_line_chart | 2015–2025 全球电动车销量(柱,左轴)与渗透率(线,右轴) |
| P04 | chart | stacked_bar_chart | 2020–2025 全球销量按中国/欧洲/美国/其他堆叠 |
| P05 | chart | line_chart | 2019–2025 美国、日本、欧洲渗透率走势 |
| P06 | chart | horizontal_bar_chart | 2025 年欧洲主要国家渗透率及两年变化 |
| P07 | chart | grouped_bar_chart | 新兴市场 2023 vs 2025 渗透率对比 |
| P08 | chart | stacked_area_chart | 2019–2025 全球 BEV 与 PHEV 销量堆叠 |
| P09 | chart | waterfall_chart | 2025→2035 STEPS 情景增量按地区分解 |
| P10 | table | comparison_matrix | 市场三级优先级:各市场 2025 销量、渗透率、2035 情景、进入方式 |
| P12 | table | record_table | 风险登记:风险、触发指标、影响、应对 |
| P14 | table | metric_table | 附录:各地区 2020–2025 销量与渗透率 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页备注写三段:这页要读者记住的一句话;页面上每个计算值的公式与源表位置(sheet/行/列);讲解时的过渡语。事实只引用工作簿,不补充外部信息
- **Total duration**: 20 分钟(14 页,证据页各 1.5 分钟,结论与建议页各 2 分钟)
- **Notes style**: formal
- **Presentation purpose**: 先给出判断再逐条证明,最后请管理层对 2026–2028 的市场优先级与产品组合节奏做出决定

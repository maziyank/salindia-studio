<!-- ppt-master-schema: design-spec/v1 -->
# Apple FY2025 经营复盘 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | apple_fy2025_review |
| Canvas Format | ppt169 (1280×720) |
| Page Count | 14 |
| Primary Language | zh-CN |
| Target Audience | 苹果管理层与机构投资者;已经熟悉业务与分部口径,不需要重新介绍公司 |
| Communication Intent | 先给出 FY2025 的整体结论,再逐项解释每一处重大变化的来源;把两处结构性收缩放在与增长同等的位置上暴露出来;最后交出三个必须由管理层回答的问题。报告与暴露风险优先,决策请求排在最后 |
| Desired Audience Outcome | 读完能说出 FY2025 增长的真实来源(服务贡献了 51.7% 的收入增量、77.6% 的毛利增量)、能指出净利润 +19.5% 中的基数效应、能定位大中华区与可穿戴两处收缩,并对三个未决问题各自有判断 |
| Core Message / Ask / Action | FY2025 总量健康(收入 416,161 百万美元,+6.43%),质量确有提升(毛利率 46.91%),但增长与毛利同时向服务集中,而风险集中在大中华区与可穿戴两个可定位的地方;净利润 +19.5% 中相当部分是 FY24 一次性税项造成的基数效应,剔除后为 +7.72% |
| Delivery Context | 管理层经营复盘会,主讲人带读为主;会后作为可离线阅读的留存文档分发 |
| Artifact Afterlife | 审阅、存档,并作为后续季度复盘沿用同一页面形状的基线 |
| Reading Mode | balanced |
| Content Strategy | 忠实于两个源文件,不引入外部事实;所有比率、增速、占比均由源表数字两三步算出并在 notes 中写明公式;源表未覆盖的因果一律标注"现有口径无法判定" |
| Design Style | 账页式数据复盘:中性纸白场、发丝细线栅格、等宽表格数字、状态色只编码状态 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 工作流默认(final Stage-2 proactive policy 保持默认 true) |
| Custom Animations | enabled — 用户明确要求 animations.json 必写、Morph ≥2 对 |
| Narration Audio | disabled — 工作流默认;用户未要求配音 |
| Created Date | 2026-09-05 |

- **Template Application**: 挂用 operating-review Style 方法模板,只取其 Direction / method 段:采用"结果 → 偏差 → 原因 → 承诺"的复盘骨架、按位置阅读的固定区域(状态区 / 数字区 / 说明区)、变化量优先于原值的页面纪律、以及"漏项与达成同等醒目、口径不可追溯就写明未定"的措辞纪律;表格采用固定列契约(本期 / 上期 / 变化 / 变化率),图表在变化是重点处画出比较基线。身份层(色彩、字体、图标)由本项目自行决定,模板的 Fallback 配色仅作为状态映射的起点并按 WCAG AA 收紧。本项目没有"计划值",一律以上年同期为比较基准并在每页标明;模板要求的责任人与日期在源数据中不存在,因此"纠正行动"页降级为"待回答问题"页,不虚构 owner 与 date。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | ppt169 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上下左右 64px |
| Content Area | x 64–1216,y 64–656(1152 × 592) |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: briefing, pyramid
- **Mode Behavior**: 用简报的方式开场——直接给出本期结果,不复述受众已有的背景;随后对每一处重大变化用金字塔方式收口:偏差是什么、哪一个原因解释了它的大部分、证据在哪、还剩什么没定论。深度跟随重要性而非版面对称:平稳的指标一行带过,移动了的指标给完整链条。页面形状跨期保持稳定,让返场受众直接比较而不是重新认路。
- **Visual style**: custom
- **Visual Style References**: data-journalism, swiss-minimal
- **Visual Style Behavior**: 账页式栅格。纸白场上用发丝细线(而非卡片与阴影)划分区域,分栏与基线严格对齐,页面像一张可以逐格审计的账页;每页固定三个区域——顶部断言句、中部数字/图表主体、底部来源与口径行——位置跨页不变。装饰为零:没有渐变、发光、圆角 KPI 卡与仪表盘外壳,状态只由色 + 形/标签双重编码。数字全部走等宽字族并右对齐,列与列之间靠对齐而不是容器分组。留白用于把"结果"与"解释"分开,而不是用于稀释密度。
- **Theme**: 一份可审计的年度账页——每一个数字都能指回源表的某一行某一列
- **Tone**: 克制、直述、不软化坏数字

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 全部页面的中性纸白场 |
| Secondary background | #F4F6F8 | 表格分组带、记分卡单元格、区域底衬 |
| Primary | #1E293B | 主文字、标题、发丝线与主数字 |
| Accent | #2B6CB0 | 当前讨论中的指标或驱动因子(焦点色) |
| Secondary accent | #2E7D5B | 达成/改善状态(on plan) |
| Body text | #1E293B | 正文 |
| Secondary text | #64748B | 注释、脚注、来源行、坐标轴标签 |
| Divider | #D8DEE6 | 区域分隔发丝线与表格横线 |

补充的复用语义角色(与上表同为 deck 级锚点,投影进 spec_lock):

| Role | HEX | Purpose |
| --- | --- | --- |
| Surface | #F4F6F8 | 与 Secondary background 同值,用作面板抬升 |
| Grid | #E8EDF2 | 图表网格线,比 Divider 更浅 |
| Positive | #2E7D5B | 改善/增长(与 Secondary accent 同值) |
| Warning | #8A5A12 | 观察项;由模板 Fallback 的 #B7791F 压暗到白底 5.76:1 以满足 AA |
| Negative | #B4342C | 收缩/下滑;固定映射到大中华区与可穿戴两条收缩序列 |
| Series alt | #7BA7D4 | 分类编码用的第二蓝,由 Accent 派生,仅用于多序列图表 |

状态映射全卷固定:改善 = Positive + 向上三角 + `+` 号;观察 = Warning + 空心方块;收缩 = Negative + 向下三角 + `−` 号。色永远与形状或符号成对出现,灰度打印仍可读。

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 紧凑中性无衬线,靠字重与对齐拉层级 | Microsoft YaHei | Microsoft YaHei | 无 |
| Body | 同族,正文中性 | Microsoft YaHei | Microsoft YaHei | 无 |
| Data | 真等宽,表格数字等宽等高,列可逐位对齐 | Consolas | Consolas | 无 |
| KPI hero | 大号数字,与 Data 同族以保证与表内数字一致 | Consolas | Consolas | 无 |

- **Title stack**: `Microsoft YaHei`
- **Body stack**: `Microsoft YaHei`
- **Data stack**: `Consolas`
- **KPI hero stack**: `Consolas`
- **Role rationale**: 标题与正文同族是 operating-review §V Typography Character 的明确要求(用一套紧凑中性无衬线,层级由字重和对齐产生而非容器);第二个族 `Data` 单独存在,是因为本卷有 9 个原生数据对象、上百个需要逐位对齐的数字,`Consolas` 提供真正的等宽表格数字。中文标签一律走 Body 族,`Data` 族只承载数字、百分号、货币符号与拉丁缩写。两个族均写单一具体名,不写逗号栈。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 44 |
| Subtitle | 30 |
| Annotation | 18 |
| Cover title | 72 |
| Lead | 28 |
| KPI hero | 64 |
| Data | 24 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 自上而下——顶部断言句先落地结论,中部把支撑它的那个数字放到最大,底部给口径与来源;横向上把"变化量"放在比"原值"更靠左或更大的位置。
- **Composition tendency**: 每页一个主导事实 + 一组可审计的支撑数字;图表占据中部主区并自带比较基线,说明文字沿右侧或下方成窄栏。
- **Cross-page continuity**: 顶部断言句带、底部来源行、状态色映射三者跨页不变;大中华区色块与"416,161"这两个承接物在相邻页之间保持同一形状与颜色。
- **Spacing posture**: variable by page rhythm——记分卡与问题页 breathing,图表与明细页 dense,封面与结论页 anchor。
- **Spacing anchors**: 页边距 64px;区块间距 32px;分栏栏距 24px;圆角半径 0px;正文行高 1.55。

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2
- **Brand-logo library**: simple-icons(仅用于 Apple 自身的品牌标记)

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-outline/trending-up | 改善方向标记 |
| tabler-outline/trending-down | 收缩方向标记 |
| tabler-outline/chart-bar | 数据/图表区域的类目提示 |
| tabler-outline/world | 地区分部相关页 |
| tabler-outline/device-mobile | 硬件品类相关页 |
| tabler-outline/cloud | 服务业务相关页 |
| tabler-outline/coin | 盈利与税项相关页 |
| tabler-outline/alert-triangle | 观察项与待回答问题 |
| tabler-outline/target | 结论与行动含义 |
| tabler-outline/file-text | 来源与口径 |
| tabler-outline/link | 外部链接标记 |
| tabler-outline/calendar-stats | 季度节奏与季节性 |
| simple-icons/apple | 封面与页脚的公司标记 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P02 | table | metric_table | 用固定列契约(FY2025 / FY2024 / 变化 / 变化率)一次给出全年九项核心指标的本期standing |
| P03 | chart | waterfall_chart | 把收入总增量分解为产品与服务两项贡献,并让首尾值合拢到源表合计 |
| P04 | chart | column_chart | 展示八个季度净销售额的绝对水平与 Q1 峰值节奏 |
| P05 | chart | column_chart | 服务净销售额八个季度柱序列,FY25 柱标同比,证明增长连续而非一次性 |
| P05 | chart | line_chart | 服务与产品季度毛利率双线,量级差距一眼可见 |
| P05 | chart | stacked_bar_chart | 收入增量与毛利增量两条 100% 条,给出服务在增量中的占比 |
| P06 | chart | grouped_bar_chart | 五个品类 FY2025 与 FY2024 并置比较,暴露唯一收缩项 |
| P07 | chart | stacked_bar_chart | 八个季度五地区的构成与总量同时可读 |
| P08 | chart | line_chart | 大中华区八个季度的走向,判断是方向还是波动 |
| P09 | table | comparison_matrix | 指标 × 八个季度的损益摘要,让率值跨期逐列对比 |
| P11 | chart | line_chart | 研发与销管两条费率线跨八个季度的相对走向 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

本卷 `image_usage: none`。用户明确要求不做 AI 生图、不搜网图;证据全部是数字,没有任何页面把一个真实主体、场地、产品或现场状态当作证据来呈现,因此没有一行图像资源需要准备。装饰性题字候选同样为零——用户的"不做 AI 生图"是显式禁止,该规则不激活。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页 notes 交代三件事——这一页确立了什么、页面上每个计算值的公式与中间数(例如"服务占增量 = 12,989 ÷ 25,126 = 51.7%")、以及这一页的数字取自哪个 sheet 的哪一行。凡是源表无法支撑的因果,notes 里明确写"现有口径无法判定"。不复述页面文字。
- **Total duration**: 约 18–22 分钟(14 页,平均每页 80–95 秒)
- **Notes style**: formal
- **Presentation purpose**: 先给出 FY2025 的整体结论,再逐项解释每一处重大变化的来源;把两处结构性收缩暴露出来;最后交出三个必须由管理层回答的问题

<!-- ppt-master-schema: design-spec/v1 -->
# nbs_2025_communique_briefing - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | nbs_2025_communique_briefing |
| Canvas Format | ppt169 (1280 × 720) |
| Page Count | 17 |
| Primary Language | zh-CN |
| Target Audience | 没有统计学背景、希望在 15 分钟内看懂"2025 年中国经济长什么样"的普通读者；他们熟悉新闻里的 GDP、就业、房价等词，但不清楚这些数字的量级、口径和相互关系 |
| Communication Intent | 先报告与说明：把《2025 年国民经济和社会发展统计公报》的官方数字按"总量与结构 → 人口与人 → 需求三面 → 外部与能源 → 创新与民生"的顺序摊开，让读者建立坐标系；再让读者自己判断走向，不代替读者下结论 |
| Desired Audience Outcome | 读完后能说出 2025 年中国经济的 5 个关键数字（GDP 总量与增速、人口总量与变动、城镇化率、居民收入、进出口规模）和 3 条主要走向（增长逐季回落但全年达 5.0%、人口继续负增长而城镇化仍在推进、投资收缩而消费与外贸顶住） |
| Core Message / Ask / Action | 2025 年中国经济总量 1401879 亿元、比上年增长 5.0%；在人口减少 339 万人、固定资产投资下降 3.8% 的同时，消费、外贸和新质生产力共同支撑了这个增速 |
| Delivery Context | 读者主导的自读简报，屏幕阅读为主；可在会议前作为快速铺垫材料被人翻阅，无现场讲解人 |
| Artifact Afterlife | 存档与转发；每个数字都要能回溯到公报原文，最后一页给出官方来源链接 |
| Reading Mode | balanced |
| Content Strategy | 贴近源：所有数值、口径、单位与公报完全一致，不改写、不换算、不推算；公报没有的数字标注 NO DATA。页面结构可自由重组，把公报的十二个章节重排为读者视角的叙述顺序 |
| Design Style | 数据新闻简报：出版级信息密度 + 中性陈述语气；宋体标题承担权威感，无衬线正文与衬线数字承担精度，图表是版面的脊椎 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy |
| Custom Animations | enabled — explicit user instruction (至少 2 对 Morph + entrance 家族入场) |
| Narration Audio | disabled — final Stage-2 proactive policy |
| Created Date | 2026-09-04 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | ppt169 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上 56 / 下 52 / 左右 64 |
| Content Area | x 64–1216，y 56–668（可用宽 1152，可用高 612） |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: briefing
- **Mode Behavior**: 中性、完整、可扫读。页标题写主题而不写论断（"三次产业：结构与贡献"，不是"服务业撑起了增长"）；每页 core message 说这一页铺开了什么，而不是证明了什么。同级事实等权呈现，只有公报本身把某个数字单列时才让它变大。章节按读者视角分组并给出组标签，顺序可预期。全篇不制造转折、不设悬念、不替读者下结论；唯一的例外是封面钩子和结尾要点，它们复述而非新增判断。
- **Visual style**: custom
- **Visual Style References**: data-journalism
- **Visual Style Behavior**: 出版级密度。多栏栅格承载图表与数据表，图表是页面的脊椎——版面绕着可视化排，而不是把图表装进卡片盒子里；发丝分隔线代替重卡片，整幅横贯的规则线落进统计带；侧栏切进栅格承载口径与注释；小倍数条带代替单个大图。装饰只有一条强调规则线和克制的标注。数字按含义着色（升 / 降 / 焦点），图表用同族色阶而非彩虹。整体平面，无发光、无装饰阴影。
- **Theme**: 官方统计公报的纸面出版感——暖白纸底、深墨蓝正文、砖红标记关键与下行、深绿标记上行；每页右下角一条细的来源脚注线构成跨页母题。
- **Tone**: 冷静、克制、可核查。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F4F1EA | 暖白出版纸底，全页大面积场 |
| Secondary background | #FFFFFF | 数据表、侧栏、统计带的抬起面 |
| Primary | #123B57 | 深墨蓝：标题、图表主系列、正文强调 |
| Accent | #C0392B | 砖红：关键数字、下行与收缩值、单一强调规则线 |
| Secondary accent | #2E6F4E | 深绿：上行值、第二数据系列 |
| Body text | #1F2A30 | 正文与表格文字 |
| Secondary text | #5F6B72 | 说明、坐标轴标签、图注 |
| Divider | #CFC7B8 | 发丝分隔线、表格行线、页面规则线 |
| Surface | #FFFFFF | 面板抬起（与 Secondary background 同值，语义不同：surface 用于图表底板） |
| Grid | #E4DED0 | 图表网格线，比分隔线更淡 |
| Positive | #2E6F4E | 增长、改善方向的语义色 |
| Warning | #C98B2E | 中性偏关注的量（持平、口径调整） |
| Negative | #C0392B | 下降、收缩方向的语义色 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 衬线 / 出版权威 | SimSun | Times New Roman | 无 |
| Body | 无衬线 / 屏幕精度 | Microsoft YaHei | Segoe UI | 无 |
| Display | 衬线等高数字 / 统计刊物的英雄数 | Times New Roman | Times New Roman | 无 |
| Data | 无衬线等高数字 / 表格与坐标轴数值对齐 | Arial | Arial | 无 |
| Annotation | 无衬线 / 小字说明 | Microsoft YaHei | Segoe UI | 无 |
| Footnote | 无衬线 / 来源行 | Microsoft YaHei | Segoe UI | 无 |

- **Title stack**: SimSun
- **Body stack**: Microsoft YaHei
- **Display stack**: Times New Roman
- **Data stack**: Arial
- **Annotation stack**: Microsoft YaHei
- **Footnote stack**: Microsoft YaHei
- **Role rationale**: Display 与 Data 离开正文族，因为全篇 10 张图表 + 3 张数据表 + 每页英雄数都是纯数字串：英雄数用 Times New Roman 保留衬线权威感，表格与坐标轴用 Arial；两者都是等高（lining）数字，Georgia 的旧式数字高低不齐、读数费劲，已弃用；两者尺寸差 3 倍以上，各自需要独立锚点。Data 角色只承载纯数字与拉丁标签，含中文的标签走 Annotation。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 42 |
| Subtitle | 32 |
| Annotation | 18 |
| Cover title | 84 |
| Display (hero number) | 72 |
| Lead | 30 |
| Data | 20 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 左上角标题与主题标签先落地，视线沿栅格向右下走到可视化主体，末端收在右下角来源脚注行。
- **Composition tendency**: 图表作脊椎——先定可视化占据的主栏，再让文字沿它的边缘排；英雄数按整栏尺度放；横贯规则线把页面切成上部叙述带与下部统计带；侧栏切进栅格承载口径。
- **Cross-page continuity**: 右下角来源脚注线每页复现；左上角主题标签（一产/人口/消费…）保持同一位置与字号；深墨蓝主系列、砖红关键值在全篇稳定。
- **Spacing posture**: 偏密，但由栅格约束；导读页与要点页给出呼吸。
- **Spacing anchors**: 页边距 64px、块间距 32px、栏间距 24px、圆角 0px、正文行高 36px。

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/chart-bar.svg | |
| icons/tabler-outline/chart-line.svg | |
| icons/tabler-outline/chart-pie.svg | |
| icons/tabler-outline/building-factory-2.svg | |
| icons/tabler-outline/plant-2.svg | |
| icons/tabler-outline/building-store.svg | |
| icons/tabler-outline/users.svg | |
| icons/tabler-outline/home.svg | |
| icons/tabler-outline/briefcase.svg | |
| icons/tabler-outline/coin.svg | |
| icons/tabler-outline/shopping-cart.svg | |
| icons/tabler-outline/building-bridge-2.svg | |
| icons/tabler-outline/ship.svg | |
| icons/tabler-outline/world.svg | |
| icons/tabler-outline/bolt.svg | |
| icons/tabler-outline/leaf.svg | |
| icons/tabler-outline/bulb.svg | |
| icons/tabler-outline/cpu.svg | |
| icons/tabler-outline/school.svg | |
| icons/tabler-outline/heartbeat.svg | |
| icons/tabler-outline/shield-check.svg | |
| icons/tabler-outline/file-text.svg | |
| icons/tabler-outline/link.svg | |
| icons/tabler-outline/trending-up.svg | |
| icons/tabler-outline/trending-down.svg | |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | chart | line_chart | 四个季度 GDP 同比增速沿时间轴的走向 |
| P04 | chart | donut_chart | 三次产业增加值占国内生产总值的份额 |
| P05 | chart | waterfall_chart | 三大需求各自拉动的百分点如何累加成 5.0% |
| P06 | table | hierarchical_table | 年末人口总量按城乡、性别、年龄逐层分解 |
| P07 | chart | column_chart | 出生人口与死亡人口的绝对量对比 |
| P08 | chart | horizontal_bar_chart | 全国居民五等份收入分组的人均可支配收入排序 |
| P09 | chart | stacked_bar_chart | 社会消费品零售总额按消费类型与经营地的两种拆分 |
| P10 | chart | horizontal_bar_chart | 分行业固定资产投资增速的正负分布 |
| P11 | chart | grouped_bar_chart | 出口额与进口额在四类贸易口径上的并置 |
| P12 | table | metric_table | 主要国家和地区的出口额、进口额及其增速与比重 |
| P13 | chart | pie_chart | 全年发电量按电源类型的构成 |
| P14 | chart | column_chart | 新质生产力相关行业与产品的增速排序 |
| P15 | table | metric_table | 五项社会保险年末参保人数及其比上年增量 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页一段平实读出：先说这一页摊开了什么，再把页面上的数字按顺序念一遍，最后交代口径限制。数字与页面完全一致，不得四舍五入、不得换算、不得补充公报以外的事实；标注 NO DATA 的页面在注释里说明为什么不给这个数。
- **Total duration**: 约 15 分钟（17 页，平均每页 50 秒左右）
- **Notes style**: formal
- **Presentation purpose**: 先报告与说明公报的官方数字，让读者建立坐标系并自行判断走向

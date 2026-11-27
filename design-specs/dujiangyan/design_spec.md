<!-- ppt-master-schema: design-spec/v1 -->
# dujiangyan_zh_sparse - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | dujiangyan_zh_sparse |
| Canvas Format | ppt169 (1280×720) |
| Page Count | 14 |
| Primary Language | zh-CN |
| Target Audience | 对都江堰只有"课本印象"的一般成年读者与高中/大学通识听众：知道它古老、知道它在四川，但说不清三大工程各自做什么、也不知道它今天还在运行 |
| Communication Intent | 先解释机制（三大主体工程如何分水、排沙、引水），再说明它为何能运行两千余年（治水口诀与岁修制度），最后用今天的灌区数据回收"它还在上班"这个判断；解释优先于赞叹 |
| Desired Audience Outcome | 听众能用自己的话说出鱼嘴、飞沙堰、宝瓶口各自做什么、三者如何配合，并能举出一个今天仍在运行的具体数字 |
| Core Message / Ask / Action | 都江堰不是一处古迹，而是一套仍在运行的系统：它靠"顺着水势布置"的三级分工和写进制度的岁修，把公元前 256 年的方案一直用到今天 |
| Delivery Context | 主要为有主讲人的现场科普讲解，约 15–18 分钟；次要为讲后自行翻阅的电子稿 |
| Artifact Afterlife | 作为科普/通识讲解材料留存与重复使用，可被他人直接拿去讲 |
| Reading Mode | balanced |
| Content Strategy | 用户未提出任何材料取舍要求（`content_divergence` 留空），按 balanced 默认处理：事实全部来自 `sources/dujiangyan_research.facts.json`，叙述结构由本卷自建并在页面上标注"整理" |
| Design Style | 方向 B「工程图纸」— 深色蓝图纸 × 数据出版：以工程制图的细线、引线、尺寸标注作为版面语言，数据页按新闻信息图的栅格排布 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 流程默认（用户未表态，最终 Stage 2 主动值取默认 `true`） |
| Custom Animations | enabled — 本轮执行任务书的硬性要求（dogfood 框架要求，非用户要求；流程默认本应为 `disabled`） |
| Narration Audio | disabled — 流程默认（用户未表态，最终 Stage 2 主动值取默认 `false`） |
| Created Date | 2026-09-12 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | ppt169 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上下 56 px，左右 72 px |
| Content Area | x: 72–1208，y: 56–664 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional, narrative
- **Mode Behavior**: 以"问题 → 机制拆解 → 机制合拢 → 制度 → 今天"的教学序列推进：先立成都平原涝旱并存的矛盾（narrative 的张力开场），再用三页并列拆解鱼嘴／飞沙堰／宝瓶口（instructional 的概念分解），随即把三件放回同一张总图讲一次洪水中的动作顺序（合拢），最后由治水口诀与岁修制度过渡到今天的灌区数字收束开篇的矛盾。每页标题写成一句可复述的机制判断，不写名词标签。
- **Visual style**: custom
- **Visual Style References**: blueprint, data-journalism
- **Visual Style Behavior**: 版面即图纸——深色蓝图纸底，全部结构用单一线色的细线框、引线、尺寸括号与极淡的底纹网格构成，几乎不用实心色块与圆角；原理页让示意图本身充当版式骨架，文字挂在引线端点上，角落留一个图纸标题栏（页码／页名／来源）。数据页换成 data-journalism 的多栏栅格：发丝分隔线、等宽数字、超大英雄数字、页脚来源行，图表是版面的脊柱而不是被框住的插图。全卷只有一个暖色重点色，用来标"当前正在讲的那一件"，其余一律保持低调线条。
- **Theme**: 工程图纸上的活体系统——把两千年的水工原理当成一份仍在使用的施工图来读
- **Tone**: 克制、精确、可复述；不抒情、不用"奇迹/智慧结晶"一类赞叹句撑场

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #0B1B2E | 蓝图纸深底，全卷页面底色 |
| Secondary background | #11263D | 次级区块、侧栏、表格带状底 |
| Primary | #4A90C2 | 图纸线色：所有示意图线框、连接线、分隔线与结构线 |
| Accent | #E8A33D | 唯一暖色重点：当前讲解对象、关键数字、关键路径高亮 |
| Secondary accent | #7FD1C3 | 第二数据系列与对照项（外江／洪水期一侧） |
| Body text | #D6E4F0 | 正文与主要标签 |
| Secondary text | #93AEC8 | 注记、图例、来源行、次级说明 |
| Divider | #1E3A57 | 发丝分隔线、表格框线、栅格边界 |
| Surface | #16314C | 面板抬升：数据页卡片与侧栏面板 |
| Grid | #17304A | 图纸底纹网格线（比 Divider 更弱） |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 刚直黑体：中国工程图纸标题栏的字面性格，端正、笔画等粗、无修饰 | SimHei | Consolas | sans-serif |
| Body | 人文无衬线，深底上笔画稳定不糊 | Microsoft YaHei | Consolas | sans-serif |
| Display | 与标题同族，用于超大英雄数字与章节数字，拉丁数字走等宽以对齐 | SimHei | Consolas | sans-serif |
| Annotation | 与正文同族的小号注记，图例／引线标签／图表刻度 | Microsoft YaHei | Consolas | sans-serif |
| Footnote | 与正文同族的最小号，来源行与页码 | Microsoft YaHei | Consolas | sans-serif |
| Lead | 与正文同族的导语，页面首段判断句 | Microsoft YaHei | Consolas | sans-serif |

- **Title stack**: SimHei, Consolas, sans-serif
- **Body stack**: Microsoft YaHei, Consolas, sans-serif
- **Display stack**: SimHei, Consolas, sans-serif
- **Annotation stack**: Microsoft YaHei, Consolas, sans-serif
- **Footnote stack**: Microsoft YaHei, Consolas, sans-serif
- **Lead stack**: Microsoft YaHei, Consolas, sans-serif
- **Role rationale**: Display／Annotation／Footnote／Lead 四个角色在全卷反复出现（英雄数字 5 页、引线注记 6 页、来源行 14 页、导语句 9 页），各自需要一个固定锚点，不依赖执行期的显示例外；四者不引入新字体族，只固定字号与栈。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 42 |
| Subtitle | 32 |
| Annotation | 18 |
| Cover title | 88 |
| Chapter title | 56 |
| Lead | 30 |
| Display | 72 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 先读左上角的判断句标题，再进入画面中部的图纸主体，最后沿引线落到右侧或下方的注记与数字；来源行始终在页脚最后被读到
- **Composition tendency**: 原理页让示意图占据整页并充当骨架，文字挂在引线端点；数据页改用多栏栅格，图表横跨主栏、注记退到侧栏；章节与结语页让大留白与一条贯通的水平基线承担全部结构
- **Cross-page continuity**: 岷江水道的那条带状轮廓是全卷母题——封面、总图、三张原理页、合拢页反复出现同一条河道轮廓，只改变取景与高亮位置；角落的图纸标题栏（页码／页名／来源）逐页保留
- **Spacing posture**: variable by page rhythm — 原理页与数据页偏紧凑，章节与口诀页大幅留白
- **Spacing anchors**: page margin 72 px；block gap 32 px；column gutter 40 px；corner radius 2 px；body leading 38 px

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/droplet.svg | 水量、供水、用水口径 |
| icons/tabler-outline/mountain.svg | 玉垒山、出山口、地形落差 |
| icons/tabler-outline/arrows-split.svg | 分水、内外江分流 |
| icons/tabler-outline/ripple.svg | 弯道环流、水面 |
| icons/tabler-outline/ruler-measure.svg | 尺寸、水则、堰高口宽 |
| icons/tabler-outline/calendar-repeat.svg | 岁修、年度重复的维护动作 |
| icons/tabler-outline/award.svg | 世界遗产、名录 |
| icons/tabler-outline/wheat.svg | 灌溉农田、水稻、粮食产能 |
| icons/tabler-outline/alert-triangle.svg | 洪灾、旱情、风险 |
| icons/tabler-outline/chart-line.svg | 趋势、历史演变 |
| icons/tabler-outline/map-pin.svg | 地点、覆盖市县 |
| icons/tabler-outline/topology-star.svg | 渠系网络、灌区结构 |
| icons/tabler-outline/wave-sine.svg | 水流、流量变化 |
| icons/tabler-outline/history.svg | 年代、时间线 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P05 | chart | stacked_bar_chart | 对比枯水期与洪水期内江／外江的分水比例 |
| P11 | chart | line_chart | 展示灌溉面积在选定里程碑年份上的增长 |
| P12 | table | record_table | 列出灌区渠系分级的条数与长度 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dujiangyan_weir_aerial.jpg | 1280×720 | 16:9 | 封面的实地锚点：让读者先确认这是一处真实存在、今天仍在运转的场所 | Photo | 满幅铺底，压暗后让标题落在江面较暗的一侧，河道走向与全卷的水道母题对齐 | adaptive | web | Sourced | 都江堰渠首鱼嘴分水处的俯瞰实景，岷江被分为内外两江的河道形态清晰可辨；白天、无人物特写；画面一侧留出较暗的安静区以承载标题 | none | hero_page |
| dujiangyan_channel_scene.jpg | 1280×720 | 16:9 | 口诀页的呼吸面：把六字诀放回真实的河道与堰体上 | Photo | 满幅铺底并整体压暗，引言文字居中悬浮，画面本身不承担信息 | adaptive | web | Sourced | 都江堰渠首堰体或内江渠道的地面实景，可见卵石河床与堰体线条；构图平静、中部留白，便于叠加引言 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页备注以该页最终 SVG 上真实存在的元素为准展开：先给主讲人一句过渡，再解释页面上的图形在说什么，最后补充页面没有写下的背景（如"无坝引水"为何区别于拦河坝、四六分水为何随水位自动改变）。所有外部事实只引用 `sources/dujiangyan_research.facts.json` 中已有的 fact_id，不引入新数字；自建框架页在备注中明确说明"这一分段是整理出来的讲解顺序，不是史料原有分法"。
- **Total duration**: 15–18 分钟（14 页，平均每页约 70 秒）
- **Notes style**: 讲解式口语，短句为主，可直接照读
- **Presentation purpose**: 先解释三大主体工程如何分水、排沙、引水，再说明它为何能运行两千余年，最后用今天的灌区数据收束"它还在运行"这一判断

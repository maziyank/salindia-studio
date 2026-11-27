<!-- ppt-master-schema: design-spec/v1 -->
# sanxingdui_kiosk_zh_ppt169_20260917 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | sanxingdui_kiosk_zh_ppt169_20260917 |
| Canvas Format | PPT 16:9（1280×720） |
| Page Count | 16 |
| Primary Language | zh-CN |
| Target Audience | 三星堆博物馆展厅入口的现场观众，以散客、亲子家庭与初次到访者为主；站在触摸屏前自己用手指点选，单次停留约 1–3 分钟，对三星堆多半只听过「青铜面具」这类印象词，不了解坑号、年代与展区结构 |
| Communication Intent | 先让观众在十秒内看懂全馆分几个展区、可以先看什么；再对每件重点文物交代「年代—坑号—尺寸—看点」四件事；最后把参观实务（开放时间、票价、预约、官网）交到观众手里。顺序固定：导航优先于内容，内容优先于实务 |
| Desired Audience Outcome | 观众能自己点到想看的展区，能复述至少一件文物的一个具体数字与一个看点，并知道当日开放信息该去哪儿查 |
| Core Message / Ask / Action | 三星堆不是一堆零散的「怪器物」——它是商代晚期一处古蜀都城的祭祀现场，每件重器都能落到确切的坑号、年代与尺寸上 |
| Delivery Context | 主要用途为展厅入口触摸屏自助浏览，无讲解员、无遥控器，观众只通过屏幕上的按钮导航；次要用途为工作人员在平板上快速答疑 |
| Artifact Afterlife | 现场长期循环使用；馆方按当日公告自行更新参观信息页，其余页面保持稳定 |
| Reading Mode | balanced |
| Content Strategy | 事实一律照录来源口径，不做推算、不取整、不合并单位；凡研究底稿标注口径冲突的数字（新馆开放日、大立人通高、金杖重量、新坑文物总量），页面上必须择一并在同页标出来源与年份；自建的归纳框架（时间线、文物目录、速查表）标「整理」二字 |
| Design Style | 方向 0「青铜夜展」：深场金光——以近黑墨绿为底，黄金与青铜锈两色承担全部注意力，几何精准、装饰克制，文物照片浮在暗场上 |
| AI Image Acquisition Path | 不适用（未选择 AI 图像来源） |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 最终 Stage-2 主动策略（proactive_speaker_notes: true）；触摸屏无讲解员，备注用于馆方培训与平板答疑 |
| Custom Animations | enabled — 最终 Stage-2 主动策略（proactive_custom_animations: true）；用户原话「要有动画」为显式指令，且本卷相邻页共享同一心智地图，适合用可见状态延续 |
| Narration Audio | disabled — 最终 Stage-2 主动策略（proactive_narration_audio: false）；展厅公共空间不外放音频 |
| Created Date | 2026-09-17 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上下左右各 64 px；底部导航条占用 y=624..704，正文内容不进入该带 |
| Content Area | x=64..1216，y=64..608（宽 1152、高 544） |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional
- **Mode Behavior**: 以 instructional 的「拆解后排序」为唯一骨架，改造成触摸屏的菜单式讲解：首页把全卷拆成四个可点入口并给出每条路径的长度预期；每个展区先用章节页交代「这一段要看什么」，再用内容页逐步展开；重点文物区把七件器物做成完全平行的展开——每页固定「年代 / 坑号 / 关键尺寸 / 看点」四件事，同序同深度，让观众能横向比较；页标题写这一页教什么，不写判断句。观众可以从任意入口进入、任意时刻退出，因此每页自足，不依赖上一页的铺垫。
- **Visual style**: custom
- **Visual Style References**: dark-tech
- **Visual Style Behavior**: 取 dark-tech 的暗场—发光—几何精准三件事，换成青铜与黄金的语汇：近黑墨绿满铺作深度，细金线与低透明度巨大编号浮在内容层之后，卡片用 1px 金色描边而非填充块，边角近直角（8px）；注意力靠局部高对比的金色发光承担，其余一律压低；纵深靠外发光与层叠，不用投影；文物照片以暗场直接承托、加极轻的暗角压边，不套框。等宽体只用于尺寸与坑号这类需要精确读数的标签，正文保持中文黑体的清晰度。
- **Theme**: 深场金光——观众在偏暗的展厅里抬眼看屏，屏幕本身是一盏灯；金色只出现在「可点」和「关键数字」两处，从而让导航与事实自己发光
- **Tone**: 庄重、可靠、克制；博物馆标牌的语气，不是营销页的语气

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | `#0E1512` | 全卷满铺底色，近黑墨绿，模拟展厅暗环境下的青铜暗部 |
| Secondary background | `#17211D` | 卡片、速查表行底、导航条底，比主底高一档 |
| Primary | `#C9A227` | 黄金——可点元素（导航按钮、菜单入口、外链）与关键数字的唯一主色 |
| Accent | `#4FB9A5` | 青铜锈——章节标识、当前位置指示、时间线节点 |
| Secondary accent | `#C6704A` | 陶土朱——坑号标签与「禁止出境」这类文物级别标记 |
| Body text | `#E9E5D9` | 正文米白，暗场上的主要读取色 |
| Secondary text | `#A8A396` | 注记、来源行、单位、口径说明 |
| Divider | `#2A3630` | 细分隔线、卡片描边的非强调态、表格网格 |

补充锚定的中性层（本卷反复出现、已获得稳定语义）：

| Role | HEX | Purpose |
| --- | --- | --- |
| Surface | `#1D2A24` | 浮在 secondary background 之上的抬升面，用于当前选中的菜单条目与文物页的主数据块 |
| Scrim | `#0E1512` | 文物照片上承托文字时的压暗层（透明度由执行期决定） |
| Grid | `#212C27` | 速查表与时间线的发丝线，比 divider 更轻 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 中文黑体 / 厚重、标牌感 | SimHei | Arial | sans-serif |
| Body | 中文黑体 / 中性、屏读清晰 | Microsoft YaHei | Arial | sans-serif |
| Data | 等宽 / 精确读数 | Consolas | Consolas | monospace |
| Display | 中文黑体 / 厚重、远读 | SimHei | Arial | sans-serif |

- **Title stack**: `SimHei, Arial, sans-serif`
- **Body stack**: `Microsoft YaHei, Arial, sans-serif`
- **Data stack**: `Consolas, Microsoft YaHei, monospace`
- **Display stack**: `SimHei, Arial, sans-serif`
- **Role rationale**: Data 角色独立于正文家族，因为尺寸、重量、坑号、年代在七个文物页与速查表上反复出现且需要等宽对齐才能横向比较；Display 角色显式声明家族，因为封面标题、章节巨大序号与文物页的尺寸大数字都需要 Title 的黑体厚重感，而未声明时该角色会回落到 Body 家族；其余角色（Lead、Nav label、Annotation、Footnote）沿用 Title/Body 家族，只锚定字号。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 42 |
| Subtitle | 32 |
| Annotation | 18 |
| Display | 72 |
| Lead | 28 |
| Data | 26 |
| Nav label | 20 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 视线先落在页面上三分之一的标题或主图，再向下走到事实块，最后才到底部导航条；导航条位置全卷恒定，观众一旦学会就不必再找
- **Composition tendency**: 内容页偏向「左事实 / 右图像」或「上主视觉 / 下四栏事实」的双区关系；菜单页与目录页用可点条目的纵向排布承担全部构图；文物页固定同一宏观关系，靠内容差异而非构图差异产生变化
- **Cross-page continuity**: 底部导航条、页码、来源行三件框架元素全卷同位同形；每个展区有一个恒定的色标（accent 色块 + 展区名）留在页眉；文物页的四栏事实块在七页之间保持同一相对关系，只有内容与主图变化
- **Spacing posture**: variable by page rhythm——章节页与菜单页留白充分，文物页与速查表偏紧凑但受栅格约束
- **Spacing anchors**: page margin 64 px；block gap 28 px；column gutter 32 px；corner radius 8 px；body leading 1.55

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-outline/home | 回首页 |
| tabler-outline/arrow-left | 上一页 |
| tabler-outline/arrow-right | 下一页 |
| tabler-outline/list | 返回文物目录、菜单标识 |
| tabler-outline/ruler | 尺寸 |
| tabler-outline/calendar | 年代 |
| tabler-outline/shovel | 出土坑号、发掘 |
| tabler-outline/certificate | 文物级别、禁止出境 |
| tabler-outline/star | 看点 |
| tabler-outline/crown | 王权、大立人 |
| tabler-outline/tree | 青铜神树 |
| tabler-outline/eye | 纵目面具 |
| tabler-outline/mask | 面具类器物 |
| tabler-outline/coin | 金器、黄金面具 |
| tabler-outline/box | 龟背形网格状器等容器类器物 |
| tabler-outline/flame | 祭祀、燎祭 |
| tabler-outline/building-bank | 博物馆、都城 |
| tabler-outline/clock | 开放时间 |
| tabler-outline/ticket | 票价、预约 |
| tabler-outline/world | 官方网站 |
| tabler-outline/map-pin | 馆址 |
| tabler-outline/phone | 客服电话 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P15 | table | record_table | 把七件重点文物按同一组字段并排，供观众在离开菜单前一次性速查 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sanxingdui_museum_exterior.jpg | 1280x720 | 16:9 | 首页菜单的场所锚点，让观众确认「我就在这座馆里」 | Photo | 作为整幅底图退到菜单条目之后，右侧或下部留出安静区承托可点条目 | adaptive | web | Sourced | 三星堆博物馆新馆建筑外观或遗址全景，日光或暮色均可；需要一块低细节的安静区域给文字，画面不得有明显水印或人脸特写 | none | local |
| bronze_standing_figure.jpg | 560x720 | 7:9 | 青铜大立人的本体识别 | Photo | 竖向立在页面左侧，人像完整不裁头足，右侧让给四栏事实 | no-crop | web | Sourced | 三星堆青铜大立人像整体照，正面或四分之三侧面，含底座；必须是文物本体照片而非线描或复制品 | none | local |
| bronze_sacred_tree.jpg | 560x720 | 7:9 | 一号青铜神树的本体识别 | Photo | 竖向满高，树顶与底座都在画面内，树形轮廓压住页面左半 | no-crop | web | Sourced | 三星堆一号青铜神树整体照，需看清三层九枝与沿主干的龙；深色或中性背景优先 | none | local |
| bronze_mask_protruding_eyes.jpg | 720x480 | 3:2 | 青铜纵目面具的本体识别 | Photo | 横向居中偏上，两耳完整入画，下方让给尺寸数字 | no-crop | web | Sourced | 三星堆青铜纵目面具正面照，柱状眼球与大耳完整；避免只拍局部眼部的特写 | none | local |
| gold_scepter.jpg | 720x400 | 9:5 | 金杖的本体识别与图案细节 | Photo | 横向贯通页宽，杖身水平放置，图案端朝向事实栏一侧 | no-crop | web | Sourced | 三星堆金杖整体照或其平雕图案展开图，需看清人头、鸟与鱼的图案带 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页备注以该页最终 SVG 上真实存在的信息为准，不引入页面上没有的事实；备注面向馆方工作人员与平板答疑场景，说明这一页想让观众带走什么、观众常见的误解在哪、以及可以补充的一句背景；涉及口径冲突的页面，备注必须点明本页采用了哪一种口径以及另一种口径是什么；不写讲稿式的口头语，不写时间提示
- **Total duration**: 不适用（自助浏览无固定时长）；单页备注控制在 80–140 字
- **Notes style**: 平实、解释性；先说这一页的读法，再说容易被问到的点
- **Presentation purpose**: 先让观众看懂展区结构并选定路径，再对每件重点文物交代年代、坑号、尺寸与看点，最后交付参观实务

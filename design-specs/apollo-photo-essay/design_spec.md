<!-- ppt-master-schema: design-spec/v1 -->
# apollo_photo_essay - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | apollo_photo_essay |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 13 |
| Primary Language | zh-CN |
| Target Audience | 对太空史有兴趣但不是专业读者的中文观众；知道"阿波罗登月"这个名字，记得一两张照片，但说不清这四年里到底发生了几件事 |
| Communication Intent | 先让照片建立在场感，再用少量精确的数字把四年串成一条能复述的时间线；优先顺序是"看见"在前、"记住"在后、"理解技术细节"不在本卷范围内 |
| Desired Audience Outcome | 看完后能说出这四年的四个关键时刻（1968 绕月、1969 落月、1970 事故、1972 收尾），知道卷中每张照片是谁在什么时候拍的，并且意识到"最后一次离开月面"已经过去半个多世纪 |
| Core Message / Ask / Action | 从 1968 年 12 月 21 日到 1972 年 12 月 19 日，1,459 天，人类九次抵达月球、六次落上去、十二个人走过月面——然后再没有回去 |
| Delivery Context | 主要为有主讲人的图片随笔式放映，约十分钟；次要为会后独立翻阅的图文留存 |
| Artifact Afterlife | 作为 photo-editorial 风格示例卷入库，可被再次放映、引用与拆用 |
| Reading Mode | presentation |
| Content Strategy | 题目型输入，全部可外部核验的事实来自本轮 topic-research；结构由本卷自建（四段弧线），但每个数字与日期都必须挂得上 fact_id。来源之间口径冲突时二选一并在页面上注明口径，绝不把两个口径并列或相加；本卷自行推算出的数字（如 1,459 天）标注"本卷推算"，不挂 fact_id |
| Design Style | photo-editorial × narrative：满版照片主导，文字只做指认与计数；暗色安静的文字侧，一个锈橙强调色只用在编号、细线和关键词上 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 工作流默认 `true`，无相反的显式指令 |
| Custom Animations | enabled — 用户显式要求"自定义动画必须做，Morph ≥ 2 组且有承接物" |
| Narration Audio | disabled — 工作流默认 `false`，用户未要求旁白音频 |
| Created Date | 2026-09-04 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 72 px 四边 |
| Content Area | 1136 × 576（x 72–1208, y 72–648）；满版出血页的照片与 scrim 不受此限 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Visual style**: custom
- **Theme**: 一本关于四年的月度画报。照片是版面的脊椎，文字只在照片让出来的暗部里说话。整卷共用一枚"任务章标"——一条细线加一行 `1968 · APOLLO 8` 这样的编号，它在每一页的同一个位置出现，并在相邻页之间移动、改写，成为把十三页缝起来的那根线
- **Tone**: 克制、具体、有重量。不抒情，不惊叹；靠确切的时刻（`02:56:15 UTC`）、确切的编号（`AS11-40-5903`）和确切的距离（`400,171 公里`）产生分量

- **Mode References**: narrative
- **Mode Behavior**: 以 narrative 的 situation → tension → resolution 走四年：1968 设赌注（先离开地球轨道）、1969 兑现（落脚与那 2 小时 31 分）、1970 崩塌（氧罐与回家的弧线）、1971–72 收束（开车、地质学家、最后一步）。页标题写成推进故事的句子而非标签（"他们本来是去看月球的"、"原话是过去完成时"）；张力与呼吸交替，不做机械的密度轮转；人物、时刻、器材是抓手，抽象的"人类壮举"不作为论据。
- **Visual Style References**: photo-editorial
- **Visual Style Behavior**: 满版出血照片是页面脊椎，文字只做指认、计数与图注；页面装饰只有发丝细线、编号章标和小字图注，任何卡片、图标、阴影都不与照片争夺注意力。构图在四种之间轮换——L 形文字区、标题跨压照片明暗交界、破边的浮动图注卡、以及无照片时退回 editorial 的多栏文字页。留白给文字，出血给照片；文字侧永远是安静的中性暗色，锈橙只出现在编号、细线和一两个关键词上。整卷平面，唯一允许的渐变是压字用的方向性 scrim。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #0B0E11 | 深空底色；照片未覆盖处、无照片文字页的整页底 |
| Secondary background | #161A20 | 安静的文字侧场、浮动图注卡与表格底 |
| Primary | #E9E4D9 | 骨白：标题、主要文字、章标的主体 |
| Accent | #D2622B | 锈橙：编号、发丝线、每页一两个关键词；不做面 |
| Secondary accent | #6E7B8A | 冷灰蓝：次级标记、表头、非关键的分组线 |
| Body text | #DAD5CA | 正文与引句 |
| Secondary text | #98A0A9 | 图注、口径说明、注解 |
| Divider | #39414A | 分隔发丝线、表格横线 |
| Scrim | #06080B | 压在照片上的方向性渐变基色，保证骨白文字在照片上仍可读 |
| Surface | #1E242B | 表格斑马行与图注卡的抬升面 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 编辑衬线：横细竖粗，出版物标题的骨架 | SimSun | Times New Roman | — |
| Display | 同 Title 的衬线骨架，放大到封面与英雄数字的尺度 | SimSun | Times New Roman | — |
| Body | 干净无衬线：中性、不抢戏、小字仍可读 | Microsoft YaHei | Arial | — |

- **Title stack**: `Times New Roman, SimSun`
- **Body stack**: `Arial, Microsoft YaHei`
- **Display stack**: `Times New Roman, SimSun`
- **Role rationale**: 只新增一个字族角色 `display`——封面标题与英雄数字（1,459）需要与页标题同一套衬线骨架，若继承 Body 栈会变成无衬线，与整卷的编辑衬线标题体系断开；`annotation` / `footnote`（图注、编号、署名、口径说明）继承 Body 栈，不另立字族。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 30 |
| Title | 54 |
| Subtitle | 40 |
| Annotation | 22 |
| Display | 78 |
| Footnote | 18 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 照片先被看见，再是压在它明暗交界上的标题，再是一段不超过两句的正文，最后才是小字图注与署名。每页只有一个视觉主角
- **Composition tendency**: 四种构图轮换——L 形文字区（沿左缘与下缘）、标题跨压照片明暗交界、破边的浮动图注卡、无照片时退回 editorial 多栏文字页；不重复相邻两页的同一种
- **Cross-page continuity**: 任务章标（`1968 · APOLLO 8` 这样的一行小字加一条锈橙发丝线）在每一页的同一位置出现，是整卷的框架元素；相邻页之间它承接、移动并改写编号，成为 Morph 的承接物
- **Spacing posture**: 变化：满版照片页极度呼吸（文字只占一角），文字页与表格页可以密
- **Spacing anchors**: 页边距 72 / 块间距 32 / 栏间距 40 / 圆角 4 / 正文行距 48

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P11 | table | record_table | 六次成功着陆各自的发射时间、着陆点与带回样品，一行一次任务 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01_launch.jpg | 1280x720 | 16:9 | 封面：土星五号在夜里离开地面 | Photography | 满版出血做封面场，暗侧留在左边给 L 形文字区；#P1-01 + #M2-01 方向性 scrim 压字 | adaptive | web | Sourced | 阿波罗17号 1972-12-07 凌晨的夜间发射：土星五号的火焰把发射场和云层照亮，倒影落在水面上，横幅取景，画面左侧与上方是可压字的夜色暗区；要求是升空瞬间而非静态塔架照 | — | — |
| 02_earthrise.jpg | 1280x720 | 16:9 | 阿波罗8号《地出》，本卷的第一个转折 | Photography | 满版出血；标题跨压在月平线的明暗交界上；#P1-01 + #M2-01 | adaptive | web | Sourced | NASA AS08-14-2383《地出》：地球半明半暗悬在月球地平线之上，月面占下半幅，横幅取景，右侧或下方为月面暗区可压字；须是这一帧本身，不要后期重绘或艺术再创作版本 | — | — |
| 03_ladder.jpg | 760x720 | 19:18 | 阿波罗11号：Aldrin 沿登月舱梯子下降 | Photography | 竖幅裁形放在右侧，左缘与下缘留 L 形文字区；#M1-01 几何裁形 + #P1-02 | adaptive | web | Sourced | NASA AS11-40-5868：Buzz Aldrin 背对镜头、双手扶梯从登月舱下降，登月舱腿部与梯子完整在画面内；竖向构图，主体居中偏右 | — | — |
| 04_visor.jpg | 1280x720 | 16:9 | 阿波罗11号：Aldrin 面罩肖像，面罩里映着 Armstrong | Photography | 满版出血，人物居中偏左，右侧 scrim 压字；破边的浮动图注卡压在下缘；#P1-01 + #M2-01 | adaptive | web | Sourced | NASA AS11-40-5903：Buzz Aldrin 站在月面正对镜头，面罩反射里能看到登月舱、国旗与拍摄者 Armstrong；须是这张著名的 "Visor" 全身或半身正面像，反射细节清楚 | — | — |
| 05_bootprint.jpg | 1280x720 | 16:9 | 阿波罗11号：月壤中的鞋印特写 | Photography | 满版出血做总览，右下角一枚同源圆形放大窗对准印痕边缘（#P2-04 同源放大 + 嵌套裁切），细线牵到浮动图注 | adaptive | web | Sourced | NASA AS11-40-5878：月壤上一枚清晰的靴印特写，纹路完整、光比强，画面基本被月壤填满，没有其他主体 | — | — |
| 06_apollo13_sm.jpg | 1280x720 | 16:9 | 阿波罗13号受损服务舱（仅作单色派生的母本，不上页） | Source | 仅作派生母本；本身不放置 | adaptive | web | Sourced | NASA AS13-59-8500：抛弃后的阿波罗13号服务舱漂在黑色太空中，2 号氧罐爆炸掀掉的整块面板缺口清晰可见 | — | — |
| 06_apollo13_sm_mono.jpg | 1280x720 | 16:9 | 阿波罗13号事故页的主视觉 | Photography | 满版出血铺开，主体偏右，左缘与下缘的黑色太空直接承字，不再加 scrim | adaptive | web | Sourced | Derived from 06_apollo13_sm.jpg; treatment=desaturate+contrast; 去掉残余色偏、压成近单色的冷灰，让缺口的边界更硬，事故页与其他彩色页拉开距离 | — | — |
| 07_irwin_rover.jpg | 1280x720 | 16:9 | 阿波罗15号：Irwin 向国旗行军礼，身后是登月舱与月球车 | Photography | 满版出血；标题横跨照片上缘的明暗交界；#P1-01 + #M2-01 | adaptive | web | Sourced | NASA AS15-88-11866：James Irwin 在哈德利—亚平宁着陆点向展开的美国国旗行军礼，背后是登月舱 Falcon 与 Hadley Delta 山体，月球车在画面内；横幅取景 | — | — |
| 08_schmitt_boulder.jpg | 1280x720 | 16:9 | 阿波罗17号：Schmitt 与 6 号站巨砾 | Photography | 满版出血，巨砾在中偏左、人在左下；破边的浮动图注卡压在下缘；#P1-01 + #M2-01 | adaptive | web | Sourced | NASA S73-22871：6 号站那块巨大的裂开岩块（Tracy's Rock / Split Rock）占据画面，Harrison Schmitt 站在它旁边显出尺度，黑色月空占上半可压标题；横幅取景 | — | — |
| 09_blue_marble.jpg | 1280x720 | 16:9 | 阿波罗17号《蓝色弹珠》，本卷的收束 | Photography | 满版出血，地球居中偏右，左缘 L 形文字区落在太空的黑里；#P1-01 + #M2-01 | adaptive | web | Sourced | NASA AS17-148-22727《蓝色弹珠》：整颗地球满照，非洲与南极冰盖清楚可见，四周是黑色太空；须是这一原始帧，不要后期合成的"蓝色弹珠"系列再制版 | — | — |
| 10_apollo11_liftoff.jpg | 620x620 | 1:1 | 来源页的视觉收束：阿波罗11号的土星五号升空 | Photography | 圆形裁形放在右侧做视觉句号，左侧是来源清单；#M1-01 几何裁形 | adaptive | web | Sourced | NASA：1969-07-16 阿波罗11号的土星五号点火升空，箭体与火焰在画面中轴，可裁入圆形而不丢失箭体与火焰 | — | — |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页的讲述从这一页最终 SVG 上真实可见的内容出发：照片是谁在什么时候拍的、页面上那几个数字各自意味着什么、这一页把故事推到了哪里。数字读法按中文口语展开（"两小时三十一分"而不是 "2:31:40"），编号照读英文原样。口径冲突处按 §I Content Strategy 已裁决的取值讲，不在讲稿里复述被弃用的另一个口径。图片署名与许可只在页面上出现，不进讲稿。
- **Total duration**: 约 10 分钟，13 页平均每页 40–50 秒；照片页短、文字页与表格页长
- **Notes style**: 对话式叙述，页与页之间用一句过渡承接，不用列表和标记
- **Presentation purpose**: 先让照片建立在场感，再用少量精确的数字把四年串成一条能复述的时间线

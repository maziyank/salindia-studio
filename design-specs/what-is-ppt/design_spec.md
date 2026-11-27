<!-- ppt-master-schema: design-spec/v1 -->
# 什么是 PPT - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 什么是 PPT |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 17 |
| Target Audience | 需要制作或评审演示文稿的知识工作者、学生与职场人——他们会用 PowerPoint，但大多把 PPT 只当成"做几页幻灯片"，缺少对这一媒介本质的系统认知 |
| Communication Intent | 系统性地讲清"PPT 到底是什么"：它同时是沟通媒介、可编辑文档、传递载体和原生文件结构；解释人们为什么做演示、何时该用/不该用 PowerPoint、什么是好 PPT，并纠正"PPT=漂亮几页图"的常见误解 |
| Desired Audience Outcome | 看完后能区分"PPT"的几种含义、理解 PowerPoint 原生对象模型、判断某个任务是否真的适合用演示文稿，并在下次做 PPT 前先问对关键问题 |
| Core Message / Ask / Action | PPT 不是一叠静态页面，而是有顺序、模块化、可编辑并需要持续流转的沟通产物——先想清楚受众要完成什么任务，工具才服务沟通 |
| Delivery Context | 既可作为讲解式科普演示（有主讲），也适合独立阅读；单次约 15-20 分钟 |
| Artifact Afterlife | 作为理解 PPT 本质的参考资料、培训讲义与团队入门读物长期复用 |
| Reading Mode | balanced |
| Content Strategy | balanced 默认：在忠实源文档全部事实与关系的前提下，将十节内容重构为"解构→重构→方法"三幕叙事，可重组、提炼、补足过渡，但不引入源材料之外的新事实 |
| Design Style | 自定义"蓝图×编辑"：editorial 杂志栅格与层级为底，讲结构/对象模型的页面叠加 blueprint 示意线稿与标注语汇；墨蓝暖纸浅色场，红色作单一强调 |
| Formula Policy | text-only |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Created Date | 2026-07-24 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上下左右安全边距 40px |
| Content Area | 1200 × 640（安全区，起点 40,40） |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Visual style**: custom
- **Theme**: 技术编辑体——把"PPT 是有结构的原生包"这一核心隐喻贯穿版式：正文区是清晰的杂志栅格，结构区是精细的工程蓝图示意
- **Tone**: 清晰、理性、可信，有工程质感而不冰冷；克制的编辑红只标记结构与强调
- **Mode References**: instructional, pyramid
- **Mode Behavior**: 三幕结构。第一幕"解构"先拆解"PPT"被混用的多重含义、制造认知张力（原来我们一直在说不同的东西）；第二幕"重构"逐层重建——从沟通媒介到对象模型到模板，用 instructional 的概念分解逐页只讲一个概念、平行展开可比；每个关键页用 pyramid 的结论先行，标题即断言。第三幕"方法"落到"每次做 PPT 该问的问题"，把认知转成可执行的方法闭环。
- **Visual Style References**: editorial, blueprint
- **Visual Style Behavior**: 在 editorial 的杂志栅格、细分隔线、眉题（kicker）→标题→引言→正文的强纵向层级基础上，为讲"结构/对象模型"的页面叠加 blueprint 的示意线稿与标注语汇——细单色线框、等距/等轴示意、尺寸标注线、引线箭头、坐标/代号标签、极低透明度网格背景。正文区保持编辑体清晰留白；结构图区让线稿在浅场上呼吸。单一编辑红作强调色，遵循工程图"一个高亮色"的惯例。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 主页面底色，杂志白场 |
| Secondary background | #F4F1EA | 暖纸副底：侧栏、面板、结构图衬底、引用块 |
| Primary | #1A2B4A | 墨蓝：标题、蓝图线稿主色、主要文字结构、边框 |
| Accent | #C8102E | 编辑红：单一强调、关键路径、当前项、分隔强调标记 |
| Secondary accent | #5E7089 | 次级蓝灰：眉题、次要标注、辅助线、图注 |
| Body text | #22262B | 正文近黑，长文可读 |

### AI Image Strategy

- **Image Rendering**: custom
- **Visual**: 技术蓝图线稿融合杂志信息图：细的示意线条+等距结构+少量实色块与标注
- **Mood**: 清晰、理性、有工程质感，像一份被精心排版的技术说明
- **Image Rendering Behavior**: 以 blueprint 的示意线稿、网格与标注为骨架，叠加 editorial 信息图的实色区块与层级排版；crisp 单一线宽（约 1.5px 观感）、直角与精确曲线，元素简化为示意形态（框、连接线、锚点、代号标记），可选极低透明度（5-8%）网格衬底；线条精细、无照片、无渐变噪点、无材质阴影。图像色彩全部继承演示色板：墨蓝 #1A2B4A 作线稿主色，编辑红 #C8102E 作单一高亮，白/暖纸 #F4F1EA 作场，蓝灰 #5E7089 作次级线。用于把抽象概念画成"可读的结构图"。
- **Image Rendering References**: blueprint, editorial

## IV. Typography System

### Font Plan

| Role | Chinese | English | Fallback tail |
| --- | --- | --- | --- |
| Title | Microsoft YaHei | Arial | sans-serif |
| Body | Microsoft YaHei | Consolas | monospace |

- **Title stack**: `"Microsoft YaHei", Arial, sans-serif`
- **Body stack**: `"Microsoft YaHei", Consolas, monospace`

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 42 |
| Subtitle | 32 |
| Annotation | 18 |
| Footnote | 16 |

## V. Layout Principles

### Page Structure

- **Header area**: 顶部 40-96px 区，眉题（kicker，蓝灰小字/代号）+ 主标题（断言式）；标题下可选一条墨蓝细分隔线或半幅规则线
- **Content area**: 杂志栅格，优先非对称 2:1 / 3:7 分栏与竖向规则线悬挂内容；结构页让蓝图示意图作骨架，正文/标注挂在引线与栅格上
- **Footer area**: 底部左侧页码代号（如 `P07 / 17`），右侧来源行（Footnote，蓝灰）；两者用 Footnote 尺寸

### Spacing Specification

| Element | Current Project |
| --- | --- |
| Safe margin | 40px |
| Content block gap | 24-32px |
| Icon-text gap | 12px |

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Brand-logo library**: none

| Purpose | Icon Path | Page |
| --- | --- | --- |
| 软件/应用 | icons/tabler-outline/app-window.svg | P02 |
| 演示活动 | icons/tabler-outline/presentation.svg | P02, P08 |
| 有序文档/Deck | icons/tabler-outline/stack-2.svg | P02 |
| 幻灯片放映 | icons/tabler-outline/player-play.svg | P02 |
| 数字文件包 | icons/tabler-outline/file-zip.svg | P02, P11 |
| 转化/意图 | icons/tabler-outline/transform.svg | P04 |
| 目标结果 | icons/tabler-outline/target.svg | P04, P16 |
| 告知 | icons/tabler-outline/info-circle.svg | P05 |
| 解释 | icons/tabler-outline/bulb.svg | P05, P08 |
| 说服 | icons/tabler-outline/speakerphone.svg | P05 |
| 决策 | icons/tabler-outline/checkbox.svg | P05 |
| 对齐 | icons/tabler-outline/users-group.svg | P05 |
| 教学 | icons/tabler-outline/school.svg | P05 |
| 汇报问责 | icons/tabler-outline/report.svg | P05 |
| 动员 | icons/tabler-outline/flag.svg | P05 |
| 留档交接 | icons/tabler-outline/archive.svg | P05 |
| 顺序 | icons/tabler-outline/list-numbers.svg | P06 |
| 模块化 | icons/tabler-outline/layout-grid.svg | P06 |
| 多媒体组合 | icons/tabler-outline/photo.svg | P06 |
| 演讲支持 | icons/tabler-outline/microphone.svg | P06, P09 |
| 阅读支持 | icons/tabler-outline/book.svg | P06, P09 |
| 可编辑 | icons/tabler-outline/edit.svg | P06, P16 |
| 组织可移植 | icons/tabler-outline/transfer.svg | P06 |
| 文档/报告 | icons/tabler-outline/file-text.svg | P07 |
| 电子表格 | icons/tabler-outline/table.svg | P07 |
| 白板画布 | icons/tabler-outline/layout-board.svg | P07 |
| 视频 | icons/tabler-outline/movie.svg | P07, P09 |
| Web 应用 | icons/tabler-outline/browser.svg | P07 |
| 混合场景 | icons/tabler-outline/arrows-shuffle.svg | P09 |
| Theme 主题 | icons/tabler-outline/palette.svg | P11, P12 |
| Slide Master 母版 | icons/tabler-outline/template.svg | P11, P12 |
| Slide Layout 版式 | icons/tabler-outline/layout.svg | P11, P12 |
| Placeholder 占位符 | icons/tabler-outline/rectangle.svg | P11 |
| Slide 幻灯片 | icons/tabler-outline/square.svg | P11 |
| Notes 备注 | icons/tabler-outline/notes.svg | P11 |
| 包关系 | icons/tabler-outline/link.svg | P11 |
| 事实层 | icons/tabler-outline/checklist.svg | P13 |
| 沟通层 | icons/tabler-outline/message-2.svg | P13, P16 |
| 叙事层 | icons/tabler-outline/route.svg | P13 |
| 认知层 | icons/tabler-outline/brain.svg | P13, P14 |
| 视觉层 | icons/tabler-outline/eye.svg | P13, P16 |
| 原生运行层 | icons/tabler-outline/settings.svg | P13 |
| 提问 | icons/tabler-outline/help-circle.svg | P16 |
| 受众 | icons/tabler-outline/users.svg | P16 |
| 核心信息 | icons/tabler-outline/bulb.svg | P16 |
| 复用重复 | icons/tabler-outline/refresh.svg | P16 |

## VII. Visualization Reference List

（无 catalog 图表引用；本演示的可视化均为自定义结构图与信息版式，见 §IX 各页 Layout。）

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_identities.jpg | 1280×720 | 16:9 | 封面主视觉：把"PPT 的多重身份"做成概念隐喻 | AI Illustration | #73 Full-bleed poster image + side title stack | adaptive | ai | Generated | 一个中心的演示页/文档对象，向外裂解并展开为多个等距示意面板与线框，隐喻同一件东西同时是软件、活动、文档、放映与文件包；蓝图线稿+少量实色块，构图右侧留出安置标题的平静区 | none | hero_page |
| five_meanings.jpg | 960×720 | 4:3 | "PPT 的五种含义"概念插图 | AI Illustration | #3 Right-third image + left text body | adaptive | ai | Generated | 一个"PPT"符号向右侧散射为五片各异的示意面板（应用窗口、演讲台、有序页堆、播放三角、文件包），每片风格统一但形态不同，蓝图信息图质感 | none | local |
| object_model.jpg | 1280×720 | 16:9 | PowerPoint 原生对象模型：包结构等距爆炸图 | AI Illustration | #41 Background image + measurement lines and module tags (engineering overlay) | adaptive | ai | Generated | 一个演示文稿包的等距（isometric）爆炸分层示意：自上而下 Theme、Slide Master、Slide Layout、Slide 等薄平面依次错落堆叠，用引线连接层与层；纯蓝图线稿、等距投影、极低透明度网格底，一处编辑红高亮当前层，无任何文字 | none | hero_page |
| quality_layers.jpg | 720×900 | 4:5 | "什么是好的 PPT"的六层质量剖面 | AI Illustration | #3 Right-third image + left text body | adaptive | ai | Generated | 一个纵向分层的剖面/堆叠示意：自下而上六个薄层依次收窄（事实→沟通→叙事→认知→视觉→原生运行），像一份工程剖面图，蓝图线稿+每层一个细实色块，无文字 | none | local |
| ppt_is_not.jpg | 800×800 | 1:1 | "PPT 不是什么"对照概念图 | AI Illustration | #2 Left-third image + right text body | adaptive | ai | Generated | 对照示意：左边一叠装饰化、互不相连的扁平页面被一条编辑红斜线否定；右边同样的内容被组织成有引线连接的结构化包，形成"扁平图片 vs 有结构的产物"的对比，蓝图线稿风格，无文字 | none | local |

## X. Speaker Notes Requirements

- **Filename**: 与各 SVG 文件同名，置于 `notes/`（如 `01_cover.svg` → `notes/01_cover.md`）
- **Content**: 讲解式、耐心解释的语气（instructional 底 + pyramid 每页先给结论句）；先给这一页的断言，再补 2-3 点支撑与过渡；忠实源文档事实，不引入源外新事实；外部来源（Microsoft、ECMA-376、Yates & Orlikowski、Mayer、Bartsch & Cobern、Kosslyn 等）在备注中点名
- **Total duration**: 约 15-20 分钟
- **Notes style**: conversational
- **Presentation purpose**: instruct（讲清概念）为主，兼 inform 与 report（澄清误解、给出方法）

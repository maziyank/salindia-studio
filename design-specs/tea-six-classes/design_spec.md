<!-- ppt-master-schema: design-spec/v1 -->
# tea_six_classes_a4 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | tea_six_classes_a4 |
| Canvas Format | A4 Print (1240×1754) |
| Page Count | 9 |
| Primary Language | zh-CN |
| Target Audience | 天天喝茶但没系统学过茶的普通读者——办公室泡茶的人、刚开始买茶的人；知道龙井铁观音的名字，但说不清它们凭什么分成不同的类 |
| Communication Intent | 先教会一条判据（茶类由加工工艺决定，不由颜色或产地决定），再把六类逐一讲清；最后让读者能拿着这页纸当场泡对一杯。教学优先于罗列，可查优先于好看 |
| Desired Audience Outcome | 读者能说出六类的分类依据，指着任意一类说出它的关键工序和一两个代表茶，并按页上的水温与时间泡出一杯不苦不淡的茶 |
| Core Message / Ask / Action | 六大茶类不是按颜色分的，是按工艺（尤其氧化/发酵程度）分的——记住工序，就记住了茶 |
| Delivery Context | 读者自持的印刷单页，无讲述者；每页能单独打印夹进本子，也可整册翻阅 |
| Artifact Afterlife | 长期查阅、反复打印、逐页拆用；来源需可回溯核对 |
| Reading Mode | text |
| Content Strategy | balanced（默认）——研究补充件是唯一事实来源，页面按教学顺序重新组织；未取得来源的条目写 NO DATA，冲突条目两说并列 |
| Design Style | ink-notes 手写墨线 × instructional 教学分解：近单色黑墨线承担全部结构，每类只给一个语义色（该类汤色），无纸纹、无投影、无渐变 |
| AI Image Acquisition Path | auto（Path A：image_gen.py --manifest，后端按仓库 .env 解析为 gemini） |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 工作流默认；本页为读者自持印刷物，注记写成"这页怎么用/怎么讲"的补充说明 |
| Custom Animations | enabled — 最终 Stage-2 主动建议：轴与工序链在相邻页之间是同一张地图的不同可见状态，需要 Morph 与逐条入场承担顺序 |
| Narration Audio | disabled — 最终 Stage-2 主动建议 |
| Created Date | 2026-09-04 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | A4 Print |
| Dimensions | 1240 × 1754 |
| viewBox | `0 0 1240 1754` |
| Margins | 上下左右各 72px |
| Content Area | x 72–1168，y 72–1682（1096 × 1610） |

## III. Visual Theme

### Theme Style

- **Mode**: instructional
- **Visual style**: ink-notes
- **Theme**: 一本摊开的手写茶记——墨线画结构，色只用来指认汤色。整册靠一条"发酵度轴"贯穿：封面预告它，总览页画全它，六个类页各取它的一段放大
- **Tone**: 克制、笃定、可照做；像一位讲得清楚的老师在纸上边写边画，不像商业图表

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FAF9F5 | 纸白页面底色，无纹理 |
| Secondary background | #F0EDE4 | 极少量的浅块底，用于参数区分栏 |
| Primary | #1C1A17 | 墨色：全部线条、框、箭头、题头 |
| Accent | #A62F1F | 主强调（红茶汤色）：轴的高发酵端、重点标记 |
| Secondary accent | #6E9B3A | 次强调（绿茶汤色）：轴的低发酵端、正向标记 |
| Body text | #1C1A17 | 正文墨色 |
| Secondary text | #6B665C | 注释、脚注、来源行 |
| Divider | #C9C3B4 | 细分隔线、表格细线 |
| Tea green | #6E9B3A | 绿茶语义色（汤色嫩绿明亮） |
| Tea white | #D6C079 | 白茶页标识色（页面识别用，非审评汤色；白茶汤色为 NO DATA） |
| Tea yellow | #D9A526 | 黄茶语义色（黄叶黄汤 / 橙黄明净） |
| Tea oolong | #B5761B | 青茶语义色（金黄；整类通用汤色为 NO DATA，取单品描述） |
| Tea red | #A62F1F | 红茶语义色（汤色红艳明亮） |
| Tea dark | #5A3B26 | 黑茶语义色（随氧化加深的深褐） |

### AI Image Strategy

- **Image Rendering**: ink-notes
- **Visual**: 纯净纸场上的黑墨线小图与手写题字：中锋起落有轻微抖动的单色线条，无填色块、无投影、无渐变，形体靠线的疏密与顿挫立起来
- **Mood**: 像一位茶人在白纸上用秀丽笔随手写画的备忘——克制、笃定、有手的温度；接近 Mike Rohde 视觉笔记落在中文茶记本上的样子

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 楷体骨架，手写而克制，承担 ink-notes 要求的手写题头字性 | KaiTi | Georgia | KaiTi |
| Body | 无衬线，笔画均匀，打印小字仍清楚 | Microsoft YaHei | Segoe UI | Microsoft YaHei |
| Display | 与题头同源的放大字，用于封面主字与类页大类名的原生可编辑层 | KaiTi | Georgia | KaiTi |
| Data | 等高数字，温度与时间必须对齐可比 | Times New Roman | Times New Roman | Times New Roman |

- **Title stack**: KaiTi
- **Body stack**: Microsoft YaHei
- **Display stack**: KaiTi
- **Data stack**: Times New Roman
- **Role rationale**: Data 单独立族，因为水温与时间在六页上重复出现且需要等高数字对齐比较；Display 与 Title 同族但尺寸差异达一个量级，单列锚点避免大字落进 Title 的 ±2px 带。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 46 |
| Title | 84 |
| Subtitle | 60 |
| Annotation | 34 |
| Display | 156 |
| Lead | 54 |
| Data | 68 |
| Footnote | 26 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 先看到大类名与它在轴上的位置，再看工序链，再看参数，最后看那句怎么挑；视线自上而下但每页有一处偏心的焦点，避免六页同构
- **Composition tendency**: 每页换一种 ink-notes 构图语汇——圆心概念加分支箭头、大括号归组、划掉重写、轴段放大、贯穿流线、层叠堆——不做"上题字下三行"的重复排版
- **Cross-page continuity**: 发酵度轴是唯一贯穿母题：封面给它一个淡预告，P02 画全，六个类页各在页眉带一段同位置的轴并高亮本类节点；类名题字与语义色圆点在总览与类页之间保持同一对应
- **Spacing posture**: 大面积留白（ink-notes 的空场是风格本身），信息密度靠线的疏密而不是填满
- **Spacing anchors**: 页边距 72px；块间距 40px；分栏间距 48px；圆角 6px；正文行高 70px

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-outline/temperature | 水温 |
| tabler-outline/clock | 冲泡与出汤时间 |
| tabler-outline/droplet | 汤色 |
| tabler-outline/leaf | 鲜叶与工序起点 |
| tabler-outline/flame | 杀青、烘焙等火工工序 |
| tabler-outline/arrow-narrow-right | 工序链方向 |
| tabler-outline/star | 代表茶标记 |
| tabler-outline/bulb | 怎么挑的一句提示 |
| tabler-outline/alert-triangle | 冲突两说与 NO DATA 提示 |
| tabler-outline/link | 来源页链接标记 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| leaf_green.png | 242×276 | 121:138 | 绿茶叶态标识 | Illustrated icon | 与大类名题字并置，做该页的身份记号 | no-crop | slice | Generated | Derived from tea_elements_sheet.png 的第 1 格 | none | local |
| leaf_white.png | 212×282 | 106:141 | 白茶叶态标识 | Illustrated icon | 与大类名题字并置，做该页的身份记号 | no-crop | slice | Generated | Derived from tea_elements_sheet.png 的第 2 格 | none | local |
| leaf_yellow.png | 198×240 | 33:40 | 黄茶叶态标识 | Illustrated icon | 与大类名题字并置，做该页的身份记号 | no-crop | slice | Generated | Derived from tea_elements_sheet.png 的第 3 格 | none | local |
| leaf_oolong.png | 259×234 | 259:234 | 青茶叶态标识 | Illustrated icon | 与大类名题字并置，做该页的身份记号 | no-crop | slice | Generated | Derived from tea_elements_sheet.png 的第 4 格 | none | local |
| leaf_red.png | 294×233 | 294:233 | 红茶叶态标识 | Illustrated icon | 与大类名题字并置，做该页的身份记号 | no-crop | slice | Generated | Derived from tea_elements_sheet.png 的第 5 格 | none | local |
| leaf_dark.png | 267×221 | 267:221 | 黑茶叶态标识 | Illustrated icon | 与大类名题字并置，做该页的身份记号 | no-crop | slice | Generated | Derived from tea_elements_sheet.png 的第 6 格 | none | local |
| ware_gaiwan.png | 274×260 | 137:130 | 盖碗器物元素 | Illustrated icon | 落在参数区旁，指认"用盖碗工夫冲泡"这一档 | no-crop | slice | Generated | Derived from tea_elements_sheet.png 的第 7 格 | none | local |
| ware_kettle.png | 291×287 | 291:287 | 执壶器物元素 | Illustrated icon | 落在水温标注旁 | no-crop | slice | Generated | Derived from tea_elements_sheet.png 的第 8 格 | none | local |
| ware_cup.png | 207×202 | 207:202 | 品茗杯器物元素 | Illustrated icon | 封面与来源页的收尾小记号 | no-crop | slice | Generated | Derived from tea_elements_sheet.png 的第 9 格 | none | local |
| word_green.png | 441×238 | 63:34 | 绿茶类名题字 | Illustrated icon | 作大类名的显示层，原生标题另置一行 | no-crop | slice | Generated | Derived from tea_lettering_sheet.png 的第 1 格；精确字串「绿茶」 | embedded | local |
| word_white.png | 412×237 | 412:237 | 白茶类名题字 | Illustrated icon | 作大类名的显示层，原生标题另置一行 | no-crop | slice | Generated | Derived from tea_lettering_sheet.png 的第 2 格；精确字串「白茶」 | embedded | local |
| word_yellow.png | 437×236 | 437:236 | 黄茶类名题字 | Illustrated icon | 作大类名的显示层，原生标题另置一行 | no-crop | slice | Generated | Derived from tea_lettering_sheet.png 的第 3 格；精确字串「黄茶」 | embedded | local |
| word_oolong.png | 432×250 | 216:125 | 青茶类名题字 | Illustrated icon | 作大类名的显示层，原生标题另置一行 | no-crop | slice | Generated | Derived from tea_lettering_sheet.png 的第 4 格；精确字串「青茶」 | embedded | local |
| word_red.png | 432×231 | 144:77 | 红茶类名题字 | Illustrated icon | 作大类名的显示层，原生标题另置一行 | no-crop | slice | Generated | Derived from tea_lettering_sheet.png 的第 5 格；精确字串「红茶」 | embedded | local |
| word_dark.png | 418×231 | 38:21 | 黑茶类名题字 | Illustrated icon | 作大类名的显示层，原生标题另置一行 | no-crop | slice | Generated | Derived from tea_lettering_sheet.png 的第 6 格；精确字串「黑茶」 | embedded | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页写"这页在教什么、读者最容易在哪里搞错、这页的数字出自哪条 fact"；所有事实取自 `sources/tea_six_classes_research.md` 与其 facts JSON，不得引入页面外的新事实；NO DATA 与两说条目在注记里再说明一次为什么不给单一数字
- **Total duration**: 无口播场景，按逐页阅读补充计，全册约 9–12 分钟
- **Notes style**: 教学口吻，耐心解释，先定义后使用
- **Presentation purpose**: 先教会"茶类由工艺决定"这一条判据，再把六类逐一讲清，最后让读者能按参数泡对一杯

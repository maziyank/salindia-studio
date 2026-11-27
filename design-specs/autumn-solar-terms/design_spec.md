<!-- ppt-master-schema: design-spec/v1 -->
# 二十四节气手账·秋 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 二十四节气手账·秋 |
| Canvas Format | Story/Vertical 1080×1920 |
| Page Count | 14 |
| Primary Language | zh-CN |
| Target Audience | 对传统文化有轻度兴趣、习惯手机竖屏阅读的普通读者：叫得出六个秋节气的名字，但说不准日期，也没读过七十二候原文 |
| Communication Intent | 先把秋天拆成六个可以分别过的日子并给出确切日期，再把七十二候原文完整交到读者手里；每一站结尾都落到一件今天就能做的事 |
| Desired Audience Outcome | 读者能按顺序说出 2026 年秋季六个节气及其日期，记住至少一条三候原文，并在下一个节气到来时真的去做一件事 |
| Core Message / Ask / Action | 秋天不是一整块，它有六个可以分别过的日子——挑一个，照着过一次 |
| Delivery Context | 主要为手机竖屏自读（社媒滑动式浏览，无主讲人）；次要为打印成手账内页夹在本子里 |
| Artifact Afterlife | 2026 年秋天反复回查节气日期与物候原文；打印留存为手账内页 |
| Reading Mode | balanced |
| Content Strategy | 平衡：以研究补充中的事实为准重新组织为手账叙事，日期与七十二候原文逐字保留，查不到的字段标 NO DATA 不推算 |
| Design Style | showcase 视觉主导叙事 × sketch-notes 手绘手账视觉 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 最终 Stage-2 proactive 值 |
| Custom Animations | enabled — 用户明确指令（本轮必须包含 Morph 与 path 轨迹动画） |
| Narration Audio | disabled — 最终 Stage-2 proactive 值 |
| Created Date | 2026-09-04 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | Story/Vertical |
| Dimensions | 1080 × 1920 |
| viewBox | `0 0 1080 1920` |
| Margins | 左右 80；表意文字、标题与行动提示守 y=120..1740，纸底与插画可出血 |
| Content Area | x 80..1000，y 120..1740 |

## III. Visual Theme

### Theme Style

- **Mode**: showcase
- **Visual style**: sketch-notes
- **Theme**: 一本翻开的秋日手账——暖纸底、黑墨抖线、蜡笔色块；六个节气是路线上的六站，一条手绘波浪路线贯穿全卷作为跨页母题，节气页取其中一段作为页面骨架
- **Tone**: 亲切、慢、带点手写的随意；不端着，也不卖萌

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FBF6EA | 暖纸底，全卷统一画布 |
| Secondary background | #F1E5CE | 次级纸块、便签、表格底 |
| Primary | #A8502A | 秋叶赭：标题墨色之外的主色、主要色块与关键线条 |
| Accent | #E39A1F | 金桂黄：每页只留 1–2 处强调（关键箭头、被圈出的日期） |
| Secondary accent | #6F8C5A | 残绿：物候、草木、次要色块 |
| Body text | #33302A | 墨褐：正文与全部手绘线条的墨色 |
| Secondary text | #6B6355 | 注释、图注、脚注 |
| Divider | #D8C9AC | 手绘分隔线、虚线路线、表格线 |
| Block shade | #EDE0C6 | 蜡笔色块的底层平涂，比纸底低一档 |

### AI Image Strategy

- **Image Rendering**: sketch-notes
- **Visual**: 暖奶油纸上黑色手绘抖线，蜡笔／粉彩色块略微溢出线框；简笔卡通造型，无渐变、无投影、无高光
- **Mood**: 温暖、可亲、像一位耐心的老师在笔记本边缘随手画的插图

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 楷体书写感，带手写笔意 | KaiTi | Georgia | serif |
| Body | 清晰人文无衬线，长句可读 | Microsoft YaHei | Trebuchet MS | sans-serif |
| Display | 与标题同源的大字书写体，用于大日期与节气序号 | KaiTi | Georgia | serif |
| Caption | 与正文同源，用于物候候名与图注 | Microsoft YaHei | Trebuchet MS | sans-serif |
| Annotation | 与正文同源，缩小档 | Microsoft YaHei | Trebuchet MS | sans-serif |
| Footnote | 与正文同源，最小档 | Microsoft YaHei | Trebuchet MS | sans-serif |

- **Title stack**: KaiTi
- **Body stack**: Microsoft YaHei
- **Display stack**: KaiTi
- **Caption stack**: Microsoft YaHei
- **Annotation stack**: Microsoft YaHei
- **Footnote stack**: Microsoft YaHei
- **Role rationale**: Display 与 Title 同族但独立锚定，因为大日期数字与节气序号在 8 页上重复出现且尺寸远超页面标题；Caption 承载六页节气页反复出现的三候候名与图注，Annotation 与 Footnote 沿用正文族，三者仅锁尺寸不换族。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 56 |
| Title | 100 |
| Cover title | 160 |
| Display | 128 |
| Subtitle | 72 |
| Lead | 68 |
| Caption | 40 |
| Annotation | 44 |
| Footnote | 32 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 竖屏自上而下——题字或主视觉先抓眼，接住日期，再落到三候，最后一行口语提示收尾
- **Composition tendency**: 每页换一种 sketch-notes 几何：波浪箭头旅程路线、放射思维图、手绘横幅、编号圆沿虚线跳、云朵框；不允许连续两页用同一种
- **Cross-page continuity**: 一条手绘波浪路线是全卷母题，六个节气页各取其中一段并保留编号圆；纸底与墨色恒定，色块随节气冷暖推移
- **Spacing posture**: 可变——节气页 dense，色卡与食物页 breathing，封面/总览/收尾/来源 anchor
- **Spacing anchors**: 页边距 80；块间距 56；分栏槽 40；圆角 28；正文行距 84

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/calendar-event.svg | 日期、交节时刻 |
| icons/tabler-outline/leaf.svg | 草木、秋叶 |
| icons/tabler-outline/wind.svg | 凉风至 |
| icons/tabler-outline/droplet.svg | 白露、露水 |
| icons/tabler-outline/sun.svg | 昼、暑气 |
| icons/tabler-outline/moon.svg | 夜、祭月 |
| icons/tabler-outline/snowflake.svg | 霜、寒 |
| icons/tabler-outline/cloud.svg | 天气、天地始肃 |
| icons/tabler-outline/bowl.svg | 汤、秋汤 |
| icons/tabler-outline/cup.svg | 茶、白露茶 |
| icons/tabler-outline/wheat.svg | 禾乃登、丰收 |
| icons/tabler-outline/egg.svg | 竖蛋 |
| icons/tabler-outline/mountain.svg | 登高 |
| icons/tabler-outline/flame.svg | 进补、灶 |
| icons/tabler-outline/link.svg | 来源链接 |
| icons/tabler-outline/feather.svg | 鸿雁、玄鸟 |
| icons/tabler-outline/fish.svg | 鱼片滚汤 |
| icons/tabler-outline/plant.svg | 秋菜、草木 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P12 | table | record_table | 六个节气各一行，日期与三候原文按固定字段并置对照 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| term_liqiu.png | 268×269 | 1:1 | 立秋页主视觉 | Illustration element | 页面上半区主视觉，压在波浪路线的第一站上 | no-crop | slice | Generated | Derived from sheet_terms.png; 第1格 | none | local |
| term_chushu.png | 294×309 | 19:20 | 处暑页主视觉 | Illustration element | 横幅标题右侧，与河灯栏并置 | no-crop | slice | Generated | Derived from sheet_terms.png; 第2格 | none | local |
| term_bailu.png | 257×307 | 5:6 | 白露页主视觉 | Illustration element | 页面下半区，承接雁的飞行弧线终点 | no-crop | slice | Generated | Derived from sheet_terms.png; 第3格 | none | local |
| term_qiufen.png | 258×289 | 17:19 | 秋分页主视觉 | Illustration element | 中轴对称构图的轴心 | no-crop | slice | Generated | Derived from sheet_terms.png; 第4格 | none | local |
| term_hanlu.png | 268×265 | 1:1 | 寒露页主视觉 | Illustration element | 上坡路线的坡顶 | no-crop | slice | Generated | Derived from sheet_terms.png; 第5格 | none | local |
| term_shuangjiang.png | 269×252 | 16:15 | 霜降页主视觉 | Illustration element | 云朵框内的主体 | no-crop | slice | Generated | Derived from sheet_terms.png; 第6格 | none | local |
| ph_coolwind.png | 240×204 | 20:17 | 凉风至 | Illustration element | 三候行的行首小图 | no-crop | slice | Generated | Derived from sheet_phenology.png; 第1格 | none | local |
| ph_cicada.png | 184×251 | 11:15 | 寒蝉鸣 | Illustration element | 三候行的行首小图 | no-crop | slice | Generated | Derived from sheet_phenology.png; 第2格 | none | local |
| ph_goose.png | 270×215 | 5:4 | 鸿雁来 | Illustration element | 沿手绘飞行弧线移动的主体，白露与寒露两页复用 | no-crop | slice | Generated | Derived from sheet_phenology.png; 第3格 | none | local |
| ph_swallow.png | 238×232 | 21:20 | 玄鸟归 | Illustration element | 三候行的行首小图 | no-crop | slice | Generated | Derived from sheet_phenology.png; 第4格 | none | local |
| ph_chrysanthemum.png | 262×225 | 7:6 | 菊有黄花 | Illustration element | 三候行的行首小图 | no-crop | slice | Generated | Derived from sheet_phenology.png; 第5格 | none | local |
| ph_frost.png | 237×231 | 21:20 | 霜与草木黄落 | Illustration element | 三候行的行首小图 | no-crop | slice | Generated | Derived from sheet_phenology.png; 第6格 | none | local |
| decor_star.png | 349×348 | 1:1 | 星星簇装饰 | Illustration element | 空白角落点缀 | no-crop | slice | Generated | Derived from sheet_decor.png; 第1格 | none | local |
| decor_arrow.png | 367×268 | 26:19 | 波浪箭头 | Illustration element | 连接两块内容的指向 | no-crop | slice | Generated | Derived from sheet_decor.png; 第2格 | none | local |
| decor_route.png | 438×54 | 73:9 | 虚线路线段 | Illustration element | 总览页与收尾页的路线装饰 | no-crop | slice | Generated | Derived from sheet_decor.png; 第3格 | none | local |
| decor_ribbon.png | 452×166 | 49:18 | 手绘横幅飘带 | Illustration element | 承载页面标题的横幅 | no-crop | slice | Generated | Derived from sheet_decor.png; 第4格 | none | local |
| food_watermelon.png | 277×240 | 15:13 | 啃秋西瓜 | Illustration element | 食物页拼盘中的一件 | no-crop | slice | Generated | Derived from sheet_food.png; 第1格 | none | local |
| food_duck.png | 274×213 | 9:7 | 处暑鸭 | Illustration element | 食物页拼盘中的一件 | no-crop | slice | Generated | Derived from sheet_food.png; 第2格 | none | local |
| food_longan.png | 250×282 | 8:9 | 白露龙眼 | Illustration element | 食物页拼盘中的一件 | no-crop | slice | Generated | Derived from sheet_food.png; 第3格 | none | local |
| food_qiucai.png | 261×316 | 14:17 | 秋分秋汤 | Illustration element | 食物页拼盘中的一件 | no-crop | slice | Generated | Derived from sheet_food.png; 第4格 | none | local |
| food_sesame.png | 257×214 | 6:5 | 寒露芝麻 | Illustration element | 食物页拼盘中的一件 | no-crop | slice | Generated | Derived from sheet_food.png; 第5格 | none | local |
| food_persimmon.png | 235×281 | 5:6 | 霜降柿子 | Illustration element | 食物页拼盘中的一件 | no-crop | slice | Generated | Derived from sheet_food.png; 第6格 | none | local |
| let_cover.png | 1237×173 | 143:20 | 封面题字「二十四节气手账·秋」 | Lettering element | 封面横幅上方的显示层，原生标题另置 | no-crop | slice | Generated | Derived from sheet_lettering_title.png; 第1格 | embedded | hero_page |
| let_liqiu.png | 366×170 | 28:13 | 题字「立秋」 | Lettering element | 节气页顶部显示层，原生标题另置 | no-crop | slice | Generated | Derived from sheet_lettering_terms.png; 第1格 | embedded | local |
| let_chushu.png | 344×204 | 27:16 | 题字「处暑」 | Lettering element | 节气页顶部显示层，原生标题另置 | no-crop | slice | Generated | Derived from sheet_lettering_terms.png; 第2格 | embedded | local |
| let_bailu.png | 335×191 | 7:4 | 题字「白露」 | Lettering element | 节气页顶部显示层，原生标题另置 | no-crop | slice | Generated | Derived from sheet_lettering_terms.png; 第3格 | embedded | local |
| let_qiufen.png | 361×181 | 2:1 | 题字「秋分」 | Lettering element | 节气页顶部显示层，原生标题另置 | no-crop | slice | Generated | Derived from sheet_lettering_terms.png; 第4格 | embedded | local |
| let_hanlu.png | 360×214 | 32:19 | 题字「寒露」 | Lettering element | 节气页顶部显示层，原生标题另置 | no-crop | slice | Generated | Derived from sheet_lettering_terms.png; 第5格 | embedded | local |
| let_shuangjiang.png | 361×215 | 32:19 | 题字「霜降」 | Lettering element | 节气页顶部显示层，原生标题另置 | no-crop | slice | Generated | Derived from sheet_lettering_terms.png; 第6格 | embedded | local |
| let_seal.png | 253×254 | 1:1 | 「秋」字印章 | Lettering element | 收尾页的落款印记 | no-crop | slice | Generated | Derived from sheet_lettering_title.png; 第2格 | embedded | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Content**: 每页一段口语旁白，讲清这一页在整条秋线上的位置与情绪；事实一律以页面上已有的日期、三候原文与习俗为准，不引入页面之外的新事实；节气页的旁白以那一句"这个节气怎么过"收尾
- **Total duration**: 约 7 分钟（14 页，每页 25–35 秒）
- **Notes style**: conversational
- **Presentation purpose**: 先把秋天拆成六个可以分别过的日子并给出确切日期，再把七十二候原文完整交到读者手里；每一站结尾都落到一件今天就能做的事

<!-- ppt-master-schema: design-spec/v1 -->
# nine_heritage_goods - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | nine_heritage_goods |
| Canvas Format | Moments/Instagram 1080×1080 |
| Page Count | 11 |
| Primary Language | zh-CN |
| Target Audience | 微信朋友圈里刷到九宫格的普通中文读者，对老物件、上海制造、怀旧题材有兴趣但不了解具体年份与厂家 |
| Communication Intent | 先让每一张单独成立地讲清一件老国货的来历与它当年为什么风靡，再把怀旧收束到“今天还能怎么遇见它”这件可行动的事上；九张连起来还要看得出一条 1935→1972 的时间线 |
| Desired Audience Outcome | 读者看完能说出其中几件的诞生年份与产地，知道哪几件今天仍买得到或看得到，并愿意转发或去找一件 |
| Core Message / Ask / Action | 这九件 1935–1972 年的中国国货不是回忆里的东西，它们大多还在生产、还在货架上、还在博物馆里——今天仍然遇得到 |
| Delivery Context | 主要为微信朋友圈九宫格连发，读者自主浏览、无主讲人、单图停留数秒；次要用途是单张转发与存图 |
| Artifact Afterlife | 单张转发与存图；PPTX 作为可再编辑源文件保留，讲者备注作为每张的朋友圈配文草稿 |
| Reading Mode | balanced |
| Content Strategy | 事实必须严格来自 `sources/nine_heritage_goods_research.facts.json`，查不到的写 NO DATA、不编造；文案措辞可自由重写为海报口吻，年份、产地、厂名、数字与奖项不得改动 |
| Design Style | 方向 A「国营门市」：showcase 叙事 × vintage-poster 视觉，暖土色三主色平涂 + 黑体美术字标题；九件按诞生年份排成一条线，编号徽章逐页承接 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 最新显式指示未涉及，采用最终 Stage-2 主动值 true；备注在本项目承担“每张的朋友圈配文草稿”这一实际职能 |
| Custom Animations | enabled — 用户显式要求“自定义动画必跑（≥2 对 Morph、入场用 entrance 家族）” |
| Narration Audio | disabled — 最新显式指示未涉及，采用最终 Stage-2 主动值 false |
| Created Date | 2026-09-04 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | Moments/Instagram |
| Dimensions | 1080 × 1080 |
| viewBox | `0 0 1080 1080` |
| Margins | 72 |
| Content Area | 72, 72 – 1008, 1008（936 × 936） |

## III. Visual Theme

### Theme Style

- **Mode**: showcase
- **Visual style**: vintage-poster
- **Theme**: 国营门市部的印刷海报——牛皮纸色纸面、三块暖土色平涂、略微离轴的圆角几何、半调网点当油墨；一件物、一个年份、一枚编号徽章，九张连成一条 1935→1972 的时间线
- **Tone**: 温热、笃定、不煽情；像柜台上贴了三十年的那张纸，褪色但字还很硬

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F4E7CE | 纸面主场，每页的底色 |
| Secondary background | #E3CFA4 | 牛皮纸色的次级大块——地平线带、拱门、叠块的底层 |
| Primary | #B3402F | 主色朱红：大块平涂、题字底板、编号徽章、主要几何体 |
| Accent | #E0952B | 芥黄：太阳盘、射线楔、半调网点着色、关键数字 |
| Secondary accent | #2F6B5E | 松绿：第三块平涂，用于“今天”一栏与对比块 |
| Body text | #2A2420 | 正文与标签的暖近黑油墨 |
| Secondary text | #6B5C4A | 注释、来源、图注 |
| Divider | #C3AC80 | 细分隔线、栏界、边框 |

### AI Image Strategy

- **Image Rendering**: vintage-poster
- **Visual**: 中世纪现代主义海报的减法造型——厚而带手感的轮廓线、圆角有机边、限定三到五块平涂色、网点或纸纹叠在填色上；实物一律画成图形化剪影而非写实，题字为中文美术字，字形本身就是画面
- **Mood**: 温暖、笃定、怀旧而不媚俗——1950–70 年代旅行海报与国营商店门头的气质，接近 Saul Bass 与老上海月份牌之间

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 展示体／厚重黑体，海报美术字的骨架 | SimHei | SimHei | — |
| Body | 中性无衬线，读小字不费劲 | Microsoft YaHei | Microsoft YaHei | — |

- **Title stack**: SimHei
- **Body stack**: Microsoft YaHei
- **Numeral stack**: SimHei
- **Role rationale**: `numeral` 承担每页的诞生年份大数字与封面的“9”，与正文的中性无衬线必须拉开重量，故沿用标题的黑体骨架并单列角色。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 30 |
| Title | 54 |
| Subtitle | 38 |
| Lead | 36 |
| Annotation | 22 |
| Footnote | 18 |
| Numeral | 88 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 先看见一件物与它的名字，再看见年份，最后才读到四行小字；视线从大色块的重心走向标签行
- **Composition tendency**: 每页换一种 vintage-poster 的构图母题（太阳盘／拱门／射线楔／地平线带／徽章封印／取景框／离轴叠块／同心弧），九件不重复；一件物永远压着某条边或某个块缝，不居正中
- **Cross-page continuity**: 编号徽章①–⑨逐页承接并换位；纸面底色、三主色比例、标签行的四个图标语汇全卷不变；每页右下角保留同一枚方形印章
- **Spacing posture**: 由页面节奏决定——dense 页四行标签齐整，breathing 页只留一行与大片纸面
- **Spacing anchors**: 页边距 72、块间距 32、栏间距 40、圆角半径 24、正文行距 46

## VI. Icon Usage Specification

- **Primary bundled library**: chunk-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/chunk-filled/calendar.svg | 诞生年份标签 |
| icons/chunk-filled/factory.svg | 产地与厂家标签 |
| icons/chunk-filled/fire.svg | 当年为什么风靡 |
| icons/chunk-filled/shop.svg | 今天还能怎么遇见它 |
| icons/chunk-filled/trophy.svg | 获奖、纪录、第一次这类荣誉性事实 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| word_cover.png | 1320x327 | 4.04:1 | 封面题字《九件老国货》 | Decorative lettering | 压在太阳盘上缘、占封面上半的显示层，原生标题另置一行 | no-crop | slice | Generated | 切自母表 cover_sheet.png（1x1 单枚） | embedded | local |
| word_huili.png | 601x450 | 1.34:1 | P02 名号题字「回力」 | Decorative lettering | 拱门顶端，原生标题在其下 | no-crop | slice | Generated | 切自母表 letter_sheet.png 第 1 行 1 格 | embedded | local |
| word_yongjiu.png | 600x436 | 1.38:1 | P03 名号题字「永久」 | Decorative lettering | 骑在射线扇的轴线上 | no-crop | slice | Generated | 切自母表 letter_sheet.png 第 1 行 2 格 | embedded | local |
| word_guangming.png | 600x442 | 1.36:1 | P04 名号题字「光明」 | Decorative lettering | 悬在地平线带之上的天空区 | no-crop | slice | Generated | 切自母表 letter_sheet.png 第 1 行 3 格 | embedded | local |
| word_shanghai.png | 640x431 | 1.48:1 | P05 名号题字「上海牌」 | Decorative lettering | 压在圆盘上缘、略微离轴 | no-crop | slice | Generated | 切自母表 letter_sheet.png 第 2 行 1 格 | embedded | local |
| word_dabaitu.png | 640x437 | 1.46:1 | P06 名号题字「大白兔」 | Decorative lettering | 徽章封印内侧的横向字带 | no-crop | slice | Generated | 切自母表 letter_sheet.png 第 2 行 2 格 | embedded | local |
| word_yingxiong.png | 600x432 | 1.39:1 | P07 名号题字「英雄」 | Decorative lettering | 大留白页的左上，独自成立 | no-crop | slice | Generated | 切自母表 letter_sheet.png 第 2 行 3 格 | embedded | local |
| word_haiou.png | 600x429 | 1.40:1 | P08 名号题字「海鸥」 | Decorative lettering | 取景框外的上边缘，跨出框线 | no-crop | slice | Generated | 切自母表 letter_sheet.png 第 3 行 1 格 | embedded | local |
| word_hudie.png | 621x430 | 1.44:1 | P09 名号题字「蝴蝶」 | Decorative lettering | 压在两块离轴叠块的缝上 | no-crop | slice | Generated | 切自母表 letter_sheet.png 第 3 行 2 格 | embedded | local |
| word_hongdeng.png | 600x436 | 1.38:1 | P10 名号题字「红灯」 | Decorative lettering | 同心弧圆心一侧，字面朝向声波 | no-crop | slice | Generated | 切自母表 letter_sheet.png 第 3 行 3 格 | embedded | local |
| good_shoe.png | 1040x718 | 1.45:1 | P02 回力球鞋插画 | Illustration | 斜置在拱门内，鞋头越过拱线 | no-crop | slice | Generated | 切自母表 goods_sheet.png 第 1 行 1 格 | none | local |
| good_bike.png | 1280x806 | 1.59:1 | P03 永久自行车插画 | Illustration | 骑在射线扇的对角线上，前轮压出页边 | no-crop | slice | Generated | 切自母表 goods_sheet.png 第 1 行 2 格 | none | local |
| good_icebrick.png | 554x761 | 0.73:1 | P04 光明冰砖插画 | Illustration | 立在地平线带上，四周大量纸面 | no-crop | slice | Generated | 切自母表 goods_sheet.png 第 1 行 3 格 | none | local |
| good_watch.png | 582x801 | 0.73:1 | P05 上海牌手表插画 | Illustration | 压在巨型圆盘中心偏上，略微离轴 | no-crop | slice | Generated | 切自母表 goods_sheet.png 第 2 行 1 格 | none | local |
| good_candy.png | 680x632 | 1.08:1 | P06 大白兔奶糖插画 | Illustration | 徽章封印中央，另有散粒糖果作节奏 | no-crop | slice | Generated | 切自母表 goods_sheet.png 第 2 行 2 格 | none | local |
| good_pen.png | 1036x1064 | 0.97:1 | P07 英雄100钢笔插画 | Illustration | 沿一条强对角线横贯整页 | no-crop | slice | Generated | 切自母表 goods_sheet.png 第 2 行 3 格 | none | local |
| good_camera.png | 494x842 | 0.59:1 | P08 海鸥双反相机插画 | Illustration | 取景框内居中，镜头对着读者 | no-crop | slice | Generated | 切自母表 goods_sheet.png 第 3 行 1 格 | none | local |
| good_sewing.png | 1040x764 | 1.36:1 | P09 蝴蝶缝纫机插画 | Illustration | 横跨两块离轴叠块的缝 | no-crop | slice | Generated | 切自母表 goods_sheet.png 第 3 行 2 格 | none | local |
| good_radio.png | 840x603 | 1.39:1 | P10 红灯711收音机插画 | Illustration | 同心声波弧的圆心处，弧线自机身发出 | no-crop | slice | Generated | 切自母表 goods_sheet.png 第 3 行 3 格 | none | local |
| deco_sun.png | 522x520 | 1.00:1 | 半调太阳盘装饰件 | Illustration | P04 地平线带之上的天空，低对比 | no-crop | slice | Generated | 切自母表 deco_sheet.png 第 1 行 1 格 | none | local |
| deco_rays.png | 873x877 | 1.00:1 | 射线扇装饰件 | Illustration | P03 自行车背后的印刷射线，压在页角 | no-crop | slice | Generated | 切自母表 deco_sheet.png 第 1 行 2 格 | none | local |
| deco_badge.png | 886x881 | 1.01:1 | 玫瑰花徽章装饰件 | Illustration | P06 奶糖背后的封印底盘 | no-crop | slice | Generated | 切自母表 deco_sheet.png 第 2 行 1 格 | none | local |
| deco_stamp.png | 256x256 | 1.00:1 | 方形印章装饰件（全卷复用的页角落款） | Illustration | P01 与 P11 的页角落款，同一枚重复出现 | no-crop | slice | Generated | 切自母表 deco_sheet.png 第 2 行 2 格 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页备注写成可直接使用的朋友圈配文草稿：先一句把这件东西拉进读者的生活，再交代年份、产地与当年那条最硬的事实，最后落到今天还能怎么遇见它。数字、年份、厂名一律取自页面上已核实的内容，不得新增页面上没有的事实；不写“这张图显示”“左边是”这类描述画面的话。
- **Total duration**: 全卷约 4 分钟（每页 20–25 秒的朗读量）
- **Notes style**: 口语、短句、克制的怀旧，不煽情不感叹号堆砌
- **Presentation purpose**: 让每一张单独成立地讲清一件老国货，并把怀旧收束到“今天还能怎么遇见它”

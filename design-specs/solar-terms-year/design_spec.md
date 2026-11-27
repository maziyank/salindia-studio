<!-- ppt-master-schema: design-spec/v1 -->
# 二十四节气·全年手账 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 二十四节气·全年手账（solar_terms_year） |
| Canvas Format | ppt169 · 1280×720 |
| Page Count | 31 |
| Primary Language | zh-CN |
| Target Audience | 对二十四节气有兴趣的普通读者、家长与中小学教师：叫得出节气名，但记不住日期、说不清三候出处，也不确定“今天该做点什么” |
| Communication Intent | 先给一张全年的时间地图，再逐个节气交付可查的事实（交节时刻／三候原文／一条习俗），最后交出全部来源；教在前、记录归档在后 |
| Desired Audience Outcome | 读者能在一年中的任意一天翻到当天所属的节气页，说出交节时刻、复述三候、挑出一条当天可做的事，并能顺着来源页核对每条事实 |
| Core Message / Ask / Action | 二十四节气是一套精确到分钟的时间系统，也是一本可以照着过的一年生活手账 |
| Delivery Context | 读者主导自读为主（手账式长卷，逐页可单独查阅或打印）；无现场讲者；全年随时翻阅，无时间约束 |
| Artifact Afterlife | 归档与复用：逐页可单独打印夹进本子，来源页支撑事实复核 |
| Reading Mode | balanced |
| Content Strategy | 未提出材料取舍约束，取均衡默认：以研究对中的事实为准重新架构成手账体例，事实一律沿用来源，不外扩 |
| Design Style | 圆角手账（instructional × soft-rounded）：圆角卡片＋柔和抬升＋pill 标签＋大色块出血，四季四个语义色，其余系统整卷不变 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | disabled — final Stage-2 proactive policy: 读者主导的可打印手账，无讲者通道，全部必要含义留在页面上 |
| Custom Animations | enabled — explicit user instruction (object-level motion required: ≥4 pairs of Morph plus entrance choreography) |
| Narration Audio | disabled — final Stage-2 proactive policy |
| Created Date | 2026-09-04 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | ppt169 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 64 px 四边 |
| Content Area | x 64–1216, y 64–656（页脚带 y 656–700 为页码与季标） |

## III. Visual Theme

### Theme Style

- **Mode**: instructional
- **Visual style**: soft-rounded
- **Theme**: 一本可以翻一年的纸质手账——暖白纸底上浮着一叠圆角卡片，四季各占一个语义色，年轮环是贯穿整卷的连续母题（连续职责：让任意一页都能被定位回全年的哪一格；复用方式：封面与总览为完整环，四季分隔页为该季 1/4 弧，节气页缩为右上角的小环＋指针）
- **Tone**: 温和、笃定、有生活气；讲事实时精确到分钟，讲怎么过时说人话

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FBF8F3 | 暖白纸底，整卷唯一页面底色 |
| Secondary background | #FFFFFF | 圆角卡片面，靠柔和抬升与底色拉开 |
| Primary | #7A5C3E | 手账皮革棕：页眉页脚、环线、标题前缀、结构性线条 |
| Accent | #7A5470 | 梅紫：当前指针、超链接、跨页强调；与四季色都不同族，永不与季色抢义 |
| Secondary accent | #9C8B7A | 暖灰褐：刻度、pill 描边、次级分隔 |
| Body text | #3A332C | 正文与三候原文 |
| Secondary text | #8A8078 | 注释、来源标注、页脚 |
| Divider | #E3DACB | 卡片边界与分组细线 |
| Surface | #FFFFFF | 卡片抬升面（soft-rounded 的层次锚） |
| Grid | #EFE8DC | 比 divider 更淡的网格／年轮细刻度 |
| Scrim | #2E2A26 | 大色块出血或图上压字时的低透压暗层 |
| Season · Spring | #6FA46B | 春季语义色（P03 与 P04–P09） |
| Season · Summer | #CC5B4C | 夏季语义色（P10 与 P11–P16） |
| Season · Autumn | #D99A2B | 秋季语义色（P17 与 P18–P23） |
| Season · Winter | #5C7FA3 | 冬季语义色（P24 与 P25–P30） |

### AI Image Strategy

- **Image Rendering**: flat
- **Visual**: 减法造型的扁平矢量：圆润轮廓、无描边或极粗的同色描边、2–3 个平涂色域＋一层更浅的同色块做体积，无渐变、无投影、无透视；物象只保留最能被认出的两三个特征
- **Mood**: 像一套纸质节气日历上的小图标，或无印良品季节手账内页的插图——安静、可爱但不幼稚

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 中文黑体／中性无衬线，字面开阔、笔画等粗，让圆角卡片自己说圆 | Microsoft YaHei | Trebuchet MS | sans-serif |
| Body | 同族无衬线，正文与三候原文同一质地 | Microsoft YaHei | Trebuchet MS | sans-serif |
| Data | 人文无衬线，等高数字（lining figures），专用于日期与交节时刻 | Trebuchet MS | Trebuchet MS | sans-serif |

- **Title stack**: `Microsoft YaHei, sans-serif`
- **Body stack**: `Microsoft YaHei, sans-serif`
- **Data stack**: `Trebuchet MS, sans-serif`
- **Role rationale**: Data 单列一族，因为交节时刻是整卷 24 页都出现的重复角色，必须用等高数字；Microsoft YaHei 的西文数字在小字号下与中文混排重心不稳。Title 与 Body 同族是刻意的 concord：整卷的性格由 24 张 AI 题字（display 层）和圆角几何承担，原生标题保持中性、可搜索、可编辑。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 44 |
| Subtitle | 32 |
| Annotation | 18 |
| Display | 96 |
| Chapter title | 56 |
| Lead | 30 |
| Data | 40 |
| Quote | 26 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 节气页从左上的题字＋原生标题起手，向右下依次交出“什么时候（时刻）→ 古人看见什么（三候）→ 今人做什么（时令＋怎么过）”；总览与分隔页反过来，先给整体图形再落到文字
- **Composition tendency**: 圆角卡片叠在暖白纸底上，靠柔和抬升而非描边分层；半径家族整卷统一为 12／24／40 三档（pill 与小标签 12，内容卡 24，出血大板 40），任何页不引入第四档；每季六页在“左图右文／上题下三栏／大板出血／环形定位／对角错落／满幅卡阵”之间轮换，四季轮换顺序一致，使同季第 n 页与另一季第 n 页构图呼应
- **Cross-page continuity**: 页眉左侧季名＋节气序号、右上角年轮小环＋指针、页脚右侧页码与来源提示，24 个节气页完全一致；变化的只有季语义色、题字、主视觉与内容
- **Spacing posture**: variable by page rhythm——分隔页与封面 breathing，节气页 dense，总览与来源页 anchor
- **Spacing anchors**: page margin 64；block gap 28；column gutter 32；corner radius 24；body leading 38

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-filled/clock | 交节时刻的时间标记 |
| tabler-filled/calendar | 公历日期标记 |
| tabler-filled/sun | 昼长、日照、太阳高度相关标记 |
| tabler-filled/moon | 夜长与冬季页的对照标记 |
| tabler-filled/leaf | 春季与草木物候标记 |
| tabler-filled/flame | 夏季与暑热标记 |
| tabler-filled/droplet | 降水、露、雨相关物候标记 |
| tabler-filled/cloud | 冬季与霜雪、云气标记 |
| tabler-filled/feather | 候鸟类物候标记 |
| tabler-filled/bug | 虫类物候标记 |
| tabler-filled/soup | 时令饮食标记 |
| tabler-filled/bowl | 时令饮食的第二种载体 |
| tabler-filled/book | 出处与文献标记 |
| tabler-filled/link | 来源页的外链标记 |
| tabler-filled/star | 三候序号与要点标记 |
| tabler-filled/map-pin | 年轮上的当前定位标记 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P02 | chart | line_chart | 用 12 个中气日的太阳上中天仰角画出一年的太阳高度曲线，给全年总览一条可读的量化脊梁 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| elem_lichun.png | 310x308 | 1:1 | 立春页主视觉：解冻的东风与初芽 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_spring_elements.png; treatment=slice; | none | local |
| elem_yushui.png | 326x282 | 1.16:1 | 雨水页主视觉：獭与初萌的草木 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_spring_elements.png; treatment=slice; | none | local |
| elem_jingzhe.png | 309x310 | 1:1 | 惊蛰页主视觉：桃花与惊醒的虫 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_spring_elements.png; treatment=slice; | none | local |
| elem_chunfen.png | 251x305 | 0.82:1 | 春分页主视觉：竖起的蛋与燕子 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_spring_elements.png; treatment=slice; | none | local |
| elem_qingming.png | 308x308 | 1:1 | 清明页主视觉：青团与柳枝 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_spring_elements.png; treatment=slice; | none | local |
| elem_guyu.png | 309x294 | 1.05:1 | 谷雨页主视觉：新茶与香椿 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_spring_elements.png; treatment=slice; | none | local |
| elem_lixia.png | 314x312 | 1:1 | 立夏页主视觉：称与立夏蛋 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_summer_elements.png; treatment=slice; | none | local |
| elem_xiaoman.png | 260x296 | 0.88:1 | 小满页主视觉：将满的麦穗与苦菜 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_summer_elements.png; treatment=slice; | none | local |
| elem_mangzhong.png | 312x317 | 0.98:1 | 芒种页主视觉：青梅与带芒的麦 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_summer_elements.png; treatment=slice; | none | local |
| elem_xiazhi.png | 287x309 | 0.93:1 | 夏至页主视觉：过水面与最短的影 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_summer_elements.png; treatment=slice; | none | local |
| elem_xiaoshu.png | 319x311 | 1.03:1 | 小暑页主视觉：新米碗与蟋蟀 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_summer_elements.png; treatment=slice; | none | local |
| elem_dashu.png | 286x323 | 0.89:1 | 大暑页主视觉：仙草碗与萤火 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_summer_elements.png; treatment=slice; | none | local |
| elem_liqiu.png | 337x315 | 1.07:1 | 立秋页主视觉：西瓜与凉风 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_autumn_elements.png; treatment=slice; | none | local |
| elem_chushu.png | 360x310 | 1.16:1 | 处暑页主视觉：鸭与河灯 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_autumn_elements.png; treatment=slice; | none | local |
| elem_bailu.png | 338x316 | 1.07:1 | 白露页主视觉：草叶露珠与茶壶 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_autumn_elements.png; treatment=slice; | none | local |
| elem_qiufen.png | 337x333 | 1:1 | 秋分页主视觉：秋汤与月 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_autumn_elements.png; treatment=slice; | none | local |
| elem_hanlu.png | 324x248 | 1.31:1 | 寒露页主视觉：菊与芝麻 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_autumn_elements.png; treatment=slice; | none | local |
| elem_shuangjiang.png | 334x322 | 1.04:1 | 霜降页主视觉：柿子与霜 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_autumn_elements.png; treatment=slice; | none | local |
| elem_lidong.png | 336x274 | 1.23:1 | 立冬页主视觉：饺子与初冰 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_winter_elements.png; treatment=slice; | none | local |
| elem_xiaoxue.png | 334x272 | 1.23:1 | 小雪页主视觉：咸菜坛与鱼干 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_winter_elements.png; treatment=slice; | none | local |
| elem_daxue.png | 317x295 | 1.07:1 | 大雪页主视觉：腌肉与雪 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_winter_elements.png; treatment=slice; | none | local |
| elem_dongzhi.png | 311x288 | 1.08:1 | 冬至页主视觉：饺子汤圆与回头的太阳 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_winter_elements.png; treatment=slice; | none | local |
| elem_xiaohan.png | 345x306 | 1.13:1 | 小寒页主视觉：菜饭锅与喜鹊 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_winter_elements.png; treatment=slice; | none | local |
| elem_dahan.png | 314x309 | 1.02:1 | 大寒页主视觉：扫帚与厚冰 | Illustration | 作为该页唯一的具象锚点，与题字构成左上／右侧的一组，不与文字重叠 | no-crop | slice | Generated | Derived from sheet_winter_elements.png; treatment=slice; | none | local |
| word_lichun.png | 381x189 | 2.02:1 | 立春 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_a.png; treatment=slice; | embedded | local |
| word_yushui.png | 379x186 | 2.04:1 | 雨水 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_a.png; treatment=slice; | embedded | local |
| word_chunfen.png | 384x188 | 2.04:1 | 春分 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_a.png; treatment=slice; | embedded | local |
| word_qingming.png | 377x192 | 1.96:1 | 清明 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_a.png; treatment=slice; | embedded | local |
| word_guyu.png | 380x182 | 2.09:1 | 谷雨 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_a.png; treatment=slice; | embedded | local |
| word_lixia.png | 662x300 | 2.21:1 | 立夏 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_a.png; treatment=slice; | embedded | local |
| word_xiaoman.png | 379x190 | 1.99:1 | 小满 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_a.png; treatment=slice; | embedded | local |
| word_mangzhong.png | 377x194 | 1.94:1 | 芒种 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_b.png; treatment=slice; | embedded | local |
| word_xiazhi.png | 371x200 | 1.85:1 | 夏至 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_b.png; treatment=slice; | embedded | local |
| word_xiaoshu.png | 380x202 | 1.88:1 | 小暑 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_b.png; treatment=slice; | embedded | local |
| word_dashu.png | 380x201 | 1.89:1 | 大暑 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_b.png; treatment=slice; | embedded | local |
| word_liqiu.png | 384x192 | 2.00:1 | 立秋 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_b.png; treatment=slice; | embedded | local |
| word_chushu.png | 380x202 | 1.88:1 | 处暑 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_b.png; treatment=slice; | embedded | local |
| word_bailu.png | 365x202 | 1.81:1 | 白露 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_b.png; treatment=slice; | embedded | local |
| word_qiufen.png | 385x194 | 1.98:1 | 秋分 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_b.png; treatment=slice; | embedded | local |
| word_hanlu.png | 390x209 | 1.87:1 | 寒露 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_c.png; treatment=slice; | embedded | local |
| word_shuangjiang.png | 396x204 | 1.94:1 | 霜降 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_c.png; treatment=slice; | embedded | local |
| word_lidong.png | 394x204 | 1.93:1 | 立冬 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_c.png; treatment=slice; | embedded | local |
| word_xiaoxue.png | 394x200 | 1.97:1 | 小雪 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_c.png; treatment=slice; | embedded | local |
| word_daxue.png | 390x200 | 1.95:1 | 大雪 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_c.png; treatment=slice; | embedded | local |
| word_dongzhi.png | 393x206 | 1.91:1 | 冬至 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_c.png; treatment=slice; | embedded | local |
| word_xiaohan.png | 394x206 | 1.91:1 | 小寒 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_c.png; treatment=slice; | embedded | local |
| word_dahan.png | 389x207 | 1.88:1 | 大寒 的手写题字（display 层） | Lettering | 置于原生标题之上或之左，作 display 层；原生标题与副标题独立存在，保证可搜索可编辑 | no-crop | slice | Generated | Derived from sheet_lettering_c.png; treatment=slice; | embedded | local |
| orn_ring.png | 400x400 | 1:1 | 装饰母题：年轮圆环 | Illustration | 整卷复用的装饰件，只做陪衬，永不承载信息 | no-crop | slice | Generated | Derived from sheet_ornament.png; treatment=slice; | none | local |
| orn_corner.png | 251x148 | 1.70:1 | 装饰母题：角落云纹 | Illustration | 整卷复用的装饰件，只做陪衬，永不承载信息 | no-crop | slice | Generated | Derived from sheet_ornament.png; treatment=slice; | none | local |
| orn_sunmoon.png | 256x206 | 1.24:1 | 装饰母题：日月合符 | Illustration | 整卷复用的装饰件，只做陪衬，永不承载信息 | no-crop | slice | Generated | Derived from sheet_ornament.png; treatment=slice; | none | local |
| orn_divider.png | 258x72 | 3.58:1 | 装饰母题：小分隔花饰 | Illustration | 整卷复用的装饰件，只做陪衬，永不承载信息 | no-crop | slice | Generated | Derived from sheet_ornament.png; treatment=slice; | none | local |

## X. Speaker Notes Requirements

- **Generation**: disabled

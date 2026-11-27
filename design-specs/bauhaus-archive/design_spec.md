<!-- ppt-master-schema: design-spec/v1 -->
# 包豪斯 1919–1933 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | bauhaus_1919_1933_ppt169 |
| Canvas Format | ppt169 (1280×720) |
| Page Count | 13 |
| Primary Language | zh-CN |
| Target Audience | 对设计史感兴趣的大众与设计专业学生：听过“包豪斯”这个词，熟悉现代家具与无衬线字体的样子，但不清楚学校本身的时间线、制度与人物 |
| Communication Intent | 先讲清一所学校的来龙去脉（三地、三任校长、关闭），再解释它真正的发明——预备课程与工坊双导师制，用四件代表作品让方法可见，最后说明流散如何把方法带到世界 |
| Desired Audience Outcome | 听众能说出魏玛→德绍→柏林三阶段与年份，说出预备课程与双导师制如何运作，能把台灯、钢管椅、通用字体、德绍校舍与“艺术×工业”的方法联系起来，并知道关闭后理念经由谁、去了哪里 |
| Core Message / Ask / Action | 包豪斯只存在了 14 年、三易其址，但它把“造型教育 + 工坊生产”变成了一套可迁移的方法；1933 年的关闭反而让这套方法随师生流散，成为现代设计的通用语法 |
| Delivery Context | 主要为讲者主导的 25 分钟设计史讲座/课堂；次要为会后独立翻阅的专题讲义 |
| Artifact Afterlife | 作为设计史课程讲义与 ppt-master 示例 deck 留存，出处需可追溯 |
| Reading Mode | balanced |
| Content Strategy | balanced（未填 content_divergence）：以叙事弧重组研究材料，保留全部事实与出处，不引入研究外数字 |
| Design Style | 设计史档案册（custom）：纸本编辑排版 + 编辑式摄影裁切，包豪斯基本形作为页面场与图片窗口 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — explicit user instruction（任务书：Speaker Notes=true） |
| Custom Animations | enabled — explicit user instruction（任务书：Custom Animations=true，相邻页 Morph ≥2 处） |
| Narration Audio | disabled — explicit user instruction（任务书：Narration Audio=false） |
| Created Date | 2026-10-24 |

- **Confirmation provenance**: 用户把确认门明确委派给执行代理；Stage 1 选 `free_design`（无模板意图、无 workspace root），不启动 Confirm UI，无 UI 回执。Stage 2 三个方向：① 设计史档案册（选中）；② 构成主义暗场——墨黑底、海报式巨型年份与粗规则线、vintage-poster 渲染，放弃：暗场压低照片与纸本质感，且易滑向“海报贴纸”；③ 工坊纸样——纸雕层叠与柔和投影、paper-cut 渲染，放弃：亲和但与包豪斯机械精确的气质相悖。选①理由：受众是读者+听众双重身份，纸本编辑排版最接近“设计史专题”，基本形承担图片窗口与页面场，而不是装饰贴纸。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 64 px left/right, 56 px top, 48 px bottom |
| Content Area | x 64–1216, y 56–672 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: narrative, instructional
- **Mode Behavior**: 整体走叙事弧——1919 年的宣言（起）→ 三地十四年（展开）→ 方法：预备课程与双导师制（核心讲解，按 instructional 拆解顺序：先基础课再工坊）→ 四件作品作为方法的证据 → 1933 年关闭（转折）→ 流散与影响（解决）；标题写成推进的判断句，讲解页用并列结构便于比较。
- **Visual style**: custom
- **Visual Style References**: editorial, photo-editorial
- **Visual Style Behavior**: 暖白纸本底色上的编辑排版：细规则线、栏线、小号编号 kicker、大号年份数字（Arial Black）锚定页面；照片做编辑式裁切——放进圆/方/三角窗口、跨越栏线、或以双色调（墨黑×纸白）满版铺底；圆、方、三角作为页面场与图片遮罩出现，每页至多一个主形，红色只用于一个焦点，绝不散布成彩色几何贴纸；无阴影，层次靠规则线粗细与留白。
- **Theme**: 设计史专题刊物——像一本印刷精良的包豪斯展览图录
- **Tone**: 冷静、精确、带一点印刷品的温度

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F2EEE5 | 暖白纸本主底 |
| Secondary background | #E4DDCF | 次级纸面、图注底、分区色块 |
| Primary | #161616 | 墨黑：标题、粗规则线、暗场页底、双色调暗部 |
| Accent | #C23B22 | 朱红：每页唯一焦点（一个圆、一条线、一个年份） |
| Secondary accent | #B8862B | 赭黄：次级标记（阶段标签、时间刻度），用量少于朱红 |
| Body text | #1E1E1C | 正文 |
| Secondary text | #6B665C | 图注、出处、注释 |
| Divider | #BDB5A6 | 细规则线、栏线 |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: corporate-photo, screen-print
- **Image Rendering Behavior**: 以纪实摄影的真实材质与景深描绘无人的工坊场景（corporate-photo 负责光线、景深与材质真实感），再整体压成墨黑×纸白的双色调并带轻微半调网点与纸纹（screen-print 负责有限色与印刷质感）；画面安静、空旷、无文字无人物，可与 Commons 的历史照片同页并置而不突兀。
- **Visual**: 晨光中的空旷工坊——织机、金属车床、木工台，双色调印刷质感
- **Mood**: 像展览图录里一张翻拍的旧照片：安静、克制、有温度

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 几何无衬线粗体，呼应拜耳的无衬线主张 | Microsoft YaHei | Arial | sans-serif |
| Body | 中性无衬线 | Microsoft YaHei | Arial | sans-serif |
| Display | 海报黑体，用于巨型年份与编号 | Microsoft YaHei | Arial Black | sans-serif |
| Quote | 衬线引文，宣言与名句 | SimSun | Cambria | serif |

- **Title stack**: "Microsoft YaHei", Arial, sans-serif
- **Body stack**: "Microsoft YaHei", Arial, sans-serif
- **Display stack**: "Arial Black", "Microsoft YaHei", sans-serif
- **Quote stack**: SimSun, Cambria, serif
- **Role rationale**: Display 让 1919/1925/1933 等年份成为页面锚点；Quote 用衬线与无衬线形成编辑式对照，只用于宣言与引语。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 22 |
| Title | 40 |
| Subtitle | 28 |
| Lead | 26 |
| Annotation | 16 |
| Footnote | 13 |
| Cover title | 72 |
| Display | 120 |
| Quote | 34 |
| Kicker | 15 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: kicker（编号+章节）→ 判断句标题 → 一个焦点（年份/图片/基本形）→ 正文与图注
- **Composition tendency**: 不对称编辑栏；照片跨栏或嵌入基本形窗口；暗场页（P11）与满版照片页（P07）打断纸本节奏
- **Cross-page continuity**: 朱红圆作为贯穿母题——封面的大红圆在 P02 缩为宣言页的印章；作品三页（P08–P10）共用同一“展台”结构：左侧对象窗口的基本形依次由圆→方→三角变化；页眉统一一条细规则线 + 页码 + “BAUHAUS 1919–1933”
- **Spacing posture**: 按节奏变化——dense 页紧凑，anchor/breathing 页大留白
- **Spacing anchors**: page margin 64 px · block gap 32 px · column gutter 40 px · corner radius 0 px · body leading 1.5

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | chart | gantt_chart | 把魏玛、德绍、柏林三阶段与三任校长任期按真实年份长度排在同一时间轴上 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dessau_building.jpg | 3827×2983 | 1.28 | 德绍校舍原图（衍生母本，P07 原色使用） | Photo | 满版铺底，工坊翼玻璃幕墙占画面右侧，标题落在左侧天空/暗区 | adaptive | web | Sourced | Bauhaus Dessau building by Walter Gropius, exterior, workshop wing glass curtain wall and bridge visible, daylight, Wikimedia Commons CC/PD | none | local |
| dessau_duotone.jpg | 1800×1403 | 1.28 | 封面主视觉：校舍双色调 | Photo | 放进巨型方形窗口，朱红圆压住一角形成封面钩子 | adaptive | web | Sourced | Derived from dessau_building.jpg; treatment=duotone; 墨黑 #161616 × 纸白 #F2EEE5 | none | local |
| feininger_cathedral.jpg | 3272×4912 | 0.67 | P02 宣言封面木刻《大教堂》 | Artwork | 完整展示作品（不裁），旁边是衬线宣言引文 | no-crop | web | Sourced | Lyonel Feininger, Cathedral (Kathedrale), woodcut, title page of the Bauhaus Manifesto 1919, Wikimedia Commons public domain scan | none | local |
| workshop_scene.jpg | 2752×1536 | 1.79 | P05 工坊场景氛围图 | Scene | 放进右侧大矩形窗口并被一条栏线切开，左侧为工坊双导师结构 | adaptive | ai | Generated | 空旷的魏玛时代工坊：前景木质织机与纱线，中景金属工坊的车床与铜器，晨光从高窗斜射；无人物、无文字、无标识；四周留出安静暗部便于裁切 | none | local |
| mt8_lamp.jpg | 2152×1908 | 1.13 | P08 瓦根菲尔德台灯 | Product | 放进圆形窗口，灯罩球体与圆形窗口同心 | adaptive | web | Sourced | Wagenfeld table lamp MT8 / WG24, glass base, opal glass dome, chrome shaft, isolated or museum shot, Wikimedia Commons CC | none | local |
| wassily_chair.jpg | 2500×1953 | 1.28 | P09 布劳耶 B3 钢管椅 | Product | 放进方形窗口，椅子钢管与方框对齐 | adaptive | web | Sourced | Marcel Breuer Wassily chair B3, chrome tubular steel and black leather, three-quarter view, plain background, Wikimedia Commons CC | none | local |
| tel_aviv_white_city.jpg | 3264×2448 | 1.33 | P12 特拉维夫白城建筑（流散的落点之一） | Photo | 嵌入三角/梯形窗口，成为路线图的一个落点 | adaptive | web | Sourced | White City Tel Aviv Bauhaus International Style building, curved balconies, white facade, Wikimedia Commons CC | none | local |

- **Plan repair (2026-10-24, Step 5)**: bauhaus_masters_1926.jpg 在 Wikimedia/Openverse 多组变体与翻页后无合格候选；bayer_universal.png 原稿受版权保护（拜耳 1985 年去世），开放许可库中无此图。两行移出计划：P06 改为纯排版人物索引，P10 改用原生字母样张示意。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 以页面为准展开讲解与过渡；只用研究文件中有 fact_id 的事实，冲突处（伊顿离任时间、学生人数口径）按研究文件说明表述
- **Total duration**: 约 25 分钟
- **Notes style**: conversational，叙事+讲解
- **Presentation purpose**: 解释包豪斯的时间线、方法、作品与流散，让听众带走“方法而非风格”的判断

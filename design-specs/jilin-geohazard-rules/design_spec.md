<!-- ppt-master-schema: design-spec/v1 -->
# jilin_geohazard_rules_beautify - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | jilin_geohazard_rules_beautify |
| Canvas Format | ppt169 (1280×720) |
| Page Count | 20 |
| Primary Language | zh-CN |
| Target Audience | 全省市、县级自然资源主管部门及勘查、设计、施工、监理等参建单位的项目管理人员 |
| Communication Intent | 解读《吉林省地质灾害治理工程项目管理办法》：先交代出台背景与政策依据，再讲清七章框架与各环节规范要求，最后归纳主要特点，帮助各方明确流程、职责与时限 |
| Desired Audience Outcome | 听众知道《办法》的来由与依据，理解项目入库、实施、验收、运行管护的流程与时限，并能对照找到本单位职责 |
| Core Message / Ask / Action | 《办法》把地质灾害治理工程项目管理规范为从入库、实施、验收到运行管护、全过程监督的一整套运行规程 |
| Delivery Context | 主要为政策宣讲会上有主讲人的逐页解读；次要为政府网站公开附件供会后自主阅读 |
| Artifact Afterlife | 公开发布、存档，并作为各级主管部门与参建单位的培训参考 |
| Reading Mode | balanced |
| Content Strategy | keep source wording and page structure verbatim（Beautify 1:1 锁定：每页文字逐字不变，页数页序不变，只重做版式、层级、留白与视觉处理） |
| Design Style | 政务条文手册（源稿复刻方向）：白底、源稿政务蓝为主色、红色标注关键时限与禁止事项，以山形折线为跨页母题 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | disabled — final Stage-2 proactive policy (delegated): Beautify 逐字冻结，源稿备注页只有页码占位、无讲稿，不新增讲稿内容 |
| Custom Animations | enabled — explicit user instruction (2026-09-11，经协调者转达："示例 deck 必须有自定义动画"；对象级：主角进场、框架与配角不动，含 Morph 配对)；取代先前 Stage-2 委托值 disabled |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-11 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 左右 56px；上 24px（页眉区）；下 32px |
| Content Area | x 56–1224，y 112–688（页眉以下正文区） |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: briefing
- **Mode Behavior**: 以 briefing 为唯一基底：逐页中立、完整、可查找；源稿 20 页一一对应、顺序与文字逐字不变，页标题沿用源稿的章节式主题标题（"一、出台背景""四、规范内容"），同级条款同形同权，只在源稿已标注的关键词、时限与禁止事项上加强强调，不制造结论句。
- **Visual style**: custom
- **Visual Style Behavior**: 政务条文手册：白色纸面，页眉用左侧深色主题标题 + 蓝色章节标签 + 右上角圆形厅徽，页眉下一条细分隔线，其左段由一段蓝色山形折线（取自厅徽的山形）替代直线，作为全篇母题；条款抬头用满宽蓝色条带（白字、黄色高亮关键词），并列条款用同尺寸浅蓝底面板或编号行，编号用大号蓝色数字或圆形编号牌，流程用竖向或横向编号轨道并以连接线表达先后；小圆角（6px）、无投影或仅截图卡片有轻微投影；强调只用两级色：蓝色加粗标关键词，红色加粗标时限、禁止与关键结论；截图以白边卡片呈现，剪贴画保留原貌并加细框。
- **Theme**: 吉林省自然资源厅政务蓝身份延续——源稿蓝色页眉、红色强调、厅徽；把源稿零散的色块与艺术字统一为一套条文手册版式
- **Tone**: 庄重、清楚、便于查找

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 页面底色 |
| Secondary background | #EEF4FB | 并列条款面板、目录与流程底面 |
| Primary | #0070C0 | 源稿页眉蓝：条款条带、编号、连接线、蓝色关键词强调 |
| Accent | #D7141A | 源稿红色强调：时限、禁止事项、关键结论（加粗） |
| Secondary accent | #E07A1F | 源稿橙色：主要特点交替标题、第五章保修期内外对照中的"期内"一侧 |
| Body text | #1F2328 | 正文 |
| Secondary text | #5A6472 | 注释、英文机构名、次级说明 |
| Divider | #C9D6E5 | 细分隔线、面板描边 |
| Title text | #0B2A5B | 页标题、封面机构名（源稿深藏青 #002060 的延续） |
| Highlight | #FFC000 | 蓝色条带内的黄色关键词高亮（源稿同色） |
| Panel edge | #5B9BD5 | 面板左侧色条、次级编号（源稿主题 accent1） |

**Inline emphasis mapping (source → deck)**: 源稿蓝字 #0000FF → Primary 加粗；源稿红字 #FF0000 / #C00000 → Accent 加粗；源稿绿字 #00B050（第17页"保修期限内/施工单位"与蓝字"超出保修期限/管护单位"对照）→ Secondary accent 加粗；蓝色条带内黄字 #FFC000 → Highlight。只改颜色角色，不增删、不移动被强调的字；源稿逐行切碎的同色片段合并为一个强调片段；以红/蓝为底色、内部夹黑字的"反相"段落改为"引导词着色 + 其余正文色"。

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 端正无衬线黑体，加粗 | Microsoft YaHei | Arial | sans-serif |
| Body | 中性无衬线 | Microsoft YaHei | Arial | sans-serif |
| Numeral | 几何无衬线数字，加粗 | Arial | Arial | sans-serif |

- **Title stack**: "Microsoft YaHei", Arial, sans-serif
- **Body stack**: "Microsoft YaHei", Arial, sans-serif
- **Numeral stack**: Arial, "Microsoft YaHei", sans-serif
- **Role rationale**: numeral 为反复出现的步骤编号、目录编号与条款序号（01–06、1–5），用 Arial 粗体与中文正文形成对比。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 36 |
| Subtitle | 28 |
| Annotation | 18 |
| Cover title | 56 |
| Lead | 26 |
| Numeral | 32 |
| Footnote | 14 |

Body 取自 `observed.sizes_pt` 首位 18pt（承载 3190 字）× 4/3 = 24px，源画布 1280px 与 ppt169 同宽，缩放系数 1；与各页正文实际渲染字号（18pt 为主）一致。满页（第6、13、15、17页）在 ±2px 带内用 22px。

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 页眉主题标题 → 条款条带/小标题 → 编号条目或段落；读者先定位"在讲哪一章哪一条"，再逐条读
- **Composition tendency**: 条款页用"蓝色条款条带 + 编号网格/编号轨道"；流程与时限页用带连接线的编号轨道；带图页用图文分栏，截图以卡片呈现；封面与封底用满宽蓝色带承载标题
- **Cross-page continuity**: 页眉（主题标题 + 章节标签 + 厅徽 + 山形折线分隔线）在第3–19页恒定；第8、9、11、13页的"第X条：X单位在项目实施过程中职责"条带同形；编号牌样式全篇一致
- **Spacing posture**: 以 dense 为主，按 page_rhythm 在第12、18页放开留白
- **Spacing anchors**: page margin 56px · block gap 24px · column gutter 32px · corner radius 6px · body leading 1.45×（24px 正文行距约 35px）

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-filled/book.svg | 总则、法规文件 |
| icons/tabler-filled/database.svg | 项目库、入库 |
| icons/tabler-filled/building-bridge-2.svg | 工程实施 |
| icons/tabler-filled/clipboard-check.svg | 验收 |
| icons/tabler-filled/shield-check.svg | 运行管护、安全 |
| icons/tabler-filled/eye.svg | 监督检查、监理 |
| icons/tabler-filled/file-text.svg | 附则、设计文件 |
| icons/tabler-filled/scale.svg | 管理原则、法规依据 |
| icons/tabler-filled/zoom-check.svg | 核查、审核 |
| icons/tabler-filled/calendar.svg | 期限 |
| icons/tabler-filled/clock.svg | 时限 |
| icons/tabler-filled/archive.svg | 资料归档 |
| icons/tabler-filled/list-check.svg | 资料清单 |
| icons/tabler-filled/writing-sign.svg | 签订协议、明确责任 |
| icons/tabler-filled/map-pin.svg | 设置标牌、项目现场 |
| icons/tabler-filled/circle-check.svg | 核销、完成 |
| icons/tabler-filled/mountain.svg | 地质灾害、山体 |
| icons/tabler-filled/rosette.svg | 主要特点 |
| icons/tabler-filled/flag.svg | 目标、要点 |
| icons/tabler-filled/alert-triangle.svg | 禁止、风险 |
| icons/tabler-filled/briefcase.svg | 单位职责 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.jpeg | 550×550 | 1.00 | 吉林省自然资源厅厅徽（封面、目录、封底及内容页页眉的机构标识） | Logo | 圆形裁切的厅徽，封面/封底放大，内容页页眉右上角小尺寸 | adaptive | user | Existing | 源稿第1、2、20页与版式页眉使用；源稿即以圆形裁切显示，圆形裁切只去掉青色方底角 | none | local |
| 2.png | 886×763 | 1.16 | 第3页证据：2023年《通知》的网站公开页面截图 | Screenshot | 白边截图卡片，与背景段落并排，作为"原通知"证据 | no-crop | user | Existing | 源稿第3页右侧 | none | local |
| 3.png | 774×874 | 0.89 | 第4页证据：中国政府网《地质灾害防治条例》页面截图 | Screenshot | 截图卡片，取上部含网站头与条例标题的区域，与另两张截图叠放成证据栏 | adaptive | user | Existing | 源稿第4页已裁切为上部横条（显示比 3.56）；焦点为顶部网站头与"地质灾害防治条例"标题 | none | local |
| 4.png | 1206×435 | 2.77 | 第4页证据：自然资源部规章《地质灾害防治单位资质管理办法》页面截图 | Screenshot | 证据栏中的截图卡片，完整显示 | no-crop | user | Existing | 源稿第4页 | none | local |
| 5.png | 795×255 | 3.12 | 第4页证据：国家法律法规数据库《吉林省地质灾害防治条例》页面截图 | Screenshot | 证据栏中的截图卡片，完整显示 | no-crop | user | Existing | 源稿第4页 | none | local |
| 6.jpeg | 500×375 | 1.33 | 第7页配图："政府采购 公开·公正·公平"剪贴画，对应第八条"政府采购" | Clipart | 与第八条段落同栏的上方配图，细框完整显示 | no-crop | user | Existing | 源稿第7页下方（源稿裁成 1.14），图内含文字，完整显示 | none | local |
| 7.jpeg | 375×279 | 1.34 | 第7页配图："质量终身责任"卡通（勘察、设计、施工、监理），对应第七条主管部门职责 | Clipart | 与第七条段落同栏的上方配图，细框完整显示 | no-crop | user | Existing | 源稿第7页上方 | none | local |
| 8.jpeg | 430×242 | 1.78 | 第12页配图：转包、分包、挂靠剪影图，对应第十五条禁止转包/违法分包 | Clipart | 右侧配图卡片，与左侧条款并排 | no-crop | user | Existing | 源稿第12页（源稿裁成 1.12），图内含"转包/分包/挂靠"字样，完整显示 | none | local |

## X. Speaker Notes Requirements

- **Generation**: disabled

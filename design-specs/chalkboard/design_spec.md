<!-- ppt-master-schema: design-spec/v1 -->
# 粉笔写下的节日 · 教师节黑板报 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 粉笔写下的节日 · 教师节黑板报 |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 13 |
| Primary Language | zh-Hans-CN |
| Target Audience | 中小学师生与到校家长,以及负责出黑板报的宣传委员和班主任;他们知道教师节是 9 月 10 日,但基本说不出这个日期怎么定下来的,也没见过教师队伍的整体数字 |
| Communication Intent | 先把教师节的来历讲清楚(四次改期与 1985 年设节的动议链条),再用官方数据让"老师"这个群体有具体体量感,最后落到今天就能做出的尊师表达;顺序上"讲清来历"优先于"讲数据",数据服务于情感落点 |
| Desired Audience Outcome | 看完能说出教师节为什么定在 9 月 10 日、能举出至少一个尊师典故,并愿意在今天对老师说一句具体的话 |
| Core Message / Ask / Action | 教师节不是凭空定下来的——它被提了四次、改了四次日期,才在 1985 年落到 9 月 10 日;今天全国有 1870.10 万名专任教师站在讲台后面 |
| Delivery Context | 主:教室投影,班会课上由老师或宣传委员逐页讲;次:导出后作为校园公众号推文素材与打印板报底稿留存 |
| Artifact Afterlife | 存档复用——明年教师节换一组数据可再用;也可拆页作为黑板报版式参考 |
| Reading Mode | balanced |
| Content Strategy | 自采事实为唯一数字与史实来源,官方共识与出处不确的传闻分开写并标注;版式上按黑板报栏目自由重组,不受源文件段落顺序约束 |
| Design Style | 黑板报:深板面 + 干涩粉笔笔触 + 粉质彩粉点缀;每页一块板报版面(报头 + 主栏 + 小栏目 + 粉笔花边) |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 最终 Stage-2 proactive 默认值 `true`,用户未作相反指示 |
| Custom Animations | enabled — 用户在任务书中明确要求 `animations.json` 与自定义入场/承接动画 |
| Narration Audio | disabled — 最终 Stage-2 proactive 默认值 `false` |
| Created Date | 2026-09-10 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上下左右各 56px;板面木框内侧再留 20px 粉笔留白 |
| Content Area | x 56–1224, y 56–664(可用 1168 × 608) |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: narrative, instructional
- **Mode Behavior**: 全卷主轴用 narrative 的 situation → tension → resolution 走"教师节被提了四次、改了四次日期,才落到 9 月 10 日"这条曲折;每一页内部改用 instructional 的分块并列——一个主栏把这一段讲透,两到三个小栏目(数字角/小知识角/名言角)平行承载可扫读的碎片,像真实黑板报那样一版多栏。转场页用板擦擦过的动作完成幕的切换。
- **Visual style**: chalkboard
- **Theme**: 教室后墙的一整排黑板报——深板面、木框、粉笔槽;报头是手写粉笔艺术字,主栏用手绘粉笔框圈住,小栏目用非对齐点的粉笔线框,页脚有粉笔灰与半截粉笔头
- **Tone**: 怀旧、亲切、课堂气;不端着,也不卖萌

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #1E2B27 | 黑板板面主色(深墨绿石板) |
| Secondary background | #26352F | 栏目底板、板面分区、木框内侧的稍亮区块 |
| Primary | #F4F1E8 | 主粉笔白——报头、主标题、主栏正文的主要笔迹 |
| Accent | #F3C969 | 粉质暖黄——重点圈画、关键数字、当前节点 |
| Secondary accent | #9FD0C0 | 粉质薄荷绿——次级强调、图表第二序列、时间轴刻度 |
| Body text | #E8E4D8 | 正文粉笔字 |
| Secondary text | #B4AE9E | 注释、栏目落款、图注、来源行 |
| Divider | #46564F | 粉笔分栏线、表格格线、栏目边框 |
| Chalk rose | #E8A0A8 | 粉质胭脂——图表第三序列与引文标记 |
| Surface | #2B3A34 | 小栏目卡片抬起一档的底 |
| Grid | #38473F | 图表网格发丝线(比 divider 更淡) |
| Block shade | #24322C | 手绘框的错位投影块(平涂,非阴影) |

### AI Image Strategy

- **Image Rendering**: chalkboard
- **Visual**: 粉笔画在深色石板上——干涩起毛的白色主线、粉质彩色点染、笔画末端有断续与粉尘,没有渐变与高光,没有描边外框
- **Mood**: 课间刚被人画完的那块黑板报,粉笔灰还浮在空气里;像小学教室后墙拍下来的一角

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 手写楷体,粉笔书写的顿挫感 | KaiTi | Trebuchet MS | serif |
| Body | 清晰黑体,投影可读 | Microsoft YaHei | Arial | sans-serif |
| Quote | 古文引句,竖排感的楷书 | KaiTi | Times New Roman | serif |
| Data | 等高数字,图表与数字角专用 | Trebuchet MS | Trebuchet MS | sans-serif |
| Annotation | 小字注释与图注 | Microsoft YaHei | Arial | sans-serif |
| Emphasis | 等高数字,比率强调 | Trebuchet MS | Trebuchet MS | sans-serif |

- **Typography upgrade (Reference)**: 若目标机安装了「华文行楷」或「方正粉笔体」,可将 Title 与 Quote 角色替换为其一,粉笔手写感更强;未安装时保持 KaiTi
- **Title stack**: `KaiTi, "Trebuchet MS", serif`
- **Body stack**: `"Microsoft YaHei", Arial, sans-serif`
- **Quote stack**: `KaiTi, "Times New Roman", serif`
- **Data stack**: `"Trebuchet MS", "Microsoft YaHei", sans-serif`
- **Annotation stack**: `"Microsoft YaHei", Arial, sans-serif`
- **Emphasis stack**: `"Trebuchet MS", "Microsoft YaHei", sans-serif`
- **Role rationale**: Emphasis 是 P09 三个生师比数字反复出现的比率显示档,低于 Data 的 64 而高于 Subtitle,须单独命名;Quote 与 Data 各自需要不同族——古文引句要楷体的书写体势,而 KaiTi 的数字不等高,图表与数字角必须换成等高数字的 Trebuchet MS

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 44 |
| Subtitle | 32 |
| Cover title | 84 |
| Column head | 28 |
| Lead | 30 |
| Quote | 30 |
| Data | 64 |
| Annotation | 18 |
| Emphasis | 40 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 视线从左上角报头(艺术字 + 原生标题)进入,沿主栏向右下读完,再被粉笔花边引到右侧或下方的小栏目;每页只有一个主栏
- **Composition tendency**: 一版多栏的板报式分区——主栏占约三分之二,小栏目沿一条边排开;分区靠粉笔线与留白,不靠卡片堆叠
- **Cross-page continuity**: 木框与粉笔槽每页复现且位置不变;报头永远在左上;页脚右下角永远有半截粉笔与粉笔灰;时间轴弧线在 P03–P05 连续推移
- **Spacing posture**: variable by page rhythm——anchor 页放空,dense 页栏目排满但每栏内部保持行距宽松
- **Spacing anchors**: 页边距 56px;区块间距 32px;分栏槽 40px;圆角 12px;正文行高 38px

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/chalkboard-teacher.svg | 教师、讲台、课堂角色 |
| icons/tabler-outline/school.svg | 学校、学段、校园场景 |
| icons/tabler-outline/pencil.svg | 书写、提议、起草 |
| icons/tabler-outline/book-2.svg | 典籍、课文、引文出处 |
| icons/tabler-outline/calendar-event.svg | 日期、节点、改期 |
| icons/tabler-outline/quote.svg | 名言角、引句标记 |
| icons/tabler-outline/award.svg | 表彰、优秀教师 |
| icons/tabler-outline/users-group.svg | 教师队伍、人数规模 |
| icons/tabler-outline/star.svg | 粉笔星点缀、重点标记 |
| icons/tabler-outline/bulb.svg | 小知识角、提示 |
| icons/tabler-outline/ruler-2.svg | 度量、比例、生师比 |
| icons/tabler-outline/world.svg | 各国教师节 |
| icons/tabler-outline/snowflake.svg | 程门立雪 |
| icons/tabler-outline/mail-heart.svg | 慰问信、给老师的话 |
| icons/tabler-outline/link.svg | 来源链接栏 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P08 | chart | column_chart | 按学段比较 2025 年专任教师人数,让"1870 万"落成七根可读的柱子 |
| P09 | chart | horizontal_bar_chart | 比较四个学段专任教师中本科及以上学历的比例,呈现学历结构的台阶 |
| P10 | table | record_table | 六个国家/国际组织各占一行,列出教师节日期与它的来历 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_lettering.png | 1760×627 | 2.81:1 | 封面刊头艺术字「粉笔写下的节日」 | Illustration | 横贯封面上半的手写粉笔大字,原生副标题在其正下方另起一行 | no-crop | slice | Generated | Derived from cover_head_sheet.png; grid cell 1 | embedded | local |
| head_p02.png | 800×158 | 5.06:1 | P02 刊头字 | Illustration | 报头左上角,原生小标题在其右下 | no-crop | slice | Generated | Derived from head_sheet_a.png; grid cell 1 | embedded | local |
| head_p03.png | 800×124 | 6.46:1 | P03 刊头字 | Illustration | 报头左上角 | no-crop | slice | Generated | Derived from head_sheet_a.png; grid cell 2 | embedded | local |
| head_p04.png | 800×139 | 5.75:1 | P04 刊头字 | Illustration | 报头左上角,与 P03 同位承接 | no-crop | slice | Generated | Derived from head_sheet_a.png; grid cell 3 | embedded | local |
| head_p05.png | 800×170 | 4.7:1 | P05 刊头字 | Illustration | 报头左上角 | no-crop | slice | Generated | Derived from head_sheet_a.png; grid cell 4 | embedded | local |
| head_p06.png | 800×174 | 4.61:1 | P06 刊头字 | Illustration | 报头左上角 | no-crop | slice | Generated | Derived from head_sheet_a.png; grid cell 5 | embedded | local |
| head_p07.png | 1400×255 | 5.49:1 | P07 转场页刊头字 | Illustration | 居中放大,作为幕间大字 | no-crop | slice | Generated | Derived from head_sheet_a.png; grid cell 6 | embedded | local |
| head_p08.png | 800×148 | 5.4:1 | P08 刊头字 | Illustration | 报头左上角 | no-crop | slice | Generated | Derived from head_sheet_b.png; grid cell 1 | embedded | local |
| head_p09.png | 800×143 | 5.58:1 | P09 刊头字 | Illustration | 报头左上角 | no-crop | slice | Generated | Derived from head_sheet_b.png; grid cell 2 | embedded | local |
| head_p10.png | 800×201 | 3.99:1 | P10 刊头字 | Illustration | 报头左上角 | no-crop | slice | Generated | Derived from head_sheet_b.png; grid cell 3 | embedded | local |
| head_p11.png | 800×234 | 3.42:1 | P11 刊头字 | Illustration | 报头左上角 | no-crop | slice | Generated | Derived from head_sheet_b.png; grid cell 4 | embedded | local |
| head_p12.png | 800×251 | 3.18:1 | P12 刊头字 | Illustration | 报头左上角 | no-crop | slice | Generated | Derived from head_sheet_b.png; grid cell 5 | embedded | local |
| head_p13.png | 800×201 | 3.98:1 | P13 刊头字 | Illustration | 报头左上角 | no-crop | slice | Generated | Derived from head_sheet_b.png; grid cell 6 | embedded | local |
| art_chalk_stub.png | 694×483 | 1.44:1 | 半截粉笔与板擦——页脚复现物与承接件 | Illustration | 页脚右下角小尺寸复现;P07 放大为主角 | no-crop | slice | Generated | Derived from chalk_sheet.png; grid cell 1 | none | local |
| art_podium.png | 765×593 | 1.29:1 | 讲台与黑板一角——封面与数字页的场景锚 | Illustration | 封面右下角压住木框;P08 缩小为栏目角标 | no-crop | slice | Generated | Derived from chalk_sheet.png; grid cell 2 | none | local |
| art_book_brush.png | 792×519 | 1.53:1 | 线装书与毛笔——典故与引文栏的插图 | Illustration | P11 主栏右侧 | no-crop | slice | Generated | Derived from chalk_sheet.png; grid cell 3 | none | local |
| art_snow_gate.png | 800×604 | 1.32:1 | 程门立雪——雪中门前两个身影 | Illustration | P11 主栏主视觉,与引文左右并置 | no-crop | slice | Generated | Derived from chalk_sheet.png; grid cell 4 | none | local |
| art_globe_caps.png | 800×511 | 1.56:1 | 地球与不同学士帽——各国教师节栏插图 | Illustration | P10 表格右上角留白处 | no-crop | slice | Generated | Derived from chalk_sheet.png; grid cell 5 | none | local |
| art_flower_card.png | 771×469 | 1.64:1 | 粉笔花与贺卡——收尾页尾花 | Illustration | P13 右下尾花 | no-crop | slice | Generated | Derived from chalk_sheet.png; grid cell 6 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页写给站在班上讲这块板报的老师或宣传委员——先一句把本页的板报版面指给听众看,再按主栏、小栏目的顺序讲;所有数字与史实只复述页面上已有的内容,不引入页面外的新事实;古文引句先读原文再给一句白话;涉及出处不确的传闻一律不讲
- **Total duration**: 全卷约 11–13 分钟,平均每页 50–60 秒,P07 转场页约 20 秒
- **Notes style**: conversational——课堂口语,可以直接对学生发问
- **Presentation purpose**: 先把教师节的来历讲清楚,再用官方数据让教师群体有体量感,最后落到今天就能做出的尊师表达

<!-- ppt-master-schema: design-spec/v1 -->
# 中国铁路 2024:数据与现场 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 中国铁路 2024:数据与现场 |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 15 |
| Primary Language | zh-CN |
| Target Audience | 来访的省交通运输部门代表团(处级与业务骨干),熟悉交通运输统计口径,关心全国铁路的总量、结构与本省可对标的指标,但未系统读过《2024年铁道统计公报》 |
| Communication Intent | 先完整汇报 2024 年全国铁路的运输生产、建设、装备、路网与节能减排数据,让来访方掌握全年事实;其次通过国际对照与现场影像建立直观印象;最后给出三条可带走的判断 |
| Desired Audience Outcome | 来访方能复述 2024 年客运、货运、投资与路网的关键数值及其同比方向,知道每个数字出自公报的哪一处,并能区分公报口径与世界银行口径 |
| Core Message / Ask / Action | 2024 年全国铁路客运创历史高位(43.12 亿人,+11.9%),货运总量稳中有升而周转量小幅回落,路网与装备继续扩张,能耗强度微升而主要污染物持续下降 |
| Delivery Context | 主要为有主讲人的现场汇报(约 25 分钟,会议室投影);次要为会后留档传阅的电子文件 |
| Artifact Afterlife | 作为接待记录与数据引用底稿留档,供对方回本省后按页引用并核对出处 |
| Reading Mode | balanced |
| Content Strategy | 数值与口径严格跟随附件,一处不改;叙述结构由编者重组为汇报节奏,凡属编者归纳的框架页在页面上标注"整理" |
| Design Style | 数据新闻式的证据版面 + 瑞士栅格的克制留白 + 照片主导的现场页,构成"数据"与"现场"两种质地交替的汇报 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 工作流默认 true,用户未提出相反指示 |
| Custom Animations | enabled — 用户明确要求"要有自定义动画和 Morph" |
| Narration Audio | disabled — 用户未要求旁白,工作流默认 false |
| Created Date | 2026-09-12 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 左右 72px,上 64px,下 56px |
| Content Area | x 72–1208,y 64–664(页脚来源条占 y 664–700) |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: pyramid, briefing
- **Mode Behavior**: 开篇用 pyramid 把全年判断提到第二页,主体按 briefing 的等权板块推进(客运→货运→周转→装备→路网→国际→科技安全→绿色→监管),每个板块的标题写成一句可复述的判断句,板块内先给数字再给结构;末页回到三条判断收束。板块之间不制造悬念,也不为节奏牺牲完整性。
- **Visual style**: custom
- **Visual Style References**: data-journalism, swiss-minimal, photo-editorial
- **Visual Style Behavior**: 由 data-journalism 负责数据页的多栏证据密度、边注与每页底部的来源条;由 swiss-minimal 负责统一的左对齐栅格、直角容器、发丝分隔线与大留白,容器只用直角矩形和 1px 规则线,不用圆角卡片堆叠;由 photo-editorial 负责现场页——照片整幅出血、文字只作为压在照片安静区的点与说明,署名以极小字号贴在照片边缘。两种质地交替出现:数据页白底高密度,现场页深色照片低密度。
- **Theme**: 铁轨的水平线——每页顶部一条 2px 主色横规则线贯穿版心,页码与板块名坐在这条线下方,像时刻表的表头;数据页在这条线下展开栅格,现场页让照片穿过这条线。
- **Tone**: 克制、可核对、有现场温度

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 数据页底色 |
| Secondary background | #F2F5F9 | 表格斑马行、KPI 底板、边注区 |
| Primary | #0B3A6F | 顶部规则线、标题、图表主系列、板块名 |
| Accent | #C8102E | 当年值、需要读者先看的一个数字、图表中的当前系列 |
| Secondary accent | #1E6FB8 | 图表次系列、对照系列、链接性标注 |
| Body text | #1E2733 | 正文与表格正文 |
| Secondary text | #5A6775 | 注记、单位、照片署名、来源条 |
| Divider | #D8DEE6 | 表格横线、栅格发丝线 |
| Surface | #F8FAFC | 图表绘图区底 |
| Grid | #E6EBF1 | 图表网格线(比分隔线更浅) |
| Scrim | #0A1B2E | 照片上的压暗层与现场页文字底 |
| Positive | #2E7D32 | 同比上升的方向标注 |
| Negative | #C62828 | 同比下降的方向标注 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 黑体/方正的公文分量,笔画平直无修饰 | SimHei | Arial | sans-serif |
| Body | 屏幕可读的中性无衬线 | Microsoft YaHei | Arial | sans-serif |
| Display | 与标题同族的重量,承担页面上最大的数字 | SimHei | Arial | sans-serif |
| Annotation | 与正文同族,用于注记与单位 | Microsoft YaHei | Arial | sans-serif |
| Footnote | 与正文同族,用于来源条与照片署名 | Microsoft YaHei | Arial | sans-serif |

- **Title stack**: SimHei, Arial, sans-serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Display stack**: SimHei, Arial, sans-serif
- **Annotation stack**: Microsoft YaHei, Arial, sans-serif
- **Footnote stack**: Microsoft YaHei, Arial, sans-serif
- **Role rationale**: Display 与 Title 同族但独立成角色,因为 15 页中有 6 页把一个数字放到 60px 以上;Annotation 与 Footnote 同族不同号,分别承担图表注记与全卷来源条/照片署名两种复现结构。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 40 |
| Subtitle | 32 |
| Cover title | 76 |
| Lead | 28 |
| Display | 64 |
| Annotation | 18 |
| Footnote | 15 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 从顶部规则线下的判断句标题开始,向下进入左侧的主证据(图/表/大数),右侧或下方接解释与结构拆分,最后落到页底来源条
- **Composition tendency**: 数据页用两栏或"主证据 + 右侧窄解释栏"的不对称分割;现场页取消栅格,照片整幅出血,文字收到一角
- **Cross-page continuity**: 顶部 2px 主色规则线、右上角板块名、页底来源条三件框架元素每页复现且不参与动画;复兴号封面照片在 P01→P02 之间以同一构件缩放推移;货运总量数字在 P06→P07 之间推移
- **Spacing posture**: 按 page_rhythm 变化——dense 页贴近栅格上限,breathing 页把内容压到半幅以下
- **Spacing anchors**: 页边距 72px;块间距 32px;栏间距 40px;圆角半径 0px;正文行高 1.7em(≈41px)

## VI. Icon Usage Specification

- **Primary bundled library**: chunk-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/chunk-filled/train.svg | 客运、列车、动车组 |
| icons/chunk-filled/users.svg | 旅客发送量、人次 |
| icons/chunk-filled/truck.svg | 货运总量 |
| icons/chunk-filled/box.svg | 集装箱、班列标箱 |
| icons/chunk-filled/fire.svg | 煤炭等燃料品类 |
| icons/chunk-filled/factory.svg | 冶炼物资、工业品类 |
| icons/chunk-filled/droplet.svg | 石油品类 |
| icons/chunk-filled/seedling.svg | 粮食、化肥及农药品类 |
| icons/chunk-filled/leaf.svg | 节能减排、绿色 |
| icons/chunk-filled/recycle.svg | 排放下降、循环 |
| icons/chunk-filled/bridge.svg | 桥梁、工程 |
| icons/chunk-filled/route.svg | 路网、营业里程 |
| icons/chunk-filled/coin.svg | 固定资产投资 |
| icons/chunk-filled/shield-check.svg | 运输安全 |
| icons/chunk-filled/badge-check.svg | 技术标准 |
| icons/chunk-filled/trophy.svg | 科技奖项 |
| icons/chunk-filled/lightbulb.svg | 科技创新 |
| icons/chunk-filled/globe.svg | 国际对照、国际标准 |
| icons/chunk-filled/gauge-high.svg | 综合能耗强度 |
| icons/chunk-filled/file.svg | 规章与行政规范性文件 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | chart | column_chart | 六年旅客发送量的逐年变化与 2024 年的位置 |
| P04 | table | hierarchical_table | 公报原表:全国铁路旅客运输量的分项与同比 |
| P06 | chart | column_chart | 六年货运总发送量的逐年变化 |
| P07 | chart | horizontal_bar_chart | 2024 年六大品类运量的量级排序 |
| P08 | chart | area_chart | 六年总换算周转量的总量走势 |
| P09 | table | record_table | 机车/客车/货车三类装备的拥有量与构成 |
| P11 | chart | line_chart | 八国铁路营业里程 2000–2021 的长期对照 |
| P13 | chart | line_chart | 化学需氧量与二氧化硫排放量的六年下降 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fuxing_train.jpg | 3840x2560 | 1.50 | 封面主视觉,并在总览页以同一张照片的窄立幅延续 | Photography | 封面整幅铺底,车头偏右、左侧天空作安静区承接标题;总览页把同一张收成右侧窄立幅,只留车头 | adaptive | user | Existing | CR400AF-2007 复兴号动车组(N509FZ,CC BY-SA 4.0);同一文件在 P01 与 P02 用不同裁切复用,构成尺寸与位置推移 | — | — |
| beijing_south_station.jpg | 2560x1600 | 1.60 | 客运结构页的现场佐证 | Photography | 沿站台纵深裁成横条压在表格上方,人流方向朝向表格 | adaptive | user | Existing | 北京南站站台(颐园新居,CC BY-SA 4.0) | — | — |
| shanghai_hongqiao.jpg | 3840x2558 | 1.50 | 现场页主图,承担"现场"一侧的质地 | Photography | 候车大厅整幅出血,顶部结构线留白、底部压暗后承接文字 | adaptive | user | Existing | 上海虹桥站候车大厅(Patrick Nagel,CC BY-SA 3.0) | — | — |
| fuxing_interior.jpg | 3840x2560 | 1.50 | 装备页的车内实景,与装备表并置 | Photography | 竖切放右侧半幅,与左侧装备表齐顶 | adaptive | user | Existing | CR400AF-AE-2399 商务座车厢内景(N509FZ,CC BY-SA 4.0) | — | — |
| danyang_kunshan_bridge.jpg | 3840x2158 | 1.78 | 路网页的工程实景 | Photography | 桥体水平线横切成半幅横条压在页面上半,下方接里程数字 | adaptive | user | Existing | 丹昆特大桥(无锡段)(MNXANL,CC BY-SA 4.0) | — | — |
| qinghai_tibet_railway.jpg | 2400x1800 | 1.33 | 绿色低碳页的线路实景,给排放曲线一个现场落点 | Photography | 方形小幅裁切放页面右下,与曲线末端呼应 | adaptive | user | Existing | 青藏铁路车厢(Hiroki Ogawa,CC BY 3.0) | — | — |
| fuxing_train_wash.jpg | 1920x1280 | 1.50 | 结论页的压暗收束场,与封面构成同一照片的首尾呼应 | Derived photography | 整幅压暗铺底,三条结论压在中部安静区 | adaptive | user | Existing | Derived from fuxing_train.jpg; treatment=brightness 0.55 + desaturate 0.8 + fit 1920x1280 | — | — |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页备注写主讲人现场讲法:先一句本页要让来访方记住的判断,再说明页面上数字的出处(公报第几部分或世界银行表的哪一行),最后给一句过渡。凡页面标注"整理"的推算,备注必须复述其算式与依据。数字一律复述附件原值,不得引入附件之外的事实。
- **Total duration**: 约 25 分钟(15 页,平均每页 90–110 秒)
- **Notes style**: 正式、可照读,面向接待汇报场景
- **Presentation purpose**: 先完整汇报 2024 年全国铁路数据,再通过国际对照与现场影像建立印象,最后给出三条可带走的判断

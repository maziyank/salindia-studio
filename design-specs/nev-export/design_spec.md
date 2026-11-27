<!-- ppt-master-schema: design-spec/v1 -->
# nev_export_bilingual_zh_en - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | nev_export_bilingual_zh_en |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 15 |
| Primary Language | zh-CN |
| Target Audience | 一半中国同事(产业研究、销售与战略)、一半海外合作伙伴(经销商与合资方);双方都熟悉汽车行业,但对中国统计口径、企业口径与政策细节的掌握程度不同 |
| Communication Intent | 先用公开数据说明 2025 年中国新能源汽车出海的规模与结构;再解释关税与本地化如何改变出海方式;最后对齐 2026 年双方可共同判断的方向。报告与解释优先,不做投资建议 |
| Desired Audience Outcome | 中外双方能用同一套口径明确的数字描述 2025 年出海格局,能说出关税与海外建厂之间的因果关系,并对"增量重心从整车出口转向海外生产"形成共识 |
| Core Message / Ask / Action | 2025 年中国新能源汽车出口翻倍至 261.5 万辆(中汽协口径),但增长方式已从"卖整车"转向"在当地造车、建网络";2026 年的增量要靠海外产能与价格承诺机制 |
| Delivery Context | 主要为有主讲人的 30 分钟双语行业例会现场讲解(投影);次要为会后中外双方各自独立阅读的简报材料 |
| Artifact Afterlife | 作为双方共享的事实基线与后续合作讨论的引用材料,需要可追溯到来源机构与年份 |
| Reading Mode | balanced |
| Content Strategy | 平衡默认(用户未声明素材取舍偏好):按本简报的沟通目标重新组织调研补充中的事实,保留全部实质内容与口径限定,不引入调研之外的事实 |
| Design Style | 方向一「双语公报 / Bilingual Gazette」——数据新闻式栅格公报,中文主行与英文副行成对分层 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 工作流默认值(Stage 2 proactive notes 取默认 true,用户未反对) |
| Custom Animations | enabled — 用户显式要求"要有自定义动画和 Morph"(对象级动画 + 页间 Morph 转场) |
| Narration Audio | disabled — 工作流默认值(用户未要求旁白音频) |
| Created Date | 2026-09-12 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上 56 / 下 64 / 左右 72;底部 64 含常驻来源条 |
| Content Area | x 72–1208(宽 1136),y 56–656(高 600) |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: briefing, pyramid
- **Mode Behavior**: 每一部分的首页先给一句可引用的判断句(pyramid 的结论先行),部分内的页面按 briefing 的等权可扫读方式铺开事实与口径,标题写成判断而非话题词;结尾把四个部分的判断收束为双方可共同使用的议题,不做投资建议。
- **Visual style**: custom
- **Visual Style References**: data-journalism, swiss-minimal, editorial
- **Visual Style Behavior**: 以 data-journalism 负责多栏证据密度、微型图注与常驻来源条;swiss-minimal 负责 12 栏硬栅格、大留白与近零装饰,使同页双语不靠色块分区而靠栅格与细规则线分层;editorial 负责中文衬线标题与拉丁衬线副标题的层级互文、细规则线与边注。中文主行与英文副行永远上下成对,英文行以更小字号、次级文字色与 0.5px 细线左缘标记为副层,不另起色块。
- **Theme**: 出海年鉴——用公报式栅格承载两种语言,同一栏里中文在上、英文在下,数字与来源常驻可引用
- **Tone**: 克制、可核查、供双方引用;不渲染胜利叙事,也不淡化壁垒

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 页面主底,公报纸感 |
| Secondary background | #F2F4F7 | 数据面板、表格与口径框的底 |
| Primary | #0E3A66 | 中文标题、栅格主线、结构性文字 |
| Accent | #D4541E | 关键数字、增长方向与当页焦点(每页仅一处主焦点) |
| Secondary accent | #2E7D8F | 第二数据序列、海外产能与网络类信息 |
| Body text | #1B2430 | 中文正文 |
| Secondary text | #5C6673 | 英文副行、注释、图注 |
| Divider | #D8DEE6 | 分栏细线、表格边线 |
| Surface | #FAFBFC | 面板抬升层,比 secondary background 更浅 |
| Grid | #E8ECF1 | 图表网格与发丝线,比 divider 更浅 |
| Positive | #2E7D32 | 同比增长、正向变化 |
| Negative | #C62828 | 同比下降、税率与壁垒 |
| Warning | #F57C00 | 未生效、待确认的机制(价格承诺) |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: editorial, minimalist-swiss
- **Visual**: 扁平矢量编辑插画——只用简化的几何体块与 1.5px 轮廓表现滚装码头、厂房与充电阵列,平面无渐变,单一光源方向的浅色块面,不含任何真实品牌标识、车标与文字
- **Mood**: 克制的行业年鉴插图,像《经济学人》图表页旁的说明插画,而非广告主视觉
- **Image Rendering Behavior**: 由 editorial 负责杂志信息图的体块归纳与说明性构图,由 minimalist-swiss 负责大留白、硬边缘与近零装饰;线条为等宽 1.5px 深蓝轮廓,质感为纯平色块与 8% 主色薄阴影,深度靠体块重叠而非渐变,材质统一为哑光纸面,情绪安静、可引用。

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 衬线/公报权威 | SimSun | Cambria | serif |
| Body | 无衬线/屏幕可读 | Microsoft YaHei | Cambria | sans-serif |
| En title | 衬线/拉丁副标题 | Cambria | Cambria | serif |
| En body | 衬线/拉丁副行与全部数字 | Cambria | Cambria | serif |
| Display | 衬线/封面与章节大字 | SimSun | Cambria | serif |

- **Typography upgrade (Reference)**: 若目标机确认安装思源宋体 Source Han Serif,可将中文标题由 SimSun 升级为 Source Han Serif SC;未确认前保持 SimSun。
- **Title stack**: SimSun
- **Body stack**: Microsoft YaHei
- **En title stack**: Cambria
- **En body stack**: Cambria
- **Display stack**: SimSun
- **Role rationale**: 双语同页使两条拉丁文本行成为结构性角色(每页标题副行 + 每个要点的英文行),故把拉丁面单独声明为 `en_title` / `en_body` 两个复现角色,并让全卷数字统一走该拉丁面(Cambria 为 lining figures),避免中文面渲染西文数字造成的字宽与基线漂移;三个字族到顶,不再引入第四族。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 22 |
| Title | 40 |
| Subtitle | 28 |
| Annotation | 17 |
| Display | 64 |
| Lead | 26 |
| Footnote | 14 |
| En title | 24 |
| En body | 18 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 左上判断句 → 右侧或下方证据(图/表/数字)→ 底部来源条;同一栏内永远中文在上、英文在下,读者选定语言后只需垂直扫一列
- **Composition tendency**: 12 栏硬栅格上的双语成对分层;每页一个焦点数字或一个证据对象,其余为支撑栏;部分首页在右上角标出部分序号与双语部分名
- **Cross-page continuity**: 常驻元素为页眉细规则线、右上角部分索引、底部来源条(机构 + 年份);Morph 页对之间保留同一数据对象的位置与命名,仅改变其状态
- **Spacing posture**: variable by page rhythm——dense 页用双栏或三栏并列,breathing 页只留一条中央论证轴
- **Spacing anchors**: 页边距 72px;块间距 28px;栏间距 32px;圆角 0px(公报硬边);正文行距 34px

## VI. Icon Usage Specification

- **Primary bundled library**: chunk-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/chunk-filled/ship.svg | 整车出口、滚装运输、出海总量 |
| icons/chunk-filled/factory.svg | 海外工厂、本地生产、产能 |
| icons/chunk-filled/truck.svg | 商用车与物流、交付 |
| icons/chunk-filled/plug.svg | 充电与补能网络 |
| icons/chunk-filled/globe.svg | 目的市场、区域分布 |
| icons/chunk-filled/map-pin.svg | 具体国家与工厂所在地 |
| icons/chunk-filled/chart-bar.svg | 数量对比与排名 |
| icons/chunk-filled/chart-line.svg | 年度序列与增速 |
| icons/chunk-filled/table.svg | 口径对照与企业对照 |
| icons/chunk-filled/percent.svg | 税率、占比、同比 |
| icons/chunk-filled/shield-check.svg | 合规、价格承诺、准入 |
| icons/chunk-filled/circle-exclamation.svg | 壁垒、风险与未生效事项 |
| icons/chunk-filled/circle-checkmark.svg | 已落地事实与已投产 |
| icons/chunk-filled/calendar.svg | 生效日期与时间表 |
| icons/chunk-filled/coin.svg | 投资额与均价 |
| icons/chunk-filled/building.svg | 企业主体与机构 |
| icons/chunk-filled/target.svg | 2026 目标与展望 |
| icons/chunk-filled/arrow-trend-up.svg | 增长方向 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P04 | chart | donut_chart | 2025 年汽车出口总量中新能源与传统燃料的构成比例 |
| P05 | chart | column_chart | 2022–2025 年新能源汽车出口量的逐年台阶式变化 |
| P07 | chart | horizontal_bar_chart | 2025 年前三大出口目的国的出口量对比 |
| P08 | table | metric_table | 五家代表企业 2025 年出口量、同比与主要落点的对照 |
| P10 | table | record_table | 四个海外基地的国别、时间、产能与投资额记录 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_port_roro.jpg | 2048×2048 | 1:1 | 封面主视觉:出海的实体场景锚点 | Illustration | 右侧竖幅满高图版,与左侧双语标题栏以一条竖向细规则线相接,图像只占右 45% 宽 | adaptive | ai | Generated | 简化几何体块的滚装码头:一艘侧视滚装船、三层车辆甲板轮廓、岸边两台岸桥与整齐排列的无标识乘用车块;深蓝主色体块 + 暖橙单点强调;无任何品牌标识、车标、文字与人物 | none | hero_page |
| local_plant.jpg | 1264×848 | 1.49:1 | 本地化部分首页:说明"在当地造车"的场景 | Illustration | 右栏说明性插画,与左栏三步框架并列,底边与框架末行对齐 | adaptive | ai | Generated | 简化几何体块的整车工厂:长条厂房轮廓、两座焊装车间体块、屋顶光伏条纹、厂前三辆无标识整车与一列集装箱;深蓝轮廓 + 青蓝屋面;无品牌标识与文字 | none | local |
| charging_array.jpg | 1376×768 | 1.79:1 | 充电与售后网络页:补能网络的视觉锚点 | Illustration | 页面下半幅横向带状插画,上方为三地闪充站数字,插画作为数字的底座 | adaptive | ai | Generated | 简化几何体块的公共快充站阵列:六根等距充电桩剪影、顶棚横板、两辆无标识车辆侧视轮廓、地面标线;深蓝轮廓 + 暖橙充电指示点;无品牌标识与文字 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页备注先中文段后英文段,英文段为中文段的对应表述而非逐字直译;内容只使用本页已在页面上出现的事实与 `sources/nev_export_2025_research.facts.json` 中的事实,数字一律带机构与年份;主讲人换语言时的过渡句写在中文段末尾;不加入页面上没有的新数据,不做投资建议
- **Total duration**: 约 30 分钟(15 页,平均每页约 2 分钟,含中英两次表述)
- **Notes style**: formal
- **Presentation purpose**: 先用公开数据说明 2025 年规模与结构,再解释关税与本地化的因果,最后对齐 2026 年的共同判断

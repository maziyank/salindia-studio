<!-- ppt-master-schema: design-spec/v1 -->
# 北斗卫星导航系统:从一颗星到全球组网 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 北斗卫星导航系统:从一颗星到全球组网 |
| Canvas Format | ppt169 (1280 × 720) |
| Page Count | 14 |
| Primary Language | zh-CN |
| Target Audience | 科普展厅循环播放区的公众观众,含中小学生与陪同家长。他们每天用手机地图,但不知道手机里就有北斗,不了解卫星导航的原理、北斗的建设历程,也说不清"为什么中国要自己建一套"。停留时间短,随时可能中途加入观看。 |
| Communication Intent | 先讲清楚"这是什么、为什么必须自己建",再用一条清晰的时间线讲"三步走怎么走完",然后把"三种轨道各自在做什么""定位原理""短报文为什么是北斗独有"三件事讲透,最后落到"它已经在你身边"和"下一步"。优先级:可信 > 易懂 > 自豪感;不喊口号,只用能标出处的事实说话。 |
| Desired Audience Outcome | 观众离开时能用自己的话说出三件事:北斗走了三步、用三种轨道、能发短报文;并且知道自己手机里就有北斗。 |
| Core Message / Ask / Action | 北斗不是"中国版GPS",而是一套按自己的路线走出来的时空基础设施——三步走完、三轨混合、导航与通信合一,而这条独创的路从第一颗星就已经定下。 |
| Delivery Context | 录播/自动播放(recorded, self-running):科普展厅常设循环播放的讲解片,无现场讲解员,配逐字旁白音频、字幕与自动换页,全片5–7分钟;观众可能中途加入,因此每一场景自身要能读懂。次要用途:线上短视频与课堂播放。 |
| Artifact Afterlife | 长期归档与复用:作为展厅常设素材反复播放,并可交付学校做课堂材料;需保留逐字旁白脚本与来源标注以备核查。 |
| Reading Mode | presentation |
| Content Strategy | 无现成文章可贴近,全部事实来自 topic-research 的权威事实卡片,因此叙事线由本方案自由重组;但每一个数字、每一个日期都必须回到 `sources/beidou_navigation_research.facts.json` 的某一条 fact_id,页面上标出来源名与年份。没有可追溯出处的数字一律不用。 |
| Design Style | 深空仪表台(custom mode + custom visual style):近黑深蓝的太空场作底,信号蓝画轨道与结构,暖金只留给关键数字;页面像一台精密仪器的读数面板,而不是一叠卡片。 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 启用的 Narration Audio 依赖项;同时本片的逐字旁白就是备注内容 |
| Custom Animations | enabled — 录播/自动播放交付,动效需与旁白 cue 对齐(video-design §4 的 narration-governed motion 分支) |
| Narration Audio | enabled — 用户明确要求 MiniMax 逐字旁白全链路 |
| Created Date | 2026-09-11 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | ppt169 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 72 px 四边安全边 |
| Content Area | x 72–1208, y 72–648(可用宽 1136,可用高 576);背景场、轨道弧线与整幅图像允许出血至画布边缘 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Visual style**: custom
- **Theme**: 一台观测仪的读数面。全片共用一个"深空观测"心智地图:近黑深蓝的天场恒定不变,地球与轨道是反复出现的锚点,每一页只改变这台仪器正在读的那一个量。跨页母题是**一条贯穿页面的细水平基线**(y 固定),时间轴、轨道剖面、精度刻度、报文长度条都挂在这同一条线上——它是本片的"仪器横梁",让 14 个场景看起来是同一台设备的连续读数,而不是 14 张各自为政的幻灯片。
- **Tone**: 克制、精确、有分量。解说的语气是"我把事实摆给你看",不是"你看我们多厉害"。
- **Mode References**: instructional, narrative
- **Mode Behavior**: 骨架用 instructional 的概念分解与分步推进(每一场景只推进一个理解台阶,前一台阶的结论是下一台阶的前提);但历史那一段(三步走)按 narrative 的张力走——起点是"只有一颗试验星、用户还得自己发信号",转折是"从有源到无源",收束是"提前半年,18箭30星"。两者的分工固定:凡是讲"怎么回事"的页用分解,凡是讲"怎么走过来"的页用故事推进。标题一律写成陈述句而非话题词,让中途加入的观众读标题就拿到该页的主张。
- **Visual Style References**: dark-tech, blueprint, data-journalism
- **Visual Style Behavior**: 近黑深蓝的连续天场(dark-tech 的暗场与发光强调),其上用 blueprint 的示意线语言——细实线、细虚线、刻度、引出线与标注,几何一律用原生形状画(圆、椭圆弧、连接线、预设形状),不用卡片网格承载概念;面板只在需要把读数与天场分开时出现,直角无圆角,靠一条 1px 分隔线而不是阴影抬起。数据页借 data-journalism 的纪律:每个数字下面必须有一条极小的来源行(来源名 + 年份),来源行是本片的视觉签名,出现在每一个有外部事实的页面。装饰密度低——除轨道弧线、刻度与那条仪器横梁外不加任何纯装饰元素;留白大面积留给天场本身,让发光的少数元素成为焦点。排版性格:标题用钝头黑体的方正力量对住天场,数字用等宽体排成仪表读数,两者的对比就是本片的字体戏剧。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #060B1A | 全片恒定的深空天场,所有页面的底 |
| Secondary background | #0E1730 | 读数面板、表格底、图表绘图区的抬高层 |
| Primary | #4EA8FF | 信号蓝:轨道线、结构线、连接线、图表主序列、页面主强调 |
| Accent | #FFC24B | 暖金:关键数字、当前焦点标记、时间轴上的"现在"点;全片最稀缺的颜色,每页至多一处主用 |
| Secondary accent | #35D0A5 | 青绿:第三类编码(MEO/全球服务/对照序列),只在需要三类并置时出现 |
| Body text | #D8E0F0 | 正文与标题的单色实心字 |
| Secondary text | #8FA0C0 | 说明、标签、坐标轴文字 |
| Divider | #1E2B4A | 分隔线、面板描边、刻度细线 |
| Surface | #111C38 | 图表/表格面板的实底(比 secondary background 再抬一层) |
| Grid | #1A2747 | 网格与刻度发丝线,永远比 divider 更浅 |
| Scrim | #060B1A | 图像之上的压暗层(以 alpha 施加),保证叠字对比 |

### AI Image Strategy

- **Image Rendering**: custom
- **Visual**: 电影级夜景摄影的光与景深。极低照度,单一冷蓝主光,画面里只允许一处暖金点光源;真实大气、真实噪点、真实镜头景深,不是插画也不是三维渲染。每张图都必须留出一块大面积近黑的安静区供叠字,主体推到画面一侧。画面内不得出现任何文字、界面、标注、logo 或可识别的真实人物面孔。
- **Mood**: 安静、辽阔、有人在值守的感觉。参照物是纪录片里的夜间观测镜头——不是宣传片的高饱和英雄镜头。
- **Image Rendering Behavior**: 以真实摄影的线与质地为唯一基底:自然的镜头虚化、可见但克制的暗部噪点、冷蓝到近黑的连续影调过渡,材质靠光而不是靠描边表达;深度来自景深与大气透视,不来自投影或高光贴图;情绪是低照度纪录片的克制,不加任何风格化滤镜、渐变叠加或发光特效。
- **Image Rendering References**: corporate-photo

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 钝头黑体 / 方正、等宽感强、笔画末端平切,对住天场有分量 | SimHei | Arial | sans-serif |
| Body | 人文黑体 / 字面大、开口开,投影距离下可读 | Microsoft YaHei | Arial | sans-serif |
| Display | 钝头黑体放大 / 封面主词与章节大字,与 Title 同族但自成尺寸锚点 | SimHei | Arial | sans-serif |
| Year | 等宽定宽数字放大 / 时间轴与对比表上的年份标记,与 Data 同族但自成尺寸锚点 | Consolas | Consolas | monospace |
| Data | 等宽 / 定宽数字、等高衬线数码,排成仪表读数;所有外部事实数字、坐标轴、刻度、来源行都走这一族 | Consolas | Consolas | monospace |

- **Title stack**: `SimHei, Arial, sans-serif`
- **Body stack**: `Microsoft YaHei, Arial, sans-serif`
- **Display stack**: `SimHei, Arial, sans-serif`
- **Data stack**: `Consolas, Microsoft YaHei, monospace`
- **Year stack**: `Consolas, Microsoft YaHei, monospace`
- **Role rationale**: 增设 Data 一族是因为本片每一页都有外部事实数字、刻度或来源行(37 条 fact 全部带数字或日期),等宽定宽数字让跨页的读数纵向对齐、位数不跳动;这正是"仪表读数"这一身份的承重点,不是一次性装饰。另设 Year 40 是因为年份在 P03/P04/P05/P13/P14 五页反复出现且必须比普通数据标签更重,属于结构性复现角色,不能靠 Executor 的稀疏 display 例外承载。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Display(封面主词、章节大字) | 96 |
| Hero number(关键数字,Data 族) | 88 |
| Title(页面标题) | 52 |
| Subtitle | 40 |
| Year(时间轴/对比表年份,Data 族) | 40 |
| Lead(导入句) | 36 |
| Body | 30 |
| Annotation(标注、标签,Data 或 Body 族) | 22 |
| Data(坐标轴、刻度,Data 族) | 22 |
| Footnote(来源行,Data 族) | 18 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 先读标题(陈述句,一眼拿到主张)→ 再读页面上那一个被暖金标出的读数或焦点 → 最后读挂在仪器横梁上的结构与标注。中途加入的观众在两秒内应当拿到前两级。
- **Composition tendency**: 每页只允许一个主体占据画面主导,其余元素退成结构与标注。避免把要点平均分进等宽格子——这是本片最需要躲开的失败模式。天场是连续的,构图靠"在这片天上把东西放在哪儿"决定,而不是靠给内容加边框。
- **Cross-page continuity**: 那条仪器横梁(单条细水平基线)在需要挂载结构的页面上保持同一 y;地球与轨道环在 P06/P07/P09/P10 之间保持可辨认的同一身份与朝向,只改变被强调的那一层;来源行的位置与字号全片不变。封面、章节与收束页可以放掉横梁。
- **Spacing posture**: variable by page rhythm——anchor 页大幅留白让天场说话,dense 页把结构收紧到横梁附近,breathing 页只放一个对象加一行字。
- **Spacing anchors**: 页边距 72 px;块间距 32 px;分栏槽 40 px;圆角半径 0 px(直角,示意图与仪表台的语言);正文行高 1.6。

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 3
- **Brand-logo library**: 不使用(本片内容不涉及任何公司或产品品牌标识)

| Icon Path | Suitable Scenarios |
| --- | --- |
| `icons/tabler-outline/satellite.svg` | 卫星、星座、在轨对象 |
| `icons/tabler-outline/world.svg` | 全球服务、覆盖范围 |
| `icons/tabler-outline/clock.svg` | 授时、时延、时间基准 |
| `icons/tabler-outline/broadcast.svg` | 信号播发、无源接收 |
| `icons/tabler-outline/map-pin.svg` | 定位、位置解算结果 |
| `icons/tabler-outline/message.svg` | 短报文通信 |
| `icons/tabler-outline/ship.svg` | 渔业、海上应用 |
| `icons/tabler-outline/plane.svg` | 航空应用 |
| `icons/tabler-outline/tractor.svg` | 农业应用 |
| `icons/tabler-outline/bolt.svg` | 电力调度应用 |
| `icons/tabler-outline/device-mobile.svg` | 大众手机应用 |
| `icons/tabler-outline/route.svg` | 交通运输、导航路径 |
| `icons/tabler-outline/rocket.svg` | 发射、组网节点 |
| `icons/tabler-outline/target.svg` | 精度、指标 |
| `icons/tabler-outline/lifebuoy.svg` | 国际搜救、救灾减灾 |
| `icons/tabler-outline/link.svg` | 星间链路 |
| `icons/tabler-outline/antenna.svg` | 地面站、用户终端 |
| `icons/tabler-outline/radar.svg` | 监测、测控 |
| `icons/tabler-outline/mountain.svg` | 遮挡、低仰角环境 |
| `icons/tabler-outline/map.svg` | 服务区、区域覆盖 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P05 | table | comparison_matrix | 三代北斗按同一组判据横向对比,让"每一步解决了上一步的什么问题"成为可读的网格 |
| P08 | chart | donut_chart | 30 颗卫星按三种轨道的构成比,中心承载总数 |
| P12 | chart | horizontal_bar_chart | 区域短报文与全球短报文的单次容量对比,长度差本身就是论据 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_orbit_earth.png | 2752x1536 | 16:9 | 封面主视觉的生成原片,仅用于派生,不直接上页 | Source | 原片保留完整画幅,不做任何页面构图承诺 | no-crop | ai | Generated | 从中地球轨道高度俯瞰的地球夜面弧线,大气层边缘一道极细冷蓝辉光,弧线上方是深空;左上大面积近黑安静区;画面右下一处极小暖金光点作为唯一暖色;无文字无界面无地名标注 | none | hero_page |
| cover_orbit_earth_fit.jpg | 1280x714 | 16:9 | 封面实际置入件:把观众直接放到"从轨道上看地球"的位置,给全片定下深空场 | Background | 整幅出血作底,地球弧线压在画面下缘偏右,上方三分之二留作近黑安静区承载主词与副题;不做卡片式插入 | adaptive | ai | Generated | Derived from cover_orbit_earth.png; treatment=fit 1280x720; | none | hero_page |
| scene_night_sea.png | 2752x1536 | 16:9 | P11 短报文场景的生成原片,仅用于派生,不直接上页 | Source | 原片保留完整画幅,不做任何页面构图承诺 | no-crop | ai | Generated | 夜间开阔海面上一艘小型渔船的远景剪影,驾驶舱一盏暖金小灯是画面唯一暖光源,海面反射极弱;天空占三分之二为深蓝到近黑;镜头远、景深浅、大气感强;无文字无船名无可辨认人脸 | none | local |
| scene_night_sea_fit.jpg | 1280x714 | 16:9 | P11 实际置入件:让"没有信号的地方还能发出一句话"这件事有真实的重量 | Illustration | 主体推到画面右侧下三分之一,左半保持近黑海面与夜空供叠标题与指标;与页面横梁在同一水平带上交接 | adaptive | ai | Generated | Derived from scene_night_sea.png; treatment=fit 1280x720; | none | local |
| app_scene_base.png | 2752x1536 | 16:9 | P13 应用场景的原始摄影底片,仅用于派生,不直接上页 | Source | 原片保留完整画幅,不做任何页面构图承诺 | no-crop | ai | Generated | 破晓前的沿海平原横向全景:远处港口塔吊与近处规整农田同处一个画面,几点冷白作业灯散布;天色是深蓝转灰的过渡;极低对比、极安静;无文字无品牌无可辨认人脸 | none | local |
| app_scene_muted.jpg | 1280x714 | 16:9 | P13 实际置入件:压暗去饱和后作为页面下缘的标签带底,让应用领域标签能直接叠在图上而不失可读性 | Illustration | 作为页面下缘的整幅横带(在 SVG 里原生裁出下半带),应用标签沿横带排布并与图中元素位置呼应;图本身退为质地,不与文字争 | adaptive | ai | Generated | Derived from app_scene_base.png; treatment=desaturate 0.7 + brightness 0.72 + fit 1280x720; | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 备注即本片的逐字旁白脚本,由本方案在页面 roster 定稿并通过 Gate 2 之后、SVG 动笔之前一次性写入 `notes/total.md`(`# Slide N` + `---`),作为页面设计的输入而不是事后补写的解说。脚本按场景切分,一场景一段,每段只讲这一页能看见的东西;页面上出现而脚本没讲的主张,改页面或回到规划,不许事后改脚本凑画面(video-design §4)。脚本为本方案自撰(非用户提供的 final/literal script),因此允许在终检后、合成音频之前做一次基于最终 SVG 的校订。每个外部事实在旁白中口语化复述时,页面上必须有对应的来源行。
- **Total duration**: 全片 5–7 分钟;14 个场景,平均每段约 90–130 字(按中文播音约 4.5 字/秒估算),封面与收束段偏短。
- **Notes style**: 讲解式口语,陈述句为主,不用"大家好""让我们一起"这类主持腔;数字念完整(如"三万五千七百八十六公里"),年份念"二〇二〇年七月三十一日";每段最后一句留一个向下一场景的推进,但不说"下一页"。
- **Presentation purpose**: 见 §I Communication Intent——先讲清为什么必须自己建,再用时间线讲三步走,然后讲透三种轨道、定位原理与短报文,最后落到身边应用与2035。

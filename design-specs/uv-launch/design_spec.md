<!-- ppt-master-schema: design-spec/v1 -->
# uv_launch - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | uv_launch |
| Canvas Format | ppt169 (1280×720) |
| Page Count | 14 |
| Primary Language | zh-CN |
| Target Audience | 中文 Python 开发者与技术负责人:日常靠 pip + venv + requirements.txt 干活,听说过 uv 但没系统了解,关心迁移成本与"能不能今天就用" |
| Communication Intent | 先讲清 uv 到底替掉了哪些日常摩擦(说明,最高优先级),再用官方文档与 Astral 自己公布的基准说法建立可信度(说服),最后给一条今天就能执行的第一步(动员);顺序即优先级 |
| Desired Audience Outcome | 听完能说出 uv 收编了哪几件工具、能复述项目工作流的四条命令、知道哪些能力还挂着 preview 标记、并且愿意在自己的一个项目上跑通第一条命令 |
| Core Message / Ask / Action | uv 是一个 Rust 写的单二进制,把 pip / pip-tools / pipx / pyenv / virtualenv / twine 那一摊收进一套命令,并给出跨平台 lockfile;所有性能倍数都来自 Astral 在 macOS 上的测量,不是听众自己机器上的结果 |
| Delivery Context | 主用途:presenter-led 的团队内部技术分享,约 25–30 分钟;次要用途:会后当作迁移参考文档自读 |
| Artifact Afterlife | 供团队传阅与复用,作为是否迁移到 uv 的决策参考材料 |
| Reading Mode | balanced |
| Content Strategy | 贴近源:命令、终端输出、版本号、发布日期一律照官方文档与 CHANGELOG 原样引用,不改写、不取整、不合并;中文只用于解释与串联 |
| Design Style | Direction 2「终端里的深色发布会」:showcase 叙事 + dark-tech 视觉,深底之上让终端块与倍数数字自己发光 |
| AI Image Acquisition Path | not applicable(本 deck 不使用 AI 图像) |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 工作流默认值(Stage 2 主动建议 true,用户未反对) |
| Custom Animations | enabled — 用户在任务书中显式要求写 animations.json 并给出 Morph 与入场要求 |
| Narration Audio | disabled — 工作流默认值 |
| Created Date | 2026-09-05 |

- **Template Application**: 采用 library Style `product-launch` 的沟通方法与评估口径,不引入任何原型或结构:§II 的"先演示再命名""标题写用户得到什么""已发布/preview/计划中必须一眼分开""每个性能数字带测量口径与日期"整段照用;§III 的九个页面角色作为骨架来源,按实际内容决定各角色占几页;§IV 的证据纪律照用(图表只在数字本身是重点时使用,轴不裁、基线不省,数字紧邻其出处)。§V 的 `photo-editorial` 与 §VI 的 `corporate-photo` 不采纳——本 deck 没有任何照片或产品界面截图可用,照片主导的构图语言在这里会落空;改用 dark-tech,把 §V "让画面保持中性或深色,让主角占住视线"和"只留一个强调色"的意图用终端块+发光强调色实现。页面为 flat 自由设计。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | ppt169 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上下 56px,左右 72px |
| Content Area | x 72–1208,y 56–664(可用 1136 × 608) |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: showcase
- **Mode Behavior**: 按发布会节奏推进:每页只放一个能力、一个收益或一个时刻,并且先让终端跑出来的东西占住画面,再用标题给它命名。张力页只讲听众自己每天在经历的那件麻烦事,定位页把主张单独给整页,能力页让"制品"(终端窗口、命令序列、文件树)主导而说明退到从属位置,证据页只留一个主数字。整卷不把两个 reveal 塞进一页,也不用图标阵列冒充能力清单。
- **Visual style**: custom
- **Visual Style References**: dark-tech
- **Visual Style Behavior**: 深色画布上做几何精确的分区:整页由一个近黑蓝底 + 若干抬起一档的面板构成,面板用 1px 细线勾边而不是投影堆叠。终端块是本卷的主角载体——等宽字、左侧命令提示符列、深一档的窗口底、顶部一条极细的窗口条,窗口边缘用主色发一层很淡的辉光标记"这是正在跑的东西"。强调色只用在三处:reveal 的那一件事、改善的那一侧、结尾的那一个动作。数字用等宽字放到很大,靠字号而不是装饰建立层级。装饰只有细线、细网格和方角/微圆角(4px)的面板,不用渐变网格、不用漂浮粒子、不用多层阴影。
- **Theme**: 一个二进制把一摊工具收干净——整卷的连续物是"终端窗口":它在张力页是六个各自为政的小窗,在定位页合成一个,在能力页放大成主角,在结尾缩回一条可以照抄的命令。
- **Tone**: 克制、工程口吻、有把握但不吹;所有倍数与版本号都紧挨着出处和日期出现。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #0B1220 | 整卷页底,近黑的深蓝,让终端块和数字自己发光 |
| Secondary background | #131C2E | 面板、终端窗口底、表格底,比页底抬起一档 |
| Primary | #4CC9F0 | 主强调:reveal 的那一件事、终端窗口的辉光边、命令关键字、当前页的标记 |
| Accent | #FF8A3D | 改善侧与结尾动作的唯一强调色,也用于 uv 一侧的对照 |
| Secondary accent | #A78BFA | 仅用于 preview 状态标记与次级注记,不参与常规强调 |
| Body text | #E6EDF3 | 正文与终端输出文字 |
| Secondary text | #9BA9BC | 注记、出处行、页脚、表格次要列 |
| Divider | #243349 | 分隔线、面板描边、表格行线 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Display | 无衬线/重字重,封面与收束页的主张尺度 | Microsoft YaHei | Arial | sans-serif |
| Title | 无衬线/中等字重,靠字号建立层级 | Microsoft YaHei | Arial | sans-serif |
| Body | 无衬线/常规字重,长段中文可读 | Microsoft YaHei | Arial | sans-serif |
| Code | 等宽/终端口吻,数字为等宽等高数字 | Consolas | Consolas | monospace |
| Data | 等宽/超大号,倍数与版本号 | Consolas | Consolas | monospace |
| Annotation | 无衬线/小号,出处与口径 | Microsoft YaHei | Arial | sans-serif |

- **Display stack**: Microsoft YaHei, Arial, sans-serif
- **Title stack**: Microsoft YaHei, Arial, sans-serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Code stack**: Consolas, monospace
- **Data stack**: Consolas, monospace
- **Annotation stack**: Microsoft YaHei, Arial, sans-serif
- **Role rationale**: Display 承担封面与收束页的主张尺度(anchor 页共三处),与 Title 同族但另立锚点,避免结构性标题依赖执行期的稀疏例外;Code 与 Data 另立等宽族——终端输出与命令必须列对齐,倍数/版本号需要等高数字;两者共用 Consolas 但字号锚点不同,Data 是页面主角尺度,Code 是可读的正文尺度。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Display | 64 |
| Title | 42 |
| Subtitle | 32 |
| Lead | 30 |
| Data | 88 |
| Code | 20 |
| Annotation | 18 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 视线先落在页面主角(终端块、大数字、对照表),再上移读标题,最后下移到出处行;标题与主角不争夺同一区域。
- **Composition tendency**: 单焦点为主——reveal 与 demonstration 页给主角整幅或近整幅,说明退到一侧的窄栏;landscape、availability、来源页允许多区,但每区仍只讲一件事。
- **Cross-page continuity**: 终端窗口的窗口条与左侧提示符列在整卷保持同一形制;右下角固定一条极细的出处行位置;强调色的用法在整卷保持同一含义。
- **Spacing posture**: variable by page rhythm——anchor 页最松,dense 页允许信息密但仍留出主角呼吸区。
- **Spacing anchors**: 页边距 72px;块间距 32px;栏间距 40px;圆角 4px;正文行高 1.6(38px)。

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2
- **Brand-logo library**: simple-icons(内容里出现的真实品牌:Python、PyPI、GitHub、Rust、Astral,以及三个平台标)

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-outline/terminal-2 | 终端、命令、演示时刻 |
| tabler-outline/package | 包、依赖、安装 |
| tabler-outline/bolt | 速度、性能主张 |
| tabler-outline/lock | lockfile、可复现 |
| tabler-outline/versions | Python 版本管理、多版本切换 |
| tabler-outline/rocket | 发布、上手、第一步 |
| tabler-outline/download | 安装方式、获取渠道 |
| tabler-outline/tool | 工具运行与安装(uvx / uv tool) |
| tabler-outline/file-code | 脚本、内联依赖元数据 |
| tabler-outline/box | 虚拟环境、项目环境 |
| tabler-outline/clock-bolt | 冷/热缓存、耗时对比 |
| tabler-outline/check | 已发布状态 |
| tabler-outline/arrow-right | 迁移方向、前后对照 |
| tabler-outline/alert-triangle | preview / 有条件、注意事项 |
| tabler-outline/world | 跨平台、跨机器可复现 |
| tabler-outline/stack-2 | 能力全景、多层结构 |
| tabler-outline/refresh | 自更新、缓存清理 |
| tabler-outline/route | 迁移路径、下一步 |
| simple-icons/python | Python 生态 |
| simple-icons/pypi | 包索引 |
| simple-icons/github | 源码与 CHANGELOG 出处 |
| simple-icons/rust | uv 用 Rust 写成 |
| simple-icons/astral | uv 背后的 Astral |
| simple-icons/linux | 支持平台 |
| simple-icons/apple | 支持平台(也是 Astral 基准的测量平台) |
| simple-icons/windows | 支持平台 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P08 | table | comparison_matrix | 把同一件任务的传统命令与 uv 命令逐行对齐,让改善被看见而不是被断言 |
| P09 | chart | column_chart | 用 Astral 自己公布的倍数下限比较冷缓存与热缓存两种场景 |
| P11 | table | feature_matrix | 按能力 × 状态展示已发布与 preview 的分界及其出处版本 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

> 本 deck 的图像来源为 `none`:开发者工具的"制品"就是终端与它的输出,没有任何可用的产品界面截图、实物或现场照片;Style §VI 明确禁止把不存在的界面画成近似图形冒充产品真实输出,AI 生成的假终端也属同一禁区。所有视觉主角由原生 SVG 的终端块、原生表、原生图表与图标承担。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页讲稿以该页最终 SVG 上的可见内容为准,补充口头串联、上下页过渡与页面上放不下的背景;凡涉及性能倍数,讲稿必须复述测量者、平台与日期;不引入源文件之外的事实
- **Total duration**: 约 25 分钟(14 页,平均每页 1.5–2 分钟,P05 与 P09 各留 3 分钟)
- **Notes style**: conversational(工程师之间的分享口吻,不用市场话术)
- **Presentation purpose**: 先讲清 uv 替掉了哪些日常摩擦,再用官方与 Astral 自己公布的口径建立可信度,最后给一条今天就能执行的第一步

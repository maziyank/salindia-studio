<!-- ppt-master-schema: design-spec/v1 -->
# infosec_training_zh_long - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | infosec_training_zh_long |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 28 |
| Primary Language | zh-CN |
| Target Audience | 公司新入职员工（非安全专业岗，含研发、运维、销售、职能），已签保密协议但尚未接触内部安全制度；他们关心"这跟我有什么关系"和"我具体要做什么"，对法条编号和统计口径没有耐心 |
| Communication Intent | 先让新员工承认"个人日常操作就是企业的风险敞口"，再按账号、数据设备、合规红线三个面教会可执行的行为准则，最后把"发现异常立即上报"固化成动作；教学优先于告知，合规红线一节需要有威慑力但不制造恐慌 |
| Desired Audience Outcome | 员工能说出三条与自己相关的法律红线和自己要承担的个人责任，能在一封仿冒邮件里指出至少三处破绽，能说出"发现异常 4 小时内报给谁"，并当堂通过 5 道判断题 |
| Core Message / Ask / Action | 攻击者的首选入口是员工而不是系统，法律罚到个人、还能禁业；而及时上报是免责条款，不是追责起点 |
| Delivery Context | 主要为入职培训现场由安全负责人主讲的 45 分钟必修课；次要为员工在内网自学与年度复训时独立阅读 |
| Artifact Afterlife | 作为入职必修培训记录留档，用于举证《个人信息保护法》第五十一条与《数据安全法》第二十七条的培训义务；并作为年度复训与合规审计材料 |
| Reading Mode | balanced |
| Content Strategy | balanced（用户未就素材取舍提出要求）：以研究事实底座为唯一事实来源，按培训教学顺序重新架构，不引入底座之外的外部事实；自建的归纳框架在页面上标注"整理"，统计与法条一律标出处与年份 |
| Design Style | 合规卷宗（Compliance Dossier）——米白纸面上的编辑式法规卷宗，左侧贯穿的纵向卷宗轨承接章节编号，章节页整版反转为深墨底，印章红只用于红线与警示 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 用户明确要求"答案放讲者备注"，并需全卷备注支撑主讲与自学 |
| Custom Animations | enabled — 用户明确要求"要有自定义动画和 Morph" |
| Narration Audio | disabled — 工作流默认，用户未要求旁白音频 |
| Created Date | 2026-09-12 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上 64 / 下 56 / 左 72 / 右 72 |
| Content Area | x 72–1208，y 64–664（可用宽 1136，可用高 600） |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional, pyramid
- **Mode Behavior**: 以 instructional 的概念分解与固定教学顺序作为全卷骨架——先建立"你是入口"的前提，再按账号、数据设备、合规红线、应急上报四步分解，同级概念用同样的深度与结构并列，最后用随堂自测检验；每一章内部借 pyramid 的结论先行，章节页与内容页标题直接写判断句而不是话题标签，证据与法条随后展开，每章末页用一句可执行的"你要做的"收束。
- **Visual style**: custom
- **Visual Style References**: editorial, swiss-minimal, data-journalism
- **Visual Style Behavior**: swiss-minimal 负责严格的基线网格、非对称栏宽与大留白，方角、单一线重、少量大面积几何平面；editorial 负责刊头式眉标、细规则线、边注栏、引块与超大编号的排版层级；data-journalism 负责证据页的密度组织——图表作为页面脊柱而非被框住的插图、全幅 hero 数字、每页底部一条来源行。全卷靠规则线粗细与实色块拉开层级，不用阴影与发光；章节页整版反转为深墨实底承接超大编号。
- **Theme**: 卷宗轨——每页左侧一条从上贯到下的纵向细线，线上按当前章节落一个编号刻度；章节推进时刻度下移，章节页把这条轨放大成整页的编号轴。它的连续性职责是让 28 页在视觉上始终能回答"我现在在第几章"，复用方式为固定位置、按章变化刻度。
- **Tone**: 克制、可核验、带分量；像一份被人反复批注过的法规汇编，而不是一场安全产品发布会

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F7F4EE | 纸面底色，承载全部内容页 |
| Secondary background | #EBE6DC | 次级纸面：引块、表头带、边注栏底 |
| Primary | #1F2A37 | 深墨：标题、卷宗轨、章节页整版反转底 |
| Accent | #C0392B | 印章红：法律红线、警示、错误做法、关键数字 |
| Secondary accent | #1D6A73 | 墨青：正确做法、正向指标、第二数据系列 |
| Body text | #232A31 | 正文与表格单元文字 |
| Secondary text | #5A6068 | 图注、边注、来源行、页码 |
| Divider | #D5CEC2 | 规则线、表格横线、卷宗轨 |
| Surface | #FFFFFF | 需要从纸面抬起一层的面（表格奇数行、邮件示意面板） |
| Grid | #E4DED3 | 图表网格发丝线，比 Divider 更浅 |
| Block shade | #E0D9CC | 实色块底，比次级纸面重一档 |
| Warning | #B26A00 | 需注意但非红线的提示 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 有法条与公文分量的中文衬线，横细竖粗、字面方正 | SimSun | Cambria | serif |
| Body | 屏幕与投影都清楚的中文无衬线，中性、让位于内容 | Microsoft YaHei | Arial | sans-serif |

- **Title stack**: SimSun, Cambria, serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 44 |
| Subtitle | 32 |
| Annotation | 18 |
| Cover title | 88 |
| Chapter title | 56 |
| Chapter numeral | 160 |
| Lead | 28 |
| Data | 64 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 视线从左侧卷宗轨的章节刻度起步，横入眉标与判断句标题，再落到页面主体的单一 primary 载体，最后沉到底部来源行
- **Composition tendency**: 非对称栏宽（窄边注栏 + 宽主栏）为常态，证据页让图表或表格占据主栏全宽充当页面脊柱，结论页改为大留白单焦点，章节页整版反转
- **Cross-page continuity**: 卷宗轨、眉标格式（章号 · 章名）、底部来源行与页码在全卷固定；每章末页右下角预告下一章编号，章节页把它放大——这组编号是跨页连续单元
- **Spacing posture**: variable by page rhythm——证据页紧凑，结论页与章节页大留白
- **Spacing anchors**: 页边距 72 / 区块间距 28 / 栏间距 32 / 圆角 0 / 正文行高 1.65

## VI. Icon Usage Specification

- **Primary bundled library**: chunk-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/chunk-filled/envelope.svg | 邮件、外发 |
| icons/chunk-filled/fish.svg | 钓鱼 |
| icons/chunk-filled/triangle-exclamation.svg | 风险、红线、警示 |
| icons/chunk-filled/shield-check.svg | 合规达标、防护到位 |
| icons/chunk-filled/key.svg | 口令 |
| icons/chunk-filled/keyhole.svg | 身份认证 |
| icons/chunk-filled/user.svg | 员工个人 |
| icons/chunk-filled/users.svg | 团队、内部人员 |
| icons/chunk-filled/building.svg | 企业主体 |
| icons/chunk-filled/eye.svg | 监控、发现异常 |
| icons/chunk-filled/clock.svg | 时限 |
| icons/chunk-filled/hourglass-half-top.svg | 潜伏时长、耗时 |
| icons/chunk-filled/phone.svg | 语音钓鱼 |
| icons/chunk-filled/comment.svg | 短信与即时通信 |
| icons/chunk-filled/magnifying-glass.svg | 核查、识别 |
| icons/chunk-filled/laptop.svg | 办公终端 |
| icons/chunk-filled/wifi.svg | 网络连接 |
| icons/chunk-filled/mobile.svg | 移动端 |
| icons/chunk-filled/floppy-disk.svg | 可移动介质 |
| icons/chunk-filled/arrow-up-from-bracket.svg | 数据外发、上传 |
| icons/chunk-filled/database.svg | 数据资产 |
| icons/chunk-filled/book.svg | 法规文本 |
| icons/chunk-filled/bug.svg | 木马、恶意程序 |
| icons/chunk-filled/link.svg | 可疑链接 |
| icons/chunk-filled/circle-x.svg | 错误做法 |
| icons/chunk-filled/circle-checkmark.svg | 正确做法 |
| icons/chunk-filled/megaphone.svg | 上报 |
| icons/chunk-filled/clipboard.svg | 清单、自测 |
| icons/chunk-filled/trash.svg | 删除、销毁 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P04 | chart | pie_chart | 把数据泄露根因拆成恶意攻击、人为失误、IT 故障三块，让受众看到近半与人直接相关 |
| P05 | chart | column_chart | 并列四种初始入侵途径的占比，凸显钓鱼与凭据滥用合计的体量 |
| P06 | table | record_table | 逐案记录公开通报的内部人员案件：案件、手法、结果、来源年份 |
| P09 | table | comparison_matrix | 以"旧规矩 / 现行要求"两列对照口令的五项规则 |
| P12 | chart | horizontal_bar_chart | 按初始攻击途径比较平均泄露成本，说明社工类途径最贵 |
| P16 | chart | donut_chart | 用一个占比环说明可移动介质在全部泄露中的份额 |
| P20 | table | record_table | 网络安全法条号新旧对照：内容、旧条号、现行条号 |
| P22 | table | metric_table | 三部法律对单位与直接责任人员的罚则区间与附加后果 |
| P26 | table | record_table | 上报时限表：报告主体、报告对象、最迟时限 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

全卷不使用图片资源。全部页面的视觉主体是法条、公开通报案例与统计数据：没有需要"以其本来面目出现"的可核验视觉主体；而钓鱼邮件辨识页若使用截图或 AI 生成的邮件画面，等于制造伪造的证据材料，用户已明确要求自绘原生 SVG 邮件界面示意。因此全部视觉载体由原生 SVG 几何、原生图表与原生表格承担。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 中文讲稿，逐页对应最终 SVG 上的可见内容；每页先给一句过渡与本页判断，再按页面元素出场顺序展开，数据与法条复述时保留年份与出处，不引入页面上没有的新事实。第 28 页的备注必须完整给出五道判断题的答案（全部为"错"）与每题的一句解析和依据来源。备注不复制页面文字，承担页面未写出的解释、过渡与答案。
- **Total duration**: 约 45 分钟（28 页，平均每页约 1.6 分钟）
- **Notes style**: 讲解型、耐心、先定义后使用，章节之间明确报站（"上一章我们把账号锁好了，这一章看数据"）
- **Presentation purpose**: 先让新员工承认"个人日常操作就是企业的风险敞口"，再按账号、数据设备、合规红线三个面教会可执行的行为准则，最后把"发现异常立即上报"固化成动作

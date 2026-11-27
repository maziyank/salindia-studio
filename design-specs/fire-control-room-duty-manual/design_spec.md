<!-- ppt-master-schema: design-spec/v1 -->
# 消防控制室值班手册 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 消防控制室值班手册 |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 16 |
| Primary Language | zh-CN |
| Target Audience | 新上岗的消防控制室值班员(已取得或正在取得消防设施操作员证的监控操作方向人员);受过设备按键层面的基础培训,但没有把散落在国家标准、法规和统计里的值班规则串成一条可推导的判断轴 |
| Communication Intent | 以教学为主、留档交接为辅:先建立"报警信号 → 处于哪一级 → 下一步做什么"的判断轴,再把每一级的规则回溯到它依赖的机制,最后交付可当班携带的检查表与人员配置表 |
| Desired Audience Outcome | 值班员在接到报警后不翻手册即可说出自己处于哪一级、该级唯一正确的动作是什么,并能正确填写值班与交接记录 |
| Core Message / Ask / Action | 值班不是盯屏幕,是把每一个报警信号推进到一个明确的级别,并在该级别上执行唯一正确的动作 |
| Delivery Context | 讲师主导的内部上岗培训课,约 35 分钟;课后作为电子手册留存,供当班随时翻阅 |
| Artifact Afterlife | 上岗前自查与班组复训;检查表页与人员配置表页需要能被单独打印或导出编辑 |
| Reading Mode | balanced |
| Content Strategy | 把 GB 25506-2010、《消防法》、国家职业标准与年度火灾统计中的值班规则重组为一条四级判断轴;事实一律不外扩,凡自建的分级、框架与推论在页面上标注"整理",引自条文的标注条号 |
| Design Style | Duty Manual(勤务手册)Style:判断句标题、机制先于规则、规则回溯机制页;深底硬网格、零圆角细线容器、左缘进度指示条、两种强调色分工固定 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 最终 Stage-2 主动建议值(默认 true) |
| Custom Animations | enabled — 用户在本次运行指令中明确要求自定义动画 |
| Narration Audio | disabled — 最终 Stage-2 主动建议值(默认 false) |
| Created Date | 2026-09-11 |

- **Template Application**: 采用 duty-manual Style 的全部方法层与视觉默认值:标题写成可判断的句子,机制页先于规则页,每条规则标出它回溯的机制页;深底、零圆角细线容器、左缘进度指示条(当前节亮强调色、反例页整条转警示色)、两种强调色分工固定(黄绿承载关键量与正确做法,橙红承载危险、禁止与最高级别)。Style 未提供原型与结构,页面为自由设计的 flat 结构;Style 的回退配色与字体表在本项目没有 Brand/Deck 身份可覆盖的前提下整套采用。Style §VII 的 Review Focus 仅作为自检清单,不触发 visual-review 阶段。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上 56 / 下 56 / 左 96(含左缘指示条 24 + 间距)/ 右 64 |
| Content Area | x 96–1216,y 56–664 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional, pyramid
- **Mode Behavior**: 每节以一句可判断的结论开场,再按"拆开—展开—应用"三拍讲机制:先讲对象是什么与它的代价,再讲什么条件下会变化,最后讲它要求的配置与动作。全 deck 只保留一条纵向判断轴,任何一页都能回答"现在在第几级、第几步"。标题写成判断句而不是名词短语。
- **Visual style**: custom
- **Visual Style References**: swiss-minimal, blueprint, dark-tech
- **Visual Style Behavior**: 深底之上的严格网格手册。swiss-minimal 负责基线栏、硬左对齐边与大留白;blueprint 负责细线网格、引出线注解与剖面式图解排布;dark-tech 负责深底上的荧光级强调与几何精度。容器一律为零圆角的细线方框,无投影无辉光。左缘固定一条分节进度指示条,当前节以强调色点亮,离轴内容整条转为警示色。
- **Theme**: 一本挂在值班台上的技术手册:线是信息,不是装饰;判断轴贯穿全书,读者随时知道自己在哪一格
- **Tone**: 克制、准确、可执行;不煽情,不用"务必""切记"一类空词,用条款号与代价说话

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #0E1B2E | 全 deck 深色场地 |
| Secondary background | #1A2C46 | 面板、表头、图解衬底 |
| Primary | #4A9FD8 | 结构线、次级标题、图表主系列 |
| Accent | #D8F04A | 关键量、当前级别、正确做法 |
| Secondary accent | #E85D2B | 危险、禁止、最高风险级别与离轴内容 |
| Body text | #DCE6F0 | 正文与主要标签 |
| Secondary text | #8FA3BC | 注解、脚注、来源行 |
| Divider | #2A3F5C | 分隔线与容器描边 |
| Surface | #16273D | 表格奇偶行与次级面板底,比 Secondary background 更沉 |
| Grid | #1C2E49 | 细线网格背景,永远比 Divider 更弱 |
| Scrim | #0A1422 | 压在实景图上的定向遮罩底色(配透明度使用) |

### AI Image Strategy

- **Image Rendering**: custom
- **Visual**: 两个互补的登记册共享同一深底与同一组强调色——其一是白色等线宽技术线图(无填充、正交连线、端点圆点、引出线注解),其二是冷光深色的实景画面(值班台、报警控制器面板、状态旋钮),画面内一律无文字
- **Mood**: 像一份工程图册和一组夜班现场记录被装订在同一本手册里;前者的参照是工程蓝图,后者的参照是夜间值班室里只有屏幕发光的那种冷静
- **Image Rendering Behavior**: blueprint 负责单一线宽、引出线与剖面式取景;vector-illustration 负责干净的平面主体与无渐变填充;digital-dashboard 负责荧光注解色与刻度式数值显示的观感。线图主体一律用均匀细线勾勒不填充,流向用平行流线与箭头表示,只使用两种强调色——黄绿标关键量、橙红标危险——无渐变、无阴影、无景深、图内无任何文字。实景画面保持同一深底与同一冷光方向,硬边直角嵌入,不做羽化、圆角与倾斜;需要压字处使用定向 scrim 而非整幅压暗。
- **Image Rendering References**: blueprint, vector-illustration, digital-dashboard

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 中性无衬线,方正精确;力量由判断句本身给出 | Microsoft YaHei | Arial | sans-serif |
| Body | 与标题同族;长机制段落久读不累 | Microsoft YaHei | Arial | sans-serif |
| Display | 极重无衬线,用于章节号、级别标记与冲击数字 | Arial Black | Arial Black | sans-serif |
| Data | 等宽等高数字,表格与图表数值对齐 | Arial | Arial | sans-serif |
| Annotation | 与正文同族的小号注解与引出线标签 | Microsoft YaHei | Arial | sans-serif |
| Footnote | 与正文同族的来源行与页码 | Microsoft YaHei | Arial | sans-serif |

- **Title stack**: `'Microsoft YaHei', Arial, sans-serif`
- **Body stack**: `'Microsoft YaHei', Arial, sans-serif`
- **Display stack**: `'Arial Black', 'Microsoft YaHei', sans-serif`
- **Data stack**: `Arial, 'Microsoft YaHei', sans-serif`
- **Annotation stack**: `'Microsoft YaHei', Arial, sans-serif`
- **Footnote stack**: `'Microsoft YaHei', Arial, sans-serif`
- **Role rationale**: Display 与 Data 各自换族——Display 用 Arial Black 取得与正文的重量对比,承载章节号、级别标记与冲击数字;Data 用 Arial 取等高数字,保证原生表格与图表数值右对齐后仍然列齐。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 40 |
| Subtitle | 30 |
| Lead | 28 |
| Display | 96 |
| Data | 22 |
| Annotation | 18 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 左缘指示条先回答"在哪一节",标题横贯顶部给出判断句,证据与图解向右下展开,页面以底部一行可执行结论收口
- **Composition tendency**: 硬左对齐的两栏或不对称分割;图与文在相邻页之间左右互换以形成阅读节奏;机制页图解约占半页
- **Cross-page continuity**: 左缘进度指示条每页都在,分四段对应四节;判断轴的四级标记在第 7 页建立后,在每个层级页以同一形状与位置复现;来源行固定在页脚同一基线
- **Spacing posture**: 机制页与表格页密,分隔页与技术要点页留白;每节至少一页明显低密度作为休息
- **Spacing anchors**: 页边距 56px · 块间距 28px · 栏间距 32px · 圆角 0px · 正文行高 1.55

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/bell.svg | 报警信号、警报到达 |
| icons/tabler-outline/alert-triangle.svg | 风险提示、离轴内容 |
| icons/tabler-outline/phone.svg | 拨打 119、对外报警 |
| icons/tabler-outline/clipboard-check.svg | 交接班逐项检查 |
| icons/tabler-outline/users.svg | 每班人数与岗位 |
| icons/tabler-outline/clock.svg | 时限、时段 |
| icons/tabler-outline/flame.svg | 火灾确认、着火部位 |
| icons/tabler-outline/device-desktop.svg | 图形显示装置 |
| icons/tabler-outline/toggle-right.svg | 自动/手动状态 |
| icons/tabler-outline/door-exit.svg | 疏散与安全出口 |
| icons/tabler-outline/certificate.svg | 职业资格证书 |
| icons/tabler-outline/file-text.svg | 记录与档案资料 |
| icons/tabler-outline/link.svg | 规则回溯与来源链接 |
| icons/tabler-outline/ban.svg | 禁止做法 |
| icons/tabler-outline/droplet.svg | 消防储水设施与水位 |
| icons/tabler-outline/wind.svg | 防排烟风机 |
| icons/tabler-outline/eye.svg | 核实、观察 |
| icons/tabler-outline/checklist.svg | 清单项与巡查记录 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | chart | grouped_bar_chart | 同一年度内,两个时段的火灾起数占比与亡人数占比并排对比 |
| P13 | table | record_table | 交接班逐项检查记录:检查项、合格判据、依据条款、挡住的风险 |
| P14 | table | record_table | 每班岗位设置:人数、资格要求、主要职责与依据 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_control_room_night.png | 2752x1536 | 16:9 | 封面场景的原始生成件,仅用于派生 | Source | 原始生成件不上页,派生件承担全出血 | adaptive | ai | Generated | 夜间消防控制室内景:一排火灾报警控制器与一面图形显示装置屏幕低亮发光,冷蓝夜色,值班台在前景,无人物面部,画面左半安静、右半承载设备 | none | hero_page |
| cover_control_room_night_fit.jpg | 1280x714 | 16:9 | 封面全出血场景(Slide 01) | 实景 | 全出血铺满整页,配自右向左减弱的定向 scrim,把判断句标题留在左半安静区 | adaptive | ai | Generated | Derived from cover_control_room_night.png; treatment=fit 1280x720; 降到计划上屏尺寸 | none | hero_page |
| divider_alarm_panel.png | 2752x1536 | 16:9 | 第一节分隔页底图的原始生成件,仅用于派生 | Source | 原始生成件不上页,派生件承担全出血 | adaptive | ai | Generated | 火灾报警控制器面板特写:指示灯阵列与按键行,斜向取景,深色背景,冷光,左侧留黑 | none | hero_page |
| divider_alarm_panel_fit.jpg | 1280x714 | 16:9 | 第一节分隔页底图(Slide 04) | 实景 | 全出血底图,巨大章节号与判断句压在左侧安静区,右侧留给面板本身 | adaptive | ai | Generated | Derived from divider_alarm_panel.png; treatment=fit 1280x720; 降到计划上屏尺寸 | none | hero_page |
| divider_duty_log.png | 2752x1536 | 16:9 | 第二节分隔页底图的原始生成件,仅用于派生 | Source | 原始生成件不上页,派生件承担全出血 | adaptive | ai | Generated | 值班台面俯视:摊开的空白值班记录本、手电与对讲机聚在左半幅,右半幅留空,冷光 | none | hero_page |
| divider_duty_log_fit.jpg | 1280x714 | 16:9 | 第二节分隔页底图(Slide 12) | 实景 | 全出血底图,章节号与判断句压在右侧安静区 | adaptive | ai | Generated | Derived from divider_duty_log.png; treatment=fit 1280x720; 降到计划上屏尺寸 | none | hero_page |
| diagram_signal_chain.png | 2528x1696 | 3:2 | 信号链路线图的原始生成件,仅用于派生 | Source | 原始生成件不上页,派生件承担半页线图 | no-crop | ai | Generated | 白色等线宽技术线图:探测器与手动报警按钮经正交连线汇入火灾报警控制器,再到消防联动控制器与受控设备,另有一条支路指向远程监控中心;端点小圆点,箭头示流向,无填充、无文字 | none | local |
| diagram_signal_chain_fit.png | 715x480 | 3:2 | 信号从探测器到监控中心的链路线图(Slide 06) | 线图 | 半页线图置于页面右侧,左侧承载时限判断句与引出线注解 | no-crop | ai | Generated | Derived from diagram_signal_chain.png; treatment=fit 720x480; 降到计划上屏尺寸 | none | local |
| counter_auto_manual_switch.png | 2048x2048 | 1:1 | 反例页主视觉的原始生成件,仅用于派生 | Source | 原始生成件不上页,派生件承担方形主视觉 | adaptive | ai | Generated | 联动控制器面板上旋转状态选择旋钮的近景,指针明显偏离正上方位置,旁边两枚状态指示灯,冷光,无文字 | none | local |
| counter_auto_manual_switch_fit.jpg | 720x720 | 1:1 | 反例页主视觉:自动/手动状态旋钮(Slide 15) | 实景 | 单一主视觉居右成方形硬边嵌入,禁止标记叠在其上,左侧留给机制与罚则 | adaptive | ai | Generated | Derived from counter_auto_manual_switch.png; treatment=fit 720x720; 降到计划上屏尺寸 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页备注承接该页的判断句,先给结论再给支撑;条文一律注明条款号,整理出的分级、岗位分工与推论明确说明是本手册整理;不引入页面上没有的新事实,不复述页面文字
- **Total duration**: 约 35 分钟,单页 1.5—3 分钟,表格页与反例页偏长
- **Notes style**: 讲师口语但克制,先结论后支撑;过渡句用因果关系连接,不用"接下来我们看"一类填充句
- **Presentation purpose**: 以教学为主、留档交接为辅,建立"报警信号 → 处于哪一级 → 下一步做什么"的判断轴

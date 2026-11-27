<!-- ppt-master-schema: design-spec/v1 -->
# container_shipping_editorial_ppt169_20260918 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | container_shipping_editorial_ppt169_20260918 |
| Canvas Format | PPT 16:9 (ppt169) 1280 × 720 |
| Page Count | 12 |
| Primary Language | zh-CN |
| Target Audience | 公司读书会成员,来自不同部门、非物流专业;读过或没读过《集装箱改变世界》都有,对"一个铁盒子怎么会那么重要"普遍存疑 |
| Communication Intent | 先用 1956 年那一船的具体场景把话题从"物流常识"拉到"历史转折",再解释标准化与多式联运这两个机制,最后交代代价与今天的量级,并留下一个可以当场讨论的问题;顺序不可颠倒,机制部分优先于规模数字 |
| Desired Audience Outcome | 能复述集装箱化成立的三个条件(箱、标准、整条链路),能说出至少两组带年份的量化对照(5.83 美元/吨 → 0.16 美元/吨;完全集装箱化当期 +248%),并愿意就"今天什么东西可能是下一个集装箱"发言 |
| Core Message / Ask / Action | 改变世界的不是那个铁盒子,而是所有人同意用同一个盒子——真正稀缺的是让各方放弃自有方案的那套标准 |
| Delivery Context | 主要为读书会现场主讲约 25 分钟,有投影、可随时打断讨论;次要为会后单独翻阅的读书笔记 |
| Artifact Afterlife | 读书会记录留档,内部分享转发,后续读书会的选题参考 |
| Reading Mode | balanced |
| Content Strategy | 未指定,按平衡默认:以研究补充包的事实为准重新组织叙事线,不照抄来源顺序;所有外部事实保持出处与年份,自建的归类框架在页面上标注「整理」 |
| Design Style | 杂志式满幅照片编辑体(custom mode + custom visual style),照片承担论证、文字反白压在渐变 scrim 上 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 委托确认下的最终 Stage-2 主动值 true(工作流默认亦为 enabled);读书会主讲需要逐页的讲述线与讨论抓手 |
| Custom Animations | enabled — 委托确认下的最终 Stage-2 主动值 true;全卷有一个跨页延续的章节眉标 `chapter-rail`,在 P01→P05 与 P07→P09 之间逐页重新落位,Morph 有明确职责;照片本身的「压暗预告 → 全幅展开」是静态取景延续,不参与 Morph——结构化页面的 picture 槽是 placeholder,导出会把它改写成版式占位符,不可配对 |
| Narration Audio | disabled — 委托确认下的最终 Stage-2 主动值 false;现场有主讲人,不需要旁白音轨 |
| Created Date | 2026-09-18 |

- **Template Application**: 使用库版式 `editorial_bleed` 的全部 10 个原型,`chapter_full` 与 `full_statement` 各用两次、其余各一次,共 12 页。结构严格沿用:Master/Layout 键、槽位 id/类型/索引/默认 bounds 一律不改;每页的 scrim 仍按该版式约定作为 Slide 本地 `decoration` 置于图片槽之后,不上移到 Layout。允许改动的只有三类预览值——(1) 原型里的中性预览配色(`master-background` 的 `#0F172A`、`split-bleed-accent` / `split-bleed-reverse-accent` / `full-statement-accent` 的 `#475569`)替换为本卷锁定的调色板;(2) 文字载体字号从原型的预览值改为本卷锁定的角色锚点,并相应校正 baseline 使其留在原槽位框内;(3) 图片载体的 `preserveAspectRatio` 从占位像素用的 `none` 改为 `xMidYMid slice`,以便真实照片按出血裁切。`08_image_grid_four` 不补页面标题(按该版式约定由四条字幕承担阅读顺序),`07_triptych` 的标题留在顶部渐变里。第 (4) 类允许改动是 scrim 的强度:visual-review 实测原型的 `triptych-top-paint`(0.78→0)、`triptych-bottom-paint`(0→0.80)与 `hero-side-scrim-paint`(0.88→0.30→0)在文字实际落点上已衰减到接近全透明,压字对比度不合格,因此为这三处渐变补了中间停靠点并把顶部渐隐带由 200 px 延到 300 px——四种压字技法(底部渐隐/方向性 scrim/整幅洗片/径向暗角)与槽位几何一概未动,只调强度。来源行、「整理」标记与 P10 的对照小字是 Slide 本地文本,不进入任何槽位、不改变 Layout 契约。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 文字四边 80 px;图片不留边,至少触及一条画布边 |
| Content Area | 文字 80,80 – 1200,640;图片为整幅或原型声明的分幅区域 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: narrative, showcase
- **Mode Behavior**: 以 1956 年 4 月 26 日那一船的三个具体数字开场,按"旧世界的代价 → 那一船 → 为什么它没有立刻改变世界 → 标准是怎么成立的 → 战争把它推向亚洲 → 代价与今天的量级 → 一个留给读书会的问题"推进张力弧;每一章以一句可争论的判断收束,而不是以小结收束。页面语气用 showcase 的节奏:一页一个主张,数字以版面焦点的大字对照出现,解释留给讲者与备注。
- **Visual style**: custom
- **Visual Style References**: photo-editorial, editorial, data-journalism
- **Visual Style Behavior**: 满幅照片承担论证(photo-editorial):每页的图片至少触及一条画布边,文字反白压在黑色渐变 scrim 上,版面不出现卡片、圆角容器或阴影。层级由 editorial 的杂志规矩建立:一根 6 px 橙色短棒作为章节与分栏页的起笔,标题与正文之间留一个固定的 24 px 块间距,正文左上角起排。证据层按 data-journalism 处理:每一页带外部事实的版面在 80 px 文字下边距内贴一条 16 px 的来源行,写明出处与年份;自建的归类框架在页面右端标「整理」。唯一的热点色是集装箱橙,只给数字和一个关键词,其余全部落在反白与次级灰蓝上。
- **Theme**: 港口夜色里的编辑版面——深蓝黑作为底板,历史段落走单色调、当代段落走全彩,同一张照片以"压暗预告 → 全幅展开"的方式跨页复现,构成全卷的连续动机。
- **Tone**: 克制、具体、可争论;像一篇有图版的长报道,不像培训材料。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #0B1220 | 深蓝黑底板,Master 背景;仅在照片未覆盖处可见(分栏页的文字半幅、两张 full_statement) |
| Secondary background | #16212F | 次级暗面,供分栏页文字半幅需要与底板拉开时使用 |
| Primary | #4A86B4 | 港口钢蓝,次级强调:分节短棒的冷色端、引语页归属行、图注里的次级标签 |
| Accent | #E2761C | 集装箱橙,全卷唯一热点:数字、章节短棒、关键判断中的一个词 |
| Secondary accent | #BCD4E8 | 浅钢蓝,章节眉标与「整理」标记;visual-review 后由 #8FB4CE 提亮,使 20 px 眉标在照片上的合成对比度过 4.5 |
| Body text | #E8EFF6 | 反白正文与标题 |
| Secondary text | #C7D3DE | 来源行、归属行、章节描述;visual-review 后由 #A6B8C9 提亮,使 16 px 来源行在照片上的合成对比度过 4.5 |
| Divider | #2B3A4C | 细分隔线与暗面边界 |
| Scrim | #000000 | 所有压字渐变的墨色(以 stop-opacity 分级,绝不用实心 rect) |
| Surface | #16212F | 文字半幅的暗面承托 |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: corporate-photo, editorial
- **Image Rendering Behavior**: 线条与材质由 corporate-photo 负责——真实焦段的纪实摄影,自然光与人造光混合,保留皮肤、金属、混凝土的实际质感,真实景深把主体从背景里拉出来,不做插画化处理,画面内不出现文字、标牌字样或可辨认商标。构图与色彩纪律由 editorial 负责——一个主焦区、对齐到隐形栏线、留出一块低反差安静区给压字,调色收敛到深蓝黑底色加一处集装箱橙,边缘可被裁切而不损失信息。历史段落在同一摄影语言内降饱和、走暖灰高光并保留轻微颗粒,当代段落保持全彩冷色夜景;深度靠光,不靠滤镜。
- **Visual**: 港口与码头的纪实照片:门机、箱堆、甲板、旧式散杂货作业、军用补给码头、黎明的超大船
- **Mood**: 工业的、有重量的、略带历史距离感;像《国家地理》或《财富》长报道里的跨页图版

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 硬朗等粗黑体,压在照片上不被高光吃掉 | SimHei | Cambria | sans-serif |
| Body | 屏读与投影都稳的现代黑体 | Microsoft YaHei | Cambria | sans-serif |
| Display | 反白大字断言,方正收边 | SimHei | Cambria | sans-serif |
| Chapter title | 与 Title 同一轴,放大到章节尺度 | SimHei | Cambria | sans-serif |
| Chapter number | 章节序号以衬线数字起笔,带版面的编辑感 | Cambria | Cambria | serif |
| Quote | 引语与标题同轴,居中对称 | SimHei | Cambria | sans-serif |
| Hero number | 版面焦点数字,衬线的等高数字 | Cambria | Cambria | serif |

- **Title stack**: SimHei, Cambria, sans-serif
- **Body stack**: Microsoft YaHei, Cambria, sans-serif
- **Display stack**: SimHei, Cambria, sans-serif
- **Chapter title stack**: SimHei, Cambria, sans-serif
- **Chapter number stack**: Cambria, SimHei, serif
- **Quote stack**: SimHei, Cambria, sans-serif
- **Hero number stack**: Cambria, SimHei, serif
- **Role rationale**: `chapter_number` 与 `hero_number` 从正文族切到 Cambria,因为全卷的编辑气质落在拉丁与数字上——中文一侧用 SimHei 保证压图可读,Cambria 的等高数字负责"杂志感",两者都是 Windows PowerPoint 预装面;`quote` / `chapter_title` / `display` 沿用标题族,只是尺寸角色不同。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 40 |
| Subtitle | 30 |
| Annotation | 20 |
| Footnote | 16 |
| Display | 64 |
| Chapter title | 52 |
| Chapter number | 56 |
| Quote | 44 |
| Hero number | 150 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 视线先落在满幅照片的主体上,再沿渐变 scrim 由暗处进入文字;文字块内部自左上起排,数字是每页唯一允许抢走焦点的元素。
- **Composition tendency**: 每页只解决一个主张;照片要么整幅、要么按原型声明的半幅/三分幅/四分幅切分,绝不内缩成带边距的插图;文字永远在照片最暗的一侧。
- **Cross-page continuity**: 章节眉标 `chapter-rail` 是全卷唯一的 Morph 载体,自封面的「公司读书会」起,在 P01→P02→P03→P04→P05 与 P07→P08→P09 之间逐页重新落位(Slide 本地组,可配对)。同一张照片的「压暗预告 → 全幅展开」(P02→P03、P04→P05)与四格右下角巨轮在收束页放大为整幅(P11→P12)是静态的匹配取景延续(#C3-01 / #C2-02),不作 Morph 配对——这些图片都在 picture 槽里,结构化导出会把槽改写成版式占位符。橙色短棒在两张 full_statement 与两张分栏页之间复现;来源行的位置与字号全卷一致。
- **Spacing posture**: 按 page_rhythm 变化——anchor 页只有标题与一行支撑,dense 页四条证据加一条来源行,breathing 页只有一个数字或一句引语。
- **Spacing anchors**: 页边距 80 px;块间距 24 px;分栏栏距 80 px;圆角半径 3 px(仅用于强调短棒);正文行距 38 px。

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/ruler.svg | 尺寸、规格、度量口径 |
| icons/tabler-outline/lock.svg | 锁定、专利放弃、机械锁具 |
| icons/tabler-outline/stack-2.svg | 堆叠、计量单位、可数性 |
| icons/tabler-outline/ship.svg | 船舶、航线、海运 |
| icons/tabler-outline/clock.svg | 工时、在港时间、周转 |
| icons/tabler-outline/world.svg | 全球范围、跨国采用 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_night_gantry.jpg | 2752×1536 | 16:9 | P01 封面主视觉:夜港门机与箱堆 | Photo | 整幅出血,画面下半保持低反差,让书名与那一船的三个数字压在最暗处 | adaptive | ai | Generated | 夜晚的集装箱码头,数台岸桥门机的钢结构由下向上占据画面上半,远处堆场的箱体被钠灯照出暖点;下半部为无细节的暗水面与码头地坪 | none | hero_page |
| breakbulk_1950s.jpg | 2752×1536 | 16:9 | P03 分栏页左半幅:集装箱之前的散杂货作业 | Photo | 半幅出血放在画面左侧,主体动作居中,左右各留可裁掉的余量 | adaptive | ai | Generated | 1950 年代的杂货码头,几名码头工人正把麻袋与木箱从吊网里搬下,货物散落在栈桥上,吊杆与缆绳斜切画面;人物动作居中,肩背与麻袋是视觉主体 | none | local |
| chapter1_duotone.jpg | 2752×1536 | 16:9 | P02 第一章底图:旧世界的单色调预告 | Derivative | 整幅出血,原型自带的渐变洗片再压一层,只留剪影级别的信息 | adaptive | ai | Generated | Derived from breakbulk_1950s.jpg; treatment=duotone; 把同一张散杂货照片压成暖灰单色调,作为第一章的压暗预告,下一页再全幅展开 | none | local |
| idealx_deck.jpg | 2752×1536 | 16:9 | P04 分栏页右半幅:Ideal X 甲板上的铝箱 | Photo | 半幅出血放在画面右侧,成排箱体沿透视线向画面深处退去 | adaptive | ai | Generated | 一艘 1950 年代改装油轮的甲板,成排的无标识铝制箱体固定在甲板框架上,箱体表面有铆钉与拉筋,背景是桅杆、管路与海面;透视线由近及远 | none | local |
| quote_blur.jpg | 2752×1536 | 16:9 | P05 引语页底图:同一甲板的失焦版本 | Derivative | 整幅出血且完全失焦,只作为居中引语的色场 | adaptive | ai | Generated | Derived from idealx_deck.jpg; treatment=blur; 把 P04 的甲板照片做大半径高斯模糊并轻微降饱和,使居中的引语获得均匀的暗色场 | none | local |
| iso_container_doors.jpg | 2752×1536 | 16:9 | P07 第二章底图:标准箱门与堆场 | Photo | 整幅出血,原型的均匀洗片会压掉一半反差,主体需要足够大的块面 | adaptive | ai | Generated | 黄昏时的集装箱堆场,一排箱门正对镜头,门扇上的锁杆、铰链与角件清晰可见,箱面为素色无字;透视沿箱列向右延伸 | none | local |
| std_band_size.jpg | 1651×2888 | 0.57:1 | P08 左带:尺寸 | Photo | 竖带出血,量度动作居中 | adaptive | slice | Generated | Sliced from sheet_standard_trio.png (1x3, cell 1) | none | local |
| std_band_lock.jpg | 1650×2888 | 0.57:1 | P08 中带:角件与旋锁 | Photo | 竖带出血,金属特写居中 | adaptive | slice | Generated | Sliced from sheet_standard_trio.png (1x3, cell 2) | none | local |
| std_band_count.jpg | 1651×2888 | 0.57:1 | P08 右带:可数的箱堆 | Photo | 竖带出血,箱堆阵列居中 | adaptive | slice | Generated | Sliced from sheet_standard_trio.png (1x3, cell 3) | none | local |
| vietnam_supply_port.jpg | 2752×1536 | 16:9 | P09 整幅底图:军用补给码头 | Photo | 整幅出血,左侧 880 px 会被方向性 scrim 压暗,主体须偏右 | adaptive | ai | Generated | 1960 年代末的军用补给码头,货轮靠泊,岸上堆着成排的箱体与军用物资,起重机与卡车在作业;画面主体偏右三分之一,左侧为开阔的码头地坪与天空 | none | local |
| scale_cell_piers.jpg | 2586×1444 | 16:9 | P11 左上:空置的旧码头 | Photo | 四分之一幅出血,栈桥透视居中 | adaptive | slice | Generated | Sliced from sheet_scale_quad.png (2x2, cell 1) | none | local |
| scale_cell_elizabeth.jpg | 2586×1444 | 16:9 | P11 右上:新建集装箱码头 | Photo | 四分之一幅出血,岸桥阵列居中 | adaptive | slice | Generated | Sliced from sheet_scale_quad.png (2x2, cell 2) | none | local |
| scale_cell_yard.jpg | 2586×1444 | 16:9 | P11 左下:当代港口夜间箱堆 | Photo | 四分之一幅出血,箱堆阵列居中 | adaptive | slice | Generated | Sliced from sheet_scale_quad.png (2x2, cell 3) | none | local |
| scale_cell_megaship.jpg | 2586×1444 | 16:9 | P11 右下:黎明的超大集装箱船 | Photo | 四分之一幅出血,船体侧舷居中,与收束页同一主体 | adaptive | slice | Generated | Sliced from sheet_scale_quad.png (2x2, cell 4) | none | local |
| closing_shanghai_dawn.jpg | 2752×1536 | 16:9 | P12 收束页整幅:黎明的超大船与港口 | Photo | 整幅出血,下三分之一保持低反差承载收束句 | adaptive | ai | Generated | 黎明海面上的超大集装箱船满载驶离港口,船体侧舷占据画面中段,岸桥剪影在远景;与 P11 右下格同一主体、同一时刻,但取景放到整幅 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页写给主讲人的口语讲述线:先一句把上一页接过来的过渡,再展开页面上没写全的因果与细节,最后给一个可以抛给现场的问题或停顿点。所有外部数字在备注里重复其出处与年份,与 `sources/container_shipping_research.facts.json` 的 fact_id 一致;不得引入研究补充包之外的新事实。研究补充包末节列出的九条口径冲突(第二作者为 El-Sahli、1956 年成本取 5.83 美元、越南月运量取 1,200 个、麦克莱恩生年取 1913、ISO 668 首版年份三说并存等)在相关页的备注里明确提醒主讲人,避免现场被追问时给出错误版本。
- **Total duration**: 约 25 分钟(12 页,平均每页 2 分钟,P05 与 P10 各留 1 分钟停顿供现场反应)
- **Notes style**: conversational——读书会口吻,可以直接念,允许出现"这里可以停一下问问大家"这样的现场指令
- **Presentation purpose**: 先用 1956 年那一船把话题从物流常识拉到历史转折,再解释标准化与多式联运两个机制,最后交代代价与今天的量级,并留下一个可当场讨论的问题

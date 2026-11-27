<!-- ppt-master-schema: design-spec/v1 -->
# first_aid_kit_zh_xhs_20260917 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | first_aid_kit_zh_xhs_20260917 |
| Canvas Format | 小红书 (RED) 1242×1660,3:4 竖版 |
| Page Count | 9 |
| Primary Language | zh-CN |
| Target Audience | 中国大陆普通家庭的小红书读者(非医护),多为家里有孩子或老人、想把急救包一次性配齐的人 |
| Communication Intent | 先让读者认清"四类齐全"这个骨架并照着配齐,再让他清掉家里不该留的旧药,最后教会两条最常用的现场处置流程;科普与动员并重,动员优先 |
| Desired Audience Outcome | 读者能照着清单把急救包配齐、把红药水紫药水和过期药清出去、给急救包定一个固定位置和 3 个月的检查节点,并在割伤或烫伤发生时按流程处置而不是凭土办法 |
| Core Message / Ask / Action | 急救包不是囤药,是"止血包扎 + 消毒 + 常用药 + 工具"四类齐全、位置固定、每 3 个月一查;今天就把红药水紫药水和过期药清出去 |
| Delivery Context | 主要为小红书图文轮播的手机端自读,无讲者,任何一张被单独转发也要读得懂;次要为社区急救科普小课的投屏讲解 |
| Artifact Afterlife | 读者长按保存的清单总表;社区讲课可复用的素材 |
| Reading Mode | text |
| Content Strategy | 自由重组研究材料成轮播叙事,页面顺序与标题由沟通目标决定;但医学类说法一律带出处与年份,国内外口径冲突时取国内官方口径并在页面上写明存在争议的条目 |
| Design Style | 手帐急救课(custom mode + custom visual style,暖米纸手绘手帐) |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 用户原话"我也会拿 PPT 去社区讲",委托确认下按最新显式用户意图启用 |
| Custom Animations | enabled — 用户原话"要有动画",委托确认下按最新显式用户意图启用,范围为逐页对象动画加相邻页 Morph 转场 |
| Narration Audio | disabled — 用户未提旁白,委托确认下取工作流默认值 |
| Created Date | 2026-09-17 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | 小红书 |
| Dimensions | 1242 × 1660 |
| viewBox | `0 0 1242 1660` |
| Margins | 上下左右各 88px;底部另留 104px 出处条带 |
| Content Area | x 88–1154(宽 1066),y 88–1468(高 1380),出处条带占 y 1468–1572 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional
- **Mode Behavior**: 按"先给骨架、再逐类展开、再纠错、再落地、最后给两条现场流程和一张总表"的学习顺序推进;页标题写这一页教什么,不写论断;同级的四个类别用同一形状、同一深度并列展开,便于读者在脑子里映射;每一条处置步骤都先给动作、再给参数、再给"别做什么"的注记,注记永远挂在它解释的那一步旁边而不是独立成段。
- **Visual style**: custom
- **Visual Style References**: sketch-notes, editorial
- **Visual Style Behavior**: 由 sketch-notes 提供主体质地——暖米纸底、带轻微手抖的黑墨轮廓、略微溢出边线的柔和色块、稀疏的手绘小装饰与波浪箭头、全平面无投影;由 editorial 提供竖版所需的纵向层级——眉题(kicker)、发丝分隔线、一条贯穿页面的纵向标尺挂载内容、超大序号或数字作为页面锚点、非均分的不对称分栏。两者的分工是:形状与质地归手绘,秩序与层级归编辑排版,避免手帐感变成散乱的涂鸦板。
- **Theme**: 一本摊开的家庭急救手帐——每一页都像手写在暖米纸上的一页笔记,靠一条贯穿左侧的纵向标尺和统一的手绘圆角卡片维持九页的同一性;跨页母题是"急救箱开合":封面是合着的箱子,P02 打开成四格,P07/P08 变成同一条手绘步骤链,P09 收拢成一张可保存的总表。
- **Tone**: 可靠、克制、不吓人;像社区里一位耐心的护士在纸上一条条写给你

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FBF6EC | 暖米纸主底,九页统一 |
| Secondary background | #F2E8D5 | 分区色块、表格隔行、次级卡片底 |
| Primary | #1F6F5C | 墨绿,页标题、纵向标尺、主要图标与正向结构色 |
| Accent | #D94F3D | 急救红,仅用于超大标题字、十字/警示图形与重点标记,不作正文色 |
| Secondary accent | #E8A33D | 暖橙,提醒类注记、检查周期、时间参数 |
| Body text | #2B2A26 | 墨黑正文与手绘轮廓线 |
| Secondary text | #6B6558 | 说明、出处、页码指示 |
| Divider | #D9CDB8 | 发丝线、表格线、卡片边 |

补充锁定的语义中性层与极性角色:`surface` #FFFDF7(卡片纸面)、`block-shade` #EFE3CC(手绘色块的低饱和铺底)、`positive` #3F8F5B(该留/正确做法)、`warning` #E8A33D(注意事项)、`negative` #C0392B(该清出去/禁止做法)。Accent 与 negative 对纸底对比度约 3.8:1,因此只用于 56px 以上的大字与图形,正文与注记一律使用 body text 或 secondary text。

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: sketch-notes
- **Visual**: 暖米纸底上的黑墨手绘线稿,线条带轻微手抖、粗细均匀;色块是从墨绿/暖橙/急救红派生出的低饱和柔和平涂,并略微溢出轮廓线,呈手绘上色的错位感;物体简化到可辨识即可,不追求解剖级细节;画面留白充裕,无投影、无渐变、无高光。
- **Mood**: 温和、可靠、像社区诊室墙上贴的手绘科普图,或一位老师在教学笔记本上画给你看的示意图
- **Image Rendering Behavior**: 手绘教学笔记风格——黑墨轮廓带轻微手抖,色块从 deck 的墨绿、暖橙、急救红三个角色派生为低饱和柔和平涂并略微溢出轮廓,纸面带 8–12% 的纸纹;深度完全平面,不加投影与渐变;偶有极少量手绘小装饰(短线、圆点)增加温度。九张图共用同一线宽与同一上色错位量,以此保证一致性。

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 无衬线/厚重,像马克笔写在纸上的板书标题 | SimHei | Arial Black | sans-serif |
| Body | 无衬线/人文清晰,长时间手机阅读不累 | Microsoft YaHei | Arial | sans-serif |
| Display | 无衬线/超粗,用于封面主标 | SimHei | Arial Black | sans-serif |
| Hero number | 无衬线/超粗,用于页面英雄数字(3 个月、20 分钟) | SimHei | Arial Black | sans-serif |
| Annotation | 无衬线/清晰小字,与正文同族以免手帐页面出现第三种字味 | Microsoft YaHei | Arial | sans-serif |
| Footnote | 无衬线/清晰小字,承载出处条与页序指示 | Microsoft YaHei | Arial | sans-serif |

- **Title stack**: SimHei, Arial Black, sans-serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Display stack**: SimHei, Arial Black, sans-serif
- **Hero number stack**: SimHei, Arial Black, sans-serif
- **Annotation stack**: Microsoft YaHei, Arial, sans-serif
- **Footnote stack**: Microsoft YaHei, Arial, sans-serif
- **Role rationale**: Display 与 Title 同族但独立成锚,因为封面主标 128px 与英雄数字 96px 在九页里反复出现,不能依赖 Executor 的 ±2px 带;Annotation / Footnote 与 Body 同族,只是尺寸角色,单独声明是为了让出处条、注记、页序指示在九页之间保持同一字号。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 44 |
| Title | 80 |
| Subtitle | 56 |
| Annotation | 32 |
| Display (cover title) | 128 |
| Hero number | 96 |
| Lead | 52 |
| Kicker | 36 |
| Step number | 48 |
| Table cell | 36 |
| Footnote | 26 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 竖版从上往下读——眉题 → 页标题 → 一句核心判断 → 分块内容 → 底部出处条;每页只给一个视觉主角(一张插画、一个英雄数字、一条步骤链或一张表),其余元素退为支撑。
- **Composition tendency**: 纵向堆叠优先,横向最多二等分;左侧一条贯穿全页的纵向标尺(墨绿细线加节点)承担"这是同一本手帐"的连续性;分类内容用非均分的上下带状分区而不是均匀卡片网格;每页至少有一处让内容越出分区边界(插画压线、序号出框)以打破网格感。
- **Cross-page continuity**: 纵向标尺、眉题位置、底部出处条、页序指示九页不变;插画风格、线宽、上色错位量不变;卡片圆角与色块用法不变。变化的是分区节奏、主角类型与色块的主色。
- **Spacing posture**: variable by page rhythm——anchor 页(P01/P02/P09)大留白,dense 页(P03–P08)压缩块间距但保持行距不变
- **Spacing anchors**: page margin 88px · block gap 48px · column gutter 40px · corner radius 28px · body leading 72px

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-outline/first-aid-kit | 急救包本体、总览、封面与总表的身份标记 |
| tabler-outline/bandage | 止血包扎类目、创可贴与敷料相关条目 |
| tabler-outline/vaccine-bottle | 消毒类目、碘伏与生理盐水等瓶装物 |
| tabler-outline/pills | 常用药类目、按用途分类的药品条目 |
| tabler-outline/thermometer | 工具类目中的体温计、体征测量 |
| tabler-outline/scissors | 工具类目中的圆头剪刀、剪开粘连衣物 |
| tabler-outline/droplet | 冲洗、生理盐水、流动水相关动作 |
| tabler-outline/flame | 烫伤主题标记 |
| tabler-outline/alert-triangle | 注意事项、争议条目、必须就医的判断 |
| tabler-outline/trash | 清理出去、过期药处置 |
| tabler-outline/calendar-repeat | 每 3 个月自查、每年彻底复核 |
| tabler-outline/clock-hour-3 | 时间参数(冲洗时长、浸泡时长、止血带时限) |
| tabler-outline/phone-call | 拨打 120、紧急联系电话 |
| tabler-outline/ban | 禁止做法(红药水紫药水、冰敷、挑破水疱) |
| tabler-outline/hand-stop | 直接压迫止血、用手掌按压的动作 |
| tabler-outline/mask | 医用外科口罩、施救前防护 |
| tabler-outline/shield-check | 防护到位、正确做法确认 |
| tabler-outline/cut | 割伤主题标记 |
| tabler-outline/tools | 工具类目总标记 |
| tabler-outline/bottle | 液体类物品(酒精、碘酊、双氧水)与该清出去的旧药瓶 |
| tabler-outline/stethoscope | 就医、专业处置 |
| tabler-outline/medical-cross | 急救身份标记、总表页页眉 |
| tabler-outline/snowflake | 不要冰敷、低温相关禁忌 |
| tabler-outline/bath | 别放卫生间的存放禁忌 |
| tabler-outline/clipboard-list | 检查五步、清单与记录 |
| tabler-outline/home | 存放位置、家庭场景 |
| tabler-outline/bulb | 手电筒、提示与小知识 |
| tabler-outline/emergency-bed | 送医、必须就医的判断 |
| tabler-outline/circle-number-1 | 流程步骤序号 |
| tabler-outline/circle-number-2 | 流程步骤序号 |
| tabler-outline/circle-number-3 | 流程步骤序号 |
| tabler-outline/circle-number-4 | 流程步骤序号 |
| tabler-outline/circle-number-5 | 流程步骤序号 |
| tabler-outline/arrow-narrow-right | 步骤之间的推进指向 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P09 | table | record_table | 把四类必备物品与两条"该清出去"逐条列成可长按保存的总表,每行一件物品,列为分类 / 物品 / 要点 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_kit.jpg | 1792×2400 | 3:4 | 封面主视觉:一只摊开的家用急救包 | Illustration | 满幅竖版底图,上三分之一留白让主标与钩子句落在纸面上,物件集中在下三分之二 | adaptive | ai | Generated | 俯视一只打开的布质家用急救包,内容物向外摊开:纱布卷、绷带、创可贴盒、碘伏小瓶、棉签、圆头剪刀、镊子、体温计、一次性手套。构图为竖版,画面上三分之一为空白暖米纸,物件在下三分之二呈散开的放射状,视线落点在正中的急救包本体 | none | hero_page |
| kit_bandage.jpg | 715×688 | 1.04:1 | 止血包扎类目图 | Illustrated icon | 类目标题左侧的图示,与同页另外三格同尺寸并列 | no-crop | slice | Generated | Derived from illus_sheet_a.png; cell=1 | none | local |
| kit_antiseptic.jpg | 685×682 | 1.00:1 | 消毒类目图 | Illustrated icon | 类目标题左侧的图示,与同页另外三格同尺寸并列 | no-crop | slice | Generated | Derived from illus_sheet_a.png; cell=2 | none | local |
| kit_medicine.jpg | 757×656 | 1.15:1 | 常用药类目图 | Illustrated icon | 类目标题左侧的图示,与同页另外三格同尺寸并列 | no-crop | slice | Generated | Derived from illus_sheet_a.png; cell=3 | none | local |
| kit_tools.jpg | 819×726 | 1.13:1 | 工具类目图 | Illustrated icon | 类目标题左侧的图示,与同页另外三格同尺寸并列 | no-crop | slice | Generated | Derived from illus_sheet_a.png; cell=4 | none | local |
| no_old_drugs.jpg | 804×772 | 1.04:1 | "该清出去"的旧药瓶与拆开的旧药板 | Illustrated icon | 放在禁止区块内,与手绘禁止符号叠合 | no-crop | slice | Generated | Derived from illus_sheet_b.png; cell=1 | none | local |
| kit_storage.jpg | 870×817 | 1.06:1 | 存放位置示意:抽屉柜里的急救包 | Illustrated icon | 存放区块右侧的图示,与左侧的位置条目并排 | no-crop | slice | Generated | Derived from illus_sheet_b.png; cell=2 | none | local |
| cut_press.jpg | 860×837 | 1.03:1 | 直接压迫止血动作示意 | Illustrated icon | 压在"压"这一步的步骤节点旁,与序号同高 | no-crop | slice | Generated | Derived from illus_sheet_b.png; cell=3 | none | local |
| burn_water.jpg | 857×805 | 1.06:1 | 流动自来水冲洗烫伤动作示意 | Illustrated icon | 压在"冲"这一步的步骤节点旁,与序号同高 | no-crop | slice | Generated | Derived from illus_sheet_b.png; cell=4 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Content**: 每页备注按该页最终 SVG 的可见分组逐块讲解,面向社区急救科普小课的现场讲者;用 instructional 的耐心讲解口吻,先说这一页要解决什么问题,再按页面上的语义顺序讲每一块,并补充页面上放不下的出处细节(发布机构与年份)与口径差异(如国内 3 个月 vs 美国红十字会 1 年、国内 15~30 分钟 vs NHS/ANZCOR 20 分钟);只引用 `sources/first_aid_kit_zh_research.facts.json` 里已有的 fact,不新增外部说法,不给任何剂量建议
- **Total duration**: 约 12–15 分钟(9 页,每页 80–110 秒)
- **Notes style**: conversational(耐心讲解型,面向非医护听众)
- **Presentation purpose**: 先让读者认清"四类齐全"的骨架并照着配齐,再让他清掉不该留的旧药,最后教会割伤与烫伤两条现场处置流程

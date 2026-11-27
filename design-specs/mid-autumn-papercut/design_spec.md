<!-- ppt-master-schema: design-spec/v1 -->
# mid_autumn_papercut_default - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | mid_autumn_papercut_default_ppt169_20260902 |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 16 |
| Primary Language | zh-CN |
| Target Audience | 普通中文读者与听众，对中秋有生活经验但没有系统的历史知识；知道嫦娥、月饼、团圆，不知道这些说法各自出自哪一层文本 |
| Communication Intent | 先用一条可核实的物证线索（「月饼」二字的迁徙）把中秋从习惯变成历史；再解释每一个熟悉的意象是哪一代人加上去的；最后回到今天的假期与数字，让听众看见自己正站在这条线的末端 |
| Desired Audience Outcome | 听众能说出中秋从祭仪到节日的三个关键时点（周礼—唐诗—北宋定节），能说清「月饼」一词早于「中秋送月饼」这件事，能指出嫦娥化蟾不出自《淮南子》，并愿意在今年中秋把其中一条讲给别人听 |
| Core Message / Ask / Action | 中秋不是一个从来如此的节日：它的每一层——礼、诗、饼、传说、灯火、名录、假期——都有可查的加入时间；认识这些时点，今晚的月亮会更好看 |
| Delivery Context | 主：2026 年中秋前的线下文化分享，有主讲人，约 25 分钟；次：会后作为可独立阅读的图文材料在社群里传阅 |
| Artifact Afterlife | 作为可反复取用的文化科普材料留存与转发；引用的每条史实可回溯到 sources/ 中的 fact 编号 |
| Reading Mode | balanced |
| Content Strategy | 自由重构：源材料是按研究缺口组织的事实清单，不是页面结构；按叙事弧重新编排、补写过渡与转折，但一切可外部核实的断言只能来自已记录的 fact，不得外扩 |
| Design Style | 月出东山 — 夜色剪纸叙事（custom narrative + custom paper-cut） |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 用户显式指令（客户简报「Speaker notes on」） |
| Custom Animations | enabled — 最新显式用户指令（客户变更：本卷作为展廊示例，需要逐对象自定义动画，不止页面转场；对象级编排在 customize-animations 阶段完成） |
| Narration Audio | disabled — 用户显式指令（客户简报「narration off」） |
| Created Date | 2026-09-02 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上下 56，左右 72 |
| Content Area | x 72–1208，y 56–664 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: narrative
- **Mode Behavior**: 以 narrative 的 situation → tension → resolution 贯穿全卷，并按本题材切成四幕：第一幕给出「熟悉但说不清」的处境，第二幕用「月饼一词早于送月饼」制造第一次转折，第三幕用「化蟾不出《淮南子》」制造第二次转折（把观众的既有认知本身变成冲突），第四幕以名录、假期、数字落回当下，以苏轼的词收束情绪。页标题写成推进弧线的句子而非标签；章页只承担换幕，不承担论证。
- **Visual style**: custom
- **Visual Style References**: paper-cut
- **Visual Style Behavior**: 完整采用 paper-cut 的分层剪纸体系——形体由略不规则的剪切边定义、不画描边，每个色值是一张纸，层与层之间落 8–12% 柔影，纸面带细颗粒；构图上用「一枚大剪圆（月）锚定画面」「模切窗口露出下层」「层叠波形纸自下而上堆叠」三种几何。唯一的定制是把 paper-cut 通常的暖白桌面换成深靛夜场：底层纸是夜，上层纸是月光金、朱砂红与米白，使剪纸的层叠关系靠明度而非暖度拉开。卡片网格被禁止性地替换为「纸片自由叠放」：内容块坐在裁切纸片上，纸片可出血、可轻微旋转、可互相压边。
- **Theme**: 月自海面升起，一路盈满 — 全卷保留一枚剪纸月亮作为连续状态，从封面右下的一弯细牙，经各幕逐页改变相位、尺寸与位置，到末页升至画面中央成为最大的满月；云带、桂枝、远山脊三个剪纸构件在不同页复用，构成前景/中景/背景三层纸的注册深度
- **Tone**: 沉静、有夜气、可触摸；不喜庆化，不做贺卡

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #131A33 | 夜场底纸，全卷页面底色 |
| Secondary background | #1E2748 | 抬起一层的靛蓝纸片，承载内容块与表格 |
| Primary | #E8B04B | 月光金 — 主导前景纸层、页标题、关键数字、月亮本体 |
| Accent | #D4453A | 朱砂红 — 顶层小面积剪出的强调纸片、印章式标记、转折点标注（不用于正文） |
| Secondary accent | #7FA8C9 | 月色青 — 注释、发丝线、次级引导、水面与远山 |
| Body text | #F2ECE0 | 米白宣纸色，正文与引文 |
| Secondary text | #B9C2D8 | 说明文字、图注、来源标注 |
| Divider | #33406B | 分隔线、纸片接缝、表格栏线 |
| Surface | #26305A | 再抬一层的纸面，用于表格头、引文块等需要与 secondary background 区分的层 |
| Scrim | #0C1026 | 压在整幅图像上的暗层，保证图上文字可读 |
| Block shade | #0E1329 | 纸层柔影颜色，比底纸暗一档 |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: paper-cut
- **Visual**: 分层剪纸工艺 — 形体由略带手工不规则的剪切边界定，无任何描边；每一色为一张独立纸片，层间落 8–12% 柔影产生真实厚度；纸面带 10–15% 不透明度的纸纤维颗粒；造型简化为可辨的剪纸而非插画。全部元素在夜靛底纸上以月光金、朱砂红、米白、月色青四张纸构成
- **Mood**: 夜里的手工灯笼纸 — 温度来自纸的质地而非色温；像民间剪纸窗花被逆光照亮，安静、可触摸、带一点仪式感
- **Image Rendering Behavior**: 完全承接 paper-cut 预设的线质、纹理、深度与材质（剪切边、纸颗粒、层叠柔影、卡纸材质），只把它的默认暖白底纸换成本卷的深靛夜场，并规定层叠对比靠明度差建立；人物一律为剪影级简化，不做面部细节。

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 楷体书写体 / 有笔锋的中文标题字 | KaiTi | Georgia | serif |
| Body | 中性无衬线 / 屏幕与投影可读 | Microsoft YaHei | Arial | sans-serif |
| Quote | 楷体书写体 / 古典引文 | KaiTi | Georgia | serif |
| Data | 中性无衬线 / 表格与密集标注 | Microsoft YaHei | Arial | sans-serif |
| Annotation | 中性无衬线 | Microsoft YaHei | Arial | sans-serif |
| Footnote | 中性无衬线 | Microsoft YaHei | Arial | sans-serif |
| Hero number | 衬线数字 / 有重量的西文数字 | Georgia | Georgia | serif |

- **Title stack**: KaiTi, Georgia, serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Quote stack**: KaiTi, Georgia, serif
- **Data stack**: Microsoft YaHei, Arial, sans-serif
- **Annotation stack**: Microsoft YaHei, Arial, sans-serif
- **Footnote stack**: Microsoft YaHei, Arial, sans-serif
- **Hero number stack**: Georgia, serif
- **Role rationale**: `quote` 单列一族，因为全卷有六页承载古籍原文与词句，需与正文黑体形成可识别的引文层；`hero_number` 单列 Georgia，因为楷体阿拉伯数字在大字号下结构松散，而全卷有五处需要大号数字（111、518、Ⅹ-5、1.07 亿、30 万吨）。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 42 |
| Cover title | 72 |
| Chapter title | 52 |
| Subtitle | 30 |
| Lead | 28 |
| Quote | 34 |
| Hero number | 88 |
| Data | 20 |
| Annotation | 18 |
| Footnote | 16 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 每页先有一个占据视觉重量的剪纸物件（月、饼、人物或整幅夜景），再由它引出一句判断句标题，最后才是解释文字；视线自图向文、自上而下或自右向左（跟随月亮所在的一侧）
- **Composition tendency**: 内容坐在裁切纸片上而不是卡片网格里；纸片允许出血、轻微旋转、互相压边；每页至少有一处「模切窗口」或「大剪圆」承担聚焦；禁止把一页平均切成等宽等重的多列格子
- **Cross-page continuity**: 月亮相位与位置构成全卷唯一的连续状态；云带、桂枝、远山脊三个剪纸构件跨页复用并改变尺度与角度；四枚剪纸字（中秋 / 月夕 / 月饼 / 团圆）分别落在封面与三处换幕点
- **Spacing posture**: 随 page_rhythm 变化 — anchor 页大量留出夜场底纸，dense 页允许纸片贴近但保持层间柔影可见，breathing 页只留一件主物加一句话
- **Spacing anchors**: 页边距 72px；块间距 32px；分栏间隙 40px；圆角半径 0px（剪纸不留圆角，边界靠不规则剪切路径）；正文行高 1.65

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P09 | table | comparison_matrix | 以五个流派为列、四项国标属性为行，比较广苏京潮滇的产地、饼皮工艺、口感与代表品种 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_night_field.jpg | 2752×1536 | 18:10 | 封面整幅夜景底纸（干净全画布底层） | Scene | 满版铺底，标题与剪纸构件叠在其上；底层不含主体，主体由透明切片承担 | no-crop | ai | Generated | 层叠剪纸的夜海与远岸：底部两三层波形纸构成海面，上方大片空夜，右下留出安放月牙的空区，左上三分之一保持低密度以承载竖排标题 | none | hero_page |
| kaifeng_night_market.jpg | 2752×1536 | 18:10 | P05 北宋开封中秋夜市的整幅场景 | Scene | 满版页面场，压暗层后承载文字；右侧三分之一留安静区 | no-crop | ai | Generated | 层叠剪纸的宋代城市夜市：酒楼台榭剪影、彩楼欢门、密集的灯与人形剪影自下而上堆叠三层，右上留出被云半掩的月位 | none | hero_page |
| moon_full.png | 495×500 | 10:10 | 满月 — 连续状态的终点 | Illustration element | 大剪圆锚定画面，可被文字压边或出血 | no-crop | slice | Generated | 由 sheet_moon.png 第 1 行第 1 格切出 | none | local |
| moon_gibbous.png | 490×492 | 10:10 | 盈凸月 — 换幕点的状态 | Illustration element | 小剪圆置于页角，随幕次改变位置 | no-crop | slice | Generated | 由 sheet_moon.png 第 1 行第 2 格切出 | none | local |
| moon_half.png | 254×500 | 10:20 | 上弦月 — 用作模切窗口 | Illustration element | 作为剪出的圆形窗口，露出下层纸与文字 | no-crop | slice | Generated | 由 sheet_moon.png 第 1 行第 3 格切出 | none | local |
| moon_crescent.png | 426×508 | 16:19 | 细牙月 — 连续状态的起点 | Illustration element | 封面右下低位，小而偏，留出上升空间 | no-crop | slice | Generated | 由 sheet_moon.png 第 2 行第 1 格切出 | none | local |
| moon_veiled.png | 653×464 | 24:17 | 被云半掩的月 | Illustration element | 与云带叠压，作夜市页右上角的呼吸口 | no-crop | slice | Generated | 由 sheet_moon.png 第 2 行第 2 格切出 | none | local |
| moon_reflection.png | 490×490 | 1:1 | 水面月影 | Illustration element | 置于页面下缘并被波形纸压住一半，暗示泛舟与照无眠 | no-crop | slice | Generated | 由 sheet_moon.png 第 2 行第 3 格切出 | none | local |
| cloud_band.png | 647×275 | 14:6 | 祥云带 — 中景纸层 | Illustration element | 横向掠过页面，压在月与文字之间建立中景 | no-crop | slice | Generated | 由 sheet_moon.png 第 3 行第 1 格切出 | none | local |
| osmanthus_sprig.png | 483×500 | 23:24 | 桂枝 — 角部构件 | Illustration element | 自页角斜出，可出血，跨页改变角度与尺度 | no-crop | slice | Generated | 由 sheet_moon.png 第 3 行第 2 格切出 | none | local |
| mountain_ridge.png | 621×191 | 13:4 | 远山脊 — 背景纸层 | Illustration element | 贴页面下缘的最底一层剪纸，建立地平线 | no-crop | slice | Generated | 由 sheet_moon.png 第 3 行第 3 格切出 | none | local |
| change_e.png | 755×633 | 19:16 | 嫦娥奔月剪影 | Illustration element | 主体人物，可被标题压边，形成前景层 | no-crop | slice | Generated | 由 sheet_legend.png 第 1 行第 1 格切出 | none | local |
| wu_gang.png | 393×706 | 10:18 | 吴刚伐桂剪影 | Illustration element | 与桂树成对放置，体现「树创随合」的循环 | no-crop | slice | Generated | 由 sheet_legend.png 第 1 行第 2 格切出 | none | local |
| osmanthus_tree.png | 704×623 | 17:15 | 月中桂树 | Illustration element | 与吴刚同页，作为被砍与复合的对象 | no-crop | slice | Generated | 由 sheet_legend.png 第 1 行第 3 格切出 | none | local |
| jade_rabbit.png | 524×605 | 13:15 | 玉兔捣药 | Illustration element | 长跪姿态，置于月轮之内或之侧 | no-crop | slice | Generated | 由 sheet_legend.png 第 2 行第 1 格切出 | none | local |
| toad.png | 579×481 | 12:10 | 蟾蜍 | Illustration element | 小件，与嫦娥并置以标出「化蟾」这一后加层 | no-crop | slice | Generated | 由 sheet_legend.png 第 2 行第 2 格切出 | none | local |
| elixir_jar.png | 408×508 | 12:15 | 不死药壶 | Illustration element | 小件，作为叙述起点的物证 | no-crop | slice | Generated | 由 sheet_legend.png 第 2 行第 3 格切出 | none | local |
| fire_dragon.png | 797×912 | 14:16 | 大坑舞火龙 | Illustration element | 习俗页最大的一件，斜向贯穿并可出血 | no-crop | slice | Generated | 由 sheet_custom.png 第 1 行第 1 格切出 | none | local |
| lantern_tower.png | 624×912 | 13:19 | 烧塔 / 瓦子灯 | Illustration element | 与火龙成组，尺度小一档 | no-crop | slice | Generated | 由 sheet_custom.png 第 1 行第 2 格切出 | none | local |
| lantern_pole.png | 376×932 | 2:5 | 树中秋彩灯高杆 | Illustration element | 竖向构件，用于打断横向节奏 | no-crop | slice | Generated | 由 sheet_custom.png 第 2 行第 1 格切出 | none | local |
| dice_bowl.png | 821×636 | 22:17 | 博饼骰碗 | Illustration element | 俯视小件，作为「玩法」一节的语义提示 | no-crop | slice | Generated | 由 sheet_custom.png 第 2 行第 2 格切出 | none | local |
| rabbit_lord.png | 891×1755 | 10:20 | 兔儿爷泥塑 | Illustration element | 名录页的单一主角，正面端坐 | no-crop | slice | Generated | 由 sheet_figures.png 第 1 格切出 | none | local |
| walking_pair.png | 934×1678 | 10:18 | 走月的一对行人 | Illustration element | 小尺度人形剪影，跨页复用于临安与习俗两页 | no-crop | slice | Generated | 由 sheet_figures.png 第 2 格切出 | none | local |
| cake_guang.png | 611×635 | 23:24 | 广式月饼 | Illustrated icon | 与表格首列对齐的行标识，不进容器 | no-crop | slice | Generated | 由 sheet_mooncake.png 第 1 行第 1 格切出 | none | local |
| cake_su.png | 629×503 | 10:8 | 苏式月饼 | Illustrated icon | 同上；另在 P08 放大作为「南宋点心」的物证 | no-crop | slice | Generated | 由 sheet_mooncake.png 第 1 行第 2 格切出 | none | local |
| cake_jing.png | 602×592 | 10:10 | 京式月饼 | Illustrated icon | 同上；另在 P08 放大作为「明代馈赠」的物证 | no-crop | slice | Generated | 由 sheet_mooncake.png 第 1 行第 3 格切出 | none | local |
| cake_chao.png | 599×604 | 10:10 | 潮式月饼 | Illustrated icon | 与表格首列对齐的行标识 | no-crop | slice | Generated | 由 sheet_mooncake.png 第 2 行第 1 格切出 | none | local |
| cake_dian.png | 633×504 | 10:8 | 滇式月饼 | Illustrated icon | 与表格首列对齐的行标识 | no-crop | slice | Generated | 由 sheet_mooncake.png 第 2 行第 2 格切出 | none | local |
| cake_mold.png | 678×638 | 17:16 | 木质月饼模子 | Illustration element | 章页与转折页的主物件，可大幅出血 | no-crop | slice | Generated | 由 sheet_mooncake.png 第 2 行第 3 格切出 | none | local |
| letter_zhongqiu.png | 874×615 | 17:12 | 剪纸美术字「中秋」 | Decorative lettering | 封面显示层，与原生标题分置两处 | no-crop | slice | Generated | 由 sheet_lettering.png 第 1 行第 1 格切出；原生标题另行保留 | embedded | local |
| letter_yuexi.png | 845×620 | 15:11 | 剪纸美术字「月夕」 | Decorative lettering | 第一幕章页的幕标 | no-crop | slice | Generated | 由 sheet_lettering.png 第 1 行第 2 格切出；章名另有原生文字 | embedded | local |
| letter_yuebing.png | 871×614 | 17:12 | 剪纸美术字「月饼」 | Decorative lettering | 第二幕章页的幕标 | no-crop | slice | Generated | 由 sheet_lettering.png 第 2 行第 1 格切出；章名另有原生文字 | embedded | local |
| letter_tuanyuan.png | 855×606 | 24:17 | 剪纸美术字「团圆」 | Decorative lettering | 末页的收束标记 | no-crop | slice | Generated | 由 sheet_lettering.png 第 2 行第 2 格切出；结语另有原生文字 | embedded | local |
| cover_night_field_dawn.jpg | 1600×893 | 18:10 | 末页的同场景低能量变体 | Derivative | 满版铺底，比封面暗一档、偏金，作为首尾呼应的同一片海 | no-crop | ai | Generated | Derived from cover_night_field.jpg; treatment=duotone+brightness | none | local |
| mooncake_mold_wash.png | 678×638 | 17:16 | 表格页背后的超大低对比纹样 | Derivative | 放大出血的背景纹样，压在表格之下不与文字争对比 | no-crop | ai | Generated | Derived from cake_mold.png; treatment=grayscale+brightness+fit | none | local |
| changee_flight_scrim.png | 755×633 | 19:16 | 嫦娥页的远层虚影 | Derivative | 同一主体的远层：巨大、低对比，与前景清晰切片形成注册深度 | no-crop | ai | Generated | Derived from change_e.png; treatment=desaturate+brightness | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页讲稿以页面上的可见状态为锚，先接上一页的悬念，再说清本页的一个判断，最后抛出通向下一页的问句；古籍引文在讲稿中口语化转述而不逐字念读；所有可外部核实的数字与年份只使用页面已引的 fact，讲稿不得引入新的外部断言
- **Total duration**: 约 25 分钟（16 页，平均每页 80–110 秒，章页更短）
- **Notes style**: conversational — 像和听众聊天而不是念报告，用设问制造悬念，用「差不多三分之一」这类口语化说法处理数据
- **Presentation purpose**: 先用「月饼」一词的迁徙把中秋从习惯变成历史，再解释每个熟悉意象的加入时点，最后落回今天的假期与数字

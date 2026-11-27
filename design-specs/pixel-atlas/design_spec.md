<!-- ppt-master-schema: design-spec/v1 -->
# pixel_breakfast_atlas_20260903 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | pixel_breakfast_atlas_20260903 |
| Canvas Format | PPT 16:9 · 1280×720 |
| Page Count | 16 |
| Primary Language | zh-CN |
| Target Audience | 对饮食文化感兴趣的普通观众，没有餐饮或地方志背景，认得几种早餐但说不清各自的地域、年代与做法 |
| Communication Intent | 以图鉴形式并列陈列各地代表性早餐；每条先给可核查的地域、主料、年代、口味与吃法，再在末尾给跨地区共性与两处争议；不树立中心论点，也不排名高下 |
| Desired Audience Outcome | 观众能逐条辨认 11 种地方早餐、说出各自城市与关键特征，知道哪些数字有出处、哪些本次没有取得可核来源，并能复述"碳水为主、一碗热汤、现做现吃"这组共性 |
| Core Message / Ask / Action | 中国早餐是 11 张各自成立的地方名片；它们的共性在碳水主料、一碗热汤与现做现吃，差异在主料、口味与年代 |
| Delivery Context | 主要为有主讲人的轻松科普放映（约 12 分钟）；次要为会后自行翻阅的图鉴式电子文件 |
| Artifact Afterlife | 收入公开示例库，作为像素风图鉴式 deck 的可复用参考，需保留可编辑的原生文字与表格 |
| Reading Mode | balanced |
| Content Strategy | 平衡：以研究补充件的事实为唯一内容来源，按图鉴条目重新组织；数字必须带来源年份，本次未取得可核来源的字段一律显示 NO DATA，不估算、不补写 |
| Design Style | 8-bit 图鉴：briefing 的并列等重骨架 + pixel-art 的严格像素网格与有限色板；深色瓷砖底上放大号食物 sprite，配 HUD 属性面板与图鉴进度条 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 用户明确要求"带逐页演讲者备注" |
| Custom Animations | enabled — 用户明确要求跑完终检后执行 customize-animations 并重新导出 |
| Narration Audio | disabled — 用户未要求旁白音频；工作流默认 |
| Created Date | 2026-09-03 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 上下左右各 64px；底部瓷砖地带占 y=656..720，正文不进入 |
| Content Area | x=64..1216, y=64..656 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: briefing
- **Mode Behavior**: 用 briefing 的中性完整骨架做一本图鉴：页标题是条目名而非论断，11 张条目页形状与权重完全一致以便比对与查找，每页 core message 说这页"陈列了什么"而不是"证明了什么"；条目按图鉴编号 No.01–No.11 顺序排列，前有一页读法与共性、后有争议页与对照表，全卷不设结论页。
- **Visual style**: custom
- **Visual Style References**: pixel-art
- **Visual Style Behavior**: 严格像素网格、无抗锯齿、块状轮廓、无渐变无滤镜无阴影；深色夜蓝底上铺一条底部瓷砖地带，条目页由 HUD 角括号框出内容区、阶梯像素分隔线切分栏位、底部一条 11 格图鉴进度条高亮当前条目；大号食物 sprite 稳稳压住页面左侧并留出四周空白，深浅只靠调色板分层（亮顶暗底）实现。
- **Theme**: 图鉴（Pokédex）——每页一格档案：编号、名称、城市、sprite、HUD 属性面板、要点。跨页母题是"图鉴进度条 + HUD 角括号"，在 11 张条目页上逐格推进，复用模式为固定复现、仅高亮格位变化。
- **Tone**: 轻松、克制、可查；游戏机的中性播报感，不煽情不排名

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | `#1A1C2C` | 全卷夜蓝底，像素游戏的暗场 |
| Secondary background | `#2B2F4A` | HUD 面板与条目卡底板 |
| Primary | `#EF8A3C` | 主体色：食物 sprite 主色、条目编号、进度条已过格 |
| Accent | `#FFCD4D` | 高亮：当前进度格、关键数值、题字描边亮部 |
| Secondary accent | `#41A6B5` | 冷向标签：清淡/无辣/地域格 |
| Body text | `#F4F0E6` | 正文暖白 |
| Secondary text | `#A0A8C0` | 图注、来源年份、NO DATA |
| Divider | `#4A5578` | 阶梯像素分隔线与 HUD 边框 |
| Surface | `#232741` | 面板抬起层（属性面板内条槽） |
| Grid | `#3A4266` | 瓷砖地带网格细线与空条槽 |
| Outline | `#0F1020` | 1 像素深色描边（所有块状形体） |
| Block shade | `#C25A22` | primary 的暗部像素（亮顶暗底分层） |
| Positive | `#7BD455` | 属性条低档/清淡 |
| Negative | `#E4453A` | 属性条高档/主辣 |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: pixel-art
- **Image Rendering Behavior**: 严格 8-bit 像素网格、零抗锯齿、像素大小完全一致；限定 14 色以内的复古色板，形体为块状剪影，1 像素深色描边（填充色的更暗一档）勾定轮廓；深度只靠亮顶暗底的调色板分层，不用渐变、不用模糊、不用投影；正交或轻微俯视，无透视灭点。
- **Visual**: 深色底上的高对比像素 sprite——食物成为可辨认的图标化实体（碗口、面条纹理、蒸汽块都由离散像素块构成），配件与 HUD 元件是同一网格上的小尺寸块状图形
- **Mood**: 怀旧、克制、可收集——像 90 年代掌机 RPG 的道具图鉴页，物品静静躺在暗色格子里等着被翻阅

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 粗壮无衬线、块面感强，撑得住像素框 | Microsoft YaHei | Microsoft YaHei | 无（单一具体字体名） |
| Body | 中性易读无衬线 | Microsoft YaHei | Microsoft YaHei | 无（单一具体字体名） |
| Display | 特大标题与结尾字，与 Title 同族加粗使用 | Microsoft YaHei | Microsoft YaHei | 无（单一具体字体名） |
| Data | 等宽机读感，承载 HUD 数值与价格年份 | Consolas | Consolas | 无（单一具体字体名） |
| Index | 等宽机读感的图鉴编号，块面大 | Consolas | Consolas | 无（单一具体字体名） |
| Annotation | 中性小字 | Microsoft YaHei | Microsoft YaHei | 无（单一具体字体名） |
| Footnote | 中性最小字，承载 Fact ID 与年份 | Microsoft YaHei | Microsoft YaHei | 无（单一具体字体名） |

- **Typography upgrade (Reference)**: 若目标机安装了 Press Start 2P / VT323 等点阵字，Title 与 Data 可整体替换以取得真像素字形；本次导出不依赖它，像素字形由 AI 题字承担
- **Title stack**: Microsoft YaHei
- **Body stack**: Microsoft YaHei
- **Display stack**: Microsoft YaHei
- **Data stack**: Consolas
- **Index stack**: Consolas
- **Annotation stack**: Microsoft YaHei
- **Footnote stack**: Microsoft YaHei
- **Role rationale**: Data 与 Index 用 Consolas 是唯一的家族切换——HUD 数值、价格与年份逐页对齐读取，图鉴编号 No.01–No.11 在 11 张条目页与结尾页反复出现且必须与中文标题拉开机读感；两者字号差一倍，故分列两个锚点。Display 与 Title 同族，只在封面与结尾的特大字号上单列锚点。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 44 |
| Subtitle | 32 |
| Annotation | 18 |
| Display | 64 |
| Data | 20 |
| Index | 40 |
| Footnote | 16 |
| Lead | 30 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 条目页从左侧大 sprite 起读 → 右上编号与名称 → 右中 HUD 属性面板 → 右下要点两三句 → 底部进度条定位；视线一次横穿，不做 Z 字回折
- **Composition tendency**: 左重右轻的双区结构，左区放尺寸压场的单一 sprite 并四周留白，右区用 HUD 角括号框出信息栈；封面、共性页、争议页、表格页与结尾页各自另立构图，不套条目模板
- **Cross-page continuity**: 底部瓷砖地带、HUD 角括号、11 格图鉴进度条在 11 张条目页上固定复现且只有高亮格变化；食物 sprite 一物一页不复用，配件与 HUD 图元跨页复用且保持同一缩放比
- **Spacing posture**: 变化——条目页 dense、共性页与争议页 breathing、封面与结尾 anchor
- **Spacing anchors**: 页边距 64px；块间距 32px；分栏槽 32px；圆角 0px（像素纪律，一律直角）；正文行距 36px

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P15 | table | record_table | 把 11 条图鉴逐行对照：编号、名称、城市、碳水主料、口味标签、定型年代、可核价格 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dish_doujiao.png | 1090x1110 | 0.98:1 | No.01 豆汁焦圈主体 sprite | Illustration element | 左区大 sprite 压场，四周留白，不进容器 | no-crop | slice | Generated | 取自 sheet_food_a 第 1 格 | none | local |
| dish_jianbing.png | 1233x987 | 1.25:1 | No.02 煎饼馃子主体 sprite | Illustration element | 左区大 sprite 压场，四周留白 | no-crop | slice | Generated | 取自 sheet_food_a 第 2 格 | none | local |
| dish_sidajingang.png | 1254x1212 | 1.03:1 | No.03 上海四大金刚主体 sprite | Illustration element | 左区大 sprite 压场，四件并排成一组 | no-crop | slice | Generated | 取自 sheet_food_a 第 3 格 | none | local |
| dish_reganmian.png | 1254x1211 | 1.04:1 | No.04 热干面主体 sprite | Illustration element | 左区大 sprite 压场，四周留白 | no-crop | slice | Generated | 取自 sheet_food_a 第 4 格 | none | local |
| dish_changfen.png | 1274x1069 | 1.19:1 | No.05 广州肠粉主体 sprite | Illustration element | 左区大 sprite 压场，配蒸笼配件 | no-crop | slice | Generated | 取自 sheet_food_a 第 5 格 | none | local |
| dish_changshafen.png | 1252x1151 | 1.09:1 | No.06 长沙米粉主体 sprite | Illustration element | 左区大 sprite 压场，四周留白 | no-crop | slice | Generated | 取自 sheet_food_a 第 6 格 | none | local |
| dish_xiaomian.png | 1254x1212 | 1.03:1 | No.07 重庆小面主体 sprite | Illustration element | 左区大 sprite 压场，旁挂辣椒图元 | no-crop | slice | Generated | 取自 sheet_food_a 第 7 格 | none | local |
| dish_roujiamo.png | 1233x1029 | 1.2:1 | No.08 西安肉夹馍主体 sprite | Illustration element | 左区大 sprite 压场，四周留白 | no-crop | slice | Generated | 取自 sheet_food_a 第 8 格 | none | local |
| dish_niuroumian.png | 1254x1130 | 1.11:1 | No.09 兰州牛肉面主体 sprite | Illustration element | 左区大 sprite 压场，四周留白 | no-crop | slice | Generated | 取自 sheet_food_a 第 9 格 | none | local |
| dish_xiaoguomixian.png | 1885x1189 | 1.59:1 | No.10 云南小锅米线主体 sprite | Illustration element | 左区大 sprite 压场，配红铜小锅配件 | no-crop | slice | Generated | 取自 sheet_food_b 第 1 格 | none | local |
| dish_kaobaozi.png | 1721x1230 | 1.4:1 | No.11 新疆烤包子主体 sprite | Illustration element | 左区大 sprite 压场，与奶茶并置 | no-crop | slice | Generated | 取自 sheet_food_b 第 2 格 | none | local |
| dish_naicha.png | 1640x1353 | 40:33 | No.11 咸奶茶配套 sprite | Illustration element | 与烤包子并置的次级元素，尺寸小一档 | no-crop | slice | Generated | 取自 sheet_food_b 第 3 格 | none | local |
| dish_doufunao.png | 1640x1353 | 40:33 | 豆腐脑咸甜争议页主体 sprite | Illustration element | 页面中轴单件，左右两侧各接一路配料标注 | no-crop | slice | Generated | 取自 sheet_food_b 第 4 格 | none | local |
| prop_bowl.png | 598x512 | 1.17:1 | 通用碗配件 | Illustration element | 共性页小图元，跨页复用同一缩放 | no-crop | slice | Generated | 取自 sheet_props 第 1 格 | none | local |
| prop_chopsticks.png | 647x596 | 1.09:1 | 筷子配件 | Illustration element | 共性页小图元，斜置不进容器 | no-crop | slice | Generated | 取自 sheet_props 第 2 格 | none | local |
| prop_steamer.png | 579x630 | 0.92:1 | 蒸笼配件 | Illustration element | 肠粉页次级元素，贴主 sprite 边缘 | no-crop | slice | Generated | 取自 sheet_props 第 3 格 | none | local |
| prop_cup.png | 427x631 | 0.68:1 | 豆浆纸杯配件 | Illustration element | 四大金刚页次级元素 | no-crop | slice | Generated | 取自 sheet_props 第 4 格 | none | local |
| prop_copperpot.png | 698x512 | 1.36:1 | 红铜小锅配件 | Illustration element | 小锅米线页次级元素 | no-crop | slice | Generated | 取自 sheet_props 第 5 格 | none | local |
| prop_spoon.png | 529x359 | 1.47:1 | 勺配件 | Illustration element | 争议页次级元素 | no-crop | slice | Generated | 取自 sheet_props 第 6 格 | none | local |
| hud_chili.png | 394x557 | 0.71:1 | 辣度行图标 | Illustrated icon | HUD 属性面板行首小图标，11 页复用同一尺寸 | no-crop | slice | Generated | 取自 sheet_hud 第 1 格 | none | local |
| hud_coin.png | 536x536 | 1:1 | 价格行图标 | Illustrated icon | HUD 属性面板行首小图标 | no-crop | slice | Generated | 取自 sheet_hud 第 2 格 | none | local |
| hud_clock.png | 536x537 | 1.0:1 | 年代行图标 | Illustrated icon | HUD 属性面板行首小图标 | no-crop | slice | Generated | 取自 sheet_hud 第 3 格 | none | local |
| hud_rice.png | 557x515 | 1.08:1 | 口味行图标 | Illustrated icon | HUD 属性面板行首小图标 | no-crop | slice | Generated | 取自 sheet_hud 第 4 格 | none | local |
| hud_steam.png | 475x515 | 0.92:1 | 蒸汽块图元 | Illustrated icon | 条目页 sprite 上方点缀，位置与角度逐页变化 | no-crop | slice | Generated | 取自 sheet_hud 第 5 格 | none | local |
| hud_star.png | 557x536 | 1.04:1 | 星标图元 | Illustrated icon | 表格页与结尾页的强调点 | no-crop | slice | Generated | 取自 sheet_hud 第 6 格 | none | local |
| hud_tile.png | 556x557 | 1.0:1 | 瓷砖块图元 | Illustrated icon | 共性页地块拼接单元 | no-crop | slice | Generated | 取自 sheet_hud 第 7 格 | none | local |
| hud_bracket.png | 578x557 | 1.04:1 | HUD 角括号图元 | Illustrated icon | 条目页信息区四角，固定复现 | no-crop | slice | Generated | 取自 sheet_hud 第 8 格 | none | local |
| hud_heart.png | 557x515 | 1.08:1 | 心形图元 | Illustrated icon | 结尾页收藏感点缀 | no-crop | slice | Generated | 取自 sheet_hud 第 9 格 | none | local |
| scene_stall.png | 588x634 | 0.93:1 | 早市推车摊位 | Illustration element | 共性页右下角落地元素，接住底部瓷砖带 | no-crop | slice | Generated | 取自 sheet_scene 第 1 格 | none | local |
| scene_signboard.png | 794x358 | 2.22:1 | 早点铺招牌灯箱 | Illustration element | 封面右上，可越出画布边缘 | no-crop | slice | Generated | 取自 sheet_scene 第 2 格 | none | local |
| scene_steamcloud.png | 714x301 | 2.37:1 | 宽蒸汽云 | Illustration element | 封面与共性页题字后方的低对比衬底 | no-crop | slice | Generated | 取自 sheet_scene 第 3 格 | none | local |
| scene_ground.png | 1012x347 | 2.92:1 | 瓷砖地带条 | Illustration element | 封面与结尾页底边满幅铺开 | no-crop | slice | Generated | 取自 sheet_scene 第 4 格 | none | local |
| player_stand.png | 373x649 | 0.57:1 | 玩家小人·站立 | Illustration element | 封面地带上的人形尺度参照 | no-crop | slice | Generated | 取自 sheet_player 第 1 格 | none | local |
| player_walk.png | 445x648 | 0.69:1 | 玩家小人·行走 | Illustration element | 图鉴进度条上的移动标记，相邻两页位置不同 | no-crop | slice | Generated | 取自 sheet_player 第 2 格 | none | local |
| player_bowl.png | 360x649 | 0.55:1 | 玩家小人·端碗 | Illustration element | 共性页"现做现吃"一条的图示 | no-crop | slice | Generated | 取自 sheet_player 第 3 格 | none | local |
| player_eat.png | 408x696 | 17:29 | 玩家小人·吃 | Illustration element | 结尾页与「开吃！」题字并置 | no-crop | slice | Generated | 取自 sheet_player 第 4 格 | none | local |
| player_cheer.png | 529x696 | 0.76:1 | 玩家小人·欢呼 | Illustration element | 结尾页与「图鉴完成」题字并置 | no-crop | slice | Generated | 取自 sheet_player 第 5 格 | none | local |
| player_sit.png | 408x588 | 0.69:1 | 玩家小人·蹲坐 | Illustration element | 争议页中立位置，坐在咸甜两侧之间 | no-crop | slice | Generated | 取自 sheet_player 第 6 格 | none | local |
| letter_title.png | 4128x897 | 4.6:1 | 封面主标题题字「中国早餐图鉴」 | Lettering | 封面上部题字层，旁边另留原生可编辑标题 | no-crop | slice | Generated | 取自 sheet_letter_title 唯一格；精确字符串「中国早餐图鉴」 | embedded | local |
| letter_kaichi.png | 1563x600 | 2.6:1 | 小题字「开吃！」 | Lettering | 共性页右下装饰，贴摊位元素 | no-crop | slice | Generated | 取自 sheet_letter_marks 第 1 格；精确字符串「开吃！」 | embedded | local |
| letter_complete.png | 2526x623 | 4.05:1 | 小题字「图鉴完成」 | Lettering | 结尾页题字层，旁边另留原生可编辑标题 | no-crop | slice | Generated | 取自 sheet_letter_marks 第 2 格；精确字符串「图鉴完成」 | embedded | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页备注从该页最终 SVG 的可见内容出发，平实读出这一页陈列了什么；数字照页面复述并带来源年份，NO DATA 的字段要口头说明"本次未取得可核来源"；不加页面上没有的事实，不制造悬念或"所以呢"式的收束
- **Total duration**: 约 12 分钟（封面与结尾各约 30 秒，共性页与争议页各约 60 秒，11 张条目页各约 45 秒，表格页约 60 秒）
- **Notes style**: conversational — 中性平实的播报口吻，句子短，数字念清楚
- **Presentation purpose**: 以图鉴形式并列陈列各地代表性早餐，先给可核查的地域、主料、年代、口味与吃法，再给跨地区共性与两处争议；不树立中心论点

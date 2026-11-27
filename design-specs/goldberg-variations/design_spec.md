<!-- ppt-master-schema: design-spec/v1 -->
# goldberg_variations_ppt169_20260923 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | goldberg_variations_ppt169_20260923 |
| Canvas Format | ppt169 (1280×720) |
| Page Count | 12 |
| Primary Language | zh-CN |
| Target Audience | 公司古典音乐爱好者小组成员:喜欢听古典音乐,多数没学过乐理,听过或听说过古尔德的录音 |
| Communication Intent | 导赏:先让零乐理的听众看懂全曲结构(咏叹调首尾、30 个变奏、每三首一首卡农、卡农音程逐级上升、背后的低音线),再对比古尔德 1955 与 1981 两次录音,最后给出带着地图去听的方法 |
| Desired Audience Outcome | 听完后能说出"咏叹调 + 30 变奏 + 咏叹调"的框架,找到卡农的位置并知道它的音程一路升高,理解所有变奏共用同一条低音线,并能说出古尔德两版的主要差别 |
| Core Message / Ask / Action | 《哥德堡变奏曲》是一座以低音线为地基、以卡农为梁柱的对称建筑;看懂这张结构图,就能听出它的秩序与自由 |
| Delivery Context | 主讲人现场分享(兴趣小组活动,约 30–40 分钟,可穿插播放片段);次要用途为会后在小组内传阅 |
| Artifact Afterlife | 小组内部留存,作为之后自己聆听时的"结构地图" |
| Reading Mode | balanced |
| Content Strategy | balanced(用户未指定;以导赏叙事重组调研事实,不增加来源之外的事实) |
| Design Style | 「铜版纸上的建筑」— mode custom(instructional 为基底、narrative 收束古尔德段落)+ visual style custom(editorial + ink-notes);奶油纸底、墨色线条、暗红批注,五线谱线与拱形为贯穿母题 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy(委托决定,默认开启) |
| Custom Animations | enabled — final Stage-2 proactive policy(委托决定:结构图逐页展开需要 Morph 与分步进场) |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-23 |
| Delegated Confirmation | 用户原话"所有确认都交给你决定,不用问我":Stage 1 与 Stage 2 均由 Strategist 代为决定,未启动确认页、无 UI 回执;决定与理由见下方 §III Delegated decisions |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 左右 60 px,上 48 px,下 40 px |
| Content Area | x 60–1220,y 48–680 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional, narrative
- **Mode Behavior**: 以 instructional 为主轴——先总图、再逐层拆解(分组 → 卡农阶梯 → 放大一级 → 低音地基 → 转折与小调 → 结尾回归),每页只教一件事,标题直接说这页教什么;古尔德两版与收束两页借 narrative 的"同一作品、两次人生"对照与回到起点的回环收尾。
- **Visual style**: custom
- **Visual Style References**: editorial, ink-notes
- **Visual Style Behavior**: 奶油色纸面上的墨色线条系统:editorial 负责衬线标题与无衬线正文的对位、细规则线、页边批注与出处小字;ink-notes 负责以线条而非卡片承载结构——五根平行谱线作为贯穿母题,拱形、阶梯、括号、连线用墨线勾勒,节点以小圆点/小音符头标记;暗红只用于"卡农"与当页唯一重点,灰蓝只用于小调;几乎不用阴影与卡片网格,留白由谱线与拱形组织。
- **Theme**: 乐谱即建筑——咏叹调是两端的柱脚,30 个变奏是拱身,每三首一根卡农"梁柱",低音线是地基
- **Tone**: 安静、精确、带一点手稿温度的导赏语气

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F4EFE4 | 奶油纸面主底 |
| Secondary background | #E9E1D0 | 纸面深一阶:批注带、表格表头、分区底 |
| Primary | #1F2A36 | 墨色:标题、谱线、结构线、咏叹调节点 |
| Accent | #9E2A2B | 暗红批注色:卡农节点与当页唯一重点 |
| Secondary accent | #A88452 | 旧铜金:次级强调、年份、Quodlibet 标记 |
| Body text | #2B2621 | 正文 |
| Secondary text | #6E655A | 注释、出处、页码 |
| Divider | #CBBFA8 | 细规则线、谱线浅色版 |
| Minor key | #4F6A80 | 灰蓝:仅标记三首 g 小调变奏 |

### AI Image Strategy

- **Image Rendering**: custom
- **Visual**: 18 世纪铜版雕刻/蚀刻插画线条,细密平行排线与交叉排线塑形,墨线印在奶油纸上,极少量暗红
- **Mood**: 安静庄重而精确,像 1741 年铜版印刷乐谱扉页旁的插画
- **Image Rendering Behavior**: Copperplate engraving and etching aesthetic: fine parallel hatching and cross-hatching build every form, uniform dark-ink line weight with tapered stroke ends, no gradients, no photographic texture, no color fills except the warm cream paper and at most one tiny muted red touch; depth comes only from hatch density; calm, exact, archival mood like an illustration beside an 18th-century engraved music title page.

### Delegated decisions

- **Stage 1**: 语言 zh-CN(用户中文);画布 ppt169(用户指定 16:9);沟通契约 6 项按上表由用户原话推出;`content_divergence` 留空=balanced;选择 free_design(用户未提模板且明确"别做成普通的商务模板")。
- **Stage 2 三方向**:① 「铜版纸上的建筑」(本方案,selected=0);② 「深夜录音室」:深炭灰底、琥珀色光、键盘节奏条,showcase+narrative,微软雅黑粗体+Segoe UI 同族对位,AI 图为摄影式明暗;③ 「声音蓝图」:深蓝图纸、白色线稿与尺寸线,blueprint 风格,黑体+Consolas。选①的理由:题目本身是"对称的建筑",而作品 1741 年以铜版印刷出版,纸面+墨线+谱线能同时给出"音乐感"与"建筑感";浅底对零乐理读者的结构图最易读;②偏情绪、不利于讲清结构,③偏工程感、音乐温度不足。
- **阅读模式** balanced:主讲为主但会后传阅;讲解细节由备注承担。**页数** 12(用户"12 页左右")。
- **字体**:标题 SimSun + Cambria(衬线,呼应乐谱印刷;Cambria 为衬线数字且为等高数字,适合 1741/32/30),正文 Microsoft YaHei + Segoe UI(投影可读);对比型搭配。
- **字号**:正文 22(balanced 带 22–25 的低端,因结构图页标注多),标题 38,副标题 28,导语 26,注释 16,脚注 14,展示数字 88,封面标题 60。
- **数字写法**:阿拉伯数字 + 中文量词("第 16 变奏""30 个变奏");年份用阿拉伯数字;音程用中文"同度/二度/…/九度";曲名首次出现附原文。
- **图片来源**:web(巴赫肖像、1741 初版扉页,只接受公共领域/开放许可,记 `image_sources.json`)+ ai(≤2 张:封面拱形铜版画、录音室空椅);古尔德本人照片无清楚开放许可,不放;五线谱/音符/结构图全部原生形状绘制。
- **图标**:tabler-outline,stroke 1.5(细线与墨线气质一致),只作小提示。
- **两次录音时长**:调研未找到官方或权威来源(仅维基百科转引数字 F041),按任务要求不写入页面、不做时长图表;对比页用原生表格承载可查证的事实。

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 印刷衬线,庄重 | SimSun | Cambria | serif |
| Body | 清晰无衬线 | Microsoft YaHei | Segoe UI | sans-serif |
| Display | 衬线等高数字 | SimSun | Cambria | serif |

- **Title stack**: SimSun, Cambria, serif
- **Body stack**: Microsoft YaHei, Segoe UI, sans-serif
- **Display stack**: SimSun, Cambria, serif
- **Role rationale**: display 角色用于封面与结构页的大号数字(32、30、1741、九度阶梯编号),与标题同族以保持印刷感。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 22 |
| Title | 38 |
| Subtitle | 28 |
| Lead | 26 |
| Annotation | 16 |
| Footnote | 14 |
| Display | 88 |
| Cover title | 60 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 标题(左上,衬线)→ 页面主图(结构线/谱线)→ 批注与出处;结构页让图占主导,文字作为页边批注
- **Composition tendency**: 以一条贯穿页面的"谱线/地平线"或拱形组织区域,而不是卡片网格;对比页用左右对页;封面与收尾使用大留白
- **Cross-page continuity**: 五根平行细谱线母题在每页以不同比例出现(封面为背景、结构页为基线、低音页为真实五线谱);32 个节点的拱形在 P03 建立,P04/P05/P06 由它变形而来
- **Spacing posture**: 结构页 dense 但开阔,解释页 breathing
- **Spacing anchors**: 页边距 60 px;块间距 28 px;栏间距 40 px;圆角 4 px;正文行距 1.55

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 1.5

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/headphones.svg | 聆听任务、听什么 |
| icons/tabler-outline/ear.svg | 听辨提示 |
| icons/tabler-outline/vinyl.svg | 唱片、录音版本 |
| icons/tabler-outline/piano.svg | 键盘乐器 |
| icons/tabler-outline/repeat.svg | 反复、回到开头 |
| icons/tabler-outline/moon.svg | 失眠轶事、夜 |
| icons/tabler-outline/feather.svg | 书写、手稿 |
| icons/tabler-outline/calendar.svg | 日期、年份 |
| icons/tabler-outline/microphone.svg | 录音 |
| icons/tabler-outline/stairs-up.svg | 音程递升 |
| icons/tabler-outline/building-arch.svg | 建筑隐喻 |
| icons/tabler-outline/quote.svg | 引语 |
| icons/tabler-outline/clock.svg | 速度、时间 |
| icons/tabler-outline/music.svg | 旋律、民歌 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P10 | table | comparison_matrix | 以相同维度对照古尔德 1955 与 1981 两次录音的可查证事实 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_arch.jpg | 2752×1536 | 16:9 | P01 封面主视觉 | Illustration | 全幅画面作底,左侧留出安静区放原生标题 | adaptive | ai | Generated | 一座由细墨线雕刻出的古典石拱廊从右向左延伸,拱券的横梁上隐约排着五根平行的谱线,像一段被建成建筑的乐谱;右侧拱廊细节最密,左侧约 45% 画面是空白奶油纸,供标题 | none | hero_page |
| studio_chair.jpg | 848×1264 | 2:3 | P10 录音对比页侧栏氛围图 | Illustration | 竖长侧栏,与表格并置,为"两次录音、同一间录音室"提供场景 | adaptive | ai | Generated | 空旷的老式录音室里,一架三角钢琴前放着一把很矮的旧木折叠椅,远处是高大的墙面与一支立式话筒;无人物;竖构图,钢琴与椅子位于下半部 | none | local |
| bach_portrait.jpg | 2616×3438 | 约 3:4 | P02 巴赫真身肖像 | Photo | 左侧竖向肖像框,配出处小字 | adaptive | web | Sourced | Elias Gottlob Haussmann 所绘巴赫油画肖像(1746/1748 版本),手持乐谱,半身,公共领域图像 | none | local |
| title_page_1741.jpg | 2494×3754 | 约 2:3 | P02 1741 年初版扉页 | Photo | 与肖像并置的扉页小图,完整显示 | no-crop | web | Sourced | 巴赫《键盘练习曲》第四卷(哥德堡变奏曲)1741 年初版印本扉页,文字"Clavier Ubung … ARIA mit verschiedenen Veraenderungen"清晰可辨,公共领域 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 以口语讲解承担乐理解释:术语(卡农、音程、倒影、集腔曲、低音线)首次出现时用生活类比解释;引用事实时自然说出出处;"相传"类内容明确说是轶事;不朗读页码与装饰
- **Total duration**: 约 30–35 分钟(不含播放片段)
- **Notes style**: conversational,耐心导赏
- **Presentation purpose**: 导赏——看懂结构、对比两版、带着地图去听

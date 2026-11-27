<!-- ppt-master-schema: design-spec/v1 -->
# fourier_transform_formulas_zh - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | fourier_transform_formulas_zh |
| Canvas Format | PPT 4:3 (1024×768) |
| Page Count | 15 |
| Primary Language | zh-CN |
| Target Audience | 有高中数学基础的大学新生,以及做信号/图像/通信的工程师;他们会用正弦、积分和复数记号,但没系统学过变换 |
| Communication Intent | 先教会:用一节公开课把"时域→频域"这件事讲通,顺序是直觉→级数→变换→性质→离散与快速→应用;其次是让公式可带走(课后能直接复制编辑) |
| Desired Audience Outcome | 听众能说出傅里叶变换在做什么、读懂并复述一条变换对与卷积定理、解释 FFT 为什么快,并能在自己领域指认一个傅里叶应用 |
| Core Message / Ask / Action | 傅里叶变换是一本可逆的字典:把"随时间怎么变"翻译成"由哪些频率组成",难的部分是记号,不是思想 |
| Delivery Context | 主要是有主讲人的 45 分钟公开课现场投影(传统 4:3 投影仪);次要是课后自读与公式复用 |
| Artifact Afterlife | 课后自学材料、公式取用来源、延伸阅读索引 |
| Reading Mode | balanced |
| Content Strategy | 平衡默认(用户未填写素材贴合度):事实全部取自 `sources/` 的研究对并标出处,讲授路径与类比由本卷整理 |
| Design Style | 方向二「科学期刊」— 教科书跨页式栅格,细分隔线,衬线标题配黑体正文,公式独占带状区并留边注栏 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 工作流默认(用户未指定),公开课需要讲稿 |
| Custom Animations | enabled — 用户明确要求"要有自定义动画和 Morph" |
| Narration Audio | disabled — 工作流默认(用户未要求旁白) |
| Created Date | 2026-09-12 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 4:3 |
| Dimensions | 1024 × 768 |
| viewBox | `0 0 1024 768` |
| Margins | 上下 56 px,左右 64 px |
| Content Area | x 64–960(896 px 版面宽),y 56–712 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional, briefing
- **Mode Behavior**: 以教学阶梯为主干:每页一个可验证的理解台阶,页标题写成陈述句("求和变成积分"),上一页的结论是下一页的前提;`instructional` 负责概念分解与推导顺序,`briefing` 负责变换对表与应用页那种中性、可扫读的均权陈列。每个小节先给一句直觉,再给公式,再给一句"这条公式让你能做什么"。
- **Visual style**: custom
- **Visual Style References**: swiss-minimal, editorial, data-journalism
- **Visual Style Behavior**: 教科书跨页语言:`swiss-minimal` 定 12 栅格、硬边直角与大留白;`editorial` 提供细规则线、边注栏、小节序号与衬线/黑体互文的层级;`data-journalism` 只负责公式与图表下方的来源行与刻度注记。公式独占一条浅底带状区(secondary_bg)并以左侧 3 px 主色竖条起头,右侧留 200 px 边注栏写"读法";装饰只有细线、带状区和刻度,没有卡片阴影、没有圆角、没有渐变。
- **Theme**: 一本摊开的讲义:左页讲道理,右页留公式与边注
- **Tone**: 克制、精确、可被复制;像一份排得很好的讲义而不是发布会

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 页面底色,投影下最大对比 |
| Secondary background | #F2F4F7 | 公式带状区、表头、边注栏底 |
| Primary | #123B63 | 标题、公式竖条、坐标轴与结构线 |
| Accent | #C2452D | 频域侧的强调:重点项、谐波峰、结论标记 |
| Secondary accent | #2E7D7B | 时域侧的第二色:原始波形、对照序列 |
| Body text | #1B2027 | 正文与公式文字 |
| Secondary text | #5A6472 | 边注、刻度、来源行 |
| Divider | #D6DBE1 | 细规则线、表格线、栅格分隔 |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: blueprint, editorial
- **Image Rendering Behavior**: 讲义插图而非海报:`blueprint` 给出等宽刻度、细网格底与描线感的技术图语言,`editorial` 给出杂志信息图那种干净留白与层级清晰的构成。线条均匀细实,无渐变、无发光、无立体投影;只用本卷的主色、时域青碧与频域朱红三色,底为纸白。
- **Visual**: 一条复合波形在左,向右逐渐分解成若干等间距的单频正弦,末端收成一排高低不同的频率竖线;浅网格与刻度暗示坐标系
- **Mood**: 冷静、可验证,像教科书扉页的示意图或科学期刊的图 1

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 衬线/教科书体,笔画有起收,承担"讲义"性格 | SimSun | Cambria | serif |
| Body | 无衬线/黑体,投影清晰,长句不糊 | Microsoft YaHei | Cambria | sans-serif |
| Formula | 数学排版体,与导出的原生公式同族 | Cambria Math | Cambria Math | serif |
| Annotation | 黑体小字,边注与刻度 | Microsoft YaHei | Cambria | sans-serif |
| Footnote | 黑体极小字,来源行与页码 | Microsoft YaHei | Cambria | sans-serif |
| Display | 衬线大字,章节序号与量级数字 | SimSun | Cambria | serif |

- **Title stack**: SimSun, Cambria, serif
- **Body stack**: Microsoft YaHei, Cambria, sans-serif
- **Formula stack**: Cambria Math, serif
- **Annotation stack**: Microsoft YaHei, Cambria, sans-serif
- **Footnote stack**: Microsoft YaHei, Cambria, sans-serif
- **Display stack**: SimSun, Cambria, serif
- **Role rationale**: 新增 `formula` 角色,让 SVG 里手写的公式回退与导出后的原生公式共用 Cambria Math,避免同一页出现两套数学字形;`display` 只用于章节序号与量级数字(N²、N log N),仍在标题族内。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 42 |
| Subtitle | 32 |
| Formula | 28 |
| Annotation | 18 |
| Footnote | 16 |
| Display | 60 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 自上而下——页标题(陈述句)→ 一句直觉 → 公式带状区 → 边注读法 / 来源行;视线先落在公式带上,再回到左侧文字
- **Composition tendency**: 主栏 + 边注栏的讲义式双区;公式页让公式带横贯主栏、边注栏写"每个符号读作什么";图表页反过来,图占上三分之二、公式与结论在下
- **Cross-page continuity**: 每页左上角有小节序号(Display 体)与小节名;公式带状区的样式(浅底 + 左侧主色竖条)全卷不变,是本卷的识别母题;时域一律青碧、频域一律朱红
- **Spacing posture**: variable by page rhythm——推导页 dense,小节入口与收束页 breathing
- **Spacing anchors**: 页边距 64 px,块间距 32 px,栏间距 24 px,圆角 0 px,正文行距 1.55

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/wave-sine.svg | 时域波形、单频分量 |
| icons/tabler-outline/math-function.svg | 公式、函数与变换 |
| icons/tabler-outline/chart-histogram.svg | 频谱、幅度分布 |
| icons/tabler-outline/photo.svg | 图像压缩类应用 |
| icons/tabler-outline/wifi.svg | 无线通信类应用 |
| icons/tabler-outline/activity-heartbeat.svg | 医学成像类应用 |
| icons/tabler-outline/music.svg | 音频与均衡 |
| icons/tabler-outline/clock.svg | 时间轴、时移 |
| icons/tabler-outline/repeat.svg | 周期、循环与可逆往返 |
| icons/tabler-outline/book.svg | 历史文献与延伸阅读 |
| icons/tabler-outline/bulb.svg | 直觉提示与小结 |
| icons/tabler-outline/arrows-right-left.svg | 正变换与逆变换的成对关系 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P05 | chart | column_chart | 展示方波前若干奇次谐波的幅度按 1/k 递减 |
| P08 | table | record_table | 四对常见变换对的时域式、频域式与读法并列 |
| P13 | chart | line_chart | 对比 N² 与 N·log₂N 随 N 增长的计算量 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_wave_decomposition.png | 3168x1344 | 2.36:1 | 封面主视觉的生成原件,仅用于派生落位尺寸的副本 | Source | 不上页 | adaptive | ai | Generated | 抽象示意图:左侧一条复合波形,向右渐次分离出三到四条等间距单频正弦,最右收成一排高低不同的频率竖线;浅网格与刻度暗示坐标系;无文字、无人物 | none | local |
| cover_wave_band.jpg | 1024x434 | 2.36:1 | 封面主视觉:一条复合波向右分解成单频正弦并收成频率竖线 | Illustration | 横贯封面下半的通栏带状插图,标题压在其上方留白处,不要让波形穿过标题 | adaptive | ai | Generated | Derived from cover_wave_decomposition.png; treatment=fit 1024x435; 按封面落位尺寸缩小,内容不变 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每页一段讲稿:先一句进入这页的过渡,再逐符号读出本页公式(把 e^{-iωt}、积分上下限、求和下标读成人话),最后一句给出这页要留下的结论;历史与参数类说法在备注里重复出处与年份,便于讲者当场引用;不改动页面上的事实,不添加页面外的新数字
- **Total duration**: 约 45 分钟(15 页,平均每页 2.5–3.5 分钟,推导页偏长)
- **Notes style**: 讲授式口语,面向大一新生的解释度,允许一次提问互动
- **Presentation purpose**: 先教会时域→频域这条路径,再让公式可带走复用

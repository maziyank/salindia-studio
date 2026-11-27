<!-- ppt-master-schema: design-spec/v1 -->
# typst_series_banners_wechat_20260923 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | typst_series_banners_wechat_20260923 |
| Canvas Format | wechat（公众号头图）900×383 |
| Page Count | 6 |
| Primary Language | zh-CN |
| Target Audience | 在公众号里刷到"Typst 入门"连载的中文读者：多数写过 Word/Markdown，可能听说过 LaTeX，尚未系统学过 Typst |
| Communication Intent | 先让读者在信息流里一眼认出这是同一个"Typst 入门"系列，再让每篇横幅说清本篇讲什么，并用一段取自教程原文的真实 Typst 代码让人感到"原来这么写就行" |
| Desired Audience Outcome | 读者看到任意一张横幅，能认出系列、说出本篇主题（导引 / 标记语法 / 数学公式 / 中文排版），文末横幅促使其关注并继续读下一篇 |
| Core Message / Ask / Action | Typst 让你少配置也能排版精良（整理自教程）；文末：关注本号，跟完四篇 |
| Delivery Context | 主：公众号文章头图与文末图，读者自读、静态展示、手机端为主；次：作者在 PPT 中改字复用出新篇横幅 |
| Artifact Afterlife | 作为系列横幅母版反复改字复用；每张需可单独分享 |
| Reading Mode | 不适用（非 PPT 画布）；按"扫一眼"阅读处理：每张一个主张 + 一段代码证据，等价于 presentation 的低密度语法 |
| Content Strategy | 空白（默认 balanced）：文字取自源里的说法，转述处标"整理"，代码逐字取自源 |
| Design Style | custom 模式 + custom 视觉风格：「校样台」——Swiss 网格上的排版校样纸，墨黑 + 校对红（委托决定，理由见 §III） |
| AI Image Acquisition Path | 不适用（图片来源 none） |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 工作流默认 true（用户未提及；任务书要求全卷备注） |
| Custom Animations | enabled — 执行方明确要求（委托运行的硬性指令：自定义动画 + Morph ≥2 对，对象级） |
| Narration Audio | disabled — 工作流默认 |
| Created Date | 2026-09-23 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | wechat（WeChat Article Header） |
| Dimensions | 900 × 383 |
| viewBox | `0 0 900 383` |
| Margins | 左右 40，上下 32；公众号转发卡片会取中间近方形区域，主标题与本篇主题优先落在 x≈259–641 的中央带或其近旁（执行者判断） |
| Content Area | x 40–860，y 32–351 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode Behavior**: 系列识别卡组：每张横幅只承担一个动作——头图立系列名与一句主张；章节横幅 = 章节序号 + 本篇主题 + 一段逐字取自源的代码（左源码、右效果或要点）；文末横幅把四篇路线收束成一个关注动作。标题用名词短语或短主张，不写口号。
- **Visual style**: custom
- **Visual Style References**: swiss-minimal
- **Visual Style Behavior**: 「校样台」：swiss-minimal 负责严格的模块网格、左对齐与大留白；在此之上加入排版校样语言——四角裁切线、极细基线网格、校对红的插入光标块与下划校记，代码放在墨黑"排字条"上用等宽字，标题用宋体大字承担排版气质；平面、无阴影、无渐变，装饰只来自排版工具本身的记号。
- **Theme**: 排版工具的工作台——纸、墨、校对红、等宽源码条；一个红色光标块在各张横幅间延续，章节轨道上的红色标记逐篇前移
- **Tone**: 冷静、精确、带一点手艺人的温度；不做通用科技蓝
- **Direction candidates (delegated)**: ① 校样台（选中，index 0）——Swiss 网格 + 校样记号 + 宋体标题 + 墨黑代码条；② 铅字盘——暖棕木格字盘、铅字块与铜色，标题黑体，偏复古手作；③ 源码/成品对开——左深色编辑器、右白纸成品，等宽字主导，偏工具界面。选 ① 的理由：矮宽 2.35:1 画布最怕堆满，Swiss 网格留白最能扛住手机端缩小；校样记号直接表达"排版工具"又不落科技蓝；② 的木格纹理在 900×383 缩小后发脏、需图片，③ 最接近用户说的"通用科技"观感。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F3EEE3 | 校样纸底 |
| Secondary background | #E6DECD | 纸面分区、标签底 |
| Primary | #1D1A17 | 墨黑：标题、代码排字条底色 |
| Accent | #CF3B2A | 校对红：光标块、章节标记、强调 |
| Secondary accent | #A87A2A | 铜黄：代码条内关键字、次级标记 |
| Body text | #27231F | 正文 |
| Secondary text | #6B6358 | 来源行、注记、页脚标签 |
| Divider | #CBC0AC | 裁切线、基线网格、细规则 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 书宋，排版气质，大字号 | SimSun | Cambria | serif |
| Body | 中性黑体 | Microsoft YaHei | Arial | sans-serif |
| Code | 等宽源码 | Microsoft YaHei | Consolas | monospace |
| Display | 章节大序号、系列名 | SimSun | Cambria | serif |

- **Title stack**: SimSun, Cambria, serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Code stack**: Consolas, Microsoft YaHei, monospace
- **Display stack**: SimSun, Cambria, serif
- **Role rationale**: Code 为逐字 Typst 源码的等宽角色（每张章节横幅都出现）；Display 为头图系列名与章节大序号，沿用标题家族。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 50 |
| Subtitle | 30 |
| Annotation | 18 |
| Code | 24 |
| Footnote | 15 |
| Display | 96 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 左上章节标签 → 大标题 → 代码排字条 → 右侧效果/要点；视线从左到右一次扫完
- **Composition tendency**: 矮宽横向分区：左侧约 45% 放标题组，右侧放代码条与效果；头图与文末可打破分区，用大字系列名横贯
- **Cross-page continuity**: 四角裁切线与基线网格每张都有；红色光标块从头图延续到章节横幅；底部四章轨道（01 导引 / 02 标记 / 03 数学 / 04 中文）在章节横幅上出现，当前篇红色标记逐篇前移
- **Spacing posture**: 开阔；每张只放一个主张 + 一段代码
- **Spacing anchors**: 页边距 40；块间距 20；栏间距 32；圆角 0；正文行距 1.35

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 每张横幅的作者备注：本张用途（放在哪篇文章的哪个位置）、上面每句文字与代码的源文件与行号、哪些是"整理"、改字复用时要保持的元素
- **Total duration**: 不适用（静态横幅）；每张约 20–30 秒的说明量
- **Notes style**: 简洁的制作说明，口语化
- **Presentation purpose**: 先让读者认出系列，再说清本篇主题并以真实代码引起兴趣；文末促成关注

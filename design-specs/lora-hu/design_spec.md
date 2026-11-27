# LoRA: Low-Rank Adaptation of Large Language Models - Design Spec

> 论文解读演示 · 源文档:Hu et al., 2021, Microsoft (arXiv:2106.09685v2)。设计叙事见本文;机器可读执行契约见 `spec_lock.md`(冲突以 spec_lock 为准)。

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | lora_hu_2021 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 15 |
| **Design Style** | B) 通用咨询(数据清晰优先)+ 学术技术极简 |
| **Target Audience** | 机器学习研究者 / 工程师;论文分享会、组会、技术答辩 |
| **Use Case** | 英文论文的中文讲解汇报(术语保留英文) |
| **Created Date** | 2026-05-23 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 64px,上下 56px |
| **Content Area** | 1152×608(安全区) |

---

## III. Visual Theme

### Theme Style

- **Style**: 学术技术极简 — 蓝图式结构、克制留白、数据与公式说话
- **Theme**: Light theme(白底)
- **Tone**: 严谨、可信、工程化、analytical

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#FFFFFF` | 页面底色 |
| **Secondary bg** | `#F4F7FA` | 卡片 / 区块背景 |
| **Primary** | `#1B3A5C` | 深学术蓝 — 标题、结构线、图表主轴、图标 |
| **Accent** | `#E8743B` | 暖橙 — 关键数字(10000×、零延迟)、高亮、LoRA 分支 |
| **Secondary accent** | `#3E7CB1` | 中蓝 — 次级数据系列、辅助结构 |
| **Body text** | `#1D2733` | 主体文字 |
| **Secondary text** | `#5B6776` | 注释、副标题 |
| **Tertiary text** | `#8A94A1` | 脚注、页码 |
| **Border/divider** | `#D8DEE6` | 卡片边、分割线 |
| **Success** | `#2E7D32` | 优于基线指示(LoRA 胜出) |
| **Warning** | `#C62828` | 代价 / 劣势指示(全量微调开销、延迟增加) |

**Color rules**: 60-30-10(白底 60% / 深蓝 30% / 暖橙 ≤10%);正文对比度 ≥ 4.5:1;每页 ≤ 4 色。

### AI Image Strategy

- **Image Rendering**: blueprint
- **Image Palette**: cool-corporate

> blueprint × cool-corporate 兼容矩阵为 ✓✓。全 deck AI 图共享此渲染与色彩;`text_policy: embedded`,图内可带文字(术语英文、说明可中文),生成后校验输出。HEX 为真值,palette 仅规定 60-30-10 用法。

### Gradient Scheme

```xml
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#1B3A5C"/>
  <stop offset="100%" stop-color="#3E7CB1"/>
</linearGradient>
<radialGradient id="bgDecor" cx="85%" cy="15%" r="55%">
  <stop offset="0%" stop-color="#1B3A5C" stop-opacity="0.06"/>
  <stop offset="100%" stop-color="#1B3A5C" stop-opacity="0"/>
</radialGradient>
```

---

## IV. Typography System

### Font Plan

**Typography direction**: 统一无衬线(技术论文 slides 惯例),代码 / 维度符号用等宽。

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Body** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Emphasis** | `"Microsoft YaHei"` | `Arial` | `sans-serif`(weight 对比,非换字体) |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `"Microsoft YaHei", Arial, sans-serif`
- Body: `"Microsoft YaHei", Arial, sans-serif`
- Emphasis: same as Body(靠 font-weight 700/900 制造对比)
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body = 18px(dense — 数据表 + 公式 + 多点内容)。

| Purpose | Ratio | px | Weight |
| ------- | ----- | -- | ------ |
| Cover title | 3.3x | 60 | Heavy |
| Hero number(10000× 等) | 3.1x | 56 | Heavy |
| Page title | 1.8x | 32 | Bold |
| Subtitle | 1.3x | 24 | SemiBold |
| **Body** | **1x** | **18** | Regular |
| Annotation / caption | 0.78x | 14 | Regular |
| Chart annotation | 0.72x | 13 | Regular |
| Page number / footnote | 0.61x | 11 | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 高 ~96px — 页眉标题 + 细色条 + 页序
- **Content area**: 高 ~520px — 主体(图表 / 图 / 公式 / 卡片)
- **Footer area**: 高 ~40px — 来源标注(LoRA, Hu et al. 2021)+ 页码

### Layout Pattern Library(按信息权重组合)

按页采用:单列居中(封面/结论)、非对称分栏(图 vs 要点)、三/四列卡片(优势/KPI)、image-as-canvas + 原生叠加(方法图)、负空间主导(breathing 概念页)。不把每页做成同一张卡片网格。

### Spacing Specification

**Universal**: 安全边距 64px;内容块间距 28px;图标-文字间距 10px。
**Card-based**: 卡片间距 24px;卡片内边距 24px;圆角 12px;四列卡片宽 ~264px。
**Non-card(breathing)**: 行高 1.5×;靠留白与分隔线分区。

---

## VI. Icon Usage Specification

### Source

- 库:`tabler-outline`(线性、轻盈、技术屏显),`stroke_width: 2`,deck 内不混用其它库。
- 用法:`<use data-icon="tabler-outline/<name>" stroke-width="2" .../>`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 冻结权重 | `tabler-outline/snowflake` / `tabler-outline/lock` | P03/P06 |
| 部署成本 | `tabler-outline/building-bank` / `tabler-outline/server-2` | P03 |
| 局限警示 | `tabler-outline/alert-triangle` | P04 |
| 低秩洞察 | `tabler-outline/bulb` / `tabler-outline/layers-subtract` | P05 |
| 方法 / 公式 | `tabler-outline/math-function` / `tabler-outline/transform` | P06/P07 |
| 分支 A/B | `tabler-outline/arrows-split` | P06 |
| Transformer 结构 | `tabler-outline/sitemap` / `tabler-outline/topology-star` | P08 |
| 可共享 | `tabler-outline/share-2` / `tabler-outline/git-branch` | P09 |
| 高效训练 | `tabler-outline/bolt` | P09 |
| 零推理延迟 | `tabler-outline/gauge` | P09/P10 |
| 正交可叠加 | `tabler-outline/puzzle` | P09 |
| 实验 | `tabler-outline/flask` / `tabler-outline/database` | P11 |
| 结果 | `tabler-outline/chart-bar` | P10/P12 |
| 达标 / 优于 | `tabler-outline/circle-check` | P12/P13 |
| 结论 | `tabler-outline/target` | P15 |

---

## VII. Visualization Reference List

Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim from `charts_index.json`) | Usage |
| ---- | -------- | ---- | ------------------------------------------------- | ----- |
| P02 | agenda_list | `templates/charts/agenda_list.svg` | "Pick for table of contents, meeting agendas, or presentation roadmap — numbered items + brief description + duration / owner per row." | 演示路线图(6 节) |
| P04 | vertical_list | `templates/charts/vertical_list.svg` | "Pick for 3-6 numbered key points each with a short description — design principles, core tenets, action items, key takeaways, recommendations, executive summary points." | 已有方法 3 类局限 |
| P09 | icon_grid | `templates/charts/icon_grid.svg` | "Pick for 4-9 parallel features/capabilities/services as icon cards — feature grid, service lineup, benefits matrix, brand values, product highlights." | LoRA 四大优势 |
| P10 | grouped_bar_chart | `templates/charts/grouped_bar_chart.svg` | "Pick for 2-4 series side-by-side across the same categories (e.g. YoY/QoQ)." | 各方法推理延迟增幅对比 |
| P11 | basic_table | `templates/charts/basic_table.svg` | "Pick for plain tabular text/number grid, 3-8 columns." | 模型 × 基准 × 任务实验矩阵 |
| P12 | consulting_table | `templates/charts/consulting_table.svg` | "Pick for high-density tables with embedded micro bar visuals (consulting/financial reports)." | GLUE 结果(参数量 + Avg 微条) |
| P13 | kpi_cards | `templates/charts/kpi_cards.svg` | "Pick for 4-8 standalone numeric metrics shown as overview cards (2x2 or 1x4) — exec summary opener, dashboard headline, quarterly recap, results-at-a-glance." | GPT-3 175B 四项关键指标 |
| P14 | basic_table | `templates/charts/basic_table.svg` | "Pick for plain tabular text/number grid, 3-8 columns." | 适配权重(Table 5)+ 最优秩(Table 6) |
| P15 | vertical_list | `templates/charts/vertical_list.svg` | "Pick for 3-6 numbered key points each with a short description — design principles, core tenets, action items, key takeaways, recommendations, executive summary points." | 结论 takeaways |

**Runners-up considered**:

- `numbered_steps` | rejected for P02: 演示目录是并列章节而非顺序步骤,agenda_list 自带 duration/section 列更贴合。
- `pros_cons_chart` | rejected for P04: 已有方法局限是"单边缺点清单(延迟 / 序列长度 / 质量-效率权衡)",非左右对称的 pros vs cons。
- `bar_chart` | rejected for P10: 延迟需对比 AdapterL / AdapterH 两个变体 × 序列场景,属多系列并列,grouped_bar 更准。
- `comparison_table` | rejected for P12: GLUE 想用 Avg 微条强化"少参数高分"的视觉,consulting_table 的内嵌 micro-bar 优于纯文本对比表。
- `gauge_chart` | rejected for P13: GPT-3 是多项指标(参数比 / VRAM / 吞吐 / 准确率),非单一 hero 指标,kpi_cards 合适。

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |
| cover_hero.jpg | 1280x720 | 1.78 | 封面主视觉(Slide 01) | Illustration | #1 full-bleed background with floating title + #29 two-stop scrim | ai | Pending | 冻结的大型预训练权重方阵被锁住,旁路注入一条由两个细长低秩矩阵(降维 A、升维 B)组成的可训练分支,连线汇合到输出;蓝图示意,留下方安静带给 SVG 标题 | embedded | hero_page |
| cost_explosion.jpg | 860x720 | 1.19 | 全量微调部署代价(Slide 03) | Diagram | #4 right image bleeding off the canvas edge + #32 multi-stop scrim with hue shift | ai | Pending | 同一个 175B 巨型模型被为每个下游任务整份复制成多座沉重的服务器机柜,强调"每任务一份满参数副本"的高昂存储/部署成本 | embedded | local |
| lowrank_insight.jpg | 1280x720 | 1.78 | 低秩内在维度洞察(Slide 05) | Illustration | #19 image floating in whitespace with thin frame and caption + #21 rounded rectangle crop | ai | Pending | 高维权重更新云坍缩贴合到一张低维子空间薄片上,少数主方向承载主要信息;概念示意,大量留白 | embedded | local |
| reparam_diagram_cropped.jpg | 1280x531 | 2.41 | LoRA 重参数化结构图(Slide 06) | Diagram | #44 background image + native network/architecture diagram + #41 measurement lines and module tags (engineering overlay) | ai | Pending | 输入 x 同时进入冻结的预训练权重 W 与并行低秩旁路:先经降维矩阵 A 到秩 r 瓶颈,再经升维矩阵 B,两路输出相加得 h;箭头清晰,瓶颈维度 r 标注 | embedded | local |
| attention_apply.jpg | 530x580 | 0.91 | 作用于 Transformer 注意力(Slide 08) | Diagram | #2 left-third image + right text body + #21 rounded rectangle crop | ai | Pending | 一个 Transformer 自注意力模块,四个投影矩阵 Wq/Wk/Wv/Wo,其中 Wq 与 Wv 各挂一条低秩 LoRA 旁路高亮,MLP 模块标为冻结;蓝图结构 | embedded | local |
| subspace_heatmap.jpg | 1024x1024 | 1.0 | 子空间相似度热力图(Slide 14) | Diagram | #3 right-third image + left text body + #21 rounded rectangle crop | ai | Pending | 方阵热力图:行 i 列 j 的归一化子空间相似度,左上角(top singular directions)高强度发亮、其余迅速变暗,清晰的网格单元,蓝-橙强度色阶 | embedded | local |
| formula_001.png | 688x44 | 15.64 | 前向传播公式(Slide 06) | Latex Formula | formula-block | formula | Rendered | `h = W_0 x + \Delta W x = W_0 x + B A x` — LoRA 修改后的前向传播 | | |
| formula_002.png | 1280x55 | 23.27 | 低秩分解与约束(Slide 06) | Latex Formula | formula-block | formula | Rendered | `W_0 + \Delta W = W_0 + BA, B∈R^{d×r}, A∈R^{r×k}, r≪min(d,k)` — 低秩分解 | | |
| formula_003.png | 220x91 | 2.42 | 缩放系数(Slide 07) | Latex Formula | formula-block | formula | Rendered | `\Delta W x · α/r` — ΔWx 的缩放 | | |
| formula_004.png | 604x60 | 10.07 | 可训练参数量(Slide 08) | Latex Formula | formula-block | formula | Rendered | `|Θ| = 2 × L_LoRA × d_model × r` — LoRA 可训练参数量 | | |

> 图内文字按"是否需可编辑"判别(冻结栅格 → 生成后校验);P06 采用 image-as-canvas(#44)满足 image-as-canvas 覆盖要求 — 精确公式与可改写标签走 SVG 叠加,图本身承载结构氛围。所有 AI 图同 blueprint × cool-corporate,HEX 不作为字面文字写进图内。

---

## X. Speaker Notes Requirements

- 每页一篇,存 `notes/total.md`(主文档用 `#` 标题行,文件名匹配 SVG)
- 总时长:约 18-22 分钟;风格:讲解型(conversational-professional);目的:inform + instruct
- 中文讲解,术语保留英文

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:
1. viewBox `0 0 1280 720`;背景用 `<rect>`
2. 文本换行用 `<tspan>`;禁止 `<foreignObject>`
3. 透明默认用 `fill-opacity` / `stroke-opacity`；`rgba()` 保持转换兼容
4. 禁止:`mask`、`<style>`、`class`、`foreignObject`、`textPath`、`animate*`、`script`
5. 字符写原始 Unicode(`—`、`→`、`×`、`≪`);禁止 HTML 实体;`& < >` 转义为 `&amp; &lt; &gt;`
6. `clipPath` 仅用于 `<image>`(圆角裁剪等)

### PPT Compatibility Rules:
- 默认逐子元素设置 opacity；`<g opacity>` 可转换但会产生近似保真 warning
- 图片半透明用叠加遮罩层
- 仅内联样式;禁外部 CSS / `@font-face`

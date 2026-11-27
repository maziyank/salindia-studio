# global_ai_capital_2026 - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | global_ai_capital_2026 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 18 |
| **Design Style** | B) General Consulting + Bloomberg/Economist 新闻信息图风 |
| **Target Audience** | 科技/金融行业研究者、AI 从业者、风险投资圈、媒体编辑 |
| **Use Case** | 行业洞察分享 / 投资简报 / 媒体解读专栏 |
| **Created Date** | 2026-05-16 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px / 上下 50px |
| **Content Area** | 1160×620（页眉 80 + 主体 560 + 页脚 30） |

---

## III. Visual Theme

### Theme Style

- **Style**: B) General Consulting + Bloomberg/Economist 新闻信息图风
- **Theme**: Dark theme
- **Tone**: 冷静、克制、出版级、数据导向；不是 keynote 冲击力，而是夜读财经长稿的深思感

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#0E1116` | 深石墨黑（不是纯黑） |
| **Secondary bg** | `#1A1F26` | 卡片 / 分区底色 |
| **Primary** | `#E8E6E1` | 报纸暖白 — 主文字、标题 |
| **Accent** | `#E63946` | 财经红 — 风险、警示、关键数字 |
| **Secondary accent** | `#F4A261` | 琥珀金 — 次级强调（中国 / 二线公司） |
| **Body** | `#C9C5BE` | 暖灰白 — 正文 |
| **Secondary text** | `#8A857E` | 注释 / 页脚 |
| **Tertiary text** | `#5C5852` | 极轻信息 / 来源行 |
| **Border** | `#2A2F36` | 极细分割线 |
| **Success** | `#52B788` | 正向趋势（绿涨） |
| **Warning** | `#E63946` | 复用 accent |

### AI Image Strategy

- **Image Rendering**: editorial
- **Image Palette**: dark-cinematic

### Gradient Scheme

```xml
<linearGradient id="scrim_v" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#0E1116" stop-opacity="0.3"/>
  <stop offset="100%" stop-color="#0E1116" stop-opacity="0.92"/>
</linearGradient>

<linearGradient id="accentLine" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#E63946" stop-opacity="1"/>
  <stop offset="100%" stop-color="#E63946" stop-opacity="0"/>
</linearGradient>
```

---

## IV. Typography System

**Typography direction**: 报刊编辑派 — 西文衬线 Cambria 扛标题与大字 hero number，中文走 Microsoft YaHei，正文 Latin 用 Arial 走数字精度

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `Cambria` | `serif` |
| **Body** | `"Microsoft YaHei", "PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `"Microsoft YaHei"` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `Cambria, "Microsoft YaHei", serif`
- Body: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Emphasis: `Georgia, "Microsoft YaHei", serif`
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body font size = **16px**（chart-heavy 高密度）

| Purpose | Ratio to body | Px @ 16 | Weight |
| ------- | ------------- | ------- | ------ |
| Cover title (hero headline) | 4-5x | 64-80px | Bold |
| Chapter / section opener | 2.5-3x | 40-48px | Bold |
| Page title | 1.5-2x | 24-32px | Bold |
| Hero number (大数字) | 4-6x | 64-96px | Bold（Cambria） |
| Subtitle | 1.2-1.5x | 19-24px | SemiBold |
| **Body content** | **1x** | **16px** | Regular |
| Annotation / caption | 0.7-0.85x | 11-14px | Regular |
| Page number / footnote | 0.6-0.7x | 10-11px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 上 50px — 章节番号 + 章节名（左对齐，11px tertiary） + 极细分割线
- **Content area**: 中 560px — 主可视化 / hero number / chart
- **Footer area**: 下 30px — 页码 + Sources 注脚 + 极细顶部分割线

### Layout Pattern Library

> 本 deck 主导布局：**Asymmetric split（3:7 chart vs 注解）/ Single column centered（封面 / 章节）/ Three-column（KPI cards）/ Top-bottom split（带 hero band 的图表 + 注脚）/ Full-bleed + floating text（3 张氛围图章节页）**。Z-pattern 与 Matrix grid 出现在 quadrant_text_bullets 页。

### Spacing Specification

**Universal**:

| Element | Range | This Deck |
| ------- | ----- | --------- |
| Safe margin | 40-60px | 60px |
| Content block gap | 24-40px | 28px |
| Icon-text gap | 8-16px | 10px |

**Card-based**:

| Element | Range | This Deck |
| ------- | ----- | --------- |
| Card gap | 20-32px | 24px |
| Card padding | 20-32px | 22px |
| Card border radius | 8-16px | 6px（克制，不要圆胖） |

**Non-card** (breathing 页 / 氛围底图):
- Line-height: 1.5× body
- Full-bleed text 用 `scrim_v` 渐变扛 legibility
- 不强行列宽对齐，按报刊导语自由 inset

---

## VI. Icon Usage Specification

### Source

- **Library**: `tabler-outline`（stroke 1.5）
- **Brand-logo library**: `simple-icons`（用于 OpenAI / Anthropic / xAI / Nvidia / Google / Microsoft / Amazon / Meta / Oracle / SoftBank 等 logo 标识）
- **Usage**: `<use data-icon="library/icon-name" .../>`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| Trending up（资本流入） | `tabler-outline/trending-up` | P04, P05, P11 |
| Currency dollar（估值） | `tabler-outline/currency-dollar` | P04, P06, P09 |
| Building（公司） | `tabler-outline/building` | P06, P09 |
| Chart bar（数据） | `tabler-outline/chart-bar` | P05, P15 |
| Server（基建） | `tabler-outline/server` | P14, P15 |
| Bolt（电力） | `tabler-outline/bolt` | P05, P14 |
| Alert triangle（风险） | `tabler-outline/alert-triangle` | P15, P16, P17 |
| Globe（全球） | `tabler-outline/globe` | P04, P09 |
| Cpu（芯片） | `tabler-outline/cpu` | P12, P13 |
| Trending down（衰减） | `tabler-outline/trending-down` | P15, P16 |
| Arrow right（流向） | `tabler-outline/arrow-right` | P12, P14 |
| Bookmark（章节标志） | `tabler-outline/bookmark` | 章节页 |
| OpenAI 品牌 | `simple-icons/openai` | P06, P08, P14 |
| Anthropic | `simple-icons/anthropic` | P06 |
| Nvidia | `simple-icons/nvidia` | P12, P13 |
| Google | `simple-icons/google` | P05, P06 |
| Microsoft | `simple-icons/microsoft` | P05 |
| Amazon | `simple-icons/amazon` | P05 |
| Meta | `simple-icons/meta` | P05 |
| Oracle | `simple-icons/oracle` | P14 |
| SoftBank | `simple-icons/softbank` | P14 |

---

## VII. Visualization Reference List

Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim) | Usage |
| ---- | -------- | ---- | ------------------------ | ----- |
| P04 | kpi_cards | `templates/charts/kpi_cards.svg` | "Pick for 4-8 standalone numeric metrics shown as overview cards (2x2 or 1x4) — exec summary opener, " | Q1 风投总盘子四大 KPI（VC 总额 / AI 占比 / 三笔大单 / 集中度） |
| P05 | bar_chart | `templates/charts/bar_chart.svg` | "Pick for single-series category value comparison, 3-8 categories. Skip for >12 long-label items (use" | Amazon / Microsoft / Google / Meta 四家 capex 对比 |
| P07 | dumbbell_chart | `templates/charts/dumbbell_chart.svg` | "Pick for before-vs-after or two-state difference across 5-10 items. Skip for single snapshot (use ba" | OpenAI/Anthropic/xAI 估值前后对比（年初 vs Q2） |
| P08 | bubble_chart | `templates/charts/bubble_chart.svg` | "Pick for 3-axis data (x position, y position, size). Skip for plain x-y correlation (use scatter_cha" | 三巨头 估值 × ARR × 投资人数 散点 |
| P09 | donut_chart | `templates/charts/donut_chart.svg` | "Pick for 3-6 part proportions where a center KPI/total deserves emphasis. Skip if no center value to" | OpenAI $122B 投资人构成（Amazon/Nvidia/SoftBank/MSFT/其他） |
| P10 | horizontal_bar_chart | `templates/charts/horizontal_bar_chart.svg` | "Pick for ranking 5-12 items, especially with long labels. Skip if <=8 short-label items (use bar_cha" | 中国阵营 5 家估值排名（DeepSeek/Zhipu/MiniMax/Moonshot/StepFun） |
| P11 | comparison_table | `templates/charts/comparison_table.svg` | "Pick for 2-4 plans/products compared across many feature rows (dense matrix). Skip for pricing-tier " | 中美 AI 资本路径双轨对比（私募规模/IPO/政府/估值峰值/退出方式） |
| P12 | sankey_chart | `templates/charts/sankey_chart.svg` | "Pick for 3-stage flow with magnitude (sources -> nodes -> sinks). Skip for simple linear conversion " | Nvidia 闭环：股权投资 → AI 公司 → 芯片采购回流 |
| P13 | pareto_chart | `templates/charts/pareto_chart.svg` | "Pick for 80/20 contribution: descending bars + cumulative line. Skip if cumulative line is not t" | Nvidia 客户集中度 85% 来自 6 家 |
| P14 | hub_spoke | `templates/charts/hub_spoke.svg` | "Pick for 1 core capability + 4-8 surrounding capabilities (platform/ecosystem); each spoke = title o" | Stargate 项目 hub + 7 个数据中心站点 |
| P16 | dual_axis_line_chart | `templates/charts/dual_axis_line_chart.svg` | "Pick when 2 metrics with different units/scales must be compared over time. Skip if both metrics sha" | 2020-2026 Capex（左轴 $B）vs Enterprise AI Revenue（右轴 $B）剪刀差 |
| P17 | quadrant_text_bullets | `templates/charts/quadrant_text_bullets.svg` | "Pick for any 2×2 framework where each quadrant holds a titled bullet list — SWOT (Strengths/Weakness" | 四大风险象限：资本鸿沟 / 企业 ROI / 客户集中 / 融资结构 |

**Runners-up considered**:

- `donut_chart` | rejected for P04: KPI cards 更适合 4 个独立指标并列展示，donut 强调比例切分而非单独读取
- `stacked_bar_chart` | rejected for P05: 单一指标（capex 金额）对比，无内部分组结构
- `grouped_bar_chart` | rejected for P07: dumbbell 更适合"两状态差值"叙事，grouped bar 适合 YoY 多类别
- `treemap_chart` | rejected for P09: OpenAI 投资人只有 5-6 个独立份额，donut 中心可显总额 $122B，treemap 强调层级
- `radar_chart` | rejected for P10: 5 家公司单一指标（估值）排名，radar 适合多维能力
- `hub_inward_arrows` | rejected for P12: sankey 才能表达"金额流量"，hub_inward 只有方向无量值
- `bar_chart` | rejected for P13: pareto 同时显示个体贡献 + 累积占比，bar 只有前者
- `process_flow` | rejected for P14: hub_spoke 表达"一个中枢 + 多个外围站点"的 Stargate 拓扑，process_flow 暗示线性

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |
| cover_atmosphere.jpg | 1280×720 | 1.78 | 封面氛围底图 | Background | #1 full-bleed background with floating title + #29 two-stop scrim | ai | Pending | Abstract nighttime aerial of a vast data-center campus, faint server-rack lights forming a constellation pattern; quiet wide-angle composition with reserved dark sky for title overlay; sense of capital flowing through silent infrastructure | none | hero_page |
| nvidia_circular.jpg | 1280×720 | 1.78 | Part V Nvidia 闭环章节锚点 | Background | #1 full-bleed background with floating title + #29 two-stop scrim | ai | Pending | Abstract macro shot of a circular wafer-like geometry with subtle red glow at the rim suggesting circulation; central dark void reserved for chapter title; metallic finish but no recognizable logos | none | hero_page |
| bubble_tension.jpg | 1280×720 | 1.78 | Part VI 泡沫论章节锚点 | Background | #1 full-bleed background with floating title + #29 two-stop scrim | ai | Pending | Abstract atmospheric image of a single iridescent soap-bubble suspended in deep dark space, surface tension catching a faint warning-red highlight; quiet composition with negative space; sense of fragile inflation | none | hero_page |

---

## X. Speaker Notes Requirements

- 文件命名：与 SVG 同名（`01_cover.svg` → `notes/01_cover.md`）
- 单页 100-150 字，编辑导语派口吻，不是销售也不是教学
- 全 deck 总时长目标：15-20 分钟

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background 用 `<rect>`
3. Text wrap 用 `<tspan>`
4. 透明度用 `fill-opacity` / `stroke-opacity`
5. FORBIDDEN: `mask`, `<style>`, `class`, `foreignObject`, `textPath`, `animate*`, `script`, `<symbol>`+`<use>` 自定义
   - Transparency defaults to explicit alpha attributes; `rgba()` and `<g opacity>` remain converter-compatible, with group opacity carrying an approximate-fidelity warning.
6. HTML named entities 禁用，写 raw Unicode
7. `marker-start` / `marker-end` 仅 `<marker>` in `<defs>` 且 orient="auto"
8. `clipPath` 仅作用于 `<image>`，且 single shape child

### PPT Compatibility:

- Inline styles only
- 每个元素单独设 opacity
- 字体栈每条以预装字体收尾

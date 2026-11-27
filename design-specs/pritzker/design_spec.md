# pritzker_2026_test_20260516 - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | pritzker_2026_test_20260516 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 11 |
| **Design Style** | A) General Versatile + 编辑设计 / 杂志感 / 建筑摄影主导 |
| **Target Audience** | 建筑/设计爱好者、设计行业从业者、文化媒体读者 |
| **Use Case** | 行业分享、设计课堂、自媒体长图、读书会演讲 |
| **Created Date** | 2026-05-16 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px / 上下 50px |
| **Content Area** | 1160×620 |

---

## III. Visual Theme

### Theme Style

- **Style**: 编辑杂志感 + 建筑摄影主导
- **Theme**: Light theme
- **Tone**: 克制、克难、克重——大图说话，文字点题；混凝土质感的米白底色 + 墨黑文字 + 暖金强调

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#F5F2EC` | 米白宣纸底（主背景） |
| **Secondary bg** | `#EDE8DE` | 卡片/侧栏 |
| **Primary** | `#1C1C1C` | 标题、正文 |
| **Accent** | `#B8935A` | 编号、分隔线、强调 |
| **Body text** | `#1C1C1C` | 正文主色 |
| **Secondary text** | `#5C5852` | 副文、图注 |
| **Tertiary text** | `#8B8680` | 混凝土灰，页脚、辅助 |
| **Border/divider** | `#D4CFC4` | 分隔线 |

---

## IV. Typography System

### Font Plan

**Typography direction**: editorial CJK — 西文衬线 × 中文黑体，杂志专栏感

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei", "PingFang SC"` | `Georgia` | `serif` |
| **Body** | `"Microsoft YaHei", "PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `KaiTi` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `Georgia, "Microsoft YaHei", "PingFang SC", serif`
- Body: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Emphasis: `KaiTi, Georgia, "Microsoft YaHei", serif`
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body = 22px (中等密度)

| Purpose | Ratio | Project value | Weight |
| ------- | ----- | ------------- | ------ |
| Cover title | 3.3x | 72px | Bold |
| Chapter / section opener | 2.2x | 48px | Bold |
| Page title | 1.6-1.8x | 36-40px | Bold |
| Project number (01-08 大编号) | 4x | 88px | Light Italic (Georgia) |
| Subtitle | 1.3x | 28px | SemiBold |
| **Body** | **1x** | **22px** | Regular |
| Annotation / caption | 0.7x | 15px | Regular |
| Page number / footnote | 0.55x | 12px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 50-100px（编号 + 章节锚标）
- **Content area**: ~520px（图文主体）
- **Footer area**: 30-40px（页码、来源、品牌锚）

### Layout Pattern Library

不预设主导 pattern。每页按内容性格挑节奏（详见 §VIII 表中 `Layout pattern` 列），原则：
1. 相邻两页不重复 pattern
2. 同一 pattern 全 deck 不超过 2 次
3. 图比例驱动方向（横图优先 hero/上下带，方图优先并置，竖图优先左右带）
4. 同主题多图合并到一页（多图组合）而非拆页

### Spacing Specification

**Universal**:

| Element | Range | Project |
| ------- | ----- | ------- |
| Safe margin | 40-60px | 60px |
| Content block gap | 24-40px | 32px |
| Icon-text gap | 8-16px | 12px |

**Non-card containers** (大量 breathing/hero 页):

- 行高 1.5×
- 全幅大图采用 `xMidYMid slice`；hero 文字浮层有 35-55% 半透明黑底 scrim
- 不强求等宽栏；文字宽度按可读性（每行 24-32 汉字）

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `tabler-outline`（描边 1.5px）
- 仅用于章节编号点缀、地理标识、年份徽章；不强加于每页

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 地点定位 | `tabler-outline/map-pin` | P03-P10（每页右上） |
| 时间/年份 | `tabler-outline/calendar` | P02（总览） |
| 建筑师章 | `tabler-outline/blockquote` | P11（结语） |
| 翻页指示 | `tabler-outline/arrow-right` | P02 |

---

## VII. Visualization Reference List

无数据可视化页。本 deck 完全图文叙事驱动，无图表。

---

## VIII. Image Resource List

> Layout pattern 全部 verbatim from `references/image-layout-patterns.md`。覆盖 Group A / C / D / E 至少 4 组；同组内 id 轮换；相邻页不重复。

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- |
| ando_h_rooftop.jpg | 685×514 | 1.33 | P01 封面背景（混凝土水景） | Photography | #1 full-bleed background with floating title | user | Existing | 安藤忠雄 H+ 美术馆屋顶水景 |
| ando_h_exterior.jpg | 1080×810 | 1.33 | P03 安藤代表作主图 | Photography | #41 background image with native callout cards floating over | user | Existing | H+ 美术馆临河外观 |
| ando_h_interior.jpg | 667×937 | 0.71 | P03 安藤副图（竖图） | Photography | (同上多图组合) | user | Existing | H+ 美术馆室内空间 |
| chipperfield_milan_exterior.jpg | 1080×810 | 1.33 | P04 奇普菲尔德主图 | Photography | #48 side-by-side comparison (古罗马 vs 当代) | user | Existing | 米兰冰球馆外观 |
| chipperfield_roman_amphitheater.jpg | 800×533 | 1.50 | P04 古罗马参照 | Photography | (与主图并置) | user | Existing | 古罗马圆形剧场 |
| chipperfield_milan_facade.png | 1024×1365 | 0.75 | P04 立面细节（竖图） | Photography | (副图条带) | user | Existing | 场馆立面金属环带 |
| zaha_tamkang_bridge.jpg | 960×640 | 1.50 | P05 扎哈大桥主视觉 | Photography | #15 multi-image montage with bold text spanning across | user | Existing | 淡江大桥流线姿态 |
| zaha_tamkang_structure.jpg | 960×640 | 1.50 | P05 大桥结构 | Photography | (蒙太奇成员) | user | Existing | 大桥单塔斜拉结构 |
| zaha_tamkang_full.jpg | 831×554 | 1.50 | P05 大桥远景 | Photography | (蒙太奇成员) | user | Existing | 大桥跨江全景 |
| foster_shanghai_exterior.jpg | 1080×652 | 1.66 | P06 福斯特大图 | Photography | #12 faded image as backdrop with oversized overlay text | user | Existing | 上海嘉艺术外观全景 |
| foster_shanghai_petal.jpg | 1080×1368 | 0.79 | P06 花瓣细节 | Photography | (浮层旁置小图框) | user | Existing | 花瓣立面细节 |
| oma_new_museum_before.jpg | 1080×809 | 1.33 | P07 OMA 扩建前后 (前) | Photography | #50 before/after slider-style side-by-side | user | Existing | 纽约新美术馆扩建前 |
| oma_new_museum_after.jpg | 1080×921 | 1.17 | P07 OMA 扩建前后 (后) | Photography | (#50 配对) | user | Existing | 纽约新美术馆扩建后 |
| oma_new_museum_massing.jpg | 1080×608 | 1.78 | P07 体块模型条带 | Photography | (#50 下方副条) | user | Existing | OMA 体块模型 |
| oma_new_museum_interior.png | 1080×896 | 1.21 | P07 室内（备用） | Photography | (内嵌副图框) | user | Existing | 美术馆内部 |
| zumthor_lacma_exterior.jpg | 1080×608 | 1.78 | P08 卒姆托主图 | Photography | #14 horizontal banner strip cutting through mid-section | user | Existing | LACMA 大卫·格芬画廊横幅 |
| zumthor_lacma_underside.png | 1080×720 | 1.50 | P08 底部公共空间 | Photography | (mid-section 横条之下副图) | user | Existing | 悬浮架空底部空间 |
| zumthor_lacma_interior.png | 1080×608 | 1.78 | P08 内部（备用） | Photography | (右上小景) | user | Existing | LACMA 室内 |
| gehry_abu_dhabi_render1.jpg | 1080×608 | 1.78 | P09 盖里渲染主图 | Photography | #19 image floating in whitespace with thin frame and caption | user | Existing | 阿布扎比古根海姆主渲染 |
| gehry_abu_dhabi_render2.png | 1080×607 | 1.78 | P09 渲染辅图 | Photography | (#19 第二浮层框) | user | Existing | 第二角度渲染 |
| gehry_abu_dhabi_render3.png | 1000×1000 | 1.00 | P09 方图辅 | Photography | (#19 第三浮层) | user | Existing | 鸟瞰渲染 |
| kere_senegal_exterior.jpg | 818×546 | 1.50 | P10 凯雷主图（土砖外观） | Photography | #38 background image + annotation cards | user | Existing | 塞内加尔歌德学院外观 |
| kere_senegal_courtyard.jpg | 630×944 | 0.67 | P10 院落（竖图） | Photography | (annotation 中嵌入小图) | user | Existing | 猴面包树核心院落 |
| kere_senegal_interior.jpg | 980×654 | 1.50 | P10 内部 | Photography | (annotation 中嵌入小图) | user | Existing | 学院内部空间 |

**Layout pattern 覆盖审计**:
- Group A (容器): #1 cover, #12 faded backdrop, #14 mid-section banner, #15 montage with text → 4 patterns
- Group C (overlay): #19 floating frame → 1 pattern
- Group D (image-as-canvas): #38 background + cards, #41 background + callouts → **2 patterns，满足 Group D 覆盖硬约束**
- Group E (multi-image): #48 side-by-side, #50 before/after → 2 patterns
- 共 9 个不同 pattern 跨 4 组，无任何 pattern 使用 >2 次，相邻页无重复

---

## X. Speaker Notes Requirements

- **Filename**: 与 SVG 同名（`01_cover.svg` → `notes/01_cover.md`）
- **Total duration**: 约 12 分钟
- **Notes style**: 文化随笔式，叙述温度优先于技术参数
- **Purpose**: inform + inspire

---

## XI. Technical Constraints Reminder

1. viewBox: `0 0 1280 720`
2. `<rect>` 背景，`<tspan>` 文本换行
3. 透明度默认用 `fill-opacity` / `stroke-opacity`；`rgba()` 保持转换兼容
4. 禁用：`mask`, `<style>`, `class`, `foreignObject`, `textPath`, `<animate*>`, `<script>`
   - `<g opacity>` 可转换但会产生近似保真 warning，默认改用子元素透明度
5. 字符：`—` `·` `→` 等用原生 Unicode，禁用 HTML named entities
6. 全幅图用 `preserveAspectRatio="xMidYMid slice"`；半透明 scrim 用 `<rect fill-opacity>`

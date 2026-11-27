<!-- ppt-master-schema: design-spec/v1 -->
# taiwan_super_aged_society_zh_hant - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 臺灣進入超高齡社會 |
| Canvas Format | ppt169（1280 × 720） |
| Page Count | 15 |
| Primary Language | zh-Hant-TW |
| Target Audience | 參加公開講座的一般民眾：對「人口老化」有生活感受，但不熟悉人口推估、扶養比等統計用語 |
| Communication Intent | 先說清楚「超高齡社會」的定義與臺灣跨過三道門檻的時間差，再用國發會推估解釋背後的機制（出生變少、壽命變長、出生與死亡交叉、年齡結構翻轉），最後把推估連到勞動、照顧與已公布的政策方向 |
| Desired Audience Outcome | 聽眾能說出臺灣在 2025 年底跨過 20%、從 14% 到 20% 只花 7 年；能用出生死亡交叉與金字塔翻轉解釋原因；知道扶養比、勞動力與照顧需求的推估方向與政府已公布的對策架構 |
| Core Message / Ask / Action | 20% 不是終點：臺灣老化得比多數國家快，接下來改變的是出生、工作與照顧的整體結構 |
| Delivery Context | 主講者現場講演為主（約 35 分鐘公開講座、投影）；會後提供簡報檔給聽眾自行閱讀 |
| Artifact Afterlife | 會後分享給聽眾參考；每頁保留來源與年份，收束頁保留可點擊的原始來源 |
| Reading Mode | balanced |
| Content Strategy | 未指定（平衡預設）：依國發會報告重組成講座敘事，所有數字保持出處 |
| Design Style | 刻度與證據：暖白紙面上的深藍資料新聞版式，時間刻度尺為跨頁母題，磚紅只標門檻與老年人口 |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy（委託確認取推薦值） |
| Custom Animations | enabled — final Stage-2 proactive policy（委託確認取推薦值；使用者任務要求自訂動畫） |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-11 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 左右 64、上 48、下 40 |
| Content Area | x 64–1216，y 48–680 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: pyramid, instructional
- **Mode Behavior**: 每頁標題就是該頁唯一的主導判斷句，副標一句給出關鍵數字與比較；全卷按「門檻 → 原因 → 結構 → 影響 → 已公布對策」的學習順序推進，先定義再使用術語，並列概念保持同形同深；每個資料頁都寫出來源與推估情境。
- **Visual style**: custom
- **Visual Style References**: data-journalism, editorial
- **Visual Style Behavior**: 暖白紙面上的資料新聞版式：圖表是頁面的脊柱，文字繞著圖表排而不是裝進卡片；以細髮絲線、欄線與一條橫貫的時間刻度尺分區，重點數字用欄寬級的大字，來源列固定在頁尾。磚紅只標門檻、老年人口與關鍵年份，深藍承擔主體與工作年齡，鼠尾草綠承擔出生與幼年；幾乎不用陰影，深度只來自圖片的色調處理與裁切形狀。
- **Theme**: 時間刻度尺（7% → 14% → 20% → 30% …）作為跨頁母題，在門檻頁、國際比較與收束頁以不同尺度重現
- **Tone**: 冷靜、清楚、可查證；像一篇有溫度的資料報導

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F6F3EC | 暖白紙面底色 |
| Secondary background | #ECE6DA | 側欄、表頭、分區底 |
| Primary | #1F3A5F | 標題、主體資料、工作年齡人口、死亡數 |
| Accent | #B5462F | 門檻標記、65 歲以上人口、關鍵年份 |
| Secondary accent | #5E8C6A | 出生數、幼年人口、正向變化 |
| Body text | #1E232B | 內文 |
| Secondary text | #5A6270 | 圖說、註解、來源列 |
| Divider | #D5CCBC | 髮絲線、欄線、表格線 |
| Grid | #E3DCCF | 圖表格線，比分隔線更淡 |
| Surface | #FFFFFF | 表格與圖表面板的輕微抬升 |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: screen-print
- **Visual**: 絹印海報式的平塗剪影：深藍、磚紅、紙白與少量鼠尾草綠，過渡處加半調網點，人物以輪廓清楚的剪影呈現，不畫五官細節
- **Mood**: 安靜、有尊嚴的日常；像公共圖書館海報上的社區插畫
- **Image Rendering Behavior**: 以 2–4 個平塗色塊構成畫面，形體是乾淨的鏤空剪影、邊緣略帶手工感，無漸層；過渡區用疏密變化的半調網點，整體覆蓋約 12% 的紙張顆粒與輕微套色偏移。題材是臺灣日常街景與人物（長者、孩子、照顧者），以大面積留白與幾何框構圖。圖中不出現任何文字、數字、招牌字樣或標誌。

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 繁中黑體，粗體承擔權威 | Microsoft JhengHei | Segoe UI | sans-serif |
| Body | 繁中黑體，清楚中性 | Microsoft JhengHei | Segoe UI | sans-serif |

- **Title stack**: 'Segoe UI', 'Microsoft JhengHei', sans-serif
- **Body stack**: 'Segoe UI', 'Microsoft JhengHei', sans-serif
- **Role rationale**: 繁中投影講座選用 Windows 內建的微軟正黑體（臺灣字形標準），不用微軟雅黑以免出現大陸字形；全卷同一家族，以字重與字級對比。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 40 |
| Subtitle | 30 |
| Annotation | 18 |
| Lead | 28 |
| Footnote | 14 |
| Cover title | 72 |
| Hero | 88 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 左上判斷句標題 → 大數字或圖表主體 → 右側或下方的解讀 → 頁尾來源列
- **Composition tendency**: 以不對稱欄位與橫向刻度尺組織頁面；圖表與時間尺佔主要面積，解讀文字貼著資料排；少用等寬卡片
- **Cross-page continuity**: 頁尾來源列與頁碼固定；時間刻度尺、磚紅門檻標記、三色年齡語意（綠幼年／藍工作年齡／紅老年）全卷一致；人口金字塔在相鄰兩頁以同一組長條變形
- **Spacing posture**: 依頁面節奏變化：dense 頁收緊欄距，breathing 頁大留白
- **Spacing anchors**: 頁邊 64、區塊間距 32、欄距 40、圓角 4、內文行距 1.5

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-filled/user.svg |  |
| icons/tabler-filled/man.svg |  |
| icons/tabler-filled/woman.svg |  |
| icons/tabler-filled/baby-carriage.svg |  |
| icons/tabler-filled/briefcase.svg |  |
| icons/tabler-filled/school.svg |  |
| icons/tabler-filled/medical-cross.svg |  |
| icons/tabler-filled/heart.svg |  |
| icons/tabler-filled/home.svg |  |
| icons/tabler-filled/hourglass.svg |  |
| icons/tabler-filled/external-link.svg |  |
| icons/tabler-filled/file-analytics.svg |  |
| icons/tabler-filled/flag.svg |  |
| icons/tabler-filled/bed.svg |  |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P05 | table | metric_table | 比較各國跨越 7%、14%、20% 的年份與所需年數 |
| P07 | chart | line_chart | 1990–2075 年出生數與死亡數的變化與 2020 年交叉 |
| P08 | chart | butterfly_chart | 2026 年分性別五歲組人口金字塔 |
| P09 | chart | butterfly_chart | 2075 年分性別五歲組人口金字塔 |
| P10 | chart | stacked_bar_chart | 2026–2075 年扶幼比與扶老比組成的扶養比 |
| P11 | chart | stacked_bar_chart | 2026、2040、2075 年工作年齡人口的年齡組成占比 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_street.png | 2752×1536 | 16:9 | 封面街景原圖，只供色調派生 | Source | 不直接上頁，僅作為雙色調派生的來源 | adaptive | ai | Generated | 清晨的臺灣騎樓街景：一位拄杖長者坐在騎樓下的長椅，一個背書包的孩子從畫面另一側走過，兩人之間隔著大片留白；畫面左側 40% 保持安靜的牆面與天空，供標題使用；騎樓柱列形成縱向節奏 | none | hero_page |
| cover_street_duotone.jpg | 1600×893 | 16:9 | 封面主視覺：同一條街上兩個世代 | Photography | 滿版底圖，左側安靜區放標題，人物落在右側三分之一 | adaptive | ai | Generated | Derived from cover_street.png; treatment=duotone; 深藍 #1F3A5F 暗部、紙白 #F6F3EC 亮部，讓標題文字在單一明度底上清楚 | none | hero_page |
| hands_generations.jpg | 1024×1024 | 1:1 | 章節轉折頁：少子與長壽兩股力量 | Illustration | 以圓形或拱形裁切的主圖，放在兩個關鍵數字之間 | adaptive | ai | Generated | 一隻布滿皺紋的長者的手輕握一隻嬰兒的小手，特寫，背景為大面積紙白留白，兩隻手位於畫面中央偏下，四周留白足以圓形裁切 | none | local |
| care_home.jpg | 896×1200 | 3:4 | 照顧需求頁：居家照顧的日常場景 | Illustration | 拱形裁切的直幅圖，放在頁面一側，另一側是大數字 | adaptive | ai | Generated | 室內居家場景：一位照顧者蹲在坐輪椅的年長者身旁整理毯子，窗光從左側進來，構圖主體位於中央，上方與兩側留白可做拱形裁切 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 以繁體中文（臺灣用語）寫講稿，每頁先講結論再補數字；只使用 sources/ 內國發會報告、新聞稿、開放資料與內政部統計報導的數字，推估值口頭說明為「中推估」；不提供個人理財或生活建議
- **Total duration**: 約 35 分鐘
- **Notes style**: 口語、平實、面向一般民眾的公開講座
- **Presentation purpose**: 說明超高齡社會的定義與臺灣的時間差，解釋背後機制，並把推估連到勞動、照顧與已公布的政策方向

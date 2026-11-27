<!-- ppt-master-schema: design-spec/v1 -->
# tokaido_shinkansen_60_ja - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | tokaido_shinkansen_60_ja |
| Canvas Format | ppt169 (1280×720) |
| Page Count | 15 |
| Primary Language | ja-JP |
| Target Audience | 一般の聴講者。新幹線に乗った経験はあるが、技術や統計の詳細は知らない市民(鉄道ファンに限らない) |
| Communication Intent | 60年の歩みを検証できる数字で振り返り(伝える)、速さ・本数・定時性・安全がどう積み上がったかの仕組みを示し(説明する)、最後に次の60年(中央新幹線)を公表情報どおりに位置づける |
| Desired Audience Outcome | 聴衆が「4時間→2時間21分」「1日60本→395本」「乗車中の死傷事故ゼロ」を仕組みと結びつけて説明でき、中央新幹線について公表済みの計画と未確定の点を区別できる |
| Core Message / Ask / Action | 東海道新幹線の60年は、速さだけでなく本数・定時性・安全を同時に積み上げてきた60年であり、次の60年はその大動脈を二重にする段階に入っている |
| Delivery Context | 主:登壇者による一般向け講演(会場投影、約25分);副:講演後の配布資料としての閲覧 |
| Artifact Afterlife | 講演資料として配布・再利用。各数字を出典名と参照年で追跡できること |
| Reading Mode | presentation |
| Content Strategy | balanced default(空欄のまま確認) |
| Design Style | 昭和の記念ポスター — custom mode(narrative 基盤)+ custom visual style(vintage-poster 基盤)+ custom rendering(vintage-poster 基盤) |
| AI Image Acquisition Path | auto |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy(委任確認で推奨値を採用) |
| Custom Animations | enabled — explicit instruction(依頼書:主役の登場・枠は動かさない・脇役は動かさない;オブジェクト単位) |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-11 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 左右 64px、上 56px、下 48px |
| Content Area | x 64–1216、y 56–672 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: narrative
- **Mode Behavior**: 1964年の開業という「出発の瞬間」から始め、速さ→本数→安全という三つの章で「どうやって積み上げたか」を一つずつ解き明かし、各章の山場で一つの決定的な数字を見せてから仕組みを説明する。最後に「次の60年」で未確定の点を正直に示し、二重化という次の章の問いで結ぶ。タイトルは物語の一歩を進める判断文にする。
- **Visual style**: custom
- **Visual Style References**: vintage-poster
- **Visual Style Behavior**: 昭和の記念ポスター。クリーム色の紙の地に、藍の大きな平面ブロック・朱の太陽円盤・黄土の帯を少数だけ重ね、角の丸い幾何形とやや斜めの帯でレトロな緊張を出す。数字はポスター級の大きさで一点に置き、細い二重罫と丸いバッジで出典や年代を添える。網点(ハーフトーン)と紙の粒子を低い不透明度で重ねて印刷物の質感を出し、影やグラデーションは使わず重なりで奥行きを出す。見出しは明朝の落ち着き、本文はゴシックの読みやすさ、巨大数字は極太のサンセリフ。
- **Theme**: 60年目の記念ポスター — 藍の軌道線(横に走る一本の太い帯)が各ページを貫き、年表の軸・グラフの基線・区切りとして役割を変えて繰り返す
- **Tone**: 温かく、誇らしく、しかし事実に厳密

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F3ECDD | クリーム色の紙の地 |
| Secondary background | #E6DCC6 | 一段濃い紙色の面・パネル |
| Primary | #1F3F74 | 藍。見出し・大きな平面ブロック・軌道線 |
| Accent | #C8442C | 朱。太陽円盤・強調する一点の数字 |
| Secondary accent | #D9A33A | 黄土。帯・年代バッジ・補助の強調 |
| Body text | #22262E | 本文 |
| Secondary text | #5E5A52 | キャプション・出典・注記 |
| Divider | #C7B99D | 罫線・細線 |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: vintage-poster
- **Image Rendering Behavior**: 1960年代の旅行ポスターのような簡略化した平面ブロックで描き、輪郭は太く手の気配を残し、角は丸い。藍・朱・黄土・クリームの限られた平面色の上に網点を10〜15%重ね、わずかな版ずれと紙の粒子で印刷の古さを出す。写実ではなく、山・太陽・高架橋・列車を記号的な形に還元し、影ではなく形の重なりで奥行きを作る。文字・数字・企業ロゴ・車体の社章は一切描かない。
- **Visual**: 富士山・朝日・高架橋・軌道・ガイドウェイを記号化した平面ポスター画
- **Mood**: 懐かしく前向き — 1964年の観光ポスターを60年後に新しく刷り直したような温かさ

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 落ち着いた明朝の見出し | Yu Mincho | Times New Roman | serif |
| Body | 読みやすいゴシック | Yu Gothic | Segoe UI | sans-serif |
| Display | ポスター級の極太数字 | Yu Gothic | Arial Black | sans-serif |
| Kpi | 数字ブロックの極太数字 | Yu Gothic | Arial Black | sans-serif |

- **Title stack**: 'Times New Roman', 'Yu Mincho', serif
- **Body stack**: 'Segoe UI', 'Yu Gothic', sans-serif
- **Display stack**: 'Arial Black', 'Yu Gothic', sans-serif
- **Kpi stack**: 'Arial Black', 'Yu Gothic', sans-serif
- **Role rationale**: Display は巨大な数字(4:00・395・0 など)を複数ページで繰り返すため、見出しの明朝から離れた極太ライニング数字を別ファミリーとして固定する。Kpi(64px)は複数ページの数字ブロックで繰り返すため、同じ極太ライニング数字の系統に揃える。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 28 |
| Title | 48 |
| Subtitle | 34 |
| Annotation | 22 |
| Lead | 32 |
| Footnote | 16 |
| Cover title | 96 |
| Display | 132 |
| Kpi | 64 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 左上の判断文の見出し → 一つの主役(巨大数字・図・画像) → 補足と出典の順に視線が流れる
- **Composition tendency**: 大きな平面ブロックと太陽円盤で紙面を二つか三つのゾーンに分け、主役は一点に集中させる。均等なカードの格子は避ける
- **Cross-page continuity**: 藍の軌道線(太い横帯)を毎ページどこかに置き、役割(年表の軸・基線・区切り)を変えて繰り返す。出典は各ページ下部の細い行に置く
- **Spacing posture**: presentation 読みで余白は広め。dense ページも一画面一主張
- **Spacing anchors**: page margin 64px / block gap 32px / column gutter 40px / corner radius 16px / body leading 1.5

## VI. Icon Usage Specification

- **Primary bundled library**: chunk-filled

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/chunk-filled/train.svg | |
| icons/chunk-filled/clock.svg | |
| icons/chunk-filled/stopwatch.svg | |
| icons/chunk-filled/gauge-high.svg | |
| icons/chunk-filled/users.svg | |
| icons/chunk-filled/calendar.svg | |
| icons/chunk-filled/shield-check.svg | |
| icons/chunk-filled/bolt.svg | |
| icons/chunk-filled/waveform.svg | |
| icons/chunk-filled/bridge.svg | |
| icons/chunk-filled/mountains.svg | |
| icons/chunk-filled/magnet.svg | |
| icons/chunk-filled/route.svg | |
| icons/chunk-filled/map-pin.svg | |
| icons/chunk-filled/leaf.svg | |
| icons/chunk-filled/link.svg | |
| icons/chunk-filled/chair.svg | |
| icons/chunk-filled/power.svg | |
| icons/chunk-filled/signal.svg | |
| icons/chunk-filled/wrench.svg | |
| icons/chunk-filled/flag.svg | |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | chart | horizontal_bar_chart | 東京〜大阪の所要時間を在来線・開業時・翌年・現在で比べる |
| P06 | table | record_table | 7つの型式を営業開始・最高速度・技術の要点で並べる |
| P09 | chart | column_chart | 輸送人キロの年度推移(2002〜2025年度)を示す |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_poster.jpg | 2752×1536 | 16:9 | 表紙の主視覚:60年の出発点を一枚のポスター画で示す | Hero illustration | 右側の大きなアーチ窓に切り抜き、左の無地のクリーム面に題字を置く(画像の上に題字を載せない) | adaptive | ai | Generated | 朝日を背にした富士山の前を、白い流線形の高速列車が長い高架橋を渡る。列車は右下へ向かい、画面左1/3は空と紙の余白。列車は特定の型式を再現しない記号的な形 | none | hero_page |
| era_1964.jpg | 1856×2304 | 4:5 | P04:開業の朝の空気を伝える | Illustration | 縦長の窓として右側に置き、角丸の枠で切り抜く | adaptive | ai | Generated | 1960年代のプラットホームで、旗を振って見送る人々の後ろ姿と、丸い先頭の白と青の列車が朝の光の中で出発を待つ。人物は顔を描かない簡略化したシルエット | none | local |
| rails_dusk.png | 2752×1536 | 16:9 | 安全章の背景の元画像(派生の親) | Source | 直接は置かない | adaptive | ai | Generated | 夕暮れに遠くへ収束する複線の軌道と架線柱、線路脇の小さな機器箱。人物・列車なし、静かで整然 | none | local |
| rails_dusk_duotone.jpg | 1600×900 | 16:9 | P11:「死傷事故ゼロ」の背景として紙面全体を静かに支える | Background | 全面の背景に敷き、左側に藍の平面を重ねて数字の地を作る | adaptive | ai | Generated | Derived from rails_dusk.png; treatment=duotone+fit; 藍 #1F3F74 と クリーム #F3ECDD の二色化、1600×900 に縮小 | none | local |
| guideway_dawn.jpg | 2752×1536 | 16:9 | P14:次の60年(超電導リニア)への視線を作る | Illustration | 朱の太陽円盤の形に丸く切り抜き、右側に大きく置く | adaptive | ai | Generated | 夜明けの山あいを貫くU字形のコンクリートのガイドウェイがトンネルへ吸い込まれる。車両は描かないか、形の定まらない白い光の筋だけ。ロゴ・文字なし | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 各ページの判断文を話し言葉で補い、数字は出典名と参照年を添えて読み上げる。スライドにない数字は研究ノート(sources/tokaido_shinkansen_60_research.md)の事実IDに限る。日本語で書く
- **Total duration**: 約25分(1ページ平均1分40秒)
- **Notes style**: conversational(一般聴衆への語りかけ、問いかけで次ページへ橋渡し)
- **Presentation purpose**: 60年の歩みを検証できる数字で振り返り、速さ・本数・定時性・安全の積み上げの仕組みを示し、次の60年(中央新幹線)を公表情報どおりに位置づける

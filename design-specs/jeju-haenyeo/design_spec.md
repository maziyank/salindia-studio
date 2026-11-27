<!-- ppt-master-schema: design-spec/v1 -->
# 제주 해녀 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | jeju_haenyeo_ko_20260911 |
| Canvas Format | ppt169 (PPT 16:9, 1280×720) |
| Page Count | 15 |
| Primary Language | ko-KR |
| Target Audience | 제주 해녀에 관심 있는 일반 시민(공개 강연 청중). "해녀=제주의 잠수하는 여성" 정도의 사전 지식을 가진 사람들 |
| Communication Intent | 먼저 물질이 어떤 방식과 규칙으로 조직되는지 설명하고, 그 공동체 방식이 왜 유네스코·FAO 유산으로 평가받았는지 보여 준 뒤, 해녀 수와 연령 구성의 변화로 전승 위기를 드러내고 무엇이 전승을 가능하게 하는지 생각하게 한다 |
| Desired Audience Outcome | 청중이 물질의 조직(상군·중군·하군, 불턱, 어촌계)과 두 국제 유산 지정의 이유를 자기 말로 설명할 수 있고, 1970년 14,143명 → 2025년 2,371명, 60세 이상 4.6% → 90.1%라는 변화가 무엇을 뜻하는지 이해한다 |
| Core Message / Ask / Action | 제주 해녀는 '숨'이라는 개인 기량을 공동체의 규칙으로 묶어 바다밭을 함께 가꾸어 온 체계이며, 그 체계를 이어 갈 사람이 빠르게 줄고 있다 |
| Delivery Context | 주: 발표자가 진행하는 일반 시민 대상 공개 강연(약 35분). 부: 강연 후 청중이 다시 열어 보는 공유 자료 |
| Artifact Afterlife | 강연 후 배포·열람. 수치마다 출처와 연도를 쪽에 남기고, 마지막 쪽에서 주요 출처로 바로 이동할 수 있게 한다 |
| Reading Mode | balanced |
| Content Strategy | 지정 없음 — 균형(balanced) 기본값: 조사 자료의 사실을 모두 유지하되 서사 순서로 재구성; 자체 틀은 「정리」로 표시 |
| Design Style | 방향 A「수심의 기록」 — custom mode(narrative 기반) + custom visual style(editorial 기반) + custom 이미지 렌더링(screen-print 기반) |
| AI Image Acquisition Path | auto (위임 확인에서 추천값 채택; Path A `image_gen.py --manifest` 우선) |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy (위임 확인, 추천값 true) |
| Custom Animations | enabled — final Stage-2 proactive policy (위임 확인, 추천값 true: 인접 쪽 Morph 두 쌍과 주인공 요소 입장이 순서를 설명함) |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-09-11 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 좌우 64, 위 56, 아래 48 |
| Content Area | x 64–1216, y 56–672 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: narrative
- **Mode Behavior**: 상황(물질의 모습) → 구조(무리·기량·불턱·바다밭) → 평가(여섯 번의 지정과 그 이유) → 긴장(인원과 연령 구성의 변화, 들어오는 사람과 떠나는 사람) → 실마리(전승 장치) → 정리로 흐르는 서사. 모든 쪽 제목은 판단 문장이고 한 쪽에 한 주장만 세운다. 수치 쪽은 출처와 연도를 쪽 아래에 적고, 조사 자료에 없는 자체 틀은 「정리」로 표시한다.
- **Visual style**: custom
- **Visual Style References**: editorial
- **Visual Style Behavior**: 소금기 밴 종이색 바탕 위의 잡지형 편집. 가는 수평 규칙선과 비대칭 2단, 세리프 제목 × 산세리프 본문, 제목 위 킥커와 쪽 아래 출처 줄이 위계를 만든다. 교차 모티프는 '수면선' — 쪽마다 한 줄의 수평선이 수면 역할을 하고, 수심이 의미를 가질 때만 0·5·10m 눈금이 붙는다. 이미지는 실크스크린 판화처럼 평면 색 블록으로 들어와 원형·아치 창이나 넓은 띠로 잘리고, 데이터 쪽은 장식 없이 넓은 여백과 강조 숫자 하나로 선다. 그림자는 쓰지 않고, 표지·장 전환·마무리는 짙은 바다색 전면 면으로 반전한다.
- **Theme**: 수심의 기록 — 바다의 단면, 판화 같은 해녀 이미지, 신문 지면 같은 사실 기록
- **Tone**: 담담하고 단단함. 감상보다 사실이 먼저 말하고, 사람의 무게는 이미지와 숫자 하나가 짊어진다

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F4F1EA | 소금기 종이색 본문 바탕 |
| Secondary background | #E3ECEB | 옅은 물빛 면, 표·보조 영역 |
| Primary | #123B4A | 짙은 바다색: 제목, 반전 면, 차트 주 계열 |
| Accent | #E0662B | 테왁 주황: 강조 숫자 하나, 킥커 규칙선, 핵심 막대 |
| Secondary accent | #3F8C8A | 옥빛 물: 보조 계열, 수심 눈금, 아이콘 |
| Body text | #1E2A30 | 본문 |
| Secondary text | #5B6970 | 캡션, 출처 줄, 주석 |
| Divider | #C9CFCC | 규칙선, 표 테두리, 헤어라인 |

### AI Image Strategy

- **Image Rendering**: custom
- **Image Rendering References**: screen-print
- **Image Rendering Behavior**: 실크스크린 포스터 판화. 덱 색 역할(짙은 바다·옥빛 물·테왁 주황·소금 종이) 안에서 3~4색 평면 블록만 쓰고, 물의 명암이 바뀌는 곳에 하프톤 점을 두며, 판이 1~2px 어긋난 흔적과 종이결 15%를 남긴다. 인물은 스텐실로 오린 실루엣으로만 그려 얼굴 세부가 없고, 그림 안에 글자는 없다.
- **Visual**: 스텐실 실루엣 해녀 + 평면 색 블록 바다 + 하프톤 물빛
- **Mood**: 담담하고 단단한 1960년대 문화 포스터 — 해양 박물관 기획전 포스터를 떠올리게 하는 분위기

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 한글 명조 계열 세리프, 기록물 같은 무게 | Batang | Cambria | serif |
| Body | 중립 한글 고딕, 투사 가독성 | Malgun Gothic | Segoe UI | sans-serif |

- **Title stack**: 'Cambria', 'Batang', serif
- **Body stack**: 'Segoe UI', 'Malgun Gothic', sans-serif
- **Role rationale**: 표지 제목(cover_title)·강조 숫자(display)·리드(lead)·출처 줄(footnote)은 크기만 다른 반복 역할이며 가족은 Title/Body를 따른다.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 40 |
| Subtitle | 30 |
| Annotation | 18 |
| Lead | 28 |
| Footnote | 14 |
| Cover title | 96 |
| Display | 96 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 킥커 → 판단 문장 제목 → 리드 한 줄 → 증거(이미지·차트·표) → 쪽 아래 출처 줄
- **Composition tendency**: 비대칭 2단(좁은 글 단 + 넓은 증거 단)과 전면 반전 면의 교대; 한 쪽에 초점 하나
- **Cross-page continuity**: 수면선 모티프(수평 헤어라인)가 모든 본문 쪽에 있고, 물질 쪽에서만 수심 눈금이 붙는다. 킥커는 장 번호 + 장 이름. 출처 줄 형식은 「출처: 기관명, 자료명(연도)」로 고정
- **Spacing posture**: 쪽 리듬에 따라 가변 — dense 쪽은 2단 정보 밀도, breathing 쪽은 넓은 여백
- **Spacing anchors**: 쪽 여백 64 · 블록 간격 32 · 단 사이 40 · 모서리 반경 0 · 본문 행간 36

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/ripple.svg | |
| icons/tabler-outline/fish.svg | |
| icons/tabler-outline/swimming.svg | |
| icons/tabler-outline/lungs.svg | |
| icons/tabler-outline/clock.svg | |
| icons/tabler-outline/calendar.svg | |
| icons/tabler-outline/users-group.svg | |
| icons/tabler-outline/flame.svg | |
| icons/tabler-outline/school.svg | |
| icons/tabler-outline/currency-won.svg | |
| icons/tabler-outline/certificate.svg | |
| icons/tabler-outline/world.svg | |
| icons/tabler-outline/map-pin.svg | |
| icons/tabler-outline/external-link.svg | |
| icons/tabler-outline/ruler-measure.svg | |
| icons/tabler-outline/heart-handshake.svg | |
| icons/tabler-outline/basket.svg | |
| icons/tabler-outline/book.svg | |
| icons/tabler-outline/hourglass.svg | |
| icons/tabler-outline/user-plus.svg | |
| icons/tabler-outline/user-minus.svg | |
| icons/tabler-outline/trending-down.svg | |
| icons/tabler-outline/plant.svg | |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P08 | table | record_table | 여섯 번의 유산 지정을 연도·대상·지정·범위 레코드로 나열 |
| P10 | chart | column_chart | 1970~2025년 현직 해녀 수의 감소를 연도별 막대로 비교 |
| P11 | chart | stacked_bar_chart | 1970년과 2025년의 연령 구성 비율(%)을 두 막대로 대비 |
| P12 | chart | column_chart | 2015~2022년 신규 해녀 어촌계 가입 인원을 연도별로 제시 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cover_surface.jpg | 2752×1536 | 16:9 | 표지 훅: 막 떠오른 해녀와 주황 테왁 | Illustration | 전면 배경; 왼쪽 빈 수면 위에 제목, 제목 쪽에 그라데이션 스크림 | adaptive | ai | Generated | 수면 높이에서 본 넓은 바다. 오른쪽 1/3에 주황 테왁을 붙잡고 막 떠오른 해녀 한 명(뒷모습 실루엣, 얼굴 식별 불가). 왼쪽 60%는 잔잔한 수면과 하늘만 있는 조용한 영역 | none | hero_page |
| cover_surface_dim.jpg | 2752×1536 | 16:9 | 마무리 쪽의 표지 회상 띠 | Illustration | 쪽 한쪽의 좁은 세로 띠로 표지 장면을 다시 부름 | adaptive | ai | Generated | Derived from cover_surface.jpg; treatment=grayscale+brightness; | none | local |
| dive_column.jpg | 1792×2400 | 3:4 | 물질의 수직 단면: 수면에서 바닥까지 | Illustration | 오른쪽 세로 창(윗단 아치), 수심 눈금과 겹쳐 수심을 읽게 함; 다음 쪽에서 같은 장면이 이동(Morph) | adaptive | ai | Generated | 수면(상단 12%)부터 현무암 바닥(하단 15%)까지 한 화면의 수직 수중 단면. 머리를 아래로 두고 내려가는 해녀 한 명(실루엣), 위에서 내려오는 빛줄기, 바닥의 전복·소라·미역, 수면에 뜬 주황 테왁 | none | local |
| bulteok_ring.png | 2048×2048 | 1:1 | 불턱 원본 | Source | 원본은 쪽에 놓지 않고 파생본만 사용 | adaptive | ai | Generated | 위에서 내려다본 둥근 현무암 돌담 불턱. 가운데 작은 모닥불, 둘러앉은 해녀 네다섯 명(정수리와 어깨만, 얼굴 없음), 둘레의 검은 바위 해안 | none | local |
| bulteok_ring_duo.jpg | 2048×2048 | 1:1 | 불턱: 공동체 공간 | Illustration | 원형 창으로 잘라 둘레에 기능 세 가지를 배치 | adaptive | ai | Generated | Derived from bulteok_ring.png; treatment=duotone; | none | local |
| sea_field.jpg | 2752×1536 | 16:9 | 바다밭: 함께 가꾸는 공유지 | Illustration | 쪽 아래 절반을 채우는 넓은 해저 띠, 위쪽 조용한 물빛 위에 글 | adaptive | ai | Generated | 사람이 없는 얕은 해저 바다밭. 현무암 바위, 미역·감태 숲, 전복·소라·성게. 위쪽 40%는 물빛만 있는 조용한 영역 | none | local |
| two_divers.jpg | 2752×1536 | 16:9 | 전승: 나이 든 해녀와 젊은 해녀 | Illustration | 쪽 왼쪽 절반을 채우는 편집 크롭, 오른쪽에 글 단 | adaptive | ai | Generated | 현무암 해안에서 바다로 걸어 들어가는 두 해녀의 뒷모습. 한 명은 등이 굽은 노년, 한 명은 곧은 자세의 젊은 해녀, 둘 다 테왁을 듦. 얼굴은 보이지 않음 | none | local |

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 쪽마다 화면의 판단 문장을 먼저 말하고, 화면의 수치는 출처 기관과 연도를 함께 말한다. 조사 자료(`sources/jeju_haenyeo_ko_research.md`)에 없는 사실은 추가하지 않는다. 계산값은 "계산하면"으로 밝힌다
- **Total duration**: 약 35분 (쪽당 2~3분)
- **Notes style**: 대화체 — 청중에게 질문을 던지고 앞 쪽과 다리를 놓는 강연 말투
- **Presentation purpose**: 물질의 조직을 설명하고, 유산 지정의 이유를 보여 준 뒤, 인원·연령 변화로 전승 과제를 드러낸다

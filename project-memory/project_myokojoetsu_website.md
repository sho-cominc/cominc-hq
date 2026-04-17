---
name: myokojoetsu.com regional media site
description: 妙高と高田を宣伝する地域メディアサイト。ComInc. とは完全に切り離し。
type: project
---

# myokojoetsu.com — Design Brief

## 1. コンセプト

**一言で**: 妙高と高田（上越）を紹介する英語メディアサイト。ComInc. とは無関係。

### ポジショニング

| 項目 | myokojoetsu.com | cominc.co | joetsuexplorer.com |
|------|----------------|-----------|-------------------|
| 主語 | 場所（妙高・高田） | Sho（人） | 上越エリア（休止中） |
| 目的 | 地域の宣伝・情報発信 | ガイド・宿泊の販売 | エリアガイド |
| 視点 | 第三者（メディア） | 一人称（Sho） | — |
| マネタイズ | 広告収入（将来） | サービス売上 | — |
| ComInc. ブランド | 一切なし | 全面 | サブブランド |
| ターゲット | 英語圏の旅行計画者 | 英語圏のゲスト | — |

### なぜ別サイトにするか
- ComInc. は「Sho という人間」を売る。myokojoetsu.com は「場所そのもの」を売る。混ぜると両方ぼやける
- SEO で情報検索クエリ（"things to do in Joetsu"、"Myoko restaurants"）を拾う受け皿。cominc.co ではこの種の純粋な情報コンテンツは浮く
- 将来的に広告マネタイズする場合、事業サイトと分離されている必要がある

---

## 2. デザイン方針

### 出発点（Sho のスクリーンショット）
Sho が以前作った myokojoetsu.com のモックアップ：
- **カラー**: beige/warm cream 背景、dark green-black テキスト、powder blue アクセント
- **タイポ**: Serif italic ヘッドライン、editorial magazine 風
- **レイアウト**: たっぷりの余白、写真とテキストの交互配置
- **ヘッダー**: "myokojoetsu.com" テキストロゴ + SNS アイコン + 予約ボタン（※予約は削除）
- **ヒーロー**: "Shop / Eat Myoko / Joetsu" — カテゴリベースの分岐
- **3カラム**: "Shoppaholic? / or both? / Food explorer?" — ペルソナ分岐

### カラーパレット

```
背景系:
  --cream:       #EDE8DF    ← メイン背景（スクショの beige）
  --cream-light: #F5F1EB    ← セクション交互
  --white:       #FAFAF7    ← カード背景

テキスト系:
  --ink:         #2A3A2A    ← メインテキスト（dark green-black、スクショ準拠）
  --ink-light:   #5A6A5A    ← サブテキスト
  --ink-faint:   #8A9A8A    ← キャプション等

アクセント:
  --blue:        #B8D4E3    ← powder blue（スクショ中央カードの色）
  --brown:       #8B7355    ← warm brown（仕切り線、ボーダー）
  --green:       #4A6A4A    ← 妙高の緑（CTA、リンク）
```

### タイポグラフィ

| 用途 | フォント | ウェイト | スタイル |
|------|---------|---------|---------|
| ヘッドライン（EN） | Cormorant Garamond | 300, 400 | italic |
| ヘッドライン（JP） | Noto Serif JP | 400 | normal |
| ボディ（EN） | Inter | 300, 400 | normal |
| ボディ（JP） | Noto Sans JP | 300, 400 | normal |
| ナビ / ラベル | Inter | 500 | uppercase, letter-spacing: 0.15em |

**注意**: cominc.co も Cormorant Garamond を使っているが、cominc.co は sakura/dark テーマ、myokojoetsu.com は beige/cream テーマ。同じフォントでも色とトーンで別サイトに見える。

### レイアウト原則
1. **Editorial magazine 型**: 大きなタイポグラフィ + 余白 + 写真。ブログ風ではない
2. **Mobile-first**: 旅行者はスマホで検索する。768px ブレークポイント
3. **グリッド**: デスクトップ 4 列 / タブレット 2 列 / モバイル 1 列
4. **写真**: 実写を前提とするが、プロトタイプは gradient placeholder で代替
5. **アニメーション**: scroll reveal（opacity + translateY）のみ。重い装飾なし

### やらないこと（cominc.co との差別化）
- ❌ Sho の写真・プロフィール
- ❌ "Cultural Translation" の文言
- ❌ 予約・問い合わせフォーム
- ❌ ComInc. ロゴ・リンク
- ❌ 価格表・チャーター料金
- ❌ ダークモード / 夜桜テーマ

---

## 3. コンテンツ設計

### サイト構成（初期）

```
myokojoetsu.com
├── Header
│   ├── "myokojoetsu.com" テキストロゴ（Cormorant italic）
│   └── SNS アイコン（Instagram, X）
│
├── Hero
│   ├── "Myoko / Joetsu" or "Myoko & Takada"
│   ├── サブコピー: "Snow country's best kept secret."
│   └── スクロールキュー
│
├── Intro（1段落）
│   └── 妙高と高田がどんな場所か、2-3 文で
│
├── カテゴリ（メインコンテンツ）
│   ├── Shop — 高田の商店街、雁木通り、地元クラフト・陶器
│   ├── Eat  — 地元グルメ（へぎそば、日本酒、海鮮、B級グルメ）
│   ├── See  — 高田城の桜、妙高の山、スキー、温泉、歴史
│   └── Stay — 温泉宿、旅館、エリア紹介（特定施設の宣伝ではない）
│
├── 四季セクション
│   ├── Winter — パウダースノー、スキー、温泉、冬の日本海
│   ├── Spring — 高田城の桜（日本三大夜桜）、田植え
│   ├── Summer — 登山、祇園祭、避暑
│   └── Autumn — 紅葉、新米、新酒、収穫祭
│
├── Access
│   ├── 東京から: 北陸新幹線 → 上越妙高駅（約2時間）
│   ├── 成田/羽田から: 新幹線経由ルート
│   └── 地図（将来的に Google Maps embed）
│
└── Footer
    ├── "myokojoetsu.com" + copyright
    └── SNS リンク
```

### トーン & ボイス
- **視点**: 第三者。"we" でも "I" でもない。場所が主語
- **言語**: 英語メイン。日本語は固有名詞と雰囲気のために併記（例: 雁木 / gangi）
- **具体性**: "amazing food" ではなく "hand-rolled soba from buckwheat harvested in October"
- **感覚的**: 匂い、音、触感を含める（"the cedar-scented air of a 200-year-old warehouse"）
- **比較しない**: "better than Niseko" などの攻撃的比較はしない。静かに存在を示す

### SEO キーワード戦略（Cat 観点）

**一次キーワード（英語）**:
- "Myoko Kogen travel guide"
- "Joetsu things to do"
- "Takada castle cherry blossoms"
- "Myoko restaurants"
- "Joetsu shopping"
- "snow country Japan travel"
- "Niigata day trip from Tokyo"

**二次キーワード（日英混合）**:
- "gangi street Takada"
- "hegi soba Joetsu"
- "Myoko onsen guide"
- "Joetsu sake brewery"
- "Takada history walk"

**cominc.co との棲み分け**: myokojoetsu.com は純粋な情報クエリ（"things to do"、"where to eat"）を拾う。cominc.co はサービスクエリ（"private guide Myoko"、"kominka stay"）を拾う。カニバリゼーションなし。

---

## 4. 技術方針

### 初期実装
- 生 HTML + inline CSS（cominc-website と同じアプローチ）
- Google Fonts CDN で読み込み
- JS は scroll reveal のみ（IntersectionObserver）
- ビルドツールなし

### ディレクトリ
```
cominc-hq/
├── cominc-website/          ← cominc.co（既存）
├── myokojoetsu-website/     ← myokojoetsu.com（新規）
│   └── index.html
```

### デプロイ（将来）
- Cloudflare Pages（cominc.co と同じインフラ）
- ドメイン: myokojoetsu.com（Sho が保有しているか要確認）

### 将来の拡張パス
1. サブページ化（/shop, /eat, /see, /stay を個別ページに）
2. ブログ / 記事機能（広告マネタイズの基盤）
3. Astro + Notion CMS 移行（記事数が増えたら）
4. 広告枠（Google AdSense 等）
5. 地図連携（Google Maps embed）
6. 日本語版（/ja/ サブパス）

---

## 5. スクショからの修正点

元のスクショから**変える**ポイント：

| スクショの要素 | 修正 | 理由 |
|-------------|------|------|
| "予約" ボタン | 削除 | サービス販売しない |
| "Fullday charter 300 USD" 料金表 | 削除 | マネタイズはガイド業ではない |
| LinkedIn アイコン | 削除（Instagram + X のみ） | 地域メディアに LinkedIn は不要 |
| 3カラムの "or both?" + 料金 | カテゴリカードに変更 | 料金ではなく場所紹介 |
| "Shoppaholic?" コピー | より落ち着いたコピーに | editorial トーンに合わせる |

元のスクショから**残す**ポイント：

| 要素 | 理由 |
|------|------|
| beige 背景 + dark text | ブランドトーンとして成立している |
| serif italic ヘッドライン | editorial magazine 感の核 |
| "myokojoetsu.com" テキストロゴ | ドメイン = ブランド名 |
| カテゴリベースの構成（Shop / Eat） | ユーザーのインテントに沿った IA |
| たっぷりの余白 | 「雪国の余白」的な美学 |

---

## 6. 次のアクション

- [ ] ドメイン myokojoetsu.com の所有状況を確認（Sho）
- [ ] HTML プロトタイプを `myokojoetsu-website/index.html` に実装（次セッション）
- [ ] 写真素材の方針を決める（Sho の手持ち写真 / フリー素材 / 撮影計画）
- [ ] joetsuexplorer.com との関係を整理（統合 / 共存 / 引退）

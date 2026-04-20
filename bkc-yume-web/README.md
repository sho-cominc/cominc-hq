# bkc-yume-web

BLACK KITCHEN CAR ゆめ の公式ウェブサイト（プロトタイプ）。

- Astro 4 + Tailwind + TypeScript
- 日本語 / 英語（`/ja/` `/en/` サブパス）
- Cloudflare Pages にデプロイ（GitHub自動連携）

## セットアップ

```bash
cd bkc-yume-web
npm install
npm run dev
# http://localhost:4321/ja/
```

## ビルド

```bash
npm run build
# → dist/
```

## コンテンツ更新

### 次回の出店を更新する

`src/data/next-event.json` を編集し、`main` に push するだけで Cloudflare Pages が自動で再デプロイします（〜30秒）。

```json
{
  "date": "2026-05-03",
  "venue_ja": "会場名（日本語）",
  "venue_en": "Venue name (English)",
  "address_ja": "住所（日本語）",
  "address_en": "Address (English)",
  "startTime": "10:00",
  "endTime": "16:00",
  "mapsUrl": "https://...",
  "note_ja": "補足",
  "note_en": "Note"
}
```

### メニューを更新する

`src/data/menu.json` を編集。各アイテムは日英併記（`name_ja` / `name_en`）。写真ファイルは `public/images/` に置いて `image` パスで参照。

### コピーテキストを変える

サイト全体の文言は `src/i18n/ja.json` と `src/i18n/en.json` に集約されています。ハードコードされた日本語・英語は基本ありません（Cat が一元管理できるように）。

## Instagram 埋め込み

`InstagramFeed.astro` は Behold.so 連携前提です。

1. [Behold.so](https://behold.so/) で無料アカウントを作成し、Instagram `@bkc_yu____me` を連携
2. 発行されるウィジェットIDを取得
3. `src/components/InstagramFeed.astro` を使用している各ページで `beholdId="..."` を渡す
4. 未設定時は自動で Instagram へのCTAカードにフォールバック

## ディレクトリ

```
bkc-yume-web/
├── public/               # 静的アセット（favicon、プレースホルダ画像）
├── src/
│   ├── components/       # 共通UIパーツ
│   │   └── pages/        # 各ページの本体（locale を受け取る）
│   ├── data/             # menu.json, next-event.json（更新対象）
│   ├── i18n/             # ja.json, en.json（全コピー）
│   ├── layouts/          # Base.astro（meta / hreflang / フォント）
│   ├── pages/
│   │   ├── ja/ en/       # ロケールごとのルート
│   │   └── index.astro   # `/` → `/ja/` リダイレクト
│   ├── styles/global.css # Tailwind + デザイントークン
│   └── utils/i18n.ts     # t() ヘルパ / SNSリンク
├── astro.config.mjs
├── tailwind.config.mjs
└── package.json
```

## デプロイ（Cloudflare Pages）

- Framework preset: **Astro**
- Build command: `npm run build`
- Build output directory: `dist`
- Node version: `20`
- 仮公開URL: `https://bkc-yume-web.pages.dev`

独自ドメインは Cloudflare Pages ダッシュボードから後日追加可能。

## TODO（Phase 2）

- [ ] 独自ドメイン接続（`bkc-yume.com` 等、オーナー決定後）
- [ ] Behold.so ウィジェットID反映
- [ ] 正式ロゴ差し替え（Clare 制作）
- [ ] 新規撮影写真への差し替え
- [ ] Google Calendar 連携による次回出店の自動更新
- [ ] Contact のメールアドレス確定

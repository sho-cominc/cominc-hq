---
name: myokojoetsu.com セッション開始プロンプト
description: Claude Code で myokojoetsu.com の作業を始めるときに貼り付ける
type: reference
---

# myokojoetsu.com — セッション開始ガイド

---

## ⚠️ 事前準備（初回のみ）

### GitHub リポへのアクセスを許可する

Claude Code (Web) で `myokojoetsu.com` リポに直接プッシュするには、
GitHub 連携の許可リポに追加する必要がある。

**claude.ai/code の場合:**
1. セッション開始画面で「Repository」を選ぶとき、`sho-cominc/myokojoetsu.com` を選択
2. もしリストに出ない場合 → GitHub App の設定画面で「Repository access」に追加:
   - GitHub → Settings → Applications → "Claude Code" → Configure → Repository access
   - `sho-cominc/myokojoetsu.com` を追加

**ローカル CLI の場合:**
- `claude` コマンドはローカル git を使うので、普通に clone してあればOK

---

## 📋 コピペ用プロンプト

以下をセッション冒頭に貼り付ける：

```
■ プロジェクト: myokojoetsu.com（地域メディアサイト）
■ リポジトリ:
  - ソース: sho-cominc/cominc-hq（myokojoetsu-website/ ディレクトリ）
  - デプロイ: sho-cominc/myokojoetsu.com（Cloudflare Pages に接続済み）
  - ※ 両方のリポにアクセスできる状態で作業すること

■ サイト概要
妙高と高田（上越）を紹介する英語 editorial メディアサイト。
ComInc.（cominc.co）とは完全に切り離し。第三者視点。Sho の個人宣伝なし。

■ 技術スタック
- 生 HTML + inline CSS/JS（ビルドツールなし）
- Google Fonts: Cormorant Garamond (italic), Inter, Noto Serif/Sans JP
- Cloudflare Pages デプロイ（sho-cominc/myokojoetsu.com リポから自動）

■ デザインルール
- カラー: --cream #EDE8DF / --ink #2A3A2A / --blue #B8D4E3 / --brown #8B7355 / --green #4A6A4A
- タイポ: Cormorant Garamond italic (見出し) + Inter 300 (本文)
- トーン: editorial magazine。"amazing food" ではなく "hand-rolled soba from buckwheat harvested in October"
- 視点: 第三者。"we" "I" なし。場所が主語
- ComInc. / Sho のブランディングなし（WIP セクションのみ例外）
- 比較しない（"better than Niseko" などNG）

■ 現在のページ構成（2026-06-07 時点、全ページ完成済み × 3言語）
  /            — EN ランディングページ + WIP notice
  /winter.html — 冬  /spring.html — 春  /summer.html — 夏  /autumn.html — 秋
  /see.html    — 観  /shop.html   — 買  /eat.html    — 食  /stay.html   — 泊
  /zh-Hant/    — 繁体字中国語版（全9ページ、台湾・香港向け）
  /ja/         — 日本語版（全9ページ）
  ※ 全27ページに OGP + hreflang + 3言語切替ナビ実装済み

■ 重要な注意点
- 古民家は「中央高田の城下町」にある（田舎の農家ではない）。城まで徒歩5分、雁木パブ通り10分、スキー場25分
- stay.html の古民家は「カテゴリ」として紹介。Sho の具体的な物件宣伝はしない
- デプロイは myokojoetsu.com リポにプッシュすれば Cloudflare が自動で反映

■ リサーチ資料
  myokojoetsu-website/PAGES-RESEARCH.md — 全ページのリサーチ結果
  myokojoetsu-website/SITEMAP.md — サイト構成と meta descriptions
  project-memory/project_myokojoetsu_website.md — デザインブリーフ
  project-memory/project_myokojoetsu_ec.md — EC戦略（STORES → Shopify）

■ エージェント（必要に応じて）
  @Webber — ディレクション  @Clare — デザイン  @Dev — コーディング
  @Cat — コピー・マーケ  @Hana — レビュー  @Yuri — UX/UI
```

---

## 🔧 使い方

### パターン A: claude.ai/code（Web）
1. claude.ai/code を開く
2. リポに `sho-cominc/cominc-hq` を選択（作業ファイルがここにある）
3. 上のプロンプトを貼り付け
4. 作業内容を続けて書く

### パターン B: ローカル CLI
1. `cd cominc-hq`
2. `claude` で起動
3. 上のプロンプトを貼り付け
4. 作業内容を続けて書く

### デプロイ手順（ファイル変更後）
cominc-hq で作業 → myokojoetsu.com リポにコピー → push で自動デプロイ

**Web セッション（両リポにアクセスある場合）:**
GitHub MCP の push_files でそのまま myokojoetsu.com リポにプッシュ可能。

**ローカル:**
```powershell
copy myokojoetsu-website\*.html ..\myokojoetsu.com\
cd ..\myokojoetsu.com
git add . && git commit -m "Update pages" && git push
```

---

## 📌 次にやること（TODO）
- [ ] 写真素材の追加（gradient placeholder → 実写） — ストック素材不足、Sho 自撮りが主軸。Wikimedia の高田城桜・妙高山は暫定利用可
- [x] ナビのリンクを各ページに接続 ✅ 2026-06-07
- [ ] EC ショップ連携（STORES or Shopify、summer 2026 予定）
- [x] 日本語版 /ja/ 全9ページ完成 ✅ 2026-06-07
- [x] 繁体字中国語版 /zh-Hant/ 全9ページ完成 ✅ 2026-06-07
- [x] 3言語間 hreflang + 言語切替ナビ ✅ 2026-06-07
- [ ] Google Analytics / Search Console 設定 — トラッキング ID 待ち
- [x] OGP + Twitter Card メタタグ追加（全27ページ） ✅ 2026-06-07
- [ ] OGP 画像（og:image）— 実写写真待ち

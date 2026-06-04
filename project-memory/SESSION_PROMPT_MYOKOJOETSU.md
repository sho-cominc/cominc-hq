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

■ 現在のページ構成（2026-06-04 時点、全ページ完成済み）
  index.html   — ランディングページ + WIP notice (@shoxkiwi Instagram)
  winter.html  — 冬: パウダー、温泉、新酒、かんずり、静寂
  spring.html  — 春: 高田城桜、星峠棚田、岩の原葡萄園、苗名滝、水芭蕉
  summer.html  — 夏: 火打山、蓮、祇園祭、妙高山、海、雁木
  autumn.html  — 秋: 紅葉、新米、ひやおろし、寒ブリ、いもり池
  see.html     — 観: 高田城、妙高山、火打山、苗名滝、春日山城、雁木
  shop.html    — 買: かんずり、地酒、蓮茶、和菓子、ビール、雁木商店街
  eat.html     — 食: へぎそば、雪むろ酒かすラーメン、海鮮、酒文化、山菜、コシヒカリ
  stay.html    — 泊: 妙高七湯、古民家（カテゴリ）、赤倉観光ホテル、燕温泉野天風呂、ロッテアライ、山小屋

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
- [ ] 写真素材の追加（gradient placeholder → 実写）
- [ ] ナビのリンクを各ページに接続（現在 Shop/Eat/See/Stay は # リンク）
- [ ] EC ショップ連携（STORES or Shopify、summer 2026 予定）
- [ ] 日本語版の検討（/ja/ サブパス）
- [ ] Google Analytics / Search Console 設定
- [ ] OGP 画像・Twitter Card の追加

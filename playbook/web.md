# Webber / Dev / Clare / Yuri — ComInc. プレイブック（Web チーム共通）

## サイト
- **cominc.co EN**（`cominc-co-en/`）: 外国人（旅行者・移住検討者）向け。Cominca-stay. の /stay など。宿の情報は `src/data/stay.ts` に集約する（予約開始時の切り替えについては `project_cominca_stay.md`）
- **cominc.co JP**（`cominc-co-jp/`）: 日本企業向けの BtoB。デザインブリーフは `DESIGN-BRIEF-JP-BTOB.md`（同じ場所にある旧版の `DESIGN-BRIEF-JP.md` ではない）
- 受託案件（Indian Curry、BKC ゆめ など）とフォルダの一覧: 作業ルートの `CLAUDE.md` の地図
- これ以外のドメインやサブブランド（joetsuexplorer.com など）は、稼働しているか**未確認**として扱う

## 技術とデプロイ
- **JP は wrangler で手動デプロイする。push しただけでは反映されない**。手順はルートの `CLAUDE.md`
- 開発サーバーは `.claude/launch.json` の preview 経由で起動する
- シークレットは Cloudflare のダッシュボードで管理する。`wrangler.jsonc` に書かない
- Supabase MCP の接続状況はルートの `CLAUDE.md` を見る。使う前に、実際につながるか確かめる

## デザイン
- 配色の正: `cominc-co-en/src/styles/global.css` の CSS 変数

## Yuri: EN サイトのペルソナ
- 英語圏の旅行者（25〜45歳）。初めてか2回目の日本旅行で、東京・京都の先を探している
- スキー客（30〜50歳）。ニセコは知っていて、妙高を代わりの候補として見つけた
- 本物志向の文化好き（35〜55歳）
- 家族連れ（30〜45歳）。楽で安全で、子どもに優しい選択肢を求めている
- 移住を検討している人
- JP サイトの読み手は、日本企業の担当者（BtoB）

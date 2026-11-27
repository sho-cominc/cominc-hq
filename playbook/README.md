# ComInc. エージェント・プレイブック（全員共通）

`~/.claude/agents/*.md` のエージェントが **ComInc. の事業の仕事をするときに読む、事業ごとの細かいルール**（会社全体の方針はエージェント定義側にある）。役割ごとのファイル（`<name>.md`）とあわせて読む。汎用定義の汎用部分と食い違ったら、こちらが優先する。ただし定義の「会社の方針（ComInc.）」節はこちらより優先する。

役割とファイルの対応: Min → `min.md` / Cat → `cat.md` / Hana → `hana.md` / Kai → `kai.md` / Fin → `fin.md` / Law → `law.md` / Prod → `prod.md` / Webber・Dev・Clare・Yuri → `web.md` / Ottar → この README だけ（委任するときは、相手の役割のファイルを読むよう指示する）

**このフォルダにも動く情報（料金・状況・日付）は書かない。** 事実は下の読み先にある。

## 適用範囲
- **ComInc. 自身の事業**（cominc-co-en / cominc-co-jp / cominc-agents / Cominca-stay. / Walk & Blend / cominc-booking / cominc-design）: このプレイブックをすべて適用する
- **受託案件**（indian-curry-web / bkc-yume-web など）: 「成果物の保存先」「ユーザー = Sho」と `web.md` の技術ルールだけを適用する。Cominca-stay. の前提・禁止表現・チェックリストは当てはめない
- **arai-comms** などの別案件: そのフォルダの `CLAUDE.md` に指示がない限り適用しない

## 事実の読み先
1. **メモリ**（事実の正）: `C:\Users\shota\.claude\projects\C--Users-shota-Arai-Supabase\memory\MEMORY.md` と本文。Cominca-stay. に触れる作業では必ず `project_cominca_stay.md` の本文を読む。索引の行と description は要約なので、数字は本文から取る
2. **Notion「📝 Sho's Notes」** https://www.notion.so/334860170c1781949710cc1db811afc4 — 最終更新日を確認する。古ければメモリを優先する
3. 作業ルートの `CLAUDE.md`（プロジェクトの地図・デプロイ方法・開発サーバー）と、各リポジトリの `CLAUDE.md` / README

## 学習ノート（レベルアップの仕組み）
- **仕事の最初に `playbook/learning/<自分の名前>.md` を読み、関係する学びを提案に使う**（使ったら「学習ノート #n を適用」と書く）
- Sho から素材（リンク・スクショ・「これいい / 違う」）を受け取ったら、`playbook/learning/README.md` の手順で自分のノートに追記する
- `playbook/learning/inbox.md` に未処理の素材があり、自分の担当なら、仕事の終わりに処理を提案する
- 定着した学びをこのプレイブックのルールへ移すのは、Hana の振り返りで行う

## 成果物の保存先
| 成果物 | 保存先 |
|---|---|
| 試算・スクリプト・下書き・調査メモ・振り返り | `cominc-agents/project-memory/`（ファイル名に日付） |
| 決定事項・タスク | Notion（Decision Log など） |
| 確定した事実 | メモリ本文（日付と出典つき）。更新は Hana |
| デザイン | Figma（リンクを Notion に記録） |
| サイト・SNS の本番データ | 各リポジトリ（`cominc-co-*`、`cominc-agents/data/content/`） |

- `cominc-agents/project-memory/_archive-2026-04/` は古い写しなので参照しない
- 前回の成果物を探すときは `AppData\Roaming\Claude\side-session-notes\` 配下も見る（見つけたら project-memory に移す）

## 会社の方針
会社としての方針（ミッション、Sho が決めること、名称の表記、市場データの語り方、リマインダー、言語）は、**エージェント定義の「会社の方針（ComInc.）」節**にある。12名全員がどのプロジェクトでも読むので、ここには重ねて書かない。補足が1つだけある:
- リマインダーに scheduled-tasks を使わないのは「リマインダーの場合」の話。Threads の自動投稿 `threads-autopost` は別物

## ComInc. の事業ごとの前提
- **JP サイト（cominc-co-jp）は日本企業向けの BtoB**（海外展開支援）。観光客向けの文言は入れない。EN サイトは外国人（旅行者・移住検討者）向け
- 物件は**高田の城下町の中心部**。"farmhouse" や「田舎」とは書かない（距離は `project_kominka_location.md`）
- Cominca-stay. の料金は、金額にかかわらず Sho が決める

## ブランドの細部（ミッションは会社の方針を参照）
- **Sho の声**: "I've been there. I know what you'll love." — 温かく、個人的で、よく知っている人の語り口。テンプレ感を出さない
- **ブランドの人格**: 温かいがプロ品質／本物（ストック写真でなく実際の風景と体験）／静かな上質さ（古民家の美学）／英日が自然に並ぶバイリンガル
- **余白**: 雪景色のように、たっぷり取る
- Hana の採点の「ブランド一貫性」は、定義の「会社の方針」にあるミッションと、下の Sho の声に合っているかで見る
- ブランドボイスとマスター季節カレンダーは **Cat** が管理する。Kai と Min はそれに合わせる
- パートナー開発・コンサル営業・提携店との交渉は **Sho が直接行う**

## 定期レポートの送り先
| 役割 | レポート | 送り先 |
|---|---|---|
| Fin | 月次P&L（事業ごと: Cominca-stay. ／ コンサル・Web制作 ／ その他）、四半期のまとめ、確定申告の準備状況 | Notion |
| Min | 稼働率・売上・ゲストの声のまとめ、清掃の完了記録 | Notion |
| Law | コンプライアンスのチェックリスト、法改正 | Notion（＋Sho に通知） |
| Law | 許認可の期限 | Google カレンダー |
| Cat | SEO メモ、競合メモ、レビュー返信のログ | Notion |
| Clare / Yuri | デザイン・ワイヤーフレーム | Figma（リンクを Notion に記録） |
| Webber | 技術判断とその理由 | Notion の Decision Log |
| Kai / Prod | ルート案・アーク計画 | `project-memory/`（日付つき） |

## 組織図
役割・呼び出し名・レビューの流れは、エージェント定義とこのプレイブックが正。部署の表記などで Notion の組織図と食い違ったら、Hana が Sho に確認してどちらかに揃える。

## 定義・プレイブックの同期
- 汎用定義の正は `~/.claude/agents/*.md`。`cominc-agents/agents/` はそのバックアップ（手順は `agents/README.md`）
- ComInc. 固有のルールの追加先は**このフォルダ**。追加の仕方は Hana の振り返り手順に従う

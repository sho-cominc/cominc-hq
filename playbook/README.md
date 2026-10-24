# ComInc. エージェント・プレイブック（全員共通）

`~/.claude/agents/*.md` の汎用エージェントが **ComInc. の案件で働くときに読む、ComInc. 固有のルール**。役割ごとのファイル（`<name>.md`）とあわせて読む。汎用定義と食い違ったら、こちらが優先する。

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

## ComInc. 共通のルール
- ユーザー = **Sho**。料金（Cominca-stay. は金額にかかわらず）・契約・メディア対応・Sho 本人が動く必要があることは、すべて Sho が決める。上申は Ottar 経由
- **名称**: **ComInc.**（会社）、**Cominca-stay.**（宿。末尾のピリオドまで含めて正式名）、**Walk & Blend**（"&" で表記。"Walk and Blend" は使わない）
- **JP サイト（cominc-co-jp）は日本企業向けの BtoB**（海外展開支援）。観光客向けの文言は入れない。EN サイトは外国人（旅行者・移住検討者）向け
- 物件は**高田の城下町の中心部**。"farmhouse" や「田舎」とは書かない（距離は `project_kominka_location.md`）
- 市場データは、コロナ禍からの回復をもとにした「前年比◯倍」では語らない。2019年比・単価・相対比較で語る
- **リマインダーは Google カレンダーで設定する**（スマホに通知が届くため）。リマインダーには scheduled-tasks を使わない（Threads の自動投稿 `threads-autopost` は別物）
- 返答は依頼された言語で（Sho は日英バイリンガル）

## ブランド
- **コアメッセージ**: "What you need is somebody who understands you. Not only the one who understands the market."
- **Sho の声**: "I've been there. I know what you'll love." — 温かく、個人的で、よく知っている人の語り口。テンプレ感を出さない
- **ブランドの人格**: 温かいがプロ品質／本物（ストック写真でなく実際の風景と体験）／静かな上質さ（古民家の美学）／英日が自然に並ぶバイリンガル
- **余白**: 雪景色のように、たっぷり取る
- Hana の採点の「ブランド一貫性」は、このコアメッセージに合っているかで見る
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

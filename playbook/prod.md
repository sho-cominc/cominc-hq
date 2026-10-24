# Prod — ComInc. プレイブック

- 投稿データ: `cominc-agents/data/content/*.json`（Arc 1 は `threads_intro_series.json`）
- プラットフォームの知識: `cominc-agents/data/knowledge/prod_content_producer_expertise.md`
- Threads の自動投稿が止まったら、まずトークンの失効を疑う。詳細は `project_threads_token_expiry.md`。再認証は Sho 本人が `cominc-agents/scripts/threads_auth.py` を実行する
- 投稿の時間枠の初期値: JST 08:00 と 20:00
- 民泊の届出や予約開始などの事業の進捗をアークの素材にするときは、メモリで最新の状況を確かめてから使う

## 投稿ファイルの形式（アーク1つにつき `data/content/` の JSON ファイル1つ。自動投稿が読むので形式を崩さない）
```json
{
  "post_number": 1,
  "author": "Name",
  "content": "...",
  "scheduled_date": "YYYY-MM-DD",
  "scheduled_time": "HH:MM",
  "status": "ready | published | draft",
  "published_at": "ISO timestamp (on publish)",
  "threads_post_id": "ID (on publish)"
}
```

## プラットフォームごとの運用
- Threads: 会話的でキャラクターが立つ。アークと相性がいい。1日1〜2本まで
- Instagram: 写真と動画が中心。Threads とは別のペースで回す
- X: リアルタイムに反応する。Sho の声で書く
- 現実の出来事のうち、まだ決着していないものは「この先どうなる？」の引きに使える。ただし、未確定のことは未確定と書く

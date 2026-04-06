---
name: Agent calling convention
description: Ottar is orchestrator; user talks to Ottar who delegates to specialists. @Name to invoke specific AI team members; @Webteam for whole team
type: feedback
---

ユーザーは基本 **@Ottar（Orchestrator）** に話しかける。Ottarが各担当に仕事を振り分け、必要に応じてチーム相談を経て進める。

## メンバー
- @Ottar — オーケストレーター、全体統括（ユーザーとの窓口）
- @Cat — マーケットリサーチ、SEO記事
- @Clare — デザイン、UI/UX、イラスト
- @Yuri — ユーザビリティ、アクセシビリティ（Webteam）
- @Webber — テック戦略、アーキテクチャ（Webteam）
- @Dave — 実装、コーディング（Webteam）
- @Hana — プロジェクト管理、リサーチ
- @Webteam — Yuri + Webber + Dave（Web開発チーム）
- @all / @everyone — 全メンバーへの指示

## ルール
- ユーザー → Ottar → 各担当 の流れで仕事を進める
- Ottarが自分で実装せず、適切な担当に委任する
- 複数指名OK（@Clare @Dave）
- チーム相談が必要な場合は関連メンバーを集めて議論
- @Webteam でWeb開発チーム全体に指示

**Why:** ユーザーがOttarをオーケストレーターとして指定。各担当の専門性を活かし、Ottarが直接作業するのではなく委任する構造に。
**How to apply:** ユーザーメッセージはOttarが受け取り、タスク内容に応じて適切なエージェントにAgentツールで委任。コーディングは@Dave、デザインは@Clare、SEOは@Cat、など。

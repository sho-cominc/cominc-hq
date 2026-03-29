# MCP経由でWeb構築・管理を完全自動化する方法
## 調査日: 2026-03-28

---

## 1. 推奨アーキテクチャ（結論）

```
Notion (CMS/コンテンツ管理) ← Notion MCP ✅接続済み
    ↓ ビルド時にコンテンツ取得
GitHub (コード管理) ← GitHub MCP Server 🔧要追加
    ↓ push → 自動ビルド
Astro (SSG/SSR フレームワーク)
    ↓ wrangler deploy
Cloudflare Workers/Pages ← Cloudflare MCP ✅接続済み
```

### ドメイン戦略
| ドメイン | 用途 | 状態 |
|---------|------|------|
| **cominc.co** | コーポレートサイト（コンサル/パートナー向け） | 新規構築 |
| **joetsuexplorer.com** | インバウンド観光ガイド（サブブランド） | 既存サイト |
| **myokojoetsu.com** | リダイレクト or ランディングページ | 保有済み |

---

## 2. 現在接続済みのMCPツール

### Notion MCP ✅
- `notion-create-pages` / `notion-update-page` / `notion-search`
- `notion-create-database` / `notion-create-view`
- コンテンツ管理、タスク管理、ナレッジベースとして使用
- **CMS用途**: Notion DBにブログ記事・ページコンテンツを格納 → ビルド時に取得

### Cloudflare MCP ✅
- `workers_list` / `workers_get_worker` / `workers_get_worker_code`
- `r2_bucket_create/delete/get/list` （画像・アセットストレージ）
- `kv_namespace_create/delete/get/list` （Key-Valueストア）
- `d1_database_create/delete/get/query/list` （SQLiteデータベース）
- `search_cloudflare_documentation`
- **注意**: デプロイ自体は `wrangler deploy` コマンドが必要（MCPにdeploy toolはない）

### Gmail MCP ✅
- メールの検索・読み取り・下書き作成

### Google Calendar MCP ✅
- イベント作成・更新・空き時間検索

---

## 3. 追加すべきMCPサーバー

### GitHub MCP Server 🔧 最優先
**公式**: https://github.com/github/github-mcp-server

```bash
claude mcp add github
```

**できること**:
- リポジトリの閲覧・作成・管理
- Issue / PR の作成・レビュー・マージ
- コードの検索・分析
- GitHub Actions（CI/CD）の監視
- ブランチ管理、コミット履歴の確認

**ComInc.での活用**:
- Web Developerエージェントがコードを直接pushできる
- PR作成 → Web Directorがレビュー → マージ → 自動デプロイ
- Issue管理でタスクトラッキング

### Google Drive MCP ✅ （既に接続済み）
- `google_drive_fetch` / `google_drive_search`
- ドキュメント・画像の取得に使用可能

---

## 4. Notion as CMS（推奨アプローチ）

### なぜNotionか
- 既にNotionMCPが接続済み
- Sho氏が手動で編集もできる（非エンジニアフレンドリー）
- エージェントがMCP経由で直接コンテンツを作成・更新できる
- 別途CMSの契約・学習コスト不要

### Astro + Notion 連携方法

**パッケージ**: `notion-astro-loader`（コミュニティプラグイン）

```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import { notionLoader } from 'notion-astro-loader';

export default defineConfig({
  // Notion DBからコンテンツを取得してビルド
});
```

**仕組み**:
1. NotionのDBに記事・ページを作成（エージェント or Sho氏が手動で）
2. ビルド時にNotion APIからコンテンツを取得
3. Astroが静的HTMLを生成
4. Cloudflareにデプロイ

### 制限事項
- API Rate Limit あり（ビルド時のみ呼ぶので実用上問題なし）
- ファイルURL（画像等）に有効期限がある → R2にコピーして使うのが安全
- Webhook がシグナルのみ → ビルドトリガーは GitHub Actions の cron or 手動

### Notion DBの設計（CMS用）

```
📁 ComInc. Website Content
├── 📊 Pages DB
│   ├── Title (title)
│   ├── Slug (text) → /en/about, /ja/about
│   ├── Language (select: en/ja)
│   ├── Status (select: draft/review/published)
│   ├── Content (rich_text)
│   ├── SEO Title (text)
│   ├── SEO Description (text)
│   └── Last Published (date)
│
├── 📊 Blog Posts DB
│   ├── Title (title)
│   ├── Slug (text)
│   ├── Language (select: en/ja)
│   ├── Category (select: guide/culture/food/adventure/business)
│   ├── Status (select: draft/review/published)
│   ├── Author (text)
│   ├── Content (rich_text)
│   ├── Featured Image (files)
│   └── Publish Date (date)
│
└── 📊 Partners DB
    ├── Name (title)
    ├── Type (select: accommodation/activity/restaurant)
    ├── Description EN (text)
    ├── Description JA (text)
    └── Website (url)
```

---

## 5. Cloudflare デプロイ方法

### 方法A: GitHub連携（推奨）
1. GitHubリポジトリを作成
2. Cloudflare Dashboard でリポジトリを接続
3. push するたびに自動ビルド＋デプロイ
4. PRごとにプレビューデプロイが生成される

```
エージェントがGitHub MCPでpush → Cloudflare Buildsが自動検知 → デプロイ
```

### 方法B: Wrangler CLI 直接デプロイ
```bash
npx wrangler deploy  # Workers向け（自動検出）
npx wrangler pages deploy ./dist --project-name=cominc-co  # Pages向け
```

### 方法C: Workers + Astro SSR（新しい方法）
```bash
npm create cloudflare@latest -- cominc-co --framework=astro
```
- Wrangler が Astro を自動検出して設定生成
- `@astrojs/cloudflare` アダプターが自動インストール
- SSR対応（動的ページ可能）

### DNS設定
Cloudflare MCP では直接DNS操作のツールが見当たらない。
→ Cloudflare Dashboard で手動設定、または Wrangler CLI で対応。

---

## 6. 代替CMS（Notionが合わない場合の候補）

| CMS | MCP対応 | 特徴 | コスト |
|-----|---------|------|--------|
| **Notion** | ✅接続済み | 既存利用、学習コスト0 | Free |
| **Sanity** | ✅公式MCP | 強力なスキーマ、リアルタイム | Free tier |
| **Storyblok** | ✅ネイティブMCP | Visual Editor付き | Free tier |
| **Hygraph** | ✅公式MCP | GraphQL API | Free tier |
| **dotCMS** | ✅公式MCP | エンタープライズ向け | 有料 |
| **Strapi** | ✅コミュニティMCP | セルフホスト可 | Free (OSS) |

**結論**: Phase 1ではNotionで十分。スケールが必要になったらSanityに移行。

---

## 7. 完全MCP管理フロー（理想形）

```
┌─────────────────────────────────────────────┐
│  CEO Orchestrator (Claude)                   │
│  「新しいブログ記事を公開して」              │
└──────┬──────────────────────────────────────┘
       │
       ├──→ Marketing Agent
       │    「キーワードリサーチ、記事戦略決定」
       │
       ├──→ Secretary Agent (Notion MCP)
       │    「Notion Blog Posts DBに記事作成」
       │    「Status: draft → review」
       │
       ├──→ Web Director Agent
       │    「記事レビュー、SEOチェック」
       │    「Status: review → published」
       │
       ├──→ Web Developer Agent (GitHub MCP)
       │    「git pull → astro build でNotionから取得」
       │    「GitHub に push」
       │
       └──→ Cloudflare (自動)
            「GitHub push検知 → ビルド → デプロイ」
            「cominc.co に反映」
```

### エージェントに必要なMCPアクセス

| エージェント | Notion | GitHub | Cloudflare | Gmail | Calendar |
|-------------|--------|--------|------------|-------|----------|
| Secretary | ✅ RW | - | - | ✅ | ✅ |
| Marketing | ✅ R | - | - | - | - |
| Guide | ✅ R | - | - | ✅ | ✅ |
| Minpaku | ✅ R | - | - | ✅ | ✅ |
| Web Director | ✅ RW | ✅ R | - | - | - |
| Web Developer | ✅ R | ✅ RW | ✅ R | - | - |
| Finance | ✅ RW | - | - | - | - |

---

## 8. セットアップ手順（GitHub MCP追加）

```bash
# 1. GitHub Personal Access Token を作成
# https://github.com/settings/tokens → Fine-grained token
# Repository permissions: Contents (RW), Issues (RW), Pull requests (RW)

# 2. Claude Code に GitHub MCP を追加
claude mcp add github -- npx -y @anthropic-ai/github-mcp

# または手動で ~/.claude.json に追加:
# {
#   "mcpServers": {
#     "github": {
#       "command": "npx",
#       "args": ["-y", "@anthropic-ai/github-mcp"],
#       "env": {
#         "GITHUB_TOKEN": "ghp_xxxxxxxxxxxx"
#       }
#     }
#   }
# }

# 3. リポジトリ作成
gh repo create cominc/cominc-co --private

# 4. Cloudflare Pages にリポジトリ接続
# Dashboard: Workers & Pages → Create → Connect to Git
```

---

## 9. 次のアクション（優先順）

1. **GitHub MCP Server を追加** → エージェントからコード管理可能に
2. **cominc-co リポジトリ作成** → Astro プロジェクト初期化
3. **Cloudflare Pages 連携** → GitHub push で自動デプロイ
4. **Notion CMS DB作成** → Pages / Blog Posts / Partners
5. **joetsuexplorer.com レビュー** → Web チームに現状分析させる
6. **myokojoetsu.com** → cominc.co or joetsuexplorer.com へリダイレクト設定

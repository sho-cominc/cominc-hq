# SNS MCP Auto-Post Research (2026-03-30)

## Multi-Platform MCP Servers (Best for ComInc.)

### Postiz (Recommended - Free/Self-hosted)
- GitHub: `gitroomhq/postiz-app` (~14k stars, Apache 2.0)
- Platforms: 30+ (X, IG, LinkedIn, Facebook, Reddit, Threads, Mastodon, Bluesky, Discord)
- Features: Scheduling, AI content, analytics, native MCP support
- Self-hosted: Next.js + PostgreSQL + Redis
- Cost: Free

### Ayrshare (Most Complete - Paid)
- GitHub: `vanman2024/ayrshare-mcp`
- Platforms: 13+ (X, FB, IG, LinkedIn, TikTok, YT, Pinterest, Reddit, Threads, Bluesky, Telegram, Snapchat, Google Business)
- Features: 75+ tools, scheduling, bulk ops, auto-hashtags, evergreen reposting, analytics, AI content gen
- Cost: Paid API

### Publora (Middle Ground - Free Tier)
- URL: publora.com
- Platforms: 11+ (IG, LinkedIn, X, Threads, Telegram, FB, TikTok, YT, Mastodon, Bluesky, Pinterest)
- Features: 18 MCP tools, multi-platform simultaneous posting, auto-formatting, scheduling
- Cost: Free tier available

### Vista Social (Premium)
- URL: vistasocial.com/integrations/mcp/
- Platforms: 15+
- Features: 35+ MCP tools, scheduling, analytics, inbox, optimal posting times
- Rate limit: 60 req/min
- Cost: Some features require Premium

## Platform-Specific MCP Servers

| Platform | Direct MCP Post? | Best Server |
|----------|------------------|-------------|
| X/Twitter | YES | `Infatoshi/x-mcp` or `taazkareem/twitter-mcp-server` |
| Instagram | YES (Business) | `jlbadano/ig-mcp` (Graph API required) |
| LinkedIn | YES | `lurenss/linkedin-mcp` |
| Bluesky | YES | `brianellin/bsky-mcp-server` (easiest to automate) |
| Threads | YES | `tttn13/threads-mcp` |
| Facebook | Multi-platform only | Ayrshare, Vista Social |
| TikTok | Multi-platform only | Ayrshare, Publora |
| YouTube | Limited | `ZubeidHendricks/youtube-mcp-server` |
| Pinterest | Multi-platform only | Ayrshare, Vista Social |

## Other Tools with MCP
- **Buffer**: `ahernan2/buffer-mcp` (GraphQL API, public beta Feb 2026)
- **Hootsuite**: Via Zapier MCP bridge only

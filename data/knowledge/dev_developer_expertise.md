# Dev (Web Developer) - Implementation Knowledge Base
## ComInc. Inbound Tourism Business - Joetsu/Myoko, Niigata, Japan
### Last Updated: 2026-03-29

---

## 1. Astro 4.x/5.x Practical Guide

### Project Structure
```
cominc-website/
├── astro.config.mjs        # Astro configuration
├── package.json
├── tsconfig.json
├── public/                  # Static assets (copied as-is)
│   ├── favicon.ico
│   ├── fonts/
│   └── images/              # Non-optimized static images
├── src/
│   ├── components/          # Reusable .astro components
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── LanguageSwitcher.astro
│   │   ├── BookingForm.astro
│   │   └── ActivityCard.astro
│   ├── content/
│   │   └── config.ts        # Content collection definitions
│   ├── layouts/
│   │   ├── BaseLayout.astro  # HTML shell, <head>, hreflang
│   │   ├── PageLayout.astro  # Standard page with header/footer
│   │   └── BlogLayout.astro  # Blog post layout
│   ├── pages/
│   │   ├── index.astro           # Japanese home (default locale)
│   │   ├── about.astro
│   │   ├── activities/
│   │   │   ├── index.astro       # Activity listing
│   │   │   └── [slug].astro      # Dynamic activity detail
│   │   ├── en/                   # English pages
│   │   │   ├── index.astro
│   │   │   ├── about.astro
│   │   │   └── activities/
│   │   │       ├── index.astro
│   │   │       └── [slug].astro
│   │   └── api/                  # API endpoints (SSR)
│   │       └── auth/
│   │           ├── signin.ts
│   │           ├── register.ts
│   │           └── signout.ts
│   ├── styles/
│   │   └── global.css        # Tailwind imports + custom styles
│   ├── lib/
│   │   ├── supabase.ts       # Supabase client initialization
│   │   ├── i18n.ts           # Translation utilities
│   │   └── notion.ts         # Notion rendering helpers
│   └── env.d.ts              # TypeScript env declarations
├── .env                      # Local environment variables
└── .env.example              # Template for environment variables
```

### Content Collections Configuration
```typescript
// src/content/config.ts
import { defineCollection, z } from "astro:content";
import { notionLoader } from "notion-astro-loader";

// Notion-sourced activities
const activities = defineCollection({
  loader: notionLoader({
    auth: import.meta.env.NOTION_TOKEN,
    database_id: import.meta.env.NOTION_DATABASE_ID,
    filter: {
      and: [
        { property: "Status", select: { equals: "published" } },
      ],
    },
  }),
});

// Local markdown content (area guides, etc.)
const guides = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    description: z.string(),
    language: z.enum(["en", "ja"]),
    category: z.string(),
    publishDate: z.date(),
    image: z.string().optional(),
  }),
});

export const collections = { activities, guides };
```

### SSG vs SSR Decision Matrix

| Page Type | Rendering | Reason |
|-----------|-----------|--------|
| Home, About, Area Guides | **SSG** (Static) | Content changes infrequently, maximum performance |
| Activity Listings | **SSG** | Rebuilt periodically via deploy hook |
| Activity Detail | **SSG** | Same as listings |
| Blog Posts | **SSG** | Notion content fetched at build time |
| Booking Form | **SSR** or **Client Islands** | Needs real-time availability from Supabase |
| Auth Pages (login/register) | **SSR** | Cookie handling requires server |
| Admin Dashboard | **SSR** | Protected routes, real-time data |
| API Endpoints | **SSR** | Server-only logic |

### Astro Config for Hybrid Rendering
```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import node from '@astrojs/node';

export default defineConfig({
  site: 'https://cominc.jp',
  output: 'static', // Default: static for most pages
  // Use output: 'hybrid' if you need SSR for some pages
  // output: 'hybrid',
  // adapter: node({ mode: 'standalone' }),
  integrations: [
    tailwind(),
  ],
  i18n: {
    defaultLocale: 'ja',
    locales: ['ja', 'en'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
  image: {
    domains: ['prod-files-secure.s3.us-west-2.amazonaws.com'], // Notion image CDN
    remotePatterns: [
      { protocol: 'https', hostname: '*.amazonaws.com' },
      { protocol: 'https', hostname: '*.r2.cloudflarestorage.com' },
    ],
  },
});
```

### Querying Content Collections
```astro
---
// src/pages/activities/index.astro
import { getCollection } from "astro:content";
import PageLayout from "../../layouts/PageLayout.astro";
import ActivityCard from "../../components/ActivityCard.astro";

// Filter Japanese activities
const activities = await getCollection("activities", (entry) => {
  return entry.data.properties?.Language?.select?.name === "ja";
});
---
<PageLayout title="アクティビティ" lang="ja">
  <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {activities.map((activity) => (
      <ActivityCard activity={activity} lang="ja" />
    ))}
  </section>
</PageLayout>
```

---

## 2. Tailwind CSS 4.x

### What Changed in v4 (Released January 2025)
- **CSS-first configuration**: No more `tailwind.config.js`. Configuration is done in CSS.
- **One-line setup**: Just `@import "tailwindcss"` in your CSS file.
- **No template path config**: Tailwind auto-detects your template files.
- **5x faster full builds, 100x faster incremental builds** via the new Oxide engine (Lightning CSS).
- **Built-in container queries**: No plugin needed. Use `@container` and `@min-*`/`@max-*`.
- **Native CSS nesting** support.
- **`@property` support**: Registered custom properties for animations.
- **`color-mix()` support**: For opacity modifiers.

### Setup in Astro
```css
/* src/styles/global.css */
@import "tailwindcss";

/* Custom theme values (replaces tailwind.config.js) */
@theme {
  --color-primary: #1a4d8f;      /* ComInc. brand blue */
  --color-secondary: #c0392b;    /* Accent red (torii gate) */
  --color-snow: #f0f4f8;         /* Light background */
  --color-forest: #2d5f2d;       /* Nature green */
  --font-family-sans: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
  --font-family-heading: 'Noto Sans JP', sans-serif;
  --breakpoint-xs: 475px;
}

/* Dark mode custom properties */
@media (prefers-color-scheme: dark) {
  :root {
    --color-snow: #1a1a2e;
  }
}
```

### Responsive Design Patterns for Tourism Site
```html
<!-- Hero section with responsive background -->
<section class="relative h-[60vh] md:h-[80vh] lg:h-screen overflow-hidden">
  <img
    src="/images/myoko-hero.webp"
    alt="Myoko Kogen snow landscape"
    class="absolute inset-0 w-full h-full object-cover"
    loading="eager"
    fetchpriority="high"
  />
  <div class="absolute inset-0 bg-black/40" />
  <div class="relative z-10 flex flex-col items-center justify-center h-full text-white text-center px-4">
    <h1 class="text-3xl md:text-5xl lg:text-7xl font-bold mb-4">
      妙高・上越の冒険
    </h1>
    <p class="text-lg md:text-xl lg:text-2xl max-w-2xl">
      新潟の自然を満喫する体験ツアー
    </p>
  </div>
</section>

<!-- Activity card grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 md:gap-6 p-4 md:p-8">
  <!-- ActivityCard components -->
</div>

<!-- Mobile-first navigation -->
<nav class="fixed bottom-0 left-0 right-0 bg-white shadow-lg md:static md:shadow-none z-50">
  <div class="flex justify-around md:justify-end md:gap-8 py-2 md:py-0">
    <!-- Nav items -->
  </div>
</nav>
```

### Dark Mode Implementation
```html
<!-- Toggle dark mode with class strategy -->
<html class="dark">
<!-- or detect system preference automatically -->
```

```css
/* In global.css with Tailwind v4 */
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));
```

```html
<!-- Usage in components -->
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
  <h2 class="text-primary dark:text-blue-300">Title</h2>
</div>
```

### Useful Tailwind Patterns for Tourism
```html
<!-- Price badge -->
<span class="inline-flex items-center rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-800">
  ¥5,000〜
</span>

<!-- Season tags -->
<div class="flex gap-2 flex-wrap">
  <span class="rounded-full bg-blue-100 px-2 py-0.5 text-xs text-blue-700">冬 Winter</span>
  <span class="rounded-full bg-green-100 px-2 py-0.5 text-xs text-green-700">春 Spring</span>
</div>

<!-- Rating stars -->
<div class="flex items-center gap-1 text-yellow-400">
  {[1,2,3,4,5].map(star => (
    <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20">...</svg>
  ))}
  <span class="text-sm text-gray-600 ml-1">4.8 (124 reviews)</span>
</div>
```

---

## 3. notion-astro-loader

### Installation
```bash
npm install notion-astro-loader
# or use a maintained fork:
npm install @chlorinec-pkgs/notion-astro-loader
```

### Prerequisites
1. Create a Notion Integration at https://www.notion.so/profile/integrations
2. Copy the **Internal Integration Secret** (starts with `ntn_` or `secret_`).
3. In your Notion database, click "..." > "Connections" > Add your integration.
4. Copy the **Database ID** from the database URL: `notion.so/{workspace}/{DATABASE_ID}?v=...`

### Environment Variables
```bash
# .env
NOTION_TOKEN=ntn_xxxxxxxxxxxxxxxxxxxxx
NOTION_DATABASE_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Basic Content Collection Config
```typescript
// src/content/config.ts
import { defineCollection } from "astro:content";
import { notionLoader } from "notion-astro-loader";

const blog = defineCollection({
  loader: notionLoader({
    auth: import.meta.env.NOTION_TOKEN,
    database_id: import.meta.env.NOTION_DATABASE_ID,
    filter: {
      property: "Status",
      select: { equals: "Published" },
    },
    sorts: [
      { property: "PublishDate", direction: "descending" },
    ],
  }),
});

export const collections = { blog };
```

### Advanced Schema with Zod Overrides
```typescript
// src/content/config.ts
import { z } from "astro/zod";
import { defineCollection } from "astro:content";
import { notionLoader } from "notion-astro-loader";
import {
  notionPageSchema,
  propertySchema,
  transformedPropertySchema,
} from "notion-astro-loader/schemas";

const blog = defineCollection({
  loader: notionLoader({
    auth: import.meta.env.NOTION_TOKEN,
    database_id: import.meta.env.NOTION_DATABASE_ID,
  }),
  schema: notionPageSchema({
    properties: z.object({
      // Transform Notion title to plain string
      Name: transformedPropertySchema.title,
      // Keep as Notion property type
      Category: propertySchema.select.optional(),
      Tags: propertySchema.multi_select.optional(),
      PublishDate: propertySchema.date.optional(),
      // Transform to primitive
      Slug: transformedPropertySchema.rich_text.optional(),
      Language: propertySchema.select.optional(),
    }),
  }),
});

export const collections = { blog };
```

### Rendering Notion Pages
```astro
---
// src/pages/blog/[slug].astro
import { getCollection, render } from "astro:content";
import BlogLayout from "../../layouts/BlogLayout.astro";

export async function getStaticPaths() {
  const posts = await getCollection("blog");
  return posts.map((post) => {
    const slug = post.data.properties?.Slug?.rich_text?.[0]?.plain_text
      || post.id;
    return {
      params: { slug },
      props: { post },
    };
  });
}

const { post } = Astro.props;
const { Content } = await render(post);
---
<BlogLayout
  title={post.data.properties?.Name || "Blog Post"}
  date={post.data.properties?.PublishDate?.date?.start}
>
  <Content />
</BlogLayout>
```

### Image Handling: Downloading at Build Time
The `@chlorinec-pkgs/notion-astro-loader` fork supports automatic image downloading:

```typescript
const blog = defineCollection({
  loader: notionLoader({
    auth: import.meta.env.NOTION_TOKEN,
    database_id: import.meta.env.NOTION_DATABASE_ID,
    imageSavePath: "./src/assets/notion-images/",
    // Images are downloaded during build and URLs are rewritten
  }),
});
```

### Manual Image Download Script (Alternative)
```typescript
// scripts/download-notion-images.ts
import { Client } from "@notionhq/client";
import fs from "fs";
import path from "path";
import https from "https";

const notion = new Client({ auth: process.env.NOTION_TOKEN });

async function downloadImage(url: string, filepath: string): Promise<void> {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(filepath);
    https.get(url, (response) => {
      response.pipe(file);
      file.on("finish", () => { file.close(); resolve(); });
    }).on("error", (err) => {
      fs.unlink(filepath, () => {}); // Clean up
      reject(err);
    });
  });
}

async function syncImages() {
  const response = await notion.databases.query({
    database_id: process.env.NOTION_DATABASE_ID!,
  });

  const outputDir = "./public/images/notion/";
  if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

  for (const page of response.results) {
    // Process cover images, file properties, etc.
    // Download to local directory
    // Upload to R2 if needed
  }
}

syncImages();
```

---

## 4. Render Deployment

### Static Site Deployment (Recommended for Start)
1. Push Astro project to GitHub.
2. In Render Dashboard > New > Static Site.
3. Connect GitHub repo.
4. Configure:
   - **Build Command**: `npm run build`
   - **Publish Directory**: `dist`
   - **Branch**: `main`
5. Add Environment Variables:
   - `NOTION_TOKEN`
   - `NOTION_DATABASE_ID`
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`

### SSR/Hybrid Deployment (Web Service)
```javascript
// astro.config.mjs for SSR on Render
import { defineConfig } from 'astro/config';
import node from '@astrojs/node';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  output: 'hybrid', // or 'server' for full SSR
  adapter: node({ mode: 'standalone' }),
  integrations: [tailwind()],
  // ... rest of config
});
```

Render Web Service Configuration:
- **Build Command**: `npm run build`
- **Start Command**: `node ./dist/server/entry.mjs`
- **Environment**: Node
- **Plan**: Starter ($7/month) or higher

### Environment Variables on Render
```
# Required for build
NOTION_TOKEN=ntn_xxx
NOTION_DATABASE_ID=xxx

# Required for runtime (SSR pages)
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=eyJxxx
SUPABASE_SERVICE_ROLE_KEY=eyJxxx  # Server-side only, never expose to client

# Astro
NODE_ENV=production
```

### Auto-Deploy & Deploy Hooks
- Auto-deploy triggers on every push to `main` branch.
- **Deploy Hook URL**: Create in Render Dashboard > Settings > Deploy Hook.
- Use deploy hook with a cron job to rebuild periodically (refresh Notion content):

```bash
# Example: Rebuild every 2 hours via external cron (e.g., GitHub Actions)
curl -X POST https://api.render.com/deploy/srv-xxxxx?key=xxxxx
```

### GitHub Actions for Scheduled Rebuilds
```yaml
# .github/workflows/scheduled-rebuild.yml
name: Scheduled Rebuild
on:
  schedule:
    - cron: '0 */2 * * *'  # Every 2 hours
  workflow_dispatch:         # Manual trigger

jobs:
  trigger-render-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy
        run: curl -X POST "${{ secrets.RENDER_DEPLOY_HOOK_URL }}"
```

### render.yaml (Infrastructure as Code)
```yaml
# render.yaml
services:
  - type: web
    name: cominc-website
    runtime: static
    buildCommand: npm run build
    staticPublishPath: dist
    envVars:
      - key: NOTION_TOKEN
        sync: false
      - key: NOTION_DATABASE_ID
        sync: false
    headers:
      - path: /assets/*
        name: Cache-Control
        value: public, max-age=31536000, immutable
      - path: /*
        name: X-Frame-Options
        value: DENY
    routes:
      - type: rewrite
        source: /en/*
        destination: /en/index.html
```

---

## 5. Supabase Client Setup in Astro

### Installation
```bash
npm install @supabase/supabase-js @supabase/ssr
```

### Client Initialization
```typescript
// src/lib/supabase.ts
import { createClient } from "@supabase/supabase-js";

const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY;

// Browser client (for client-side components / islands)
export const supabase = createClient(supabaseUrl, supabaseAnonKey);
```

### SSR Client (for Server-Side Pages)
```typescript
// src/lib/supabase-server.ts
import { createServerClient, parseCookieHeader } from "@supabase/ssr";
import type { AstroCookies } from "astro";

export function createSupabaseServerClient(cookies: AstroCookies) {
  return createServerClient(
    import.meta.env.PUBLIC_SUPABASE_URL,
    import.meta.env.PUBLIC_SUPABASE_ANON_KEY,
    {
      cookies: {
        getAll() {
          return parseCookieHeader(cookies.get("sb-access-token")?.value ?? "");
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value, options }) => {
            cookies.set(name, value, options);
          });
        },
      },
    }
  );
}
```

### Auth Implementation

#### Sign Up Endpoint
```typescript
// src/pages/api/auth/register.ts
import type { APIRoute } from "astro";
import { createSupabaseServerClient } from "../../../lib/supabase-server";

export const POST: APIRoute = async ({ request, cookies, redirect }) => {
  const formData = await request.formData();
  const email = formData.get("email")?.toString();
  const password = formData.get("password")?.toString();
  const fullName = formData.get("full_name")?.toString();

  if (!email || !password) {
    return new Response("Email and password required", { status: 400 });
  }

  const supabase = createSupabaseServerClient(cookies);
  const { error } = await supabase.auth.signUp({
    email,
    password,
    options: {
      data: { full_name: fullName },
    },
  });

  if (error) {
    return new Response(error.message, { status: 500 });
  }

  return redirect("/auth/confirm");
};
```

#### Sign In Endpoint
```typescript
// src/pages/api/auth/signin.ts
import type { APIRoute } from "astro";
import { createSupabaseServerClient } from "../../../lib/supabase-server";

export const POST: APIRoute = async ({ request, cookies, redirect }) => {
  const formData = await request.formData();
  const email = formData.get("email")?.toString();
  const password = formData.get("password")?.toString();

  if (!email || !password) {
    return new Response("Email and password required", { status: 400 });
  }

  const supabase = createSupabaseServerClient(cookies);
  const { error } = await supabase.auth.signInWithPassword({ email, password });

  if (error) {
    return new Response(error.message, { status: 500 });
  }

  return redirect("/dashboard");
};
```

#### Sign Out Endpoint
```typescript
// src/pages/api/auth/signout.ts
import type { APIRoute } from "astro";
import { createSupabaseServerClient } from "../../../lib/supabase-server";

export const GET: APIRoute = async ({ cookies, redirect }) => {
  const supabase = createSupabaseServerClient(cookies);
  await supabase.auth.signOut();
  return redirect("/");
};
```

### Database Queries

#### Fetch Activities
```typescript
// In an Astro page or component
const { data: activities, error } = await supabase
  .from("activities")
  .select("*")
  .eq("is_active", true)
  .eq("category", "skiing")
  .order("title_en", { ascending: true });
```

#### Check Availability
```typescript
async function checkAvailability(activityId: string, date: string) {
  const { data, error } = await supabase
    .from("availability")
    .select("*")
    .eq("activity_id", activityId)
    .eq("date", date)
    .eq("is_available", true)
    .gt("total_spots - booked_spots", 0);

  return data;
}
```

#### Create Booking
```typescript
async function createBooking(bookingData: {
  activity_id: string;
  booking_date: string;
  time_slot: string;
  num_adults: number;
  num_children: number;
  total_price: number;
}) {
  const { data: { user } } = await supabase.auth.getUser();

  const { data, error } = await supabase
    .from("bookings")
    .insert({
      ...bookingData,
      user_id: user?.id,
      status: "pending",
    })
    .select()
    .single();

  if (error) throw error;
  return data;
}
```

#### Realtime Subscription (Client-Side)
```typescript
// Subscribe to availability changes for a specific activity
const channel = supabase
  .channel("availability-changes")
  .on(
    "postgres_changes",
    {
      event: "UPDATE",
      schema: "public",
      table: "availability",
      filter: `activity_id=eq.${activityId}`,
    },
    (payload) => {
      console.log("Availability updated:", payload.new);
      // Update UI with new availability data
    }
  )
  .subscribe();

// Cleanup on component unmount
// channel.unsubscribe();
```

### Row Level Security Policies
```sql
-- Enable RLS on all public tables
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.activities ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.bookings ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.availability ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.reviews ENABLE ROW LEVEL SECURITY;

-- Activities: publicly readable
CREATE POLICY "Public read access for active activities"
  ON public.activities FOR SELECT
  USING (is_active = true);

-- Availability: publicly readable
CREATE POLICY "Public read access for availability"
  ON public.availability FOR SELECT
  USING (true);

-- Bookings: authenticated users can read their own
CREATE POLICY "Users can read own bookings"
  ON public.bookings FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

-- Bookings: authenticated users can create
CREATE POLICY "Users can create bookings"
  ON public.bookings FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

-- Reviews: public read, authenticated write on own bookings
CREATE POLICY "Public read for approved reviews"
  ON public.reviews FOR SELECT
  USING (is_approved = true);

CREATE POLICY "Users can create reviews for own bookings"
  ON public.reviews FOR INSERT
  TO authenticated
  WITH CHECK (
    auth.uid() = user_id
    AND EXISTS (
      SELECT 1 FROM public.bookings
      WHERE bookings.id = booking_id
      AND bookings.user_id = auth.uid()
      AND bookings.status = 'completed'
    )
  );

-- Add indexes for RLS performance
CREATE INDEX idx_bookings_user_id ON public.bookings(user_id);
CREATE INDEX idx_availability_activity_date ON public.availability(activity_id, date);
CREATE INDEX idx_reviews_booking_id ON public.reviews(booking_id);
```

### TypeScript Types from Supabase
```bash
# Generate types from your Supabase schema
npx supabase gen types typescript --project-id your-project-id > src/lib/database.types.ts
```

```typescript
// src/lib/supabase.ts (with types)
import { createClient } from "@supabase/supabase-js";
import type { Database } from "./database.types";

export const supabase = createClient<Database>(
  import.meta.env.PUBLIC_SUPABASE_URL,
  import.meta.env.PUBLIC_SUPABASE_ANON_KEY
);
```

---

## 6. Astro i18n Implementation

### Configuration
```javascript
// astro.config.mjs
export default defineConfig({
  site: 'https://cominc.jp',
  i18n: {
    defaultLocale: 'ja',
    locales: ['ja', 'en'],
    routing: {
      prefixDefaultLocale: false,
      // ja: /about (no prefix)
      // en: /en/about
    },
  },
});
```

### File Structure for i18n Pages
```
src/pages/
├── index.astro           # / (Japanese home)
├── about.astro           # /about (Japanese)
├── activities/
│   ├── index.astro       # /activities
│   └── [slug].astro      # /activities/ski-lesson
├── en/
│   ├── index.astro       # /en/ (English home)
│   ├── about.astro       # /en/about
│   └── activities/
│       ├── index.astro   # /en/activities
│       └── [slug].astro  # /en/activities/ski-lesson
```

### Translation System
```typescript
// src/lib/i18n.ts
export const languages = {
  ja: '日本語',
  en: 'English',
};

export const defaultLang = 'ja';

export type Lang = keyof typeof languages;

// Translation dictionaries
const translations = {
  ja: {
    'nav.home': 'ホーム',
    'nav.about': '私たちについて',
    'nav.activities': 'アクティビティ',
    'nav.booking': '予約',
    'nav.contact': 'お問い合わせ',
    'hero.title': '妙高・上越の冒険へ',
    'hero.subtitle': '新潟の自然を満喫する体験ツアー',
    'booking.date': '日付を選択',
    'booking.guests': '人数',
    'booking.submit': '予約する',
    'footer.copyright': '(c) {year} ComInc. All rights reserved.',
  },
  en: {
    'nav.home': 'Home',
    'nav.about': 'About Us',
    'nav.activities': 'Activities',
    'nav.booking': 'Book Now',
    'nav.contact': 'Contact',
    'hero.title': 'Adventures in Myoko & Joetsu',
    'hero.subtitle': 'Experience the nature of Niigata',
    'booking.date': 'Select Date',
    'booking.guests': 'Guests',
    'booking.submit': 'Book Now',
    'footer.copyright': '(c) {year} ComInc. All rights reserved.',
  },
} as const;

export function t(key: string, lang: Lang = defaultLang, params?: Record<string, string>): string {
  let text = (translations[lang] as Record<string, string>)[key] || key;
  if (params) {
    Object.entries(params).forEach(([k, v]) => {
      text = text.replace(`{${k}}`, v);
    });
  }
  return text;
}

export function getLangFromUrl(url: URL): Lang {
  const [, lang] = url.pathname.split('/');
  if (lang in languages) return lang as Lang;
  return defaultLang;
}

export function getLocalizedPath(path: string, lang: Lang): string {
  const cleanPath = path.replace(/^\/(en|ja)\//, '/');
  if (lang === defaultLang) return cleanPath;
  return `/${lang}${cleanPath}`;
}
```

### Language Switcher Component
```astro
---
// src/components/LanguageSwitcher.astro
import { languages, getLangFromUrl, getLocalizedPath } from '../lib/i18n';

const currentLang = getLangFromUrl(Astro.url);
const currentPath = Astro.url.pathname;
---
<nav aria-label="Language switcher" class="flex items-center gap-2">
  {Object.entries(languages).map(([lang, label]) => {
    const href = getLocalizedPath(currentPath, lang as any);
    const isActive = lang === currentLang;
    return (
      <a
        href={href}
        class:list={[
          "px-3 py-1 rounded-full text-sm font-medium transition-colors",
          isActive
            ? "bg-primary text-white"
            : "text-gray-600 hover:text-primary hover:bg-gray-100"
        ]}
        aria-current={isActive ? "page" : undefined}
        hreflang={lang}
      >
        {label}
      </a>
    );
  })}
</nav>
```

### hreflang Tags in Layout
```astro
---
// src/layouts/BaseLayout.astro
import { getAbsoluteLocaleUrl } from 'astro:i18n';
import { getLangFromUrl } from '../lib/i18n';

interface Props {
  title: string;
  description?: string;
}

const { title, description } = Astro.props;
const currentLang = getLangFromUrl(Astro.url);
const currentPath = Astro.url.pathname;

// Generate alternate URLs for hreflang
const jaUrl = getAbsoluteLocaleUrl('ja', currentPath.replace(/^\/(en)\//, '/'));
const enUrl = getAbsoluteLocaleUrl('en', currentPath.replace(/^\/(en)\//, '/'));
---
<!DOCTYPE html>
<html lang={currentLang}>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | ComInc.</title>
  {description && <meta name="description" content={description} />}

  <!-- hreflang tags -->
  <link rel="alternate" hreflang="ja" href={jaUrl} />
  <link rel="alternate" hreflang="en" href={enUrl} />
  <link rel="alternate" hreflang="x-default" href={jaUrl} />
  <link rel="canonical" href={new URL(Astro.url.pathname, Astro.site).href} />

  <!-- OG tags (localized) -->
  <meta property="og:locale" content={currentLang === 'ja' ? 'ja_JP' : 'en_US'} />
  <meta property="og:locale:alternate" content={currentLang === 'ja' ? 'en_US' : 'ja_JP'} />
</head>
<body class="min-h-screen flex flex-col bg-snow text-gray-900 dark:bg-gray-900 dark:text-gray-100">
  <slot />
</body>
</html>
```

### Dynamic Route with i18n
```astro
---
// src/pages/en/activities/[slug].astro
import { getCollection, render } from "astro:content";
import PageLayout from "../../../layouts/PageLayout.astro";

export async function getStaticPaths() {
  const activities = await getCollection("activities", (entry) => {
    return entry.data.properties?.Language?.select?.name === "en";
  });

  return activities.map((activity) => {
    const slug = activity.data.properties?.Slug?.rich_text?.[0]?.plain_text
      || activity.id;
    return {
      params: { slug },
      props: { activity },
    };
  });
}

const { activity } = Astro.props;
const { Content } = await render(activity);
---
<PageLayout title={activity.data.properties?.Name} lang="en">
  <article class="prose prose-lg max-w-4xl mx-auto px-4 py-8">
    <Content />
  </article>
</PageLayout>
```

---

## 7. Image Optimization

### Astro Image Component
```astro
---
// Using Astro's built-in Image component
import { Image } from 'astro:assets';

// Local image (optimized at build time)
import heroImage from '../assets/myoko-mountain.jpg';
---

<!-- Local image: fully optimized -->
<Image
  src={heroImage}
  alt="Myoko Mountain covered in snow"
  width={1920}
  height={1080}
  format="webp"
  quality={80}
  loading="eager"
  class="w-full h-auto"
/>

<!-- Remote image: must be in allowed domains -->
<Image
  src="https://pub-xxx.r2.dev/activities/ski-lesson.jpg"
  alt="Ski lesson at Myoko Kogen"
  width={800}
  height={600}
  format="webp"
  quality={80}
  loading="lazy"
  class="rounded-lg shadow-md"
/>
```

### Responsive Images with Picture
```astro
---
import { Picture } from 'astro:assets';
import activityImage from '../assets/hiking-trail.jpg';
---
<Picture
  src={activityImage}
  formats={['avif', 'webp']}
  widths={[320, 640, 960, 1280, 1920]}
  sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
  alt="Hiking trail in Myoko highlands"
  loading="lazy"
  class="w-full h-64 object-cover rounded-xl"
/>
```

### Cloudflare R2 for Persistent Image Storage
R2 solves the Notion image expiration problem by providing permanent URLs with free egress bandwidth.

#### Setup R2 Bucket
1. In Cloudflare Dashboard > R2 > Create Bucket.
2. Name: `cominc-images`.
3. Enable public access via custom domain (e.g., `images.cominc.jp`).

#### Upload Script (Build-Time)
```typescript
// scripts/sync-notion-images-to-r2.ts
import { S3Client, PutObjectCommand, HeadObjectCommand } from "@aws-sdk/client-s3";
import { Client } from "@notionhq/client";
import fetch from "node-fetch";
import crypto from "crypto";

const s3 = new S3Client({
  region: "auto",
  endpoint: `https://${process.env.CF_ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID!,
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY!,
  },
});

const notion = new Client({ auth: process.env.NOTION_TOKEN });
const BUCKET = "cominc-images";
const PUBLIC_URL = "https://images.cominc.jp";

async function uploadToR2(imageUrl: string, key: string): Promise<string> {
  // Check if already exists
  try {
    await s3.send(new HeadObjectCommand({ Bucket: BUCKET, Key: key }));
    return `${PUBLIC_URL}/${key}`; // Already uploaded
  } catch {
    // Not found, proceed with upload
  }

  const response = await fetch(imageUrl);
  const buffer = Buffer.from(await response.arrayBuffer());
  const contentType = response.headers.get("content-type") || "image/jpeg";

  await s3.send(new PutObjectCommand({
    Bucket: BUCKET,
    Key: key,
    Body: buffer,
    ContentType: contentType,
    CacheControl: "public, max-age=31536000, immutable",
  }));

  return `${PUBLIC_URL}/${key}`;
}

async function syncImages() {
  const pages = await notion.databases.query({
    database_id: process.env.NOTION_DATABASE_ID!,
  });

  for (const page of pages.results) {
    if (!("properties" in page)) continue;

    // Process cover image
    if (page.cover) {
      const url = page.cover.type === "file"
        ? page.cover.file.url
        : page.cover.external?.url;
      if (url) {
        const hash = crypto.createHash("md5").update(page.id).digest("hex");
        const key = `covers/${hash}.jpg`;
        const r2Url = await uploadToR2(url, key);
        console.log(`Uploaded cover: ${r2Url}`);
      }
    }

    // Process page blocks for embedded images
    const blocks = await notion.blocks.children.list({ block_id: page.id });
    for (const block of blocks.results) {
      if ("type" in block && block.type === "image") {
        const imageBlock = block as any;
        const url = imageBlock.image.type === "file"
          ? imageBlock.image.file.url
          : imageBlock.image.external?.url;
        if (url) {
          const hash = crypto.createHash("md5").update(block.id).digest("hex");
          const ext = url.includes(".png") ? "png" : "jpg";
          const key = `content/${hash}.${ext}`;
          const r2Url = await uploadToR2(url, key);
          console.log(`Uploaded block image: ${r2Url}`);
        }
      }
    }
  }
}

syncImages().catch(console.error);
```

#### Add to Build Pipeline
```json
// package.json
{
  "scripts": {
    "prebuild": "tsx scripts/sync-notion-images-to-r2.ts",
    "build": "astro build",
    "dev": "astro dev"
  }
}
```

### Lazy Loading Best Practices
```html
<!-- Above the fold: eager load, high priority -->
<img
  src="/images/hero.webp"
  alt="Hero image"
  loading="eager"
  fetchpriority="high"
  decoding="async"
  width="1920"
  height="1080"
/>

<!-- Below the fold: lazy load -->
<img
  src="/images/activity.webp"
  alt="Activity photo"
  loading="lazy"
  decoding="async"
  width="800"
  height="600"
/>
```

### Image Configuration in astro.config.mjs
```javascript
// astro.config.mjs
export default defineConfig({
  image: {
    // Allow remote images from these domains
    domains: [
      'prod-files-secure.s3.us-west-2.amazonaws.com', // Notion
      'images.cominc.jp',  // R2 custom domain
    ],
    remotePatterns: [
      { protocol: 'https', hostname: '**.r2.cloudflarestorage.com' },
    ],
    // Default service configuration
    service: {
      entrypoint: 'astro/assets/services/sharp', // Uses sharp for optimization
    },
  },
});
```

### Performance Checklist
- [ ] Hero/LCP image: `loading="eager"`, `fetchpriority="high"`, preloaded in `<head>`
- [ ] All other images: `loading="lazy"`, `decoding="async"`
- [ ] Always specify `width` and `height` attributes (prevents CLS)
- [ ] Use `<Picture>` component with AVIF + WebP formats
- [ ] Responsive `sizes` attribute to avoid downloading oversized images on mobile
- [ ] Serve images from Cloudflare R2 with `Cache-Control: public, max-age=31536000, immutable`
- [ ] Run `npx astro check` to verify image optimization
- [ ] Test with Lighthouse: target 90+ performance score

---

## 8. Cloudflare CDN Setup

### Architecture Overview
```
User Request --> Cloudflare Edge (285+ cities) --> Render Origin Server
                 |                                    |
                 |-- Cached? Return immediately        |-- Build from Astro
                 |-- WAF/DDoS filtering                |-- Serve static files
                 |-- SSL termination                   |
                 |-- Image optimization (Polish)       |
```

### Step-by-Step: Adding Cloudflare in Front of Render

#### 1. Add Domain to Cloudflare
- Sign up at cloudflare.com (free plan is sufficient)
- Add your domain (e.g., joetsuexplorer.com)
- Cloudflare scans existing DNS records

#### 2. Change Nameservers at Namecheap
- Log into Namecheap > Domain List > Manage
- Under "Nameservers", select "Custom DNS"
- Enter the two Cloudflare nameservers provided (e.g., `ada.ns.cloudflare.com`, `bob.ns.cloudflare.com`)
- Save changes. Propagation takes up to 48 hours but often completes in minutes
- Cloudflare will email you when the domain is active

#### 3. Configure DNS Records
```
Type    Name    Target                          Proxy
CNAME   @       cominc-website.onrender.com     DNS Only (initially)
CNAME   www     cominc-website.onrender.com     DNS Only (initially)
```

**Important**: Keep proxy OFF (grey cloud / DNS Only) initially so Render can issue TLS certificates.

#### 4. Verify Render TLS Certificate
- In Render Dashboard > your service > Settings > Custom Domain
- Add your domain and wait for the TLS certificate to be issued
- Render uses Let's Encrypt for free automatic TLS
- Once certificate shows "Valid", proceed to enable Cloudflare proxy

#### 5. Enable Cloudflare Proxy
- Go back to Cloudflare DNS settings
- Change both CNAME records from "DNS Only" to "Proxied" (orange cloud icon)
- Traffic now flows through Cloudflare's network

#### 6. SSL/TLS Configuration
- In Cloudflare Dashboard > SSL/TLS > Overview
- Set encryption mode to **Full (Strict)**
  - Full (Strict): Cloudflare connects to Render over HTTPS and validates the certificate
  - This is the correct setting because Render provides a valid TLS certificate
- Enable "Always Use HTTPS" under SSL/TLS > Edge Certificates
- Enable "Automatic HTTPS Rewrites" to fix mixed content issues

#### 7. Cloudflare SSL Options Explained
| Mode | Browser-to-CF | CF-to-Render | Certificate Needed on Render |
|------|--------------|-------------|------------------------------|
| Off | HTTP | HTTP | No |
| Flexible | HTTPS | HTTP | No (but insecure) |
| Full | HTTPS | HTTPS | Self-signed OK |
| **Full (Strict)** | HTTPS | HTTPS | **Valid cert required (Render provides)** |

### Caching Configuration

#### Cache Rules (Replaces Legacy Page Rules)
Cloudflare Cache Rules offer more granular control than the deprecated Page Rules.

**Rule 1: Cache Static Assets Aggressively**
- Match: `*.js`, `*.css`, `*.woff2`, `*.woff`, `*.ttf`, `*.ico`, `*.svg`, `*.webp`, `*.avif`, `*.jpg`, `*.png`
- Action: Cache, Edge TTL = 1 month, Browser TTL = 1 month
- This ensures fonts, images, and scripts are served from edge

**Rule 2: Cache HTML Pages**
- Match: All requests NOT matching `/api/*`
- Action: Cache, Edge TTL = 1 hour, Browser TTL = 10 minutes
- Static Astro pages change only on rebuild, but shorter TTL ensures fresh content after deploys

**Rule 3: Bypass Cache for API Routes**
- Match: URI Path starts with `/api/`
- Action: Bypass cache
- Ensures Supabase API calls and form submissions are never cached

#### Performance Optimization Settings
- **Auto Minify**: Enable for HTML, CSS, and JavaScript
- **Brotli Compression**: Enable (better compression than gzip)
- **Early Hints**: Enable (103 status code for faster resource loading)
- **HTTP/3 (QUIC)**: Enable for modern browsers
- **0-RTT Connection Resumption**: Enable for returning visitors

#### Image Optimization (Cloudflare Polish)
- Enable Polish with "Lossy" mode for photographs
- Enable WebP conversion for supported browsers
- This provides an additional optimization layer on top of Astro's build-time optimization

**Warning**: Test Rocket Loader carefully with Astro sites. Rocket Loader defers JavaScript execution, which may conflict with Astro's island hydration. Disable if islands fail to hydrate.

### Security Settings
- **WAF (Web Application Firewall)**: Free plan includes basic managed rules
- **Bot Fight Mode**: Enable to reduce unwanted bot traffic
- **Hotlink Protection**: Enable to prevent other sites from embedding your images
- **Security Headers**: Add via Transform Rules:
  - `X-Frame-Options: DENY`
  - `X-Content-Type-Options: nosniff`
  - `Referrer-Policy: strict-origin-when-cross-origin`

### Cache Purging After Deployment
When Render completes a new build, purge Cloudflare cache to serve fresh content:

```yaml
# .github/workflows/deploy-and-purge.yml
name: Deploy and Purge Cache
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy
        run: curl -X POST "${{ secrets.RENDER_DEPLOY_HOOK_URL }}"

      - name: Wait for deploy (approximate)
        run: sleep 120  # Adjust based on typical build time

      - name: Purge Cloudflare Cache
        run: |
          curl -X POST "https://api.cloudflare.com/client/v4/zones/${{ secrets.CF_ZONE_ID }}/purge_cache" \
            -H "Authorization: Bearer ${{ secrets.CF_API_TOKEN }}" \
            -H "Content-Type: application/json" \
            --data '{"purge_everything":true}'
```

### Multi-Domain Setup
For managing both cominc.co and joetsuexplorer.com:
- Add both domains to the same Cloudflare account
- Each domain gets its own zone with independent settings
- Share the same Cloudflare plan across both domains (free plan allows unlimited domains)
- Configure similar caching rules but potentially different security levels
- Corporate site (cominc.co) may need stricter WAF rules

---

## 9. Supabase MCP (Model Context Protocol)

### Overview
The Supabase MCP Server enables AI tools (Claude, Cursor, VS Code Copilot, Windsurf) to interact directly with your Supabase project through natural language commands. This is valuable for development workflow acceleration.

### What MCP Can Do
- **Project Management**: Create and manage Supabase projects from your AI tool
- **Schema Design**: Design tables and generate migration files
- **Data Queries**: Run SQL queries and generate reports
- **Branch Management**: Manage database branches for development
- **Debugging**: Retrieve logs and diagnose issues
- **Configuration**: Manage project settings and environment

### Authentication
- MCP Server uses OAuth by default (no PAT required since late 2025)
- Authentication happens via browser-based flow
- Dynamic client registration means no manual setup needed

### Setup in VS Code / Claude
```json
// .vscode/settings.json or Claude MCP config
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@supabase/mcp-server"]
    }
  }
}
```

### Practical Use Cases for ComInc. Development

**1. Schema Evolution**
Ask the AI: "Add a 'partners' table with name, type, contact_email, website_url, description, logo_url, and is_active columns, with RLS policies that allow public read for active partners."

**2. Data Analysis**
Ask the AI: "Show me booking trends for the last 30 days grouped by activity category."

**3. Migration Generation**
Ask the AI: "Create a migration that adds a 'featured' boolean column to the activities table with a default of false."

**4. RLS Policy Creation**
Ask the AI: "Write RLS policies for the reviews table so that approved reviews are publicly readable and users can only create reviews for their own completed bookings."

**5. Debug Issues**
Ask the AI: "Check the Supabase logs for any failed authentication attempts in the last hour."

### Supabase Storage for Tourism Images

#### Bucket Setup
```sql
-- Create public bucket for activity images
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
VALUES (
  'activity-images',
  'activity-images',
  true,
  5242880, -- 5MB limit
  ARRAY['image/jpeg', 'image/png', 'image/webp', 'image/avif']
);

-- Create private bucket for admin uploads
INSERT INTO storage.buckets (id, name, public)
VALUES ('admin-uploads', 'admin-uploads', false);
```

#### Storage RLS Policies
```sql
-- Public read for activity images
CREATE POLICY "Public read for activity images"
ON storage.objects FOR SELECT
USING (bucket_id = 'activity-images');

-- Authenticated users can upload to activity images
CREATE POLICY "Auth users can upload activity images"
ON storage.objects FOR INSERT
TO authenticated
WITH CHECK (bucket_id = 'activity-images');

-- Admin-only uploads (using custom claim)
CREATE POLICY "Admins can upload to admin bucket"
ON storage.objects FOR INSERT
TO authenticated
WITH CHECK (
  bucket_id = 'admin-uploads'
  AND (auth.jwt() ->> 'role') = 'admin'
);
```

#### Image Optimization via Supabase
```typescript
// Supabase Storage provides on-the-fly image transformation
const imageUrl = supabase.storage
  .from('activity-images')
  .getPublicUrl('skiing/myoko-powder.jpg', {
    transform: {
      width: 800,
      height: 600,
      resize: 'cover',
      format: 'webp',
      quality: 80,
    },
  }).data.publicUrl;
```

#### Smart CDN
- Supabase Smart CDN provides global edge caching for storage assets
- 285+ edge locations worldwide
- Automatic cache revalidation within 60 seconds of file changes
- Public buckets get better cache hit rates than private buckets
- For ComInc., use public buckets for all tourism imagery (better performance)

---

## 10. Tech Stack Integration: Full Pipeline

### End-to-End Development Pipeline

```
Figma (Design)
    |
    v
VS Code + Astro (Development)
    |
    v
GitHub Repository (Source Control)
    |
    v
Render (Build + Host)  <---- Notion (Content via loader at build time)
    |                   <---- Supabase (Data via API at build/runtime)
    v
Cloudflare CDN (Edge Delivery)
    |
    v
End User (Browser)
```

### Pipeline Step by Step

**Step 1: Design in Figma**
- UX/UI designer creates components and pages in Figma
- Uses Auto Layout, component variants, and design tokens
- Design reviews happen in Figma with comments
- Developer inspects designs in Dev Mode

**Step 2: Figma to Code (Design Tokens + Code Connect)**

**Design Tokens:**
- Define colors, typography, spacing, shadows in Figma Variables
- Export as W3C Design Tokens JSON using Figma plugin (e.g., "Variables Import Export" by Luckino)
- Transform to CSS custom properties or Tailwind @theme values using Style Dictionary or custom build script
- Keep the source of truth in the repo, sync periodically from Figma

**Code Connect (Figma feature):**
- Code Connect links Figma components to actual code components
- When a developer selects a component in Figma Dev Mode, they see the real code snippet
- Two approaches:
  - **Code Connect CLI**: Runs locally, uses `.figma.ts` mapping files in your repo
  - **Code Connect UI**: Runs inside Figma, connects to GitHub for code context
- Supports React, HTML, and other frameworks

**Code Connect Setup:**
```bash
# Install Code Connect CLI
npm install -D @figma/code-connect

# Initialize in your project
npx figma connect init

# Create a connection file
npx figma connect create src/components/ActivityCard.astro
```

**Example Code Connect file:**
```typescript
// src/components/ActivityCard.figma.ts
import figma from "@figma/code-connect";

figma.connect("https://figma.com/design/FILE_KEY/NODE_KEY", {
  props: {
    title: figma.string("Title"),
    image: figma.string("Image URL"),
    category: figma.enum("Category", {
      Skiing: "skiing",
      Hiking: "hiking",
      Onsen: "onsen",
    }),
    price: figma.string("Price"),
  },
  example: (props) =>
    `<ActivityCard
      title="${props.title}"
      image="${props.image}"
      category="${props.category}"
      price="${props.price}"
    />`,
});
```

**Step 3: Develop in VS Code with Astro**
- Write `.astro` components using Tailwind CSS
- Use Astro content collections for Notion-sourced content
- Client-side islands (React/Svelte) for interactive elements (booking form, availability checker)
- Use Supabase client for data operations
- Run `astro dev` for local development with hot reload

**Step 4: Push to GitHub**
- Feature branches for new work
- Pull Request with preview deployment on Render
- Code review by team member
- Merge to `main` triggers auto-deploy

**Step 5: Render Builds and Deploys**
- On push to `main`: Render pulls code, runs `npm run build`
- Build process:
  1. `prebuild` script syncs Notion images to R2 (if configured)
  2. Astro fetches Notion content via notion-astro-loader
  3. Astro builds static HTML, optimizes images, bundles CSS/JS
  4. Output placed in `dist/` directory
- Render serves static files from its CDN
- Deploy hooks allow scheduled rebuilds for content freshness

**Step 6: Cloudflare CDN Delivers**
- Cloudflare edge caches static assets globally
- Users in Asia, Americas, Europe all get fast response times
- SSL termination at the edge
- DDoS protection and WAF filtering
- Cache invalidation on new deploys

**Step 7: Runtime Data from Supabase**
- Public pages are static (fast, cached)
- Interactive elements (booking form) fetch real-time data from Supabase
- Authentication handled by Supabase Auth
- Realtime subscriptions for availability updates

### Notion Webhooks and Build Triggers

**The Challenge**: Content editors update Notion, but the static site won't reflect changes until a rebuild.

**Solutions (ranked by complexity):**

1. **Scheduled Rebuilds (Simplest)**
   - GitHub Actions cron job triggers Render deploy hook every 1-2 hours
   - Pros: Simple, reliable, no additional infrastructure
   - Cons: Up to 2 hours delay for content updates

2. **Notion Webhooks (2025+ Feature)**
   - Notion now supports outgoing webhooks (released 2025)
   - Configure webhook to fire on database page updates
   - Target: Render deploy hook URL or GitHub Actions webhook
   - Pros: Near-real-time content updates
   - Cons: Every small edit triggers a rebuild

3. **Automation Service (Make.com / Zapier)**
   - Monitor Notion database for changes
   - Add debounce logic (wait 10 minutes after last change before triggering)
   - Trigger Render deploy hook
   - Pros: Intelligent batching of changes
   - Cons: Additional service cost and dependency

4. **Manual "Publish" Button in Notion**
   - Add a "Trigger Publish" button in Notion that sends a webhook
   - Editors explicitly choose when to publish
   - Pros: Full control, no unnecessary rebuilds
   - Cons: Extra step for editors

### Figma MCP Integration (2026)

The Figma MCP server allows AI coding assistants to:
- Read design files and extract component specifications
- Access design tokens and variables
- Understand component structure and variants
- Generate code that matches the design intent

```json
// MCP configuration for Figma
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@anthropic/figma-mcp-server"],
      "env": {
        "FIGMA_ACCESS_TOKEN": "your-figma-token"
      }
    }
  }
}
```

This enables a workflow where the AI assistant can:
1. Read the Figma design for a new page
2. Understand the component structure and design tokens
3. Generate Astro components that match the design
4. Apply correct Tailwind classes based on design specifications

---

## 11. Astro Framework: Advanced Topics

### Astro 5 Key Features (Current Production Version)

**Content Layer API (Stable in v5):**
- Unified API for local and remote content sources
- Up to 5x faster builds for Markdown-heavy sites
- 25-50% memory reduction compared to v4
- Type-safe content with Zod schema validation
- Community loaders for any data source (Notion, Sanity, WordPress, etc.)

**Server Islands:**
- Extend the Islands architecture concept to server-rendered components
- Combine high-performance static HTML with dynamic server-generated components on the same page
- Useful for personalized content within otherwise static pages
- Example: Static activity page with a dynamic "availability" island

```astro
---
// Static page with a server island
import AvailabilityChecker from '../components/AvailabilityChecker.astro';
---
<h1>Ski Lesson at Myoko Kogen</h1>
<p>Static content about the ski lesson...</p>

<!-- This component renders on the server on each request -->
<AvailabilityChecker server:defer activityId="ski-lesson-myoko" />
```

**View Transitions:**
- Built-in page transition animations without JavaScript framework
- Smooth navigation between pages
- Persistent elements across page navigations
- Great for tourism sites where immersive browsing experience matters

### Astro 6 Beta (Early 2026 - Plan for Migration)

**Major Changes:**
- **Cloudflare Acquisition**: Astro team acquired by Cloudflare in January 2026
- Framework stays MIT-licensed and open-source
- **Vite Environment API**: New build infrastructure
- **Workerd dev server**: Dev/prod parity for Cloudflare adapter users
- **Live Content Collections**: Fetch data at runtime instead of build time (stable in v6)
- **Fonts API**: Built-in font optimization
- **CSP Support**: Content Security Policy built-in
- **Zod 4**: Updated schema validation

**Migration Consideration:**
- Stay on Astro 5.x for production stability now
- Plan migration to Astro 6 once it reaches stable release (expected mid-2026)
- Live content collections in v6 could replace the need for scheduled rebuilds for dynamic data

### Astro vs Next.js: Why Astro for ComInc.

| Criterion | Astro | Next.js |
|-----------|-------|---------|
| **Default JS shipped** | Near-zero (8 KB) | ~85 KB |
| **Build speed (1000 pages)** | ~18 seconds | ~52 seconds |
| **Lighthouse Performance** | 95-100 | 85-95 |
| **First Content Render** | ~0.5 seconds | 1-1.5 seconds |
| **Content collections** | First-class with Content Layer API | Basic with MDX |
| **Learning curve** | Lower (HTML-first) | Higher (React-first) |
| **Island architecture** | Native | Manual code-splitting |
| **Best for** | Content/marketing sites | Dynamic web apps |
| **Cloudflare support** | Excellent (acquired by CF) | Good (via adapter) |

**Verdict for ComInc.**: Astro is the clear choice because:
- Tourism sites are primarily content-driven (guides, articles, listings)
- Performance directly impacts SEO and user experience
- Minimal JavaScript means faster load times on mobile (important for tourists on data)
- Content Layer API perfectly fits the Notion-as-CMS pattern
- Islands architecture allows interactive booking components where needed
- Cloudflare acquisition means excellent edge deployment support going forward

---

## 12. GitHub Workflow & Branch Strategy

### Branch Strategy

```
main (production)
  |
  +-- develop (staging / integration)
       |
       +-- feature/homepage-redesign
       +-- feature/booking-form
       +-- content/winter-2026-guides
       +-- fix/language-switcher-mobile
       +-- chore/update-dependencies
```

**Branch naming conventions:**
- `feature/*` - New features or pages
- `content/*` - Content updates that require code changes
- `fix/*` - Bug fixes
- `chore/*` - Maintenance, dependency updates, config changes
- `hotfix/*` - Emergency production fixes (branch from `main`, merge directly)

### Git Flow Summary

1. Create feature branch from `develop`
2. Develop and commit (small, focused commits)
3. Push branch, open Pull Request to `develop`
4. Render creates preview environment automatically
5. Code review + visual QA on preview URL
6. Merge to `develop` -> auto-deploys to staging
7. When sprint is ready: merge `develop` to `main` -> auto-deploys to production
8. Cloudflare cache purge after production deploy

### Pull Request Template

```markdown
<!-- .github/pull_request_template.md -->
## Summary
<!-- Brief description of changes -->

## Type
- [ ] Feature
- [ ] Bug fix
- [ ] Content update
- [ ] Chore / maintenance

## Changes
<!-- List specific changes -->
-
-

## Bilingual
- [ ] JA content added/updated
- [ ] EN content added/updated
- [ ] Language switcher tested
- [ ] hreflang tags verified

## Testing
- [ ] Tested on mobile viewport
- [ ] Tested in Chrome and Safari
- [ ] Lighthouse score checked (Performance >= 90)
- [ ] No console errors
- [ ] Links verified (no 404s)

## Preview URL
<!-- Render preview environment URL -->

## Screenshots
<!-- If visual changes, include before/after -->
```

### GitHub Actions CI Pipeline

```yaml
# .github/workflows/ci.yml
name: CI
on:
  pull_request:
    branches: [develop, main]
  push:
    branches: [develop, main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm

      - run: npm ci

      - name: Type check
        run: npx astro check

      - name: Build
        run: npm run build
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          NOTION_DATABASE_ID: ${{ secrets.NOTION_DATABASE_ID }}
          PUBLIC_SUPABASE_URL: ${{ secrets.PUBLIC_SUPABASE_URL }}
          PUBLIC_SUPABASE_ANON_KEY: ${{ secrets.PUBLIC_SUPABASE_ANON_KEY }}

      - name: Lighthouse CI
        uses: treosh/lighthouse-ci-action@v12
        with:
          urls: |
            http://localhost:4321/
            http://localhost:4321/en/
          uploadArtifacts: true
          temporaryPublicStorage: true
```

### Scheduled Rebuild for Content Freshness

```yaml
# .github/workflows/scheduled-rebuild.yml
name: Scheduled Rebuild
on:
  schedule:
    - cron: '0 */2 * * *'  # Every 2 hours
  workflow_dispatch:         # Manual trigger

jobs:
  trigger-render-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy
        run: curl -X POST "${{ secrets.RENDER_DEPLOY_HOOK_URL }}"

      - name: Wait for build
        run: sleep 180

      - name: Purge Cloudflare Cache
        run: |
          curl -X POST "https://api.cloudflare.com/client/v4/zones/${{ secrets.CF_ZONE_ID }}/purge_cache" \
            -H "Authorization: Bearer ${{ secrets.CF_API_TOKEN }}" \
            -H "Content-Type: application/json" \
            --data '{"purge_everything":true}'
```

### Required GitHub Secrets

| Secret | Description |
|--------|-------------|
| `NOTION_TOKEN` | Notion integration API key |
| `NOTION_DATABASE_ID` | Main content database ID |
| `PUBLIC_SUPABASE_URL` | Supabase project URL |
| `PUBLIC_SUPABASE_ANON_KEY` | Supabase anonymous key |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase service role key (server only) |
| `RENDER_DEPLOY_HOOK_URL` | Render deploy webhook URL |
| `CF_ZONE_ID` | Cloudflare zone ID for cominc.co |
| `CF_API_TOKEN` | Cloudflare API token with cache purge permission |
| `R2_ACCESS_KEY_ID` | Cloudflare R2 access key |
| `R2_SECRET_ACCESS_KEY` | Cloudflare R2 secret key |

---

## 13. Astro Prefetch & View Transitions

### Prefetch Configuration

Astro's prefetch feature pre-loads pages when users hover over links, making navigation feel instant:

```javascript
// astro.config.mjs
export default defineConfig({
  prefetch: {
    prefetchAll: false,        // Only prefetch links with data-astro-prefetch
    defaultStrategy: 'hover',  // Options: 'hover', 'tap', 'viewport', 'load'
  },
});
```

```html
<!-- Explicit prefetch on specific links -->
<a href="/en/activities/ski-lesson" data-astro-prefetch>Ski Lesson</a>

<!-- Override strategy per link -->
<a href="/en/about" data-astro-prefetch="viewport">About</a>

<!-- Tap strategy for mobile (less aggressive) -->
<a href="/en/booking" data-astro-prefetch="tap">Book Now</a>
```

### View Transitions

```astro
---
// src/layouts/BaseLayout.astro
import { ViewTransitions } from 'astro:transitions';
---
<html>
<head>
  <ViewTransitions />
</head>
<body>
  <!-- Persistent elements across navigations -->
  <header transition:persist>
    <nav>...</nav>
  </header>

  <!-- Animated page content -->
  <main transition:animate="slide">
    <slot />
  </main>

  <!-- Persistent footer -->
  <footer transition:persist>...</footer>
</body>
</html>
```

**Named transitions for specific elements:**
```astro
<!-- On listing page -->
<img src={activity.image} transition:name={`activity-${activity.id}`} />

<!-- On detail page (same transition name = morphing animation) -->
<img src={activity.image} transition:name={`activity-${activity.id}`} />
```

### Performance Impact
- Prefetch reduces perceived navigation time to near-zero
- View Transitions provide SPA-like experience in a Multi-Page Application
- Both work seamlessly with Astro's island architecture and Server Islands
- Important: Test "tap" strategy fix (merged Oct 2025) if using View Transitions

---

## Quick Reference: Environment Variables

```bash
# .env.example
# Notion CMS
NOTION_TOKEN=ntn_your_integration_token
NOTION_DATABASE_ID=your_database_id

# Supabase
PUBLIC_SUPABASE_URL=https://your-project.supabase.co
PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Cloudflare R2 (for image sync script)
CF_ACCOUNT_ID=your_cloudflare_account_id
R2_ACCESS_KEY_ID=your_r2_access_key
R2_SECRET_ACCESS_KEY=your_r2_secret_key

# Render
RENDER_DEPLOY_HOOK_URL=https://api.render.com/deploy/srv-xxx?key=xxx
```

## Quick Reference: Package Installation
```bash
# Core
npm create astro@latest
npm install @astrojs/tailwind tailwindcss

# Notion CMS
npm install notion-astro-loader
# or: npm install @chlorinec-pkgs/notion-astro-loader

# Supabase
npm install @supabase/supabase-js @supabase/ssr

# SSR adapter (if needed)
npm install @astrojs/node

# Image sync to R2
npm install @aws-sdk/client-s3 @notionhq/client

# Dev tools
npm install -D tsx typescript
```

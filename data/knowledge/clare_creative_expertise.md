# Clare - Creative Designer Knowledge Base
## ComInc. — Inbound Tourism, Joetsu/Myoko, Niigata, Japan

Last updated: 2026-03-28

---

## 1. Tourism Website Design Trends 2025-2026

### Immersive Visual Storytelling
- **Full-screen hero imagery and video**: The best tourism sites open with sweeping, high-definition visuals — 360-degree virtual tours, drone footage, ambient background video — that instantly transport visitors to the destination. Travel is an emotional purchase; design must trigger wanderlust within the first 3 seconds.
- **Parallax and scroll-driven animation**: Layered scrolling creates depth and narrative flow, guiding users through a story-like experience of the destination.
- **Interactive elements**: Hover-to-reveal details, animated maps, and clickable itinerary timelines keep users engaged beyond passive browsing.

### Benchmark Sites to Study
- **japan.travel** (JNTO): Clean layout, excellent photography, strong multi-language support, seasonal content rotation.
- **experienceniseko.com**: Seasonal content strategy (winter/summer), practical info blended with inspirational imagery, resort maps with QR codes.
- **nisekotourism.com**: Regional area distinction (Kutchan, Niseko Town, Rankoshi), weather integration, foreigner-friendly infrastructure info.
- **visit-hokkaido.jp**: Luxury positioning, long-form storytelling, high-end photography direction.

### Key Visual Trends
| Trend | Application for Myoko/Joetsu |
|-------|------------------------------|
| Hyper-immersive video | Drone footage of Myoko Kogen powder snow, onsen steam, rice terraces |
| AI-personalized imagery | Show ski content to adventure seekers, onsen/ryokan to relaxation seekers |
| Sustainability visuals | Highlight eco-friendly practices, satoyama landscapes, local food culture |
| Localized authenticity | Feature real locals, artisans, farmers — not stock photos |
| VR/3D previews | Virtual tours of ski runs, ryokan rooms, hiking trails |
| Seasonal design rotation | Swap hero imagery and color accents per season (snow/sakura/green/koyo) |

### Design Principles from Top Sites
1. **Less chrome, more content**: Minimal UI elements; let photography and video be the primary interface.
2. **Emotional-first, functional-second**: Lead with inspiration (hero image/video), follow with logistics (booking, access).
3. **Mobile-first responsive**: 60%+ of travel searches start on mobile. Design for mobile, then scale up.
4. **Speed as a feature**: Compress hero images; use WebP/AVIF; lazy-load below-fold content. Target under 500KB total image weight per page.

---

## 2. Brand Identity for Small Tourism Businesses

### Logo Design for Tourism
- **Incorporate destination elements**: Logos that subtly reference the destination (mountain silhouette, snow crystal, hot spring steam) help travelers make instant associations.
- **Simplicity and scalability**: Logo must work at favicon size (16x16px) and billboard scale. Avoid overly intricate designs.
- **Typography**: Sans-serif fonts (clean, modern, approachable) dominate tourism. Consider bilingual logotype — a Latin typeface paired with a complementary Japanese typeface.
- **Icon + wordmark combo**: Most versatile format. Icon alone for social media avatars; full lockup for headers and print.

### Color Psychology for Travel Brands

| Color | Emotion | Tourism Application |
|-------|---------|---------------------|
| **Blue** | Trust, calm, serenity | Luxury travel, sky/water themes, reliability |
| **Green** | Nature, sustainability, health | Eco-tourism, outdoor adventure, mountain/forest |
| **White** | Purity, simplicity, snow | Winter sports, clean design, Japanese minimalism |
| **Red/Vermillion** | Energy, passion, excitement | Adventure travel, torii gates, Japanese accent color |
| **Gold/Warm beige** | Premium, warmth, tradition | Onsen/ryokan, cultural experiences |
| **Deep navy** | Sophistication, depth | Premium positioning, evening/winter imagery |

### Recommended Palette Direction for Myoko/Joetsu
- **Primary**: Deep forest green (#2D5016) or mountain blue (#1B4965) — anchors the brand in nature.
- **Secondary**: Snow white (#F8F9FA) + warm wood (#C4A882) — references traditional Japanese architecture.
- **Accent**: Vermillion (#D64933) — nods to torii gates, autumn leaves, Japanese cultural markers.
- **Seasonal variants**: Swap accent colors per season (sakura pink for spring, fresh green for summer, maple red for autumn, powder blue for winter).

### Photography Direction
- **Authentic over polished**: Show real moments — steam rising from an onsen at dawn, a local farmer at work, fresh powder on untouched slopes.
- **Human element**: Include people experiencing the destination (not posing). This helps visitors project themselves into the scene.
- **Golden hour priority**: Schedule shoots at sunrise/sunset for warm, emotional light.
- **Seasonal consistency**: Build a photo library organized by season. Each season needs hero images, detail shots, and lifestyle/activity images.
- **Aspect ratios to prepare**: 16:9 (hero/video), 1:1 (social), 4:5 (Instagram feed), 9:16 (Stories/Reels), 3:2 (blog/editorial).

### Japanese Traditional Color Reference (Nippon Colors)
Japan has over 250 named traditional colors drawn from nature and seasons. Key ones for Myoko/Joetsu branding:
- **Wasurenagusa-iro (勿忘草色)**: Forget-me-not blue — spring
- **Wakakusa-iro (若草色)**: Young grass green — early summer
- **Momiji-iro (紅葉色)**: Maple red — autumn
- **Yukishiro (雪白)**: Snow white — winter
- **Kitsune-iro (狐色)**: Fox brown — warm earth tones

---

## 3. Figma Best Practices

### Component Library Architecture
- **Multi-file, modular approach**: Separate your Figma files into dedicated libraries:
  - `Tokens & Variables` — foundational design tokens
  - `Core Components` — buttons, inputs, cards, navigation
  - `Page Templates` — hero sections, activity grids, booking forms
  - `Platform Variants` — Web, iOS, Android if needed
- **Naming convention**: Use clear, hierarchical naming: `Button/Primary/Default`, `Button/Primary/Hover`, `Card/Activity/Large`.
- **Documentation**: Add descriptions to every component. Use component annotations for developer notes.

### Auto-Layout Mastery
- **Use auto-layout on everything**: Every frame should use auto-layout for true responsiveness. Avoid fixed positioning except for overlays.
- **Nested auto-layout**: Combine horizontal and vertical auto-layouts for complex, responsive compositions.
- **Min/max width constraints**: Set constraints so components behave correctly across breakpoints (mobile 375px, tablet 768px, desktop 1440px).
- **Padding and gap tokens**: Use variables for spacing (4, 8, 12, 16, 24, 32, 48, 64, 96) rather than arbitrary values.

### Design Tokens & Variables (2025/2026 Best Practice)
Design tokens are the atomic language bridging design and code. Structure in three layers:

1. **Primitive tokens** (raw values):
   - `color.green.500: #2D5016`
   - `spacing.16: 16px`
   - `font.size.lg: 18px`

2. **Semantic tokens** (purpose-driven):
   - `color.brand.primary → color.green.500`
   - `spacing.component.padding → spacing.16`
   - `font.heading.size → font.size.lg`

3. **Component tokens** (specific applications):
   - `button.primary.background → color.brand.primary`
   - `card.padding → spacing.component.padding`

**Variable types in Figma (2025/2026)**:
- Number (spacing, opacity, border-radius)
- Color (raw + semantic tokens)
- String (labels, CSS outputs)
- Boolean (state logic — show/hide)
- Alias/Reference (theme switching)

**Key principle**: Your Figma variable names become your code variable names. Modes in Figma equal themes in code. Keep naming identical across design and development.

### Developer Handoff
- **Use Dev Mode**: Figma's Dev Mode provides code-ready views with precise properties and values directly from the canvas.
- **Code Connect**: Map real code components to Figma components so developers see actual code snippets, not just CSS approximations.
- **Mark "Ready for dev"**: Use Figma's status feature to signal when a frame is approved and ready for implementation.
- **Link to tickets**: Connect Figma frames to Jira/Linear tickets and documentation.
- **Annotate interactions**: Use prototyping + annotations to show hover states, transitions, and micro-interactions.
- **Accessibility plugins**: Run Stark or Contrast checker before handoff. Include contrast ratios in annotations.

---

## 4. SNS Visual Design

### Instagram Strategy for Tourism

#### Feed Post Templates (1080x1080 or 1080x1350)
- **Destination showcase**: Full-bleed photo with subtle branded overlay (logo watermark, location tag).
- **Information carousel**: Swipeable slides — "5 Things to Do in Myoko" — consistent header bar, numbered slides, CTA on final slide.
- **Quote/testimonial**: Guest review overlaid on atmospheric photo, brand fonts and colors.
- **Before/after or seasonal comparison**: Split-screen showing same location in different seasons.

#### Stories & Reels Templates (1080x1920)
- **Day-in-the-life**: Vertical video with branded lower-third (location + activity name).
- **Quick tip**: Text-overlay format — "Did you know? Myoko has 3 distinct onsen areas."
- **Behind-the-scenes**: Staff or local artisan feature with informal, authentic feel.
- **Poll/quiz interactive**: "Which season would you visit?" with swipe-up for booking.

#### Visual Consistency System
- **Color overlay**: Apply a subtle brand-colored gradient or filter to all images for cohesion.
- **Typography**: Max 2 fonts — 1 display (headings) + 1 body (captions). Use consistently across all posts.
- **Grid planning**: Plan the Instagram grid 9-12 posts ahead. Alternate between close-up, wide-angle, and graphic posts for visual rhythm.
- **Template toolkit in Figma**: Create a shared Figma library of 8-12 reusable templates. Swap photos but keep structure identical.

### Multi-Platform Consistency
| Platform | Format | Priority Content |
|----------|--------|-----------------|
| Instagram Feed | 1:1 or 4:5 | Polished destination photos, carousels |
| Instagram Reels | 9:16 | Short-form video (15-60s), trending audio |
| TikTok | 9:16 | Raw/authentic video, POV experiences |
| YouTube | 16:9 | Long-form guides, seasonal highlight reels |
| LINE (Japan) | Various | Event announcements, coupons, rich messages |
| Facebook | 16:9 / 1:1 | Event promotion, longer captions, community |

### Content Trends for Travel Brands (2025-2026)
- **UGC (User-Generated Content) outperforms studio content**: Repost guest photos/videos with permission. Authentic beats polished.
- **Short-form video dominates**: Reels and TikToks are the primary discovery channels. Gen Z and Millennials search TikTok/Instagram instead of Google for "what to do in [destination]."
- **Story-driven content**: Behind-the-scenes, staff introductions, "a day in Myoko" narratives build emotional connection.
- **Interactive features**: Polls, quizzes, countdown stickers for events boost engagement algorithm signals.

---

## 5. Japanese Aesthetics in Web Design

### Core Concepts

#### Wabi-Sabi (侘寂) — Beauty in Imperfection
- **Web application**: Organic textures (paper grain, brush strokes), slightly imperfect hand-drawn elements, natural materials in photography.
- **Design technique**: Add subtle grain or noise to backgrounds. Use hand-lettered accents alongside clean typography. Embrace asymmetric layouts.
- **Photography**: Show weathered wood, steam-fogged windows, worn stepping stones — beauty of age and use, not newness.

#### Ma (間) — The Power of Empty Space
- **Web application**: Generous whitespace is not wasted space — it is the design. Let images breathe. Use large margins between sections.
- **Design technique**: Content sections separated by 80-120px+ of whitespace. Single focal point per viewport. Allow the user's eye to rest.
- **Key insight**: While Japanese domestic websites are famously information-dense, tourism sites targeting international audiences should embrace Ma. The target audience (Western inbound tourists) expects and appreciates whitespace-driven design.

#### Mono no Aware (物の哀れ) — Pathos of Things / Seasonal Sensitivity
- **Web application**: Rotate visual themes with the seasons. Cherry blossoms in spring, lush green rice terraces in summer, fiery koyo in autumn, pristine snow in winter.
- **Design technique**: Seasonal color palette shifts, seasonal hero imagery, seasonal activity recommendations that auto-rotate or are manually curated.

#### Kanso (簡素) — Simplicity and Elimination of Clutter
- **Web application**: Remove decorative elements that don't serve function. Every pixel should earn its place.
- **Design technique**: Flat design with minimal shadows. Limited color palette. Clear typography hierarchy.

#### Shibui (渋い) — Subtle, Unobtrusive Beauty
- **Web application**: Understated elegance. Avoid flashy animations or garish colors. Let content quality speak.
- **Design technique**: Muted color palettes, slow/gentle transitions, serif or brush-style typography accents.

### Balancing Japanese and International Design Expectations
- **The paradox**: Japanese domestic users prefer information-dense, text-heavy layouts. Western visitors expect clean, image-driven, whitespace-rich design.
- **Solution for ComInc.**: Since the primary audience is inbound (Western) tourists, lean toward international design conventions with Japanese aesthetic accents. Use Ma and Kanso as organizing principles, with Wabi-sabi textures and Mono no Aware seasonal theming as distinctive touches.
- **Bilingual consideration**: Japanese text is 30-60% shorter in character count than English for equivalent meaning, but Japanese sites typically use 150% more text overall. Design layouts that accommodate both languages gracefully.

---

## 6. Accessibility in Design

### WCAG 2.1 AA Compliance — Essential Requirements

#### Color Contrast
| Element | Minimum Contrast Ratio |
|---------|----------------------|
| Normal text (under 18pt/24px) | 4.5:1 |
| Large text (18pt/24px bold, or 24pt/32px) | 3:1 |
| UI components & graphics | 3:1 against adjacent colors |
| Decorative/non-functional images | No requirement |

- **Test tools**: Use Stark (Figma plugin), WebAIM Contrast Checker, or built-in browser DevTools.
- **Common failures**: Light gray text on white backgrounds, colored text on photo backgrounds without overlay, low-contrast placeholder text in forms.
- **Fix for photos with text**: Always use a semi-transparent dark overlay (minimum 40% opacity black) behind text placed on photographs.

#### Do Not Rely on Color Alone
- Error states: Use icon + color + text (not just red).
- Required fields: Use asterisk + label, not just color change.
- Charts and maps: Use patterns, labels, or icons in addition to color coding.

#### Touch Targets
- **Minimum**: 44x44px (WCAG recommendation).
- **Recommended**: 48x48px (Google Material Design standard).
- **Spacing**: Ensure at least 8px between adjacent touch targets.

#### Responsive Images
- **Alt text**: Every meaningful image must have descriptive alt text. Decorative images get `alt=""`.
- **Responsive srcset**: Provide 3-5 image sizes (400w, 800w, 1200w, 1600w) using `<picture>` or `srcset`.
- **Format**: Use WebP as default (25-35% smaller than JPEG at equivalent quality), with JPEG fallback. Consider AVIF for next-gen browsers.
- **Hero images**: Load eagerly with `fetchpriority="high"`. Never lazy-load the LCP (Largest Contentful Paint) image.
- **Below-fold images**: Use `loading="lazy"` for native browser lazy loading.
- **Specify dimensions**: Always set `width` and `height` attributes to prevent layout shift (CLS).

#### Typography Accessibility
- **Minimum body text**: 16px (1rem).
- **Line height**: 1.5x font size minimum for body text.
- **Paragraph width**: 45-75 characters per line (optimal readability).
- **Font choice**: Avoid thin/ultralight weights below 18px. Ensure Japanese fonts render clearly at small sizes (Noto Sans JP, Yu Gothic, Hiragino Sans).

#### Motion and Animation
- **Respect `prefers-reduced-motion`**: Disable or reduce animations for users who have set this OS preference.
- **No auto-playing video with sound**: Background videos must be muted by default with visible play/pause controls.
- **Avoid flashing content**: Nothing should flash more than 3 times per second.

### Legal Context (2025-2026)
- **European Accessibility Act (EAA)**: Aligns with WCAG 2.1 AA. Compliance deadline is active.
- **US ADA**: WCAG 2.1 AA referenced in standards. Compliance deadlines: 2026 for large entities, 2027 for smaller ones.
- **Japan JIS X 8341-3**: Japanese accessibility standard aligns closely with WCAG 2.1.

### Figma Accessibility Workflow
1. **During design**: Use Stark plugin to check contrast on every text/background combination.
2. **Component level**: Build accessible states into components (focus rings, error states, disabled states).
3. **Before handoff**: Run full accessibility audit. Annotate tab order, landmark regions, and ARIA labels.
4. **Image preparation**: Write alt text in Figma annotations so developers don't have to guess.

---

## Quick Reference: Tools & Resources

### Figma Plugins
- **Stark**: Accessibility checker (contrast, vision simulation)
- **Contrast**: Quick contrast ratio checking
- **Unsplash / Pexels**: Stock photography (use sparingly; prefer original)
- **Iconify**: Icon library access
- **Content Reel**: Realistic placeholder content

### Color Tools
- **Nippon Colors** (nipponcolors.com): Traditional Japanese color reference
- **Coolors**: Palette generation and contrast checking
- **Colour Contrast Analyser**: Desktop app for precise checking

### Typography
- **Google Fonts**: Noto Sans JP (excellent Japanese + Latin coverage)
- **Adobe Fonts**: Source Han Sans, Kozuka Gothic
- **Variable fonts**: Reduce file size while offering weight flexibility

### Image Optimization
- **Squoosh** (squoosh.app): Browser-based WebP/AVIF conversion
- **ImageOptim**: Mac batch optimization
- **Cloudinary / imgix**: CDN-based automatic optimization and responsive delivery

### Inspiration
- **japan.travel**: JNTO official site
- **japanwebdesign.com**: Gallery of modern Japanese website designs
- **awwwards.com**: Award-winning web design
- **Dribbble/Behance**: Search "tourism website" or "travel UI"

---

*This knowledge base is tailored for Clare's role as Creative Designer at ComInc., focusing on visual design decisions for an inbound tourism business in the Joetsu/Myoko region of Niigata, Japan.*

# Yuri - UX/UI Designer Knowledge Base
## ComInc. — Inbound Tourism, Joetsu/Myoko, Niigata, Japan

Last updated: 2026-03-28

---

## 1. Tourism Website UX Best Practices

### Booking Flow Design
The booking journey is the critical conversion path. Research from Baymard Institute and industry leaders shows:

#### The 3-Step Rule
- **Limit the booking flow to 3 screens maximum**: Each step should have one clear task. A simple progress bar shows where the user stands and what comes next.
  - Step 1: **Select** — Choose activity/accommodation, dates, number of guests
  - Step 2: **Customize** — Add options, select preferences, review details
  - Step 3: **Confirm & Pay** — Contact info, payment, confirmation

#### Pricing Transparency
- **Show the full price early**: Display total cost (including taxes and fees) as soon as possible — ideally on the search results page. Surprise fees at checkout are the #1 cause of booking abandonment.
- **Explain inclusions**: Clearly state what is and isn't included (equipment rental, transport, meals, insurance).
- **Refund policy visibility**: Show cancellation policy prominently before the user commits.

#### Form Optimization
- **Minimize fields**: Marketo's famous case study showed a 34% conversion increase by reducing form fields from 9 to 5. Ask only for what you need at each step.
- **Smart defaults**: Pre-fill dates (default to upcoming weekend), auto-detect currency and language from geolocation.
- **Input types**: Use date pickers (not text fields) for dates, stepper controls for guest counts, radio buttons for small option sets.
- **Inline validation**: Show errors as the user types, not after form submission. Use green checkmarks for valid fields.
- **Guest checkout**: Never require account creation to book. Offer it as an optional post-booking step.

#### Booking Engine Placement
- **Persistent booking access**: Users may decide to book at any moment. Place a booking button in the site header so it is accessible from every page with a single click.
- **Sticky booking bar on mobile**: A fixed bottom bar with price summary and "Book Now" CTA that stays visible during scroll.

### Mobile-First Patterns
- **65% of travel visits are mobile**, but mobile conversion (0.7%) lags far behind desktop (2.4%). This is a design problem, not an intent problem.
- **Thumb-friendly zones**: Place primary CTAs in the bottom third of the screen (natural thumb reach). Avoid top-corner actions on mobile.
- **Sticky booking bar**: Fixed bottom bar with price + CTA — always visible.
- **Bottom navigation**: Replace hamburger menus with visible bottom tab bars (Home, Explore, Favorites, Book, More).
- **Large touch targets**: Minimum 48x48px with 8px spacing between targets.
- **Swipeable content**: Image galleries, activity cards, and date selectors should support swipe gestures.

### Multi-Language UX
- **Auto-detect language**: Use browser language settings and IP geolocation to suggest (not force) the appropriate language.
- **Language selector in header**: Persistent, visible in every page state. Show language names in their native script ("日本語", not "Japanese").
- **URL structure**: Use path-based localization (`/en/`, `/ja/`, `/zh/`) for SEO and shareability.
- **Content parity**: All languages should have equivalent content. If a page exists in English, it must exist in Japanese and vice versa. Missing translations destroy trust.
- **Currency pairing**: Auto-switch currency with language, but allow independent override.

---

## 2. User Personas for Inbound Japan Tourism

### Persona 1: The Culture Explorer
| Attribute | Detail |
|-----------|--------|
| **Name** | "Sarah & Tom" |
| **Age** | 35-55 |
| **Origin** | North America, Europe, Australia |
| **Trip type** | First or second visit to Japan, 10-14 days |
| **Motivations** | Authentic cultural experiences, onsen, local food, scenic beauty, getting off the beaten path |
| **Pain points** | Language barrier anxiety, fear of missing hidden gems, complex rural transport |
| **Digital behavior** | Research on laptop, book on desktop, use mobile on-trip. Read blogs and reviews extensively before booking |
| **Design needs** | Detailed descriptions, high-quality photos of actual experiences, clear English content, transport guides, "what to expect" sections |
| **Key insight** | Westerners value hospitality (omotenashi) more than room quality. Staff friendliness and cultural guidance are differentiators |

### Persona 2: The Adventure Seeker
| Attribute | Detail |
|-----------|--------|
| **Name** | "Jake" |
| **Age** | 25-40 |
| **Origin** | Australia, North America, Europe (ski-focused markets) |
| **Trip type** | 5-10 days, often repeat visitor, ski/snowboard focused with cultural add-ons |
| **Motivations** | Japow (Japanese powder snow), backcountry, onsen after skiing, local izakaya |
| **Pain points** | Wants real-time snow/weather info, needs to compare areas quickly, skeptical of marketing-speak |
| **Digital behavior** | Mobile-first, uses Instagram/TikTok for discovery, books on mobile, values speed |
| **Design needs** | Live snow reports, quick comparison tools, bold visuals, minimal text, fast booking, peer reviews |
| **Key insight** | Adventure seekers (18-35) are spontaneous and mobile-first. Bold visuals and energetic copy that promise excitement perform best |

### Persona 3: The Family Planner
| Attribute | Detail |
|-----------|--------|
| **Name** | "The Tanaka-Smiths" |
| **Age** | 35-50 (parents) |
| **Origin** | Southeast Asia, Australia, North America |
| **Trip type** | 7-14 days, mixed itinerary, need kid-friendly activities |
| **Motivations** | Safe, memorable family experience, cultural education for children, nature activities |
| **Pain points** | Anxiety about logistics with children, dietary restrictions, need for English-friendly services, budget management |
| **Digital behavior** | Heavy pre-trip research (weeks/months ahead), compares options on laptop, reads parent-focused reviews |
| **Design needs** | Age-appropriate activity filters, family package pricing, safety information, accessibility details, "Is this suitable for children?" indicators |
| **Key insight** | Family personas book well in advance and respond to clear communication about inclusions, flexibility, and family discounts |

### Persona 4: The Solo Experiencer
| Attribute | Detail |
|-----------|--------|
| **Name** | "Mei" |
| **Age** | 25-35 |
| **Origin** | Taiwan, Hong Kong, Singapore, South Korea |
| **Trip type** | 3-7 days, solo or with one friend, Instagrammable experiences |
| **Motivations** | Photogenic spots, unique experiences to share, local food, self-discovery |
| **Pain points** | Solo pricing penalties, safety concerns, wants reassurance through reviews and social proof |
| **Digital behavior** | Discovers via Instagram/TikTok/Xiaohongshu, books on mobile, influenced by UGC and influencer content |
| **Design needs** | Solo-friendly pricing, social proof (reviews, photos), shareable content, clear safety info, easy mobile booking |
| **Key insight** | Solo travelers value flexibility, transparent pricing, and trust-building content like testimonials |

### Cross-Persona Insights
- **Western visitors spend more on accommodation** and tend to stay longer (first-timers especially).
- **Avoid over-romanticized imagery**: Travelers increasingly push back on "Perfect Japan" portrayals. Show authentic, realistic experiences.
- **Language barrier is the #1 anxiety** for first-time Western visitors to rural Japan. Address this explicitly in UX content.

---

## 3. Information Architecture for Tourism Sites

### Recommended Site Structure

```
Home
├── Destinations & Areas
│   ├── Myoko Kogen (ski, onsen, nature)
│   ├── Joetsu (history, culture, coast)
│   └── Surrounding Areas
├── Things to Do
│   ├── By Season (Winter / Spring / Summer / Autumn)
│   ├── By Type (Adventure / Culture / Relaxation / Food)
│   └── By Audience (Families / Couples / Solo / Groups)
├── Plan Your Trip
│   ├── Getting Here (from Tokyo, Osaka, airports)
│   ├── Getting Around (local transport, rental, taxi)
│   ├── Where to Stay (ryokan, hotels, guesthouses)
│   ├── Where to Eat
│   └── Practical Info (weather, packing, etiquette, WiFi, money)
├── Book / Reserve
│   ├── Activities & Tours
│   ├── Accommodation
│   └── Packages
├── Blog / Stories
│   ├── Local Guides
│   ├── Seasonal Highlights
│   └── Traveler Stories
└── About
    ├── About ComInc.
    ├── Contact
    └── FAQ
```

### Navigation Patterns

#### Primary Navigation
- **Desktop**: Horizontal top bar with dropdown mega-menus. Maximum 6-7 top-level items.
- **Mobile**: Bottom tab bar with 5 items (Home, Explore, Book, Plan, More). Avoid hamburger-only navigation — it hides critical paths.
- **Sticky header**: Navigation stays visible on scroll (but collapses to save space).

#### Secondary Navigation
- **Breadcrumbs**: Essential for deep content pages. Help users understand where they are and backtrack without the browser back button.
- **Contextual sidebar**: On destination/activity pages, show related activities, nearby attractions, and seasonal alternatives.
- **Quick filters**: On listing pages (activities, accommodation), provide prominent filter controls: season, type, price range, duration, difficulty level.

#### Search UX
- **Prominent search bar**: Visible on every page, not hidden behind an icon.
- **Autocomplete with categories**: As users type, show suggestions grouped by type ("Activities", "Areas", "Blog Posts").
- **Search by intent**: Support natural-language queries like "things to do with kids in winter" — even if via guided filters rather than free-text AI search.
- **No-results recovery**: When search returns nothing, suggest popular activities, seasonal picks, or broaden-your-search tips.

### Content Hierarchy Principles
1. **F-pattern and Z-pattern layouts**: Users scan in these patterns. Place key information (CTAs, prices, headings) along these sight lines.
2. **Progressive disclosure**: Show essential info first (what, where, when, how much). Expandable sections for detailed descriptions, policies, and logistics.
3. **Card-based design for activities**: Each activity gets a card with: hero image, title, duration, price, rating, and a single CTA. Cards are scannable and comparable.
4. **Season as primary organizer**: For a 4-season destination like Myoko, season should be the primary content filter. Users think "What can I do in winter?" before "What adventure activities exist?"

---

## 4. Conversion Optimization for Tourism

### CTA (Call-to-Action) Strategy

#### Placement Rules
- **Above the fold**: Primary CTA visible without scrolling on every landing page.
- **After value demonstration**: Place CTAs after testimonials, photo galleries, or detailed descriptions — when the user has absorbed enough value to act.
- **Sticky mobile CTA**: Bottom-fixed bar with price summary + "Book Now" that remains visible during scroll.
- **Every page is a landing page**: Users arrive from search, social, or links — not just the homepage. Every page needs a clear next action.

#### CTA Design
- **Action-oriented text**: "Book This Experience" > "Submit". "Check Availability" > "Click Here".
- **Urgency without manipulation**: "Limited spots for Feb 15" (if true) is acceptable. Fake countdown timers destroy trust.
- **Contrasting color**: CTA button should be the highest-contrast element on the page. If the brand is blue/green, the CTA can be warm (orange, vermillion).
- **Size**: Desktop minimum 44px height. Mobile minimum 48px height, full-width on mobile.

### Form Design for Bookings
- **Single-column layout**: Forms in one column convert better than multi-column.
- **Label above field**: Not inside (placeholder-only labels disappear and confuse users).
- **Step indicators**: Numbered progress bar ("Step 1 of 3") reduces abandonment anxiety.
- **Save & resume**: For complex bookings, allow users to save progress and return later.
- **Error recovery**: Red border + icon + specific error message ("Please enter a valid email") below the field.

### Trust Signals

#### Types and Placement
| Trust Signal | Where to Place |
|-------------|----------------|
| Star ratings & review count | Activity/accommodation cards and detail pages |
| Written reviews with photos | Below activity description, before booking CTA |
| Certification badges | Footer + near payment form |
| Secure payment icons | Checkout page, near credit card fields |
| Cancellation policy | Activity detail page + booking summary |
| Response time / availability | Booking form area |
| Social proof counters | "1,200 travelers loved this" near CTA |
| Partner logos | Footer (tourism boards, hotel associations) |

#### Key Statistics
- **83% of digital natives** say reviews play an important or very important role in booking decisions (TrustYou study).
- Trust evidence should be placed **near commitment points** (CTAs, payment forms), not buried in footers.
- User-submitted **photos alongside reviews** dramatically increase trust compared to text-only reviews.

### Conversion Benchmarks
- Average travel site conversion rate: **1-3%** (desktop), **0.5-1%** (mobile).
- **Target**: Optimize mobile conversion to close the gap with desktop. This is where the biggest gains are.
- **Key metrics to track**: Booking completion rate, form abandonment rate, bounce rate on landing pages, time-to-first-booking, search-to-booking ratio.

---

## 5. Bilingual UX Design

### Language Switcher Patterns

#### Design Recommendations (from Smashing Magazine / Smart Interface Design Patterns)
- **Placement**: Top-right corner of header (international convention). Persistent on all pages.
- **Icon**: Globe icon (🌐) is the most universally recognized. Avoid flags — they represent countries, not languages (e.g., English is spoken in many countries; a UK flag alienates Americans).
- **Label format**: Show current language name in its own script + globe icon. Example: "English 🌐" or "日本語 🌐".
- **Dropdown behavior**: Click to open (not hover). Show all available languages in their native script:
  - English
  - 日本語
  - 中文 (简体)
  - 한국어
- **No redirects**: When switching language, stay on the same page — just in the new language. Never redirect to the homepage.
- **Decouple language and country**: Allow users to set language and currency independently.

#### Implementation Details
- **URL structure**: `/en/activities/skiing` → `/ja/activities/skiing`. Path-based localization is best for SEO and link sharing.
- **hreflang tags**: Essential for SEO. Tell Google which language version to show to which users.
- **Language persistence**: Remember the user's language choice via cookie or localStorage. Don't reset on every visit.
- **Fallback strategy**: If a page isn't translated yet, show the English version with a notice ("This page is not yet available in 日本語") rather than a 404 or broken page.

### Handling Japanese-English Text Differences

#### Length and Layout Considerations
- **Japanese text is 30-60% shorter** in character count than English equivalents — but each character carries more visual weight.
- **Japanese sites traditionally use ~150% more text** than English counterparts due to cultural preference for detailed information.
- **Solution**: Design layouts with flexible containers. Test with both languages. Use auto-layout in Figma to ensure components adapt.

#### Typography
- **Font pairing**: Noto Sans JP handles both Japanese and Latin characters well, but dedicated font pairs (e.g., Noto Sans JP + Inter) give better results.
- **Line height**: Japanese text needs slightly more line height (1.7-1.8x) compared to Latin text (1.5x) for readability.
- **Font size**: Japanese characters are visually denser. Consider 1-2px larger body text for Japanese versions.
- **No decorative fonts for Japanese**: Avoid overly stylized kanji. Stick to clear, readable fonts like Noto Sans JP, Yu Gothic, or Hiragino Sans.

### Content Strategy for Bilingual Sites
- **Content parity is non-negotiable**: Every page in English must exist in Japanese and vice versa. Partial translation signals unprofessionalism.
- **Culturally adapted, not just translated**: Adjust tone, examples, and emphasis per audience. Japanese users want detailed specifications; Western users want emotional storytelling.
- **Date/time formats**: Japanese (2026年3月28日), English (March 28, 2026). Handle automatically based on language setting.
- **Address formats**: Japanese (prefecture → city → detail), English (detail → city → prefecture). Adapt per language.
- **Phone numbers**: Show international format (+81) for English, domestic format (0255-xx-xxxx) for Japanese.

---

## 6. Mobile UX for Travelers

### Offline Access Patterns
Travelers frequently lose connectivity — in rural areas, on trains, in mountains. Design for this reality.

#### What Must Work Offline
- **Saved/bookmarked trip details**: Booking confirmations, itineraries, and reservation info.
- **Maps**: Downloaded area maps with key points of interest, transport routes, and walking directions.
- **Phrasebook / emergency info**: Basic Japanese phrases, emergency numbers, hospital locations.
- **Previously viewed content**: Cache recently browsed activity pages and area guides.

#### Implementation Approaches
- **Progressive Web App (PWA)**: Enable offline mode via service workers. Cache critical pages and assets.
- **Downloadable PDF itineraries**: Generate a print-friendly PDF of the user's saved itinerary with maps and contact info.
- **QR code for offline access**: Provide QR codes at physical locations that link to cached/downloadable content.

### Location-Aware Features
- **Nearby activities**: Use GPS to show "Things to do near you" when the user is in the Myoko/Joetsu area.
- **Context-aware UI**: Change interface based on trip stage:
  - **Pre-trip (at home)**: Show planning tools, inspiration, booking.
  - **In-transit**: Show transport info, arrival guides, check-in details.
  - **On-location**: Show nearby activities, maps, real-time info (weather, snow report, restaurant hours).
  - **Post-trip**: Show review prompts, photo sharing, return visit incentives.
- **Weather integration**: Show current conditions and forecast on activity pages. For ski activities, integrate live snow depth and lift status.
- **Permission handling**: Request location permission at the moment of need with a clear explanation ("Allow location to find activities near you"), not on first app load.

### Quick-Action Patterns
- **Bottom navigation bar**: 5 visible tabs replacing the hamburger menu. Primary actions always one tap away.
- **Floating Action Button (FAB)**: Single prominent button for the #1 action (e.g., "Book" or "Get Directions").
- **Swipe gestures**: Swipe cards to save/dismiss activities. Swipe between gallery images. Pull-to-refresh for live data.
- **One-tap actions**: Phone-call buttons, map-open buttons, and share buttons should require a single tap from any detail page.
- **Quick booking from cards**: "Book Now" directly on activity cards in listing views — don't force users to open the detail page first for simple bookings.

### Mobile Navigation Best Practices (2025-2026)
- **Bottom tab bar > hamburger menu**: Bottom tabs show 4-5 primary destinations. Hidden hamburger menus reduce discoverability by up to 50%.
- **Gesture-based navigation**: Support swipe-back, pull-to-refresh, and swipe-between-tabs.
- **Contextual actions**: Show relevant actions based on the page (share, save, directions, call) in a consistent action bar.
- **Search always accessible**: Persistent search icon or bar on every screen.

### Travel-Specific Mobile Features
| Feature | Implementation | Priority |
|---------|---------------|----------|
| Live snow/weather report | API integration, auto-refresh | High (winter) |
| Digital boarding passes / tickets | QR code display, offline-capable | High |
| Emergency info | Cached offline, prominent placement | Critical |
| Currency converter | Simple inline tool or persistent widget | Medium |
| Real-time transport info | Train/bus schedule API integration | High |
| Photo spot finder | GPS + curated location database | Medium |
| Restaurant finder with English menus | Location-based, filter for "English menu" | High |
| Onsen finder | Location-based, filter for "tattoo-friendly" | High (unique value-add) |

### Performance Targets for Mobile
| Metric | Target |
|--------|--------|
| First Contentful Paint (FCP) | < 1.8 seconds |
| Largest Contentful Paint (LCP) | < 2.5 seconds |
| Cumulative Layout Shift (CLS) | < 0.1 |
| First Input Delay (FID) | < 100ms |
| Total page weight | < 1.5 MB |
| Image weight per page | < 500 KB |
| Time to Interactive (TTI) | < 3.5 seconds |

---

## Quick Reference: UX Research Methods

### For Persona Validation
- **User interviews**: 5-8 interviews per persona segment. Recruit via social media travel groups, tourist info centers, and partner accommodations.
- **Survey**: Distribute via email to past visitors, embed on website post-booking confirmation page.
- **Analytics review**: Google Analytics audience data, booking pattern analysis, device/language/location breakdowns.

### For IA Testing
- **Card sorting**: Open and closed card sorts with 15-20 participants to validate navigation categories.
- **Tree testing**: Test proposed site structure with users before building. Tools: Optimal Workshop, Maze.
- **First-click testing**: Show a homepage mockup and ask "Where would you click to find [X]?" Measure success rate.

### For Booking Flow Optimization
- **Usability testing**: Task-based testing with 5 participants per round. "Book a ski lesson for 2 people on February 15."
- **A/B testing**: Test CTA copy, form layouts, pricing display, trust signal placement.
- **Funnel analysis**: Track drop-off at each booking step. Identify and fix the biggest leak.
- **Heatmaps and session recordings**: Tools: Hotjar, Microsoft Clarity (free). Watch how real users interact with booking pages.

### For Mobile UX
- **Guerrilla testing**: Test with actual tourists. Visit tourist info centers, ski lodges, or ryokan lobbies and ask travelers to try the site on their own phone.
- **Device lab testing**: Test on actual devices common among target audiences (iPhones for Western tourists, Samsung for Asian tourists).
- **Performance auditing**: Lighthouse, PageSpeed Insights, WebPageTest. Test on 3G throttled connection to simulate rural Japan connectivity.

---

## UX Tools & Resources

### Wireframing & Prototyping
- **Figma**: Primary design tool. Use for wireframes, prototypes, and developer handoff.
- **Whimsical**: Quick flowcharts and user journey mapping.
- **Miro/FigJam**: Collaborative workshops, card sorting, affinity mapping.

### User Research
- **Maze**: Unmoderated usability testing, tree testing, surveys.
- **Optimal Workshop**: Card sorting, tree testing, first-click testing.
- **Hotjar**: Heatmaps, session recordings, feedback polls.
- **Microsoft Clarity**: Free heatmaps and session recordings.

### Analytics & Optimization
- **Google Analytics 4**: Traffic, audience, conversion tracking.
- **Google Search Console**: Search performance, Core Web Vitals monitoring.
- **VWO / Optimizely**: A/B testing platform for booking flow optimization.

### Accessibility
- **axe DevTools**: Automated accessibility testing.
- **WAVE**: Web accessibility evaluation tool.
- **Stark (Figma)**: Design-time accessibility checking.

### Multi-Language
- **Phrase / Crowdin**: Translation management platforms with context for translators.
- **i18next**: Frontend internationalization framework.
- **hreflang tag generator**: Aleyda Solis' free tool for multi-language SEO setup.

---

*This knowledge base is tailored for Yuri's role as UX/UI Designer at ComInc., focusing on user experience decisions for an inbound tourism business in the Joetsu/Myoko region of Niigata, Japan.*

# myokojoetsu.com Site Map

## Navigation Structure

```
myokojoetsu.com
|
|-- / (index.html)                    Homepage — hero, intro, categories, seasons, shop teaser, access
|
|-- Discover (dropdown)
|   |-- /shop.html                    Shop — crafts, goods, and things to bring home
|   |-- /eat.html                     Eat — food, sake, and where to find them
|   |-- /see.html                     See — sights, experiences, and things to do
|   |-- /stay.html                    Stay — accommodation, onsen, and farmhouses
|
|-- Seasons (dropdown)
|   |-- /winter.html                  Winter — Dec to Mar, snow, ski, onsen, new sake
|   |-- /spring.html                  Spring — Apr to May, cherry blossoms, snowmelt, rice paddies
|   |-- /summer.html                  Summer — Jun to Aug, hiking, lotus, festivals
|   |-- /autumn.html                  Autumn — Sep to Nov, harvest, foliage, clear skies
|
|-- /shop.html                        Shop (direct link, same as Discover > Shop)
|-- /#access                          Access (anchor on homepage)
```

---

## All Pages

### Homepage
- **File**: `index.html`
- **URL**: `/`
- **Title**: myokojoetsu.com — Snow country, quietly.
- **Meta description**: An editorial guide to Myoko and Joetsu in Niigata, Japan. Snow country's best kept secret.

---

### Discover Pages

#### Shop
- **File**: `shop.html`
- **URL**: `/shop`
- **Title**: Shop — myokojoetsu.com
- **Meta description**: Pottery, hand-forged blades, textiles, and fermented goods from Joetsu and Myoko. Things worth carrying home from Niigata snow country.

#### Eat
- **File**: `eat.html`
- **URL**: `/eat`
- **Title**: Eat — myokojoetsu.com
- **Meta description**: Hegi soba, sake from centuries-old breweries, and sea fish still tasting of the morning catch. A guide to eating in Myoko and Joetsu.

#### See
- **File**: `see.html`
- **URL**: `/see`
- **Title**: See — myokojoetsu.com
- **Meta description**: Takada Castle's night sakura, sacred Mt. Myoko, and powder snow you have to ski to believe. What to see in Joetsu and Myoko, Niigata.

#### Stay
- **File**: `stay.html`
- **URL**: `/stay`
- **Title**: Stay — myokojoetsu.com
- **Meta description**: Hot-spring inns with centuries-old water, mountain lodges, and quiet farmhouses in the rice fields. Where to stay in Myoko and Joetsu.

---

### Season Pages

#### Winter
- **File**: `winter.html`
- **URL**: `/winter`
- **Title**: Winter — myokojoetsu.com
- **Meta description**: Thirteen meters of snow, outdoor onsen in the steam, new sake pressed in the cold. Winter in Myoko and Joetsu, December to March.

#### Spring
- **File**: `spring.html`
- **URL**: `/spring`
- **Title**: Spring — myokojoetsu.com
- **Meta description**: Four thousand cherry trees around Takada Castle, snowmelt rivers, and rice paddies turned to mirrors. Spring in Myoko and Joetsu, April to May.

#### Summer
- **File**: `summer.html`
- **URL**: `/summer`
- **Title**: Summer — myokojoetsu.com
- **Meta description**: Mountain hiking above the clouds, lotus blooms on the castle moat, and festival lanterns through the gangi. Summer in Myoko and Joetsu.

#### Autumn
- **File**: `autumn.html`
- **URL**: `/autumn`
- **Title**: Autumn — myokojoetsu.com
- **Meta description**: Rice harvest, new-crop sake, foliage from the peaks to the sea, and the clearest skies of the year. Autumn in Myoko and Joetsu.

---

## File Naming Conventions

- All HTML files in the root directory (flat structure)
- Kebab-case filenames: `shop.html`, `winter.html`
- No subdirectories for pages
- URLs served without `.html` extension (configured via Cloudflare Pages or server rules)

## Navigation Behavior

- **Desktop**: "Discover" and "Seasons" show dropdown menus on hover
- **Mobile**: Hamburger menu with expandable sections
- **"Shop"** appears both as a Discover sub-item and as a standalone top-level nav link
- **"Access"** links to `/#access` (homepage anchor) from all pages

## Future Pages (not yet planned in detail)

- `/about` — About the editorial team / project
- `/guides` — Long-form seasonal or thematic guides
- `/journal` — Editorial blog / field notes
- Individual article pages (e.g., `/eat/hegi-soba`, `/see/takada-castle`) — subfolder structure TBD

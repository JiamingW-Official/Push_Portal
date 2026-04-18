---
name: push-website
description: "Push website design system, brand guidelines, UI rules, content standards, and portal structure. MUST READ before any UI/frontend work."
---

# Push Website & Design — Complete Reference

## 1. Design System Rules (MANDATORY)

> **完整组件规范在 `Design.md` 中。** 本 skill 是品牌概览和内容指南；实现具体组件时必须读 Design.md。

### Color Palette (5 Colors Only)

| Color | Name | Hex | Role |
|-------|------|-----|------|
| Primary | Flag Red | `#c1121f` | CTA, brand accent, alerts |
| Accent | Molten Lava | `#780000` | Hover states, deep emphasis, dramatic accents |
| Surface | Papaya Whip | `#fdf0d5` | Page backgrounds, card surfaces, warm base |
| Dark | Deep Space Blue | `#003049` | Dark panels, text, headers, hero backgrounds |
| Tertiary | Steel Blue | `#669bbc` | Info, links, badges, secondary actions |

**No other colors allowed.** Use opacity variations for lighter shades.
- Text: `#003049` (primary) / `#669bbc` (muted)
- Background: `#fdf0d5` (not white)

### Typography

| Role | Font | Usage |
|------|------|-------|
| **Headings/Display** | `Darky` | H1–H3, page titles, hero text, display type |
| **Body/Labels** | `CS Genio Mono` | Paragraphs, subtitles, buttons, captions, nav, UI text |

- Darky for headings only. CS Genio Mono for everything else.
- No other fonts. Custom `@font-face` imports, not Google Fonts.

### Sharp Corners (直角)
ALL UI elements: `border-radius: 0`. No rounded corners.
Exceptions: map pins (50%), filter chips (50vh), back-to-top (50%).

### Spacing (8px Grid)
All spacing: multiples of 8 — 8px, 16px, 24px, 32px, 40px, 48px, 56px, 64px.

### Light Mode Only
No dark mode.

### Interaction References
- **ashleybrookecs.com**: Editorial style, massive display typography (12vw+), numbered sections (01/02/03), scroll-driven reveals
- **sanrita.ca**: Minimal artsy, scroll-to-enter, monospace aesthetic, extreme whitespace
- **Sticky Grid Scroll**: GSAP + Lenis progressive reveal grid for showcase sections

### Component Override Rule
Third-party components: ALWAYS override rounded corners to 0.

## 2. Portal Site Structure

Current site: https://jiamingw-official.github.io/Push_Portal/

### Pages
| Page | URL | Purpose |
|------|-----|---------|
| Home | index.html | Main landing, vision, how it works |
| Project Intro | project-intro.html | Detailed Push explanation |
| Strategy Core | push-strategy-core.html | Strategic framework |
| Platform Value | platform-value.html | Value proposition deep-dive |
| Challenges | challenges.html | Problem analysis |
| Prospects | prospects.html | Market opportunity |
| Standby Mechanism | standby-mechanism.html | Standby system explanation |
| Attribution | attribution.html | Attribution framework |
| Economics | economics.html | Unit economics |
| Fraud & Integrity | fraud-integrity.html | Fraud prevention |
| GTM Launch | gtm-launch.html | Go-to-market plan |
| Metrics Dashboard | metrics-dashboard.html | Metrics framework |
| Risk Defense | risk-defense.html | Risk management |
| Retention Defense | retention-defense.html | Retention strategy |
| Pitch Deck | pitch-deck.html | Investor pitch |
| Investor Q&A | investor-qa.html | Investor FAQ |
| NDA | nda.html | NDA page |
| Team Dashboard | push-team-dashboard.html | Team overview |

## 3. Website Content Standards

### Voice & Tone
- Direct, confident, no fluff
- Infrastructure language, not marketplace cliches
- Focus on outcomes and measurement, not features
- Never say: "connecting creators with businesses" (too generic)
- Always say: "verified customer acquisition through creators"

### Key Copy Points
- Push = AI-native local customer acquisition engine
- Transaction-level attribution via QR codes
- 6-tier creator progression system (anyone can start)
- Merchant pricing: Starter $19.99/mo | Growth $69/mo | Pro $199/mo
- 35% platform margin target
- Beachhead: NYC cafe + dessert + beauty

### Merchant-Facing Copy
Focus: ROI, ease, measurement
- "Stop guessing which creators work. Start buying verified results."
- "Tell us your goal. We handle creator matching, execution, and verification."
- "$19.99/month. Less than one Instagram ad."

### Creator-Facing Copy
Focus: earnings, growth, fairness
- "No followers required. Start earning from day one."
- "Your performance score is your currency. Build it, and better campaigns come to you."
- "From free coffee to $150/campaign — your progression is tracked and rewarded."

## 4. Website MVP Requirements (Phase 1)
- Landing page: both merchant and creator paths
- Merchant signup form: name, business, address, Instagram, goals, availability
- Creator signup form: name, handles, location, content type, availability
- Campaign listing page
- Simple admin dashboard for manual campaign management
- Tech: Next.js/React + Vercel + Supabase/Airtable

## 5. Design Patterns

### Buttons
- Primary: `#c1121f` bg, white text, border-radius: 0
- Secondary: `#fdf0d5` bg, `#003049` border, dark text, border-radius: 0
- Ghost: transparent bg, `1px solid var(--line)`, dark text
- Disabled: muted bg (#d0d0d0), border-radius: 0
- Font: CS Genio Mono, uppercase, weight 700

### Cards
- `#fdf0d5` bg, 1px border (`var(--line)`), border-radius: 0
- 24px padding
- Optional left border accent (4px, brand color)

### Forms
- Input: border-radius: 0, 1px border var(--line), 16px padding, CS Genio Mono
- Focus: border color → `#c1121f`
- Error: border color → `#c1121f` + CS Genio Mono error text below

### Tables
- No border-radius on cells
- Header: `rgba(0,48,73,0.04)` bg, CS Genio Mono bold
- Alternating rows optional

### Navigation
- Top nav: `#fdf0d5` bg, bottom border 1px
- Active link: `#c1121f` underline or text color
- Logo: Darky font
- Links: CS Genio Mono, uppercase

## 6. Responsive Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px
- Max content width: 1180px
- Use 8px grid for all responsive spacing

## 7. Post-Task Design Review
After EVERY task involving UI: review Design.md, compare against decisions, update if new patterns established.

# Push — Workspace Rules

## Skills Architecture

Push 的所有领域知识存储在 `.claude/skills/` 中。每次只加载需要的 skill，不要全部加载。

**入口：** 先读 `push-hub` → 根据任务路由到对应 skill。

| Skill | 领域 |
|-------|------|
| `push-hub` | 主路由器 + 快速参考数字 |
| `push-strategy` | 战略定位、Agentic路线图、竞争分析 |
| `push-creator` | 6-Tier v3.0、评分模型、招募 |
| `push-pricing` | 定价$19.99/$69/$199、单位经济 |
| `push-attribution` | QR码归因、验证、反欺诈 |
| `push-campaign` | Campaign设计、工作流、SLA |
| `push-gtm` | 冷启动12周、增长、扩张 |
| `push-metrics` | KPI、仪表板、数据模型 |
| `push-website` | 品牌视觉规范、内容标准 |
| `push-brand-voice` | 品牌声音、文案、messaging模板 |
| `push-ui-template` | SaaS模板提取：页面结构、交互行为、组件规范（子文件：sections/interactions/components） |

---

## Design System (MANDATORY)

**任何 UI/前端代码修改前，必须读 [`Design.md`](./Design.md)。**

### 核心约束（v11 · 2026-04-25 late evening · Liquid-Glass Expansion + Image-First + 3-Tier Rule Classification）

**v11 总原则：** v10 N2W 基础全部保留；v11 在 Marketing 表面叠加编辑性签名；evening 收紧网格 / 负空间 / 按钮 / 颜色清单；本次 late-evening 加 3 层规则分类 + Liquid Glass 扩到 6 use case + Image-First 4 模式。Marketing 与 Product UI 两个 register 严禁在同一 viewport 混用。

**3 层规则分类（每条规则带一个标签 — 读 Design.md § 0）：**
- **🔒 STRICT** = Identity，跨页不变（颜色清单 / 三字体 / 8px 网格 / 5 按钮 / footer / GA nav / hover-shift 等）
- **📐 STRUCTURED** = Composition，从允许 variant 集合里挑（panel 库 / 角落锚定 / 负空间 token / 列网格 / liquid-glass 6 use case / image-first 4 模式 / Editorial Table 等）
- **🎨 OPEN** = Voice，编辑性判断范围内自主（用哪张照片 / divider 哪句措辞 / eyebrow 哪个词 / 内卡片 4+4+4 还是 6+6 / Editorial Pink stamp 用不用 / Magvix accent 词等）

**Liquid Glass 扩到 6 use case（全部走同一 token set `rgba(255,255,255,0.55)` + blur(12px) + `--shadow-glass`）：**
1. Footer Tile Pair（Newsletter + Socials peek 顶边）
2. Candy Panel Stat Tile（每 panel 1 个）
3. Hero Photo Stat Peek（hero 全图右上角 1 个，mobile 隐藏）
4. Sticky Filter Rail（Photo Grid 页 nav 下方 sticky 横向 pill 条）
5. Photo Card Floating Badge（每卡 1 个 tier/category/date 小 pill）
6. Scroll Progress Pill / Anchored CTA Pop（长文页 fixed 右下，scroll 过 hero 后渐显）

**Image-First 4 模式：**
- A：Full-Bleed Hero Photograph（`border-radius: 0` 例外 1，每页 ≤1）
- B：Photo Card with Bottom Gradient Overlay（Archive / Showcase 网格用，2/3/4-up）
- C：Framed Photo Tile inside Candy Panel（`--r-2xl` 20px 内框，inset 32px，文本主、图为辅）
- D：Decorative Photo Collage（VHS+电报+卡带 漂浮，`border-radius: 0` 例外 3，每页 ≤1）

1. **封闭"允许颜色清单"**：生产 CSS 仅可使用 Design.md § 2 中列出的 token；照片与 SVG visual effect 豁免。新增颜色须先 PR 更新 Design.md
2. **11 阶暖灰梯（v11 新增 3 色）：** snow `#fff` → surface `#f8f4e8` → surface-2 `#f5f3ee` → surface-3 `#ece9e0` → **`--mist #d8d4c8`** → ink-6 → ink-5 → ink-4 → ink-3 `#61605c`（body 锁定）→ **`--char #3a3835`**（dark panel 替代 ink，更暖）→ **`--graphite #2c2a26`**（次强标题色）→ ink-2 → ink → obsidian `#000`。所有 UI 文本/分隔/暗面只从这梯子取色
3. **品牌色 3 个 role-lock**：Brand Red `#c1121f` 主 CTA / N2W Blue `#0085ff` 次 CTA / Champagne `#bfa170` 仪式（每 viewport ≤3）
4. **Editorial Moments 3 色 ≤1/viewport**：Editorial Blue `#1e5fad`（footer 唯一）/ Editorial Pink `#e8447d`（单 CTA stamp）/ GA Orange `#ff5e2b`（Ticket Panel + nav home pill）
5. **GA Tri-Color nav 仅 chrome**：Orange / `--ga-green #4ade80` / `--ga-sky #93c5fd` 仅在 `<nav>`，禁扩散到 section / button / card
6. **iOS 26 圆角 scale + 选择性 `border-radius: 0`**：标准卡片 10px / 按钮 8px / 输入 8px / Candy Panel 28px / Ticket Panel 10px / Footer 40px。**v11 允许 `border-radius: 0` 仅 3 处**：full-bleed Photo Card Hero、Editorial Hero Tile billboard、image-collage card；其他容器（按钮/卡片/输入/panel/modal）一律走 scale 不能 0
7. **8px 严格网格**：所有 width/height/padding/margin/gap/top/left 全部 8 的倍数；4px 半格仅用于 hairline 与 chip gap。无任何 `padding: 22px` 这类乱跑值
8. **列网格**：desktop 12 列 24px gutter 64px 外边距 1140px max；iPad 8 列 20px gutter 48px 外边距；mobile 4 列 16px gutter 24px 外边距。Cell-span 词汇见 § 5.5（12/8/4 全幅、6+6、4+4+4、3×4 等），禁自创 7+5
9. **负空间 token 锁定**（§ 6 全表）：每种容器的 text-to-edge / text-to-line / text-to-vector / text-to-text 间距必须用表中数值，不可目测：
   - Hero 标题 → 副标题 32px / 副标题 → CTA 48px（desktop）
   - Eyebrow → H1 16px / H1 → body 24px / body → CTA 32px
   - Card title → body 12px / body → footer 16px / 卡片网格 gap 24px
   - Icon (40px tile) → text 16px / inline icon (24px) → text 12px / eyebrow icon (12px) → text 8px
   - 按钮间 16px desktop / 12px mobile
10. **Corner-anchored title（v11 新强制）**：Hero title 贴 panel **bottom-left**（不居中），section title 贴 **top-left**，footer wordmark 贴 **bottom-left**。仅 Ticket Panel 与 Photo Card 文字叠层 / Modal 允许居中
11. **字号刻度（v11 evening 全部抬大）**：Magvix Hero `clamp(64,9vw,160)px`（v10 是 96 上限），Darky Display `clamp(56,8vw,128)px`，**Footer Giant Wordmark `clamp(140,18vw,320)px`**（v10 是 240），H1 `clamp(40,5vw,72)px`，H2 `40px`（v10 是 36），KPI 数字 `clamp(40,5vw,72)px`。Body 18px / Caption 12px / Eyebrow 12px 不变
12. **三字体 role-lock 不变**：Magvix（Regular + Italic）hero / wordmark / Signature Divider；Darky display / heading / numerals / footer giant wordmark；CS Genio Mono body / UI / labels / parenthetical eyebrow。Magvix 永不低于 28px
13. **统一按钮系统（v11 强制 5 变体）**：每个按钮在每个页面渲染必须一致：
    - **Filled Primary**：Brand Red 填充 + Snow 文字 + 8px radius + 14×28 padding + mono 16px 600 uppercase 0.04em（mobile 12×24 + 14px）
    - **Filled Secondary**：N2W Blue 填充 + Snow 文字（其他属性同 Primary）
    - **Filled Ink**：Ink 填充 + Snow 文字（仅 Ticket Panel 或 dark surface）
    - **Ghost**：transparent + 1px ink 边 + Ink 文字
    - **Pill**：surface-3 + Ink 文字 + pill radius + 8×18 padding（filter chip / status / GA nav）
    - 所有按钮都有 bottom-right hover shift `translate(2px,2px)` → active `translate(3px,3px) scale(0.98)`，**唯一例外是 GA Tri-Color nav pill（色态变化，不位移）**
    - Editorial Pink 是可选第 6 变体，每页 ≤1
    - 任何按钮的颜色 / 圆角 / padding / hover 不允许 per-page 自定义
14. **页面背景 `#f8f4e8` / Body `#61605c` / Light Mode 单一**（v10 lock）
15. **Modular Panel Discipline**：Marketing 页 3-5 个堆叠 panel，相邻暖冷交替；每 panel ≤1 liquid-glass tile + ≤1 image card + ≤1 saturated editorial moment；Magvix Italic Divider 在 panel 之间作呼吸（每页 ≤2）
16. **Footer 改 wordmark**：Editorial Blue rounded-top + 2 floating glass tile + 3 列 parenthetical eyebrow + **Darky 800 巨型 `clamp(140,18vw,320)px` "PUSH" 贴底-左**（替代 v10 Magvix Italic）
17. **Ticket Panel**（GA Orange / 10px / 4 角 16px ink grommet / 上下 dashed 穿孔 / Magvix Italic 标题居中 / Filled Ink CTA / flat 无阴影 / 每页 ≤1 / Marketing only）
18. **Mono Eyebrow Parenthetical**（Marketing 用 `(LINKS)`，Product UI 用 `LINKS`，两 register 不混）
19. **Magvix Italic Signature Divider**（`End of campaign · Fin ·` 风格，28-40px italic ink-3，每页 ≤2）
20. **Editorial Table**（mono parenthetical header + Darky 18-20px 第一列 + mono 16px 其他列 + 末列右对齐 + dotted 行隔线 + 标题 top-left；Marketing only）
21. **Photo Card with Bottom Gradient Overlay**（4:5 或 1:1 + 35% 黑渐变 + Darky 20px snow 标题 + mono 12px snow 元数据；Marketing only；hover 整体位移不缩放图）
22. **最小字号 = 12px**（Footer Wordmark ≤320px、Hero Magvix ≤160px、KPI 数字 ≤72px 是 3 个文档化例外）
23. **Mobile + iPad 自然 responsive**：同一 composition / 同一 hierarchy 跨断点，仅 spacing scale + 列数变化（mobile 4 列 / iPad 8 列 / desktop 12 列；section padding 56→80→96px V）；不画备用 layout；触控目标 ≥44×44
24. **Bottom-right hover shift = Push 交互签名**（所有 clickable）；GA nav pill / Ticket grommet / footer wordmark / Magvix Italic Divider 不动
25. **Icon**：单 family / 40×40 `--r-lg` 12px tile / 内 icon 20-24px / 颜色匹配表面（ink 或 snow）/ Candy Panel/Ticket Panel 严禁裸 SVG
26. **Motion**：GSAP ScrollTrigger + Lenis；iOS 26 spring `cubic-bezier(0.34, 1.56, 0.64, 1)`；Ticket Panel / Divider / Giant Wordmark / GA nav 不动画
27. **阴影**：3 层 soft `--shadow-1/2/3` + glass morphism；Ticket Panel / GA nav pill / Giant Wordmark / Editorial Hero Tile 全 flat 无阴影

Design.md 包含完整 v11 组件规范（Closed Allowed-Color List / 11 阶暖灰梯 / 8px grid + 12 列系统 / 负空间 token 全表 / Corner-anchored 标题规则 / 选择性 radius:0 三例 / 5 + 1 统一按钮规范 / Ticket Panel 实现 / GA Tri-Color Nav 锚点 / Editorial Table 标记 / Photo Card 渐变 / Magvix Italic Divider 措辞库 / Darky Giant Wordmark Footer / Parenthetical Eyebrow 用法地图）+ v10 N2W 基础（Candy Panel / Magvix 字体 / Liquid-Glass Tile / Modular Panel Discipline / Icon 系统 / Tier v7 重映射），是 UI 实现的权威来源。

**Marketing vs Product 两个 register 严禁在同一 viewport 混用。** 任何按钮 / 任何颜色 / 任何 spacing 都必须从 § 2 / § 6 / § 9 的清单取，不允许自由发挥。第三方组件圆角必须覆写到对应 iOS scale（除 3 个文档化 `radius:0` 例外）。如需偏离 Design.md，先问用户，再在同一 PR 内更新文档。

---

## Development Rules

- 代码简洁可读，不过度工程化
- 优先 vanilla CSS，除非用户指定框架
- 仅在逻辑不明显时加注释
- Commit: `feat:` / `fix:` / `style:` / `refactor:`
- 每个任务结束后检查 Design.md 是否需要更新

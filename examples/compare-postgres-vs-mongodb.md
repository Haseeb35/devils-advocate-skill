# Compare mode: Postgres vs MongoDB

> **Prompt:** Postgres or MongoDB for a marketplace app with orders, payments, sellers and reviews? small team, launching in 3 months

<sub>Unedited output from Claude Code with the skill installed.</sub>

## 😈 Devil's Advocate: Postgres vs MongoDB

**The decision:** Which database to use for a marketplace with orders, payments, sellers and reviews, built by a small team that launches in 3 months. What matters most is getting money handling right and shipping fast.

**Against Postgres:** Schema migrations add some friction while you're still changing the data model every week. If parts of your catalog vary a lot (category-specific attributes), you may feel boxed in. That's easy to handle with a `jsonb` column, though, so this is a small cost.

**Against MongoDB:** Your core data is relational: an order links a buyer, a seller, line items, a payment and a refund, and a review links a user, an order and a seller. In Mongo you'd either duplicate data and keep the copies in sync yourself, or rebuild joins with `$lookup`. Multi-document transactions do exist, but they're bolted on. When "charge the card, create the order, decrement stock" half-fails, you get exactly the kind of money bug a 3-month team doesn't have time to chase. Reporting is harder too ("seller payouts this month, net of refunds"), and the business side will ask for it in week one.

| | Postgres | MongoDB |
|---|---|---|
| Biggest risk | Migrations slow you down early | Inconsistent order and payment data, duplicated records drifting apart |
| Hardest to undo | Very little; `jsonb` covers the flexible parts | Moving money data into a relational model after launch |
| Best if… | You have transactions, money, relationships and reporting (that's you) | Your data is mostly self-contained documents: content, events, catalogs with no money attached |

**Verdict: ✅ Postgres**
A marketplace is basically a ledger with a storefront on top. Foreign keys, constraints and ACID transactions catch bugs for you, and SQL answers the business questions without extra work. Put variable product attributes in `jsonb`, and use a managed host (Supabase, Neon or RDS) so nobody has to run the database.

**Before you decide:** Does anyone on the team know Mongo deeply and SQL barely? That's the one thing that could tip this, and even then I'd lean toward learning Postgres given that you're handling payments.

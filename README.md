<p align="center">
  <img src="assets/banner.png" alt="Devil's Advocate — a skill for Claude" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2b2522?style=flat-square" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Claude_Code-skill-c2412d?style=flat-square" alt="Claude Code skill">
  <img src="https://img.shields.io/badge/Claude.ai-compatible-2b2522?style=flat-square" alt="Claude.ai compatible">
</p>

---

Most plans fail for reasons that were visible in advance. Nobody looked, because the person making the plan was busy being excited about it.

**Devil's Advocate** is a skill for Claude that looks for you. Give it a plan — a migration, a product launch, a career move — and it argues the strongest honest case against it, names the three most likely ways it fails, makes the best case *for* it, and then gives you a straight verdict.

It is deliberately not a pessimist. If your plan is sound, it says so.

## What you get

```
## 😈 Devil's Advocate

The plan        One-line restatement, so you know it understood you
The case against  The objection that would hurt most if true
3 ways this could fail
                Each with likelihood, an early warning sign, and a concrete fix
The case for    The best honest argument for doing it
Verdict         ✅ Go · ⚠️ Go, with changes · 🔁 Rethink · ❌ Don't
Before you decide
                The one question you should answer first
```

The whole response fits on one screen.

## Example

> **You:** I'm going to rewrite our backend from Node to Go for performance.

**The plan:** Rewrite the entire backend from Node.js to Go to improve performance.

**The case against**
There's no evidence yet that Node is the bottleneck — in most web backends, slowness comes from database queries, N+1 calls or network latency, which a language switch won't fix. A full rewrite also freezes feature work for months and re-introduces bugs you already fixed once.

**3 ways this could fail**
1. **Speed doesn't improve** — the real bottleneck is the database.
   Likelihood: High · Warning sign: profiling shows most request time in DB/IO · Prevent it: profile production traffic first.
2. **The rewrite drags on** — edge cases pile up for 6+ months while competitors ship.
   Likelihood: Medium · Warning sign: first milestone slips by 2+ weeks · Prevent it: rewrite one hot service, not everything.
3. **Team friction in Go** — unfamiliar idioms lead to new bugs and slower reviews.
   Likelihood: Medium · Warning sign: PR review times climb · Prevent it: a 2-week pilot on one small service.

**The case for**
Go handles high concurrency efficiently and can meaningfully cut hosting costs at scale. If profiling confirms CPU-bound hot paths, a targeted Go service is a well-proven move.

**Verdict: ⚠️ Go, with changes**
Profile first. If a specific service is CPU-bound, rewrite just that one and measure before going further.

**Before you decide:** Have you measured where request time is actually spent?

More examples — a business decision and a personal one — are in [`examples/`](examples).

## Installation

### Claude Code

Install for all your projects:

```bash
git clone https://github.com/Haseeb35/devils-advocate-skill.git
cp -r devils-advocate-skill/devils-advocate ~/.claude/skills/
```

Or for a single project, copy the folder into that project instead:

```bash
cp -r devils-advocate-skill/devils-advocate your-project/.claude/skills/
```

Start a new Claude Code session and the skill is available.

### Claude.ai

Zip the `devils-advocate` folder and upload it under **Settings → Capabilities → Skills**.

## Usage

Ask for it directly:

```
devil's advocate: we're moving the whole team to a 4-day week next month
```

```
/devils-advocate I'm thinking of raising prices 40% for new customers
```

Or just talk normally. The skill activates on phrases like *"poke holes in this"*, *"what could go wrong"*, *"am I crazy to…"*, *"should I really…"*, and when you're about to make a big, hard-to-reverse call — a rewrite, a stack choice, a launch, a hire, a resignation.

In a codebase, Claude will read the relevant code before arguing about it, so objections are grounded in what's actually there.

## Design principles

The skill is short, and most of it explains *why* rather than dictating rules. A few ideas it is built around:

- **Specific beats generic.** "The rewrite might take long" is noise. "Three developers and 40k lines means four to six months of frozen features" is a risk you can act on.
- **Every risk comes with a fix.** A warning sign and a prevention step turn criticism into a plan.
- **Fairness in both directions.** A critic who attacks everything is as useless as one who approves everything. The steelman and the honest verdict are what make the objections worth listening to.
- **Challenge the premise.** Sometimes the biggest risk is that the plan solves the wrong problem.
- **Tone follows stakes.** Technical decisions get blunt answers. Personal ones get the same honesty, delivered with care.

## Project structure

```
devils-advocate-skill/
├── devils-advocate/
│   └── SKILL.md        # the skill — this is all Claude needs
├── examples/           # sample outputs across domains
└── assets/             # banner
```

## Contributing

Issues and pull requests are welcome — especially:

- Real decisions where the skill gave a weak or unfair critique (include the prompt and output)
- Better example cases from domains not yet covered
- Wording improvements to `SKILL.md` that make the output sharper without making it longer

## License

[MIT](LICENSE)

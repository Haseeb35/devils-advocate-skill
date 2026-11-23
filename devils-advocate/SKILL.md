---
name: devils-advocate
description: Stress-test a plan or decision before the user commits to it. Argue the strongest honest case against it, list the three most likely ways it fails (with likelihood, early warning sign and prevention), steelman the case for it, then give a fair verdict (Go / Go with changes / Rethink / Don't). Use this whenever the user says "devil's advocate", "poke holes", "roast my plan", "what could go wrong", "sanity check this", "am I crazy to...", "should I really...", or asks for honest pushback, and also when they are about to make a big, hard-to-reverse call: a rewrite or migration, a tech/stack/architecture choice, launching or pivoting a product, pricing, hiring, quitting a job, moving, or a major purchase. Works for code, business and life decisions.
---

# Devil's Advocate

The user wants a sparring partner, not a cheerleader. People tend to fall in love with their own plans and only see the upside; your job is to surface the risks they haven't priced in, while staying fair enough that they trust your verdict. A devil's advocate who attacks everything is as useless as one who approves everything — the value comes from being honest in *both* directions.

## Before you start

Make sure you know what the plan actually is. If the user's message is too vague to critique specifically (e.g. "should I start a business?"), ask one or two short questions — what exactly, why, and what constraints (time, money, team) — then proceed. If you can reasonably infer the plan, skip the questions and just go; you can note your assumptions in the restatement.

If you have context (the codebase, earlier conversation, files the user shared), use it. Specific objections grounded in their real situation are far more useful than generic risks. In a codebase, it's worth a quick look at the relevant code before arguing about it.

## Output format

Use this structure. Keep the whole thing to about one screen — busy people need to be able to read it in a minute.

```
## 😈 Devil's Advocate

**The plan:** <one or two lines restating the plan, plus any assumption you made>

**The case against**
<2–4 sentences: the strongest honest argument against the plan. Lead with the
objection that would hurt most if true. No nitpicks.>

**3 ways this could fail**
1. **<Short name>** — <what specifically goes wrong>
   Likelihood: Low / Medium / High · Warning sign: <what to watch for> · Prevent it: <one concrete action>
2. ...
3. ...

**The case for**
<2–3 sentences: the best honest argument for doing it. Steelman, don't strawman.>

**Verdict: <emoji + label>**
<1–3 sentences explaining the call. If "Go with changes", say exactly which changes.>

**Before you decide:** <the single most important question the user should answer>
```

### Verdicts

- ✅ **Go** — the plan holds up; the risks are manageable or already handled.
- ⚠️ **Go, with changes** — worth doing, but fix specific things first.
- 🔁 **Rethink** — the goal is fine, but there's a clearly better way to reach it (name it).
- ❌ **Don't** — the risks clearly outweigh the upside right now.

## What makes it good

- **Specific beats generic.** "The rewrite might take long" is weak. "You have 3 devs and ~40k lines; a full rewrite is realistically 4–6 months of frozen features" is useful. Tie each failure mode to details of *their* plan.
- **Rank honestly.** Pick the three failure modes that are most likely or most damaging, not the most dramatic. Likelihood ratings should be your real estimate.
- **Every risk gets a fix.** A warning sign and a prevention step turn criticism into something actionable — that's what separates this from just being negative.
- **Be fair.** If the plan is genuinely good, say Go. Inventing problems to fill the template erodes trust. If you truly can't find three meaningful risks, list fewer and say so.
- **Challenge the premise when needed.** Sometimes the biggest risk is that the plan solves the wrong problem (e.g. rewriting for speed without measuring where time is spent). Say so in "The case against".
- **Match the tone to the stakes.** Technical decisions can be blunt and direct. Personal decisions (career, money, relationships, relocation) deserve the same honesty delivered with warmth — acknowledge that it's their life and their call.

## Boundaries

- Don't moralize or lecture; critique the plan, not the person.
- For decisions with serious medical, legal or financial consequences, give your honest analysis but note that a qualified professional should weigh in on the specifics.
- After the verdict, stop. Offer to dig deeper into any one risk only if it's natural — don't pad the response.

## Example

**User:** I'm going to rewrite our backend from Node to Go for performance.

## 😈 Devil's Advocate

**The plan:** Rewrite the entire backend from Node.js to Go to improve performance.

**The case against**
There's no evidence yet that Node is the bottleneck — in most web backends, slowness comes from database queries, N+1 calls or network latency, which a language switch won't fix. Meanwhile a full rewrite freezes feature work for months and re-introduces bugs you already fixed once.

**3 ways this could fail**
1. **Speed doesn't improve** — the real bottleneck is the database, so after months of work, response times barely change.
   Likelihood: High · Warning sign: profiling shows most request time in DB/IO · Prevent it: profile production traffic before deciding anything.
2. **The rewrite drags on** — edge cases pile up and it takes 6+ months while competitors ship.
   Likelihood: Medium · Warning sign: first milestone slips by 2+ weeks · Prevent it: rewrite one hot service, not everything.
3. **Team friction in Go** — unfamiliar idioms lead to new bugs and slower reviews.
   Likelihood: Medium · Warning sign: PR review times climb · Prevent it: run a 2-week pilot with one small service first.

**The case for**
Go handles high concurrency efficiently, uses less memory and can meaningfully cut hosting costs at scale. If profiling confirms CPU-bound hot paths, a targeted Go service is a well-proven move.

**Verdict: ⚠️ Go, with changes**
Don't rewrite everything. Profile first; if a specific service is CPU-bound, rewrite just that one in Go and measure the gain before going further.

**Before you decide:** Have you measured where request time is actually spent?

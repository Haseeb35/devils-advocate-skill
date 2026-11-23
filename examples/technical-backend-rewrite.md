# Technical: rewriting a backend in a new language

> **Prompt:** I'm going to rewrite our backend from Node to Go for performance.

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

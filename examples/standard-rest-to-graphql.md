# Standard mode: REST to GraphQL migration

> **Prompt:** devil's advocate: we're migrating our whole app from REST to GraphQL next sprint so the frontend team can move faster

<sub>Unedited output from Claude Code with the skill installed.</sub>

## 😈 Devil's Advocate

**The plan:** Move the whole app's API from REST to GraphQL, starting next sprint, so the frontend team can ship faster. I'm assuming a single product team that owns both frontend and backend, and a REST API already running in production.

**The case against**
This plan treats "frontend is slow" as an API-shape problem, and nobody has shown that it is. If the frontend is actually waiting on backend endpoints, unclear specs, or reviews, GraphQL doesn't help. It just moves the waiting from "add an endpoint" to "add a field or resolver." "Whole app, next sprint" is also a big-bang migration with a deadline that's almost certainly unrealistic. For weeks or months you'd run two APIs, and the backend team would carry a large new load in resolvers, auth, caching and performance work before the frontend sees any speedup.

**3 ways this could fail**
1. **Backend becomes the new bottleneck.** Naive resolvers cause N+1 query storms. Field-level authorization has to be rebuilt by hand, because REST's per-route middleware doesn't carry over. Backend velocity drops sharply while they learn DataLoader, query complexity limits and schema design.
   Likelihood: High · Warning sign: p95 latency or DB query counts per request go up after the first resolvers ship · Prevent it: use DataLoader and query depth/cost limits from day one, and port auth rules before porting endpoints.
2. **Stuck halfway, permanently.** The migration takes longer than a sprint, other priorities come back, and you end up maintaining both REST and GraphQL indefinitely, which is worse than either one.
   Likelihood: High · Warning sign: sprint 2 still has more REST endpoints than GraphQL types · Prevent it: don't migrate everything. Put GraphQL as a gateway in front of the existing REST services (resolvers call REST), and adopt it one screen at a time.
3. **Caching, observability and tooling regress.** You lose HTTP/CDN caching, since everything is a POST to `/graphql`. Every request shows up as the same endpoint in your APM, and error handling changes (200 OK responses that contain errors). Incidents get harder to debug.
   Likelihood: Medium · Warning sign: on-call can't tell which operation is slow · Prevent it: use persisted queries, name operations, and add per-resolver tracing before going live.

**The case for**
GraphQL really does help frontend velocity in the right situation: many screens that each need differently shaped data, multiple clients (web plus mobile), and constant "can you add a field to this endpoint?" requests. A typed schema with codegen also gives the frontend end-to-end types and removes a whole category of integration bugs. If that matches your situation, it's a well-proven choice.

**Verdict: 🔁 Rethink**
The goal is fine; the approach (whole app, next sprint) is the problem. Spend this sprint measuring where frontend time actually goes. If API shape really is the blocker, put a thin GraphQL layer over your existing REST services and migrate the single screen with the most churn first. Expand only once that screen is clearly faster to build and no slower to load. If the real blocker is something else (specs, backend capacity, slow reviews), cheaper fixes like typed OpenAPI clients, BFF endpoints or tRPC may get you most of the gain without a migration.

**Before you decide:** In the last month, which specific frontend tasks were slowed by the API, and would GraphQL have removed that wait or just moved it to the backend team?

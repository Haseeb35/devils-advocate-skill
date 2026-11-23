# Eval results

**Run:** 2026-11-23 · Claude Code 2.1.330 · model `claude-opus-5-5` · judge: Claude Haiku (3 votes per check) · 2 runs per case per arm · cost $2.96

Each case runs twice **with** the skill and twice **without** it (plain Claude, same model, same prompt). Every check is graded independently.

| Case | With skill | Without | Δ |
|---|---|---|---|
| `quick-mode-gut-check` | 4/4 | 0/4 | +100% |
| `compare-mode-postgres-vs-mongodb` | 6/6 | 2/6 | +67% |
| `deep-mode-premortem` | 10/10 | 4/10 | +60% |
| `standard-critiques-microservices-split` | 9/10 | 4/10 | +50% |
| `fair-verdict-on-sound-plan` | 6/6 | 4/6 | +33% |
| `vague-plan-asks-questions` | 4/4 | 4/4 | 0% |
| **Total** | **39/40 (98%)** | **18/40 (45%)** | **+53 pts** |

## Reading these numbers honestly

- **Many checks test structure.** Plain Claude can't be expected to produce a "Quick mode" answer or a pre-mortem section it was never asked for, so part of the gap measures whether the skill's format is followed — which is the point of a skill, but not the same as "better advice".
- **The checks that test judgement are the interesting ones.** Without the skill, Claude never gave a clear **Go** to the sound backup plan (0/2 vs 2/2), didn't critique each database option separately (0/2 vs 2/2), and didn't acknowledge the personal stakes of quitting a job (0/2 vs 2/2).
- **Where plain Claude already does well, the skill adds nothing** — both arms asked clarifying questions on the vague prompt, and both picked a clear database.
- **The one failure:** a Standard run rated a risk "Medium-High"; the check requires Low, Medium or High exactly.
- **Small sample.** Six cases, two runs each, written by the author of the skill. Treat this as evidence the skill does what it claims, not as a benchmark.

Reproduce with `claude plugin eval .` (billed model usage).

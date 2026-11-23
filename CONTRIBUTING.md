# Contributing

Thanks for helping make the critiques sharper. Contributions of every size are welcome.

## Ways to help

- **Report a weak critique.** If the skill gave a generic, unfair or wrong answer, [open an issue](../../issues/new?template=weak-critique.yml) with the prompt and the output. These reports are the most useful input this project gets.
- **Add an example.** Real runs from domains not yet covered (hiring, health, education, hardware, nonprofits) are especially welcome in [`examples/`](examples).
- **Add an eval case.** Each folder in [`evals/`](evals) is one test. Copy an existing case and adapt it.
- **Improve `SKILL.md`.** Wording changes that make the output sharper without making it longer.

## Making a change

1. Fork the repo and create a branch.
2. Edit the skill in `skills/devils-advocate/SKILL.md`.
3. Test it locally:
   ```bash
   claude --plugin-dir .
   ```
   Then try a few real decisions, including one where the plan is genuinely good — the skill should say **Go** rather than invent problems.
4. Run the checks:
   ```bash
   python3 scripts/validate.py
   claude plugin validate .
   ```
5. Optionally run the eval suite. These are real model runs and are billed to your account:
   ```bash
   claude plugin eval .
   ```
6. Add a line under an `Unreleased` heading in `CHANGELOG.md` and open a pull request.

## Guidelines

- **Explain the why.** The skill works best when it tells Claude *why* something matters rather than issuing rigid rules.
- **Keep it short.** Every line in `SKILL.md` is loaded each time the skill runs.
- **Don't overfit.** A change that fixes one example but makes the skill narrower is not an improvement.
- **Be kind.** Critique plans, not people — in the skill and in reviews.

## Releasing (maintainers)

1. Bump `version` in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
2. Move `Unreleased` entries in `CHANGELOG.md` under the new version.
3. Tag and push: `git tag v1.2.0 && git push origin v1.2.0`. The release workflow builds the Claude.ai zip and publishes the release.

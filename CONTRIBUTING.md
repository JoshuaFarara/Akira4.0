# Development workflow

`main` should always hold a notebook that runs. All work happens on branches and comes in through pull requests (PRs).

## The loop

1. **Start from an issue.** Open or pick a GitHub issue, for example "Add end-of-response token". Assign it to yourself so nobody else takes it.
2. **Create a branch** on GitHub (branch dropdown → type a name → *Create branch*). Name it `<your-name>/<short-topic>`, for example `rocco/eos-token`.
3. **Open your branch in Colab:**
   `https://colab.research.google.com/github/JoshuaFarara/Akira4.0/blob/<branch>/Akira4_0.ipynb`
   (Colab: *File → Open notebook → GitHub* tab, pick the repo and branch.)
4. **Work.** Run *Project Setup* first. Data and checkpoints load from the shared Drive folder.
5. **Save to GitHub:** *File → Save a copy in GitHub*
   - Repository: `JoshuaFarara/Akira4.0`
   - Branch: **your branch**, never `main`
   - Commit message: say what changed and why, for example "Add <|endofresponse|> token to dataset loader"
   - **Untick "Include cell outputs"** (keeps diffs readable; see below)
6. **Open a pull request** into `main` on GitHub. Fill in the template, link the issue (`Closes #12`), and request a review from a mentor or teammate.
7. **Merge** after approval and green checks. Delete the branch.

Save to GitHub often, at least at the end of every session. Each save is a commit, so you can always go back.

## Rules that keep it clean

- **Never commit data or weights.** `*.jsonl` and `*.pth` are git-ignored. They go in the shared Drive folder.
- **No cell outputs in commits.** Outputs make diffs unreadable and can leak training samples. CI warns if a notebook has outputs.
- **Paths go in the Project Setup cell only.** Don't hard-code `/content/...` in other cells. Read `AKIRA_DATASET_PATH` / `AKIRA_LOCAL_CHECKPOINT` instead.
- **Experiments get recorded.** When a training run matters for the research, write the config, dataset version, checkpoint filename and results in the PR description.
- **Two people editing one notebook at the same time causes merge conflicts.** Coordinate through issues, or put new work in a separate notebook (for example `notebooks/eval_blinded.ipynb`) and merge it in later.

## Fixing a merge conflict

Notebook conflicts are hard to fix in the browser. Easiest path: in Colab, open the latest `main`, copy your changed cells in, and save to a fresh branch. If you work locally, [`nbdime`](https://nbdime.readthedocs.io) (`nbdime mergetool`) handles notebook merges properly.

## Recommended repo settings (admin, one time)

- *Settings → Branches → Add rule* for `main`: require a pull request, require 1 approval, and require the `Notebook checks` status to pass.
- *Settings → Collaborators*: add each student with **Write** access.
- For the Claude agent (see below): run `/install-github-app` from Claude Code, or add an `ANTHROPIC_API_KEY` repository secret.

## Working with the Claude agent

Mention `@claude` in an issue or PR comment, for example:

- `@claude review this PR for bugs in the training loop`
- `@claude explain why responses are being cut off`
- `@claude implement this issue on a new branch`

Claude reads [CLAUDE.md](CLAUDE.md) for project context. It opens PRs, and a person still reviews and merges them.

# CLAUDE.md: guidance for AI agents working on this repo

## What this is
AkiraGPT is an undergraduate research project. It is a small GPT, about 6 layers with d_model 256 and the GPT-2 tokenizer, built from scratch in PyTorch and trained on a merged mental-health and prosocial dialogue corpus (~245k prompt/response pairs, JSONL). Students develop it in **Google Colab**, and this repo is the source of truth for the code. Research context is in `docs/research/`.

## Layout
- `Akira4_0.ipynb`: the whole pipeline, cell by cell. Project Setup (Drive paths), install/imports, dataset inspection, training (`akira_lm_train.py` cell), chat UI, parameter counter, web search helper.
- `docs/research/`: poster and research plan (RQs and phases for 5.0).
- `scripts/check_notebooks.py`: CI check for notebook validity, outputs and hard-coded paths.

## Hard rules
- **Never add datasets or model weights** (`*.jsonl`, `*.pth`) to git. They live in Google Drive at `MyDrive/Akira/`.
- **Paths come from the Project Setup cell** (`AKIRA_DATASET_PATH`, `AKIRA_LOCAL_CHECKPOINT`, `AKIRA_DRIVE_CHECKPOINT`, `AKIRA_SAVE_TO_DRIVE`). Other cells read them through `globals().get(..., fallback)` so they still run on their own.
- **Keep notebooks output-free** and valid nbformat 4 JSON. Run `python scripts/check_notebooks.py` before committing.
- **Don't change model architecture constants** (`D_MODEL`, `N_HEAD`, `N_LAYERS`, `DIM_FF`, `MODEL_MAX_LEN`) unless the task asks for it. Changing them breaks loading of existing checkpoints. The chat cell's constants must match the training cell's.
- The code must run on a **Colab GPU runtime** (T4 typically). Assume `/content` is ephemeral and Drive is persistent.
- **Sensitive domain.** This model responds to mental-health conversations. Treat safety-related changes (crisis handling, output filters) as high scrutiny: explain the change in the PR and never weaken an existing safeguard without saying so.
- Work on a branch and open a PR. Never push to `main`.

## Authorship (always)
Every commit, push, pull request and merge must be **authored by the human collaborator who asked for the work**, never by Claude or a bot identity.
- Before committing, set the git identity to that person, using their GitHub no-reply address, never a personal email:
  ```bash
  git config user.name "<Their Name>"
  git config user.email "<id>+<login>@users.noreply.github.com"   # or <login>@users.noreply.github.com
  ```
  Repo owner default: `Joshua Farara <109557415+JoshuaFarara@users.noreply.github.com>`.
- In the `@claude` GitHub Action, the requester is the person who wrote the `@claude` comment. Commit with `--author="<Their Name> <<login>@users.noreply.github.com>"`.
- Credit Claude only with a `Co-Authored-By:` trailer at the end of the commit message.
- Open PRs on behalf of the requester and say in the description who requested them. **Never merge.** A person reviews and merges.
- If a commit was made under the wrong author on an unmerged branch, fix it with `git commit --amend --reset-author` (or a rebase) and push with `--force-with-lease`. Never rewrite `main`.

## Editing notebooks
Edit `.ipynb` as JSON carefully: keep `cells[].source` as a list of lines, keep `outputs: []` and `execution_count: null`, and preserve `metadata.colab`. Check after editing with:
```bash
python scripts/check_notebooks.py
```

## Research priorities (Akira 5.0)
1. End-of-response token plus nucleus (top-p) sampling, to fix cut-off / unending output (RQ1).
2. Dedupe the corpus, record dataset licenses, and make a held-out test split with no overlap.
3. Empathy-classifier filtering and multi-turn data (RQ2).
4. Crisis/stigma safety test set and output filter (RQ3). Compare against a fine-tuned small pretrained model on the same data (RQ4).

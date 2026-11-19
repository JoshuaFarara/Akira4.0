# AkiraGPT

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JoshuaFarara/Akira4.0/blob/main/Akira4_0.ipynb)

AkiraGPT is a small GPT built from scratch by students and trained on more than 245,000 mental-health and prosocial dialogue pairs. The goal is responses that are clear, ethical and safe. This is an undergraduate research project in the Department of Computer Science, mentored by Joshua Farara and Vijayalakshmi Ramasamy, PhD.

- **4.0** (this repo, presented at the 2026 Student Research Symposium): fully reinitialized and retrained on a merged mental-health corpus.
- **5.0** (2026–27, in progress): end-of-response tokens, nucleus sampling, empathy filtering, multi-turn data, and blinded safety evaluation. See [`docs/research/akira5_research_plan.md`](docs/research/akira5_research_plan.md).

The dataset is built in [MooreRA26/Language-Dataset-Mining-and-Merging](https://github.com/MooreRA26/Language-Dataset-Mining-and-Merging).

## Quick start (Colab)

1. **One time:** in Google Drive, open the shared `Akira` folder and choose **Organize → Add shortcut → My Drive**.
2. Click the badge above, or open `https://colab.research.google.com/github/JoshuaFarara/Akira4.0/blob/<your-branch>/Akira4_0.ipynb`.
3. Run **Project Setup** first. It mounts Drive and finds the dataset and the latest checkpoint, so there is nothing to upload.
4. Run the other cells as usual.

## What lives where

| Thing | Where | Why |
|---|---|---|
| Notebook / code | GitHub (this repo) | Version history, reviews, branches |
| `merged_training_dataset.jsonl` | Shared Drive: `Akira/` | Too large for git; licensed third-party data |
| Checkpoints (`*.pth`) | Shared Drive: `Akira/checkpoints/` | Large binary files |
| Posters, proposal summaries | `docs/research/` | Research record |

The Drive folder should look like this:

```
MyDrive/Akira/
├── merged_training_dataset.jsonl
└── checkpoints/
    └── akira_gpt_model_exp.pth      # written automatically during training
```

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). In short: make a branch, save from Colab to that branch, open a pull request, and get a review before merging to `main`.

## License

The poster in `docs/research/` is licensed under CC BY-NC-ND 4.0.

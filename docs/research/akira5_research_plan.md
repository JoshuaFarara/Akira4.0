# Akira 5.0 research plan (summary)

This summarizes the 2026–2027 AEP CEC Undergraduate Research Award proposal, *"Project Akira 5.0: Data Filtering, Multi-Turn Training, and Evaluating a Custom-Built GPT to Produce Complete, Safe, and Ethically Coherent Responses"*. Student: Rocco Moore. Mentors: Joshua Farara and Vijayalakshmi Ramasamy, PhD. The signed application is kept outside this public repository.

Akira 5.0 directly continues 4.0. It uses the same repository, merged corpus and training pipeline.

## Where 4.0 left off
- Results from 4.0 (2026 Student Research Symposium poster, `Akira4.0_GS4_Symposium_Poster_2026.pptx`): compared with 3.0, it gives more ethically aligned and grammatically coherent responses.
- Known issue: **unending output**, where responses run on and get cut off.

## Research questions
- **RQ1:** Does training with end-of-response tokens, combined with nucleus sampling, eliminate cut-off responses without reducing quality?
- **RQ2:** Do the gains of 4.0 over 3.0 hold under blinded evaluation, and do empathy-based data filtering and multi-turn training improve on them?
- **RQ3:** How safely does Akira respond to crisis and high-risk prompts, and does safety-focused training with an output filter improve those responses?
- **RQ4:** How close does the custom-built Akira come to a fine-tuned pretrained model trained on the same data?

## Phases
1. End-of-response tokens and nucleus sampling. Blinded human and LLM-judge ratings of 3.0, 4.0 and 5.0.
2. Filter low-empathy pairs with an empathy classifier and add multi-turn conversations.
3. Crisis and stigma testing with an output filter. Compare with a small pretrained model fine-tuned on the same data.

## Data preparation
Deduplicate the merged corpus, record each dataset's license, create a held-out test split with no overlap, and terminate every response with an explicit end-of-response token.

## Evaluation
- No real users. Scripted batteries cover held-out prompts, multi-turn simulated conversations, and a crisis/stigma/delusion safety set.
- Measures: completion rate, repetition, grammar errors, classifier empathy, and MentalChat16K rubric scores from an LLM judge.
- Validation: two or more blinded raters, with agreement reported as Krippendorff's alpha. The LLM judge is accepted only if it agrees with the human raters. Conditions are compared with paired tests, and ablations isolate each change.

## Key references
Kim et al. 2022 (ProsocialDialog); Rashkin et al. 2019 (EmpatheticDialogues); Xu et al. 2025 (MentalChat16K); Holtzman et al. 2019 (nucleus sampling); Moore et al. 2025 (stigma in LLM mental-health responses, FAccT); Sharma et al. 2020 (computational empathy); Zheng et al. 2023 (LLM-as-a-judge).

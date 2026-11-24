# Final Prompt Sheet — P1 Resume–Job Match Evaluation

- **Prompt ID and name:** P1 — Evidence-Based Resume–Job Match Evaluation
- **Workflow step:** Compare resume evidence against job requirements; generate structured feedback.
- **Purpose:** Produce a rubric-based match score, gaps, strengths, truthful bullet rewrites and next steps.
- **Tool/model:** Prompt template designed for an LLM (ChatGPT/OpenAI, Gemini or Claude); model/provider must be recorded for each real run. The supplied local prototype does not call an LLM.
- **Settings:** Provider defaults unless explicitly recorded; use a low temperature (e.g. 0.2) when available for consistency. Record actual settings used.
- **System prompt:** None separately; role and rules are included in the user prompt template.
- **User prompt template:** See `prompts/final/resume_job_match.txt`. Variables: `{resume}` = anonymised resume text; `{job_description}` = target job posting text.
- **Examples included:** 0 in the final template; add few-shot examples only after recording the actual examples and observed effect.
- **Output format:** One JSON object with status, match_score, category_scores, gaps, strengths, rewritten_bullets, next_steps and limitations.
- **Sample run:** Use an anonymised resume and a real JD; save the exact prompt, provider/model, settings and unedited model output in `test-data/runs/`. Do not invent output.

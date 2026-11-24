# AI Resume–Job Match Assistant

**Team:** Ubiquitous  
**Member currently listed:** Vedanshi Mishra — S24CSEU0174  
**Team ID:** [EDIT: Team ID from Milestone 1]

## Problem
Students often reuse generic resumes for different job applications and receive little role-specific feedback. This prototype compares resume text with a job description and produces a rubric-based score, gaps, strengths and next steps.

## Intended prompt-engineering approach
The project uses role prompting, a fixed scoring rubric, structured JSON output and iterative prompt refinement. Three prompt versions are saved in `prompts/v1`, `prompts/v2`, and `prompts/v3`; the final prompt is in `prompts/final`.

## Scoring rubric
- Skills match: 40
- Experience/projects relevance: 30
- Job-specific keywords: 20
- Clarity/readability: 10

## Run locally
```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```
Or run `run_app.bat` on Windows.

## Important implementation note
The included Streamlit prototype runs in **local demo mode** using deterministic lexical heuristics. It does not call ChatGPT, Gemini or Claude and is not a trained hiring prediction model. The prompt files are ready for controlled testing with an LLM provider; record the actual provider/model, settings and unedited outputs for every LLM experiment. Do not claim provider integration unless implemented and tested.

## Privacy and limitations
Use anonymised or synthetic resume content. Do not upload real personal contact details without informed consent. Scores are indicative, depend on text overlap and rubric interpretation, and do not predict interview selection or hiring probability. Human review is required.

## Repository structure
- `app/` — Streamlit prototype
- `prompts/v1`, `v2`, `v3`, `final` — prompt history and final prompt
- `test-data/` — synthetic sample inputs and test matrix
- `docs/` — workflow and architecture diagrams
- `reports/` — generated PDFs (added when final team details are confirmed)
- `CHANGELOG.md` — dated changes

## Team details to edit
Replace `[EDIT: ...]` placeholders and verify the enrollment number before submission. Add every team member with a specific, evidence-backed task and agreed contribution percentage.

## Publish and finish
See `docs/GITHUB_UPLOAD_STEPS.md` for exact GitHub commands and `docs/ONE_HOUR_FINISH_CHECKLIST.md` for the remaining evidence and submission steps.

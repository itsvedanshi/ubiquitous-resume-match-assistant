# One-hour finish checklist

## 0–10 min: verify metadata
- Fill Team ID, batch/group, faculty name and all members in report and README.
- Verify enrollment number exactly from university records.
- Get team agreement on contribution percentages (sum 100%).

## 10–20 min: run prototype
- Extract ZIP and run `run_app.bat` or install requirements and run Streamlit.
- Use only synthetic/anonymised resume text.
- Run at least T01, T06, T07 and T08 first; then complete all 12 test cases.
- Save actual outputs and pass/fail honestly. Do not mark unrun tests as passed.

## 20–30 min: prompt experiments
- Run the same test inputs with v1, v2 and v3 using the chosen LLM provider.
- Record provider, exact model, settings, prompt version and unedited outputs.
- Compare rubric adherence, JSON validity, unsupported claims and missing-skill quality.
- Update the prompt iteration log with measured observations. Do not invent metrics.

## 30–40 min: evidence
- Capture 2–3 screenshots of real runs and put them in `screenshots/`.
- Add repository screenshot to Section 5 of the PDF.
- Replace report test table pending statuses with actual outcomes.

## 40–50 min: GitHub
- Follow `GITHUB_UPLOAD_STEPS.md`.
- Verify public access in a private browser window.

## 50–60 min: reel and submission
- Record a 90–150 second real screen demo using `demo_reel_script.md`.
- Upload to Drive or unlisted YouTube; allow anyone with the link to view.
- Replace all placeholders and links in the report; regenerate PDFs after edits.
- Ensure the two PDFs are below 10 MB and all links open.

# Publish this folder to GitHub (Windows, VS Code)

1. Extract `Ubiquitous_Milestone2_Complete_Package.zip`.
2. Open the extracted `Ubiquitous_Milestone2_Package` folder in VS Code.
3. Create a new **Public** repository on GitHub named `ai-resume-job-match-assistant`. Do not add a README/license/gitignore on GitHub if the local folder already contains files.
4. In VS Code: Terminal → New Terminal. Ensure the terminal is inside the extracted project folder.
5. Run these commands one at a time:

```powershell
git init
git add .
git commit -m "Add Milestone 2 resume job match assistant"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ai-resume-job-match-assistant.git
git push -u origin main
```

6. Replace `YOUR-USERNAME` with your actual GitHub username. If GitHub asks you to sign in, complete the browser sign-in.
7. Open the repository in a private/incognito browser window and verify it is publicly viewable.
8. Copy the repository URL into the report and Microsoft Form.

Never commit API keys, passwords, private resumes or personal data. This starter package contains no API keys.

---
name: cv-git-commit
description: Auto-commit and push changes to git after each task completion in this CV project.
---

# Git Auto-Commit for CV Project

## Prerequisites
Before running any git commands, start the SSH agent:
```bash
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_goviedodev
```

## Workflow

1. Run `git status` to see changed files
2. Run `git diff` to review changes
3. Run `git log --oneline -3` to see recent commits (for message style)
4. Add all changes: `git add .`
5. Create a descriptive commit message (1-2 sentences, focus on "what" changed)
6. Commit: `git commit -m "message"`
7. Push: `git push`

Commit message examples:
- "Add English CV version cv-en.tex"
- "Update technical skills with Blockchain section"
- "Fix typo in professional summary"
- "Reorder sections: skills now appear after summary"

Do NOT commit:
- Auxiliary files (*.aux, *.log, *.out) - already ignored

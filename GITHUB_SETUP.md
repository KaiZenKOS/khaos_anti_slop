# Publish KHAOS Anti Slop to GitHub

**Repository name:** `khaos-anti-slop`

**Suggested About description:**
An agent skill that challenges template UI, unnecessary code, misleading demos, and empty writing. Keep what works. Cut what doesn’t.

**Topics:** `agent-skills`, `claude-code`, `codex`, `ai-slop`, `ui-ux`, `code-quality`, `humanizer`, `developer-tools`

1. Create a **Public** repository at https://github.com/new. Choose the correct
   owner (personal account or team organization).
2. Name it `khaos-anti-slop` and paste the About description.
3. Do **not** pre-create README, .gitignore or licence on GitHub; this package
   already includes them.
4. Extract this archive, then run from its extracted folder:

```bash
git init -b main
git add .
git commit -m "feat: publish KHAOS Anti Slop"
git remote add origin https://github.com/OWNER/khaos-anti-slop.git
git push -u origin main
```

5. Replace `OWNER` with the chosen account or organization.
6. Add the suggested topics in GitHub's About settings.
7. Check the Actions tab: `Skill checks` should run. Make sure the
   `SKILL.md` preview, reference links and install commands resolve.
8. Replace `OWNER` in README.md with the published repository owner in a
   follow-up commit.

Avoid pushing credentials, private team data, or copyrighted screenshots from
someone else's Reel. This repo contains written reviews of visual patterns,
not copies of the screenshots.

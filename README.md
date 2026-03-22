---
title: Virtual Resume — Career Conversations
emoji: 💼
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 5.22.0
python_version: 3.12
app_file: app.py
pinned: false
---

<!-- Frontmatter above is generated from hf.space.toml via: python scripts/render_readme.py -->
<!-- Frontmatter above is generated from hf.space.toml via: python scripts/render_readme.py -->

# Virtual Resume — Career Conversations

Gradio chat app: **Ayush Mehrotra** career assistant (bio + LinkedIn PDF + Groq + optional Pushover tools).

**Live Space:** `https://huggingface.co/spaces/<namespace>/<name>` — values come from [`hf.space.toml`](hf.space.toml).

---

## Hugging Face CI/CD (GitHub → Space)

| Piece | Purpose |
|--------|---------|
| [`hf.space.toml`](hf.space.toml) | **Single config:** Space `namespace` / `name` + README frontmatter (title, sdk, colors, …). |
| [`scripts/render_readme.py`](scripts/render_readme.py) | Regenerates the YAML block at the top of this file after you edit `hf.space.toml`. |
| [`scripts/export_github_env.py`](scripts/export_github_env.py) | Used by Actions to read `hf.space.toml` and set `HF_NAMESPACE` / `HF_SPACE_NAME`. |
| [`.github/workflows/sync-to-huggingface.yml`](.github/workflows/sync-to-huggingface.yml) | On every push to **`main`**, runs `git push` to your Space repo. |
| [`requirements.txt`](requirements.txt) | What **Hugging Face Spaces** installs at build time (keep aligned with `app.py`). |

### One-time setup

1. **Create the Space** on Hugging Face (same `namespace` and `name` as in `hf.space.toml`), SDK **Gradio**, or use an existing Space.
2. **First sync from your laptop** (once histories match, you can rely on Actions only):

   ```bash
   git remote add space https://huggingface.co/spaces/YOUR_NAMESPACE/YOUR_SPACE_NAME
   git push --force space main
   ```

   Use your real namespace/name from `hf.space.toml`.

3. **GitHub secret:** repo → **Settings → Secrets and variables → Actions** → create **`HF_TOKEN`**  
   Use a Hugging Face token with permission to **write** to that Space repo ([HF access tokens](https://huggingface.co/settings/tokens)).

4. **Space runtime secrets** (not in git): Space → **Settings → Variables and secrets**  
   `GROQ_API_KEY`, `PUSHOVER_TOKEN`, `PUSHOVER_USER` (see [`.env.example`](.env.example)).

5. **Regenerate README frontmatter** after any `hf.space.toml` edit:

   ```bash
   python3 scripts/render_readme.py
   ```

6. Push to **`main`** on GitHub — the workflow **Sync to Hugging Face Space** updates the Space automatically.

### Changing Space or branding

Edit **`hf.space.toml`** only, then:

```bash
python3 scripts/render_readme.py
git add README.md hf.space.toml
git commit -m "Update HF Space config"
git push origin main
```

### Limits

- Files **> 10 MB** must use **Git LFS** or HF push/build may fail (workflow uses `lfs: true` on checkout).
- Official pattern reference: [Managing Spaces with GitHub Actions](https://huggingface.co/docs/hub/spaces-github-actions).

---

## Local run

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill keys
python app.py
```

Or: `uv sync && uv run python app.py` if you use the full `pyproject.toml` set.

---

## Layout

| Path | Role |
|------|------|
| `app.py` | Gradio UI, Groq client, tools |
| `me/summary.txt`, `me/AyushMehrotra_Linkedinpdf.pdf` | Context for the agent |
| `requirements.txt` | HF + minimal local installs |
| `pyproject.toml` | Broader dependency set / notebooks |

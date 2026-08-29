# Setup

Everything here is already built. You can push it as-is and the profile will
render. These are the steps to get it live, and then how to change it.

---

## 1. Create the profile repository

A GitHub profile README lives in a repository named **exactly** the same as your
username. Yours does not exist yet &mdash; `github.com/Tayab-Ahamed/Tayab-Ahamed`
currently returns 404.

1. Go to <https://github.com/new>
2. Repository name: **`Tayab-Ahamed`** (GitHub will show a note saying you've
   found a secret &mdash; that is the confirmation you got the name right)
3. Visibility: **Public** (required; a private profile repo will not render)
4. Do **not** tick "Add a README file" &mdash; this project already has one
5. Create

## 2. Push

From inside this folder:

```bash
git init
git add .
git commit -m "AI Research & Engineering Lab profile"
git branch -M main
git remote add origin https://github.com/Tayab-Ahamed/Tayab-Ahamed.git
git push -u origin main
```

Open <https://github.com/Tayab-Ahamed>. The profile is live.

> The images are relative paths inside this repository, so they only render once
> the repository is public and pushed. If you preview `README.md` locally in an
> editor, some viewers will not resolve `<picture>` &mdash; that is the editor,
> not the file.

---

## 3. Contact links

The LinkedIn and live portfolio links are configured in `README.md`.

---

## 4. Changing anything

All facts live in one file: **`scripts/repos.py`**. The SVG assets are generated from it:

```bash
python3 scripts/build_assets.py
```

No dependencies, no `pip install`. Python 3.8 or newer.

---

## 5. The GitHub Action

`.github/workflows/build-assets.yml` rebuilds and commits the assets when you
change anything in `scripts/`. It does **not** run on every push to `main`,
because the job pushes to `main` itself and that would loop.

It is optional. If you would rather just run `build_assets.py` locally before
committing, delete the `.github` folder &mdash; nothing else depends on it.

---

## 6. A note on what is not here

No star counts, no follower counts, no streak widgets, no trophy images, no
visitor counters, no contribution snake.

Those numbers are currently zero on your account. A profile that leads with
zeroes, or that dresses them up with animated widgets, undercuts the twelve real
systems it is trying to show you built. Every number on this page &mdash; twelve
repositories, four divisions, five months, one live deployment &mdash; can be
checked against your repository list in about thirty seconds.

When the stars and followers arrive, they will be worth showing. Not yet.

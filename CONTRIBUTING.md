# Contributing to RIFTWEAVE

Thanks for weaving with us. This repo is a full UE5 game — code, docs, and pipeline.

## Ground rules
- No private info: no keys, tokens, internal paths, or personal data. The `.gitignore` blocks `*.pem`, `.env`, `Saved/`, `ue5_mass_project_prompt.txt`.
- Keep commits English (or bilingual). Use Conventional Commits: `feat(weaving): add anchor charge curve`
- LFS: `*.uasset`, `*.umap`, `*.fbx`, `*.wav` must go via Git LFS.

## Getting started
```powershell
git clone <repo>
cd RiftWeave
.\Scripts\Setup.ps1   # checks VS2022 + UE5.4 + runs GenerateProjectFiles
.\Scripts\Build.ps1 -Target Editor
```

## Where to contribute
- `Source/RiftWeave/` — C++ gameplay
- `Plugins/` — weaving / streaming plugins
- `Documentation/` — GDD chapters (Markdown, keep line length < 100)
- `Content/` — only placeholder descriptors; heavy assets via LFS + Quixel pipeline (`Tools/AssetPipeline/`)
- `Scripts/` + `.github/workflows/` — automation

## Code style
- Unreal naming: `U`, `A`, `F` prefixes, PascalCase.
- Include order: Core → Engine → Project.
- Every public header needs a one-line `///` doc comment.
- Run `.\Scripts\ValidateAssets.py --all` before PR.

## Design docs
Edit under `Documentation/`, keep the single source of truth — no duplicate lore in code comments.

## Pull requests
1. Branch from `main`: `feat/your-feature`
2. `git commit -m "feat(scope): message"`
3. Push, open PR with checklist (build passed, docs updated, no secrets).
4. One reviewer from WeaveWorks required.

Happy weaving.

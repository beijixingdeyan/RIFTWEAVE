# Asset Pipeline — RiftWeave

## Flow
Quixel Bridge -> FBX/EXR -> `import.py` -> UE Content -> validate

## Scripts
- `validate_assets.py --all` : naming + Nanite + generated.h checks
- `import.py` : batch import with Nanite flags (see Config/AssetImport.json)

## Config
`Tools/AssetPipeline/AssetImport.json` defines per-folder Nanite policy.

## CI
GitHub Actions runs validate on every PR.

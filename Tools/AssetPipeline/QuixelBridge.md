# Quixel Bridge -> RiftWeave Pipeline
1. Megascans -> Bridge -> Export FBX/EXR to Tools/QuixelImport/
2. `py Tools/AssetPipeline/import.py --bridge` -> auto Nanite on/off per AssetImport.json
3. Master Material M_WeaveMaster (Substrate) assignment
4. Validate: `py Tools/AssetPipeline/validate_assets.py --all` (Nanite + generated.h + docs)
5. HLOD build: `UHLODBuilder_RiftWeave::BuildHLODForBiome` per DataLayer

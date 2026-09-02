# PCG_RiftCracks (PCG Graph)
- **Input**: Spline + DataLayer mask
- **Nodes**: SurfaceSampler (4000/km2) -> Noise (crack) -> PruneBySlope -> StaticMeshSpawner (SM_RiftCrack_A/B/C, Nanite)
- **HLOD**: Clusters 128m, validates via HLODBuilder_RiftWeave
- **Perf**: 2ms at 1km radius, cull 80m

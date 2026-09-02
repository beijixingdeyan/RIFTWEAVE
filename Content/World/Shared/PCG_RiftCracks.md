# PCG — Rift Cracks

Graph: PCG_RiftCracks (WP_RiftWeave)
- Input: Spline + DataLayer mask
- Nodes: SurfaceSampler -> Noise (crack) -> Prune by slope -> StaticMeshSpawner (SM_RiftCrack_*)
- Nanite meshes: SM_RiftCrack_A/B/C (2k-8k tris, Nanite yes)
- Perf: 4000 instances per km2, culling 80m

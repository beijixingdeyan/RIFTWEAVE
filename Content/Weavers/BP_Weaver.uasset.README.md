# BP_Weaver — Character Blueprint

- **Parent**: ARiftWeaveCharacter (C++)
- **Mesh**: MetaHuman-derived Weaver (ControlRig face + body, 4 LODs) — **Nanite: No** (skinned mesh, traditional LOD; Nanite not supported for skeletal). HLOD handled via LOD sync.
- **Anims**: WeaverAnimInstance + MotionWarping (vault/pull)
- **Cloth**: Chaos Cloth cloak, thread ribbons (wind + weave drag)
- **VFX**: Niagara NS_WeaveTrail attached to hand socket
- **Nanite policy**: Character excluded per Nanite strategy (see Documentation/04_TechImplementation.md)

To rebuild: import MetaHuman to /Content/Weavers/MH_Weaver, retarget via IK Retargeter RTG_Weaver.

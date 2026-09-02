# NS_WeaveTear (Niagara System)

- Emitter 1: Ribbon (fiber) - spawn on Chaos field sample, Substrate emissive
- Emitter 2: Mesh debris - spawn on tear progress
- Params: TearProgress (0-1), Stability (0-1)
- Perf: 2k particles max, cull 50m
- Nanite: N/A (VFX, not mesh; mesh debris uses Nanite GC via WeaveFieldSystem)

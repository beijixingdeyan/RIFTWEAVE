# MS_Loom_Base (MetaSoundSource)

- Inputs: Stability (float 0-1), BiomeBlend (float), WeaveTrigger (trigger)
- Quartz: 120 BPM, quantized to 1/8
- Graph: Granular (Stability -> grain density) + 3x filter (BiomeBlend -> crossfade)
- Output: Stereo + reverb send (Lumen-driven)
- Controlled via UMetaSoundWeaveController (C++)

## Nanite: n/a (audio)
## Lumen: drives reverb

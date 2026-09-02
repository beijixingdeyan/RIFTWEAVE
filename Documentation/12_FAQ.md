# FAQ — RiftWeave

## Does it require UE?
No. All GDD is Markdown; code is readable without building. Build only if you have UE 5.4 + VS2022. The repo is designed to be reviewable on GitHub alone.

## Is it a tech demo?
No. Nanite/Lumen/Chaos are gameplay: tear needs Nanite detail, light-drag needs Lumen GI, destruction needs Chaos. All serve the 5-min loop. We use tech to create mechanics other engines cannot (fiber-level tear + cross-dimensional GI puzzles).

## Can I play solo?
Yes. AI companion (AAIWeaverCompanion) fills anchors via StateTree + SmartObject. Solo puzzle S_max 0.6, co-op 1.2 — solo is calm puzzle, co-op is physical comedy. No content is co-op gated in a punitive way.

## How big is the world?
16km2 World Partition, 3 DataLayers (Obsidian/Frostvein/Canopy), 52 POIs, 40 Patterns, 20h main + 100h repeatable (Daily Rift, Workshop, Photo, Speedweave, async ghosts).

## Monetization?
Buy-to-play $29.99, cosmetics only, all earnable via Thread currency. No pay-to-win, no loot boxes, no stamina. Season Pass $9.99 gives early Pattern access, not exclusive.

## Performance?
See 04_TechImplementation.md scalability table. PC Ultra 4K60 (Nanite 1px, HWRT), PS5 60 (Nanite 2px, SWRT). Mass 3000 -> 1500 on console via dormancy. Tested on Test_Mass_2000 map.

## UGC?
Loom Workshop in-game (Substrate + Niagara editor); patterns tradeable in Plaza market; Creator Fund (20% season revenue shared by subscription*lights). PCG graphs shareable.

## Accessibility?
3-button core (Weave/Anchor/Interact), remappable, single-stick mode, color-blind palettes (shape + pattern, not just hue), subtitles + directional captions, haptics, FOV options.

## Why "RiftWeave"?
Rift + Weave = you tear rifts and weave them. Chinese "织裂者" = one who weaves rifts. "织裂" has tension: to weave is to mend, to rift is to break — the anti-intuitive core.

## Where to start reading?
`Documentation/README.md` is index. Non-dev: start `00_Phase0_ExperienceValidation.md`. Dev: start `04_TechImplementation.md` + `Source/RiftWeave/Public/Weaving/WeaveComponent.h`.

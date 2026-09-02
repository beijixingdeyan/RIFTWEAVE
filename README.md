# RIFTWEAVE — 织裂者

> **"Tear a volcano open, pour its lava into winter, and make a hot spring with your friends."**
> 4-player cooperative dimension-weaving adventure built in **Unreal Engine 5.4** — where Nanite, Lumen, Chaos, MassAI and MetaSounds are not tech demos, but *play*.

[![Engine](https://img.shields.io/badge/Unreal-5.4-black?logo=unrealengine)](https://www.unrealengine.com)
[![Platform](https://img.shields.io/badge/Platform-Win%20%7C%20PS5%20%7C%20XSX-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Pre--Alpha%200.9-orange)](#)

[English](#english) | [中文](#中文)

---

## English

### What is RIFTWEAVE?

RIFTWEAVE is a **large-scale, mass-market, co-op adventure** for people who don't normally play games — and for those who've played 100+ and still want surprise.

You are a **Weaver**, born with a needle that can **tear the seams between dimensions** and stitch them back together. Drag magma from the **Obsidian Forge** into the frozen **Frostvein Tundra** to create a steaming onsen. Rip the glowing canopy of the **Luminous Jungle** and graft it over a dead city to bring it back to life. Every puzzle has a chaotic, physics-driven solution that only works because 2–4 friends are holding different dimensional anchors at once.

**Golden formula:** Cinematic first impression (UE5) + 5-minute core loop (tear → drag → weave) + 100-hour freshness (emergent physics × biome chemistry) + social currency (your weaves are shareable screenshots) + UGC (in-game loom editor).

### Core Promise — 5 Minutes In

| Min | What happens | Feeling |
|-----|--------------|---------|
| 0:00 | Press Start — no logos, you wake in a broken loom-temple, thread in hand | *Mystery* |
| 0:30 | First tear — swipe RT/RMB, world peels like fabric, Lumen light bleeds through | *Power* |
| 1:30 | Drag a cube of lava across the tear — Chaos debris, Niagara sparks, it sizzles on snow | *Delight* |
| 3:00 | Puzzle: with a friend, each holds one anchor, bridge forms only when you both pull | *Laughter* |
| 5:00 | Photo Mode auto-triggers — your absurd lava-hot-spring is already Instagram-ready | *Share it* |

**Core controls (mass-market):** Move + Look + **Weave** (tear/drag) + **Anchor** (pin) + **Interact**. That's it. Depth is *where* and *when* you weave, not extra buttons.

### Why it's not "another UE5 demo"

- **Anti-intuitive design:** *Destruction is creation.* In most games you break things to remove them; here you break reality *to build* — the more you destroy, the richer the world gets.
- **UE5 as mechanic:** Nanite lets you tear a mountain down to pebble grain and Nanite re-tessellates the seam without LOD pop; Lumen's cross-dimensional GI is the puzzle — light dragged from one biome *is* the key to another; Chaos fields are your brush.
- **1+1 > 2 cooperation:** Single-player is a calm puzzle; co-op adds *coupled physics* — a river only flows when Player A holds the source and Player B tilts the sink. Miscommunication = hilarious flood.

### Three Biomes (visually, mechanically, narratively distinct)

1. **Obsidian Forge** — Volcanic foundry. Vertical, hot, Chaos destruction (shatter basalt, forge bridges). Lumen: harsh emissive lava vs. deep shadow. Story: the Forgefather who refused to let go.
2. **Frostvein Tundra** — Endless white with crystal caves. Horizontal, cold, light-as-gameplay (refract Lumen through ice to grow plants). MassAI: migrating herds of 2k frost-elk. Story: a child waiting for a thaw that never came.
3. **Luminous Canopy** — Bioluminescent megajungle. Dense, vertical+horizontal, Niagara magic + wind physics (spore clouds, vine Chaos). World Partition streaming at its densest. Story: the forest that learned to remember.

20h main path (weave the three hearts back together) + 100h repeatable (daily rifts, loom workshop, herd photography, speed-weaves).

### UE5 Architecture Highlights

| Feature | How we use it (gameplay, not brochure) |
|---------|----------------------------------------|
| **Nanite + Virtual Shadow Maps** | Every tear reveals sub-mm fabric weave; Nanite keeps 10B tris seamless |
| **Lumen HWRT** | Drag light between dimensions — puzzles where sunlight *is* a resource |
| **Chaos Destruction / Flesh / Cloth** | Seam tearing is a Chaos Field; cloaks and thread ribbons are Chaos Cloth |
| **Control Rig + Motion Warping** | Weave gestures adapt to terrain slope + distance — no foot sliding |
| **MassAI + StateTree + SmartObjects** | 3k agents (elk, drones, civilians) at 60fps; emergent herding / panic |
| **MetaSounds + Quartz** | The loom hums to your pull strength; music layers follow biome blend ratio |
| **World Partition + HLOD + Data Layers** | 16 km² seamless, per-biome streaming + dimensional data layers |
| **Iris + Replication Graph** | 4-player co-op, 50-player plaza (market), low bandwidth, server authoritative |
| **PCG + Substrate** | Procedural rift cracks + layered material blending at seams |

See [`Documentation/04_TechImplementation.md`](Documentation/04_TechImplementation.md) for full specs.

### Quick Start (Dev)

```powershell
# 1. Clone (SSH)
git clone git@github.com:YourOrg/RiftWeave.git
cd RiftWeave

# 2. Associate with UE5.4 (or right-click .uproject → Generate VS files)
# Requires Visual Studio 2022 + "Game development with C++" + .NET 8 + Windows 10 SDK

# 3. Build editor (PowerShell)
.\Scripts\Build.ps1 -Target Editor -Config Development

# 4. Open
# Double-click RiftWeave.uproject — first open builds DDC (15-30 min)

# 5. Play
# PIE → Lobby (L_Lobby) → "Host Rift" → invite via EOS/Steam
```

No UE installed? Read the design-only path: [`Documentation/`](Documentation/) is fully self-contained — you can review the entire GDD without opening the engine.

### Project Structure

```
RiftWeave.uproject
Config/               # Engine / Game / Input / Scalability (Nanite/Lumen/Chaos tuned)
Source/RiftWeave/     # C++ gameplay — Core/Dimension/Weaving/AI/Physics/Audio/World/Multiplayer/UI/Animation
Plugins/              # RiftWeaveWeavingSystem + DimensionStreaming (editor + runtime)
Content/              # World/ Biomes / Weavers / UI / Audio/MetaSounds / Niagara (placeholders + PCG graphs)
Documentation/        # 12-chapter GDD — Phase0 validation → LiveOps
Scripts/              # Build.ps1, Setup.ps1, ValidateAssets.py
Tools/AssetPipeline/  # Quixel → Nanite import + auto-LOD + validation
```

### Controls

| Action | KB/M | Gamepad |
|--------|------|---------|
| Move / Look | WASD + Mouse | LS + RS |
| Weave (Tear/Drag) | Hold LMB + drag | Hold RT + RS |
| Anchor | RMB (tap to pin, hold to charge) | LT |
| Interact / Photo | E / P | A / Share |

Accessibility: remappable, hold-to-toggle, color-blind palettes, single-stick mode, subtitles + haptics.

### Business

**Cosmetics-only**. Buy-to-play (29.99 USD) + seasonal loom patterns / emotes / housing. No pay-to-win. Every paid cosmetic is craftable via in-game weaving mastery (tradeable in player market).

### Roadmap (2-3 years scoped for 30-50 persons)

- **Pre-prod (6 mo):** Vertical slice — one rift, two players, one biome blend
- **Year 1 Prod:** Core systems + Obsidian + Frostvein + 30% content
- **Year 2 Prod:** Luminous Canopy + polish + PS5/XSX cert + accessibility
- **Live:** Seasons (new rift modifiers), Loom Workshop (UGC), Creator Fund

Full plan: [`Documentation/10_ProductionPlan.md`](Documentation/10_ProductionPlan.md)

---

## 中文

### 这是什么游戏？

《织裂者》（RIFTWEAVE）是一款**30-50人团队、2-3年量级的面向大众的合作冒险**。你是一名**织者**，手握能撕开维度缝隙的织针。你可以把火山世界的岩浆拖进冰雪世界泡温泉，把发光雨林的穹顶嫁接到废弃都市让其重生。核心乐趣是 **“撕 → 拖 → 缝”** 每5分钟一次的创造性胡闹——一个人是解谜，两个人是手忙脚乱的厨房、三个人是灾难喜剧、四个人是奇迹。

**黄金公式：** 电影级第一眼 + 5分钟上手的撕拉手感 + 100小时不重复的涌现（物理×生态化学反应）+ 社交货币（每一张缝合截图都值得发朋友圈）+ UGC（游戏内织机编辑器，玩家的缝合比官方多100倍）。

**反直觉设计：破坏即创造。** 别的游戏破坏是为了移除，这里破坏得越多，世界越丰富。

详细五问验证、首5分钟分镜、100小时内容曲线见 [`Documentation/00_Phase0_ExperienceValidation.md`](Documentation/00_Phase0_ExperienceValidation.md)。

### 如何运行

同上英文 Quick Start；无虚幻引擎也可直接阅读 `Documentation/` 完整策划案。

### 贡献

欢迎 Issue / PR。请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md) 与 [`Documentation/09_Pipeline.md`](Documentation/09_Pipeline.md) 的资产管线。

### 许可

MIT — 详见 [LICENSE](LICENSE)。美术/音频占位资源仅示例，商用需替换为 Quixel/Marketplace 授权资产。

---

**No private info in this repo.** Build with `.\Scripts\Build.ps1` — share via screenshots, not secrets.


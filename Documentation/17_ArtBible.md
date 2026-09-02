# 美术圣经 (Art Bible) — Woven Realism

## 核心
**织物现实主义 + 光学奇幻**。近看纤维(0.2mm Nanite)，远看地貌(Lumen大气)。Ref: 吉卜力+死亡搁浅+纪念碑谷+织物微距。

## 三生态
| 生态 | 形状 | 主色 | 光 | 材质 |
|------|------|------|----|------|
| Obsidian | 锋利阶梯 | 墨黑#0A0A0F+橙#FF4D00 | 硬橙 | 玄武岩织纹+熔岩emissive |
| Frostvein | 圆润平原 | 霜白#F0F8FF+青#00E5FF | 冷散 | 冰经纬+RVT雪 |
| Canopy | 有机巨柱 | 夜绿#0B1A12+荧光#1BFF8A | 斑驳 | 树皮+苔RVT+荧光 |

## 角色
- **Weaver**: 1:7.5, 中性, 4预设, 斗篷Chaos Cloth, 针发光
- **锻父**: 皱纹Nanite位移, 烫疤, ControlRig 52 BS
- **孩子**: 圆脸大眼, 1:4, MotionWarping抱
- **线灵**: 半透明, Niagara发丝, 瞳孔织线

## 材质 (Substrate)
`M_WeaveMaster`: 3 slabs (Base+Seam 2.0+RVT Cover), SeamProgress 0-1, PatternId, BiomeBlend, RVT 5000
Instances: MI_Obsidian/Frostvein/Canopy/StarrySpring

## 灯光
Lumen主导, 无烘焙, 每生态PostProcess体积, 权重由DimensionManager驱动, 黄昏三色同时出现最美

## 特效
Niagara: WeaveTear (ribbon+debris), StitchWeld (sparks~Stability), BiomeBlendFog, PhotoConfetti

## 概念板
- Obsidian: 风之谷腐海工厂+冰岛火山
- Frostvein: 死亡搁浅雪原+挪威极光
- Canopy: 吉卜力+湮灭闪光

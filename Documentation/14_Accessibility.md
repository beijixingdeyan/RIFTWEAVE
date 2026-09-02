# 无障碍设计 (Accessibility) — 面向大众的完美

## 目标
“手残也能贡献，色盲也不迷路，单手也能编织，听障也能共鸣”。

## 操作无障碍
| 需求 | 实现 | 验证 |
|------|------|------|
| **3键核心** | Move+Look+Weave/Anchor/Interact，仅5动作，Sprint折入Weave hold | EnhancedInput IMC_Weaver，`UWeaverInputConfig` |
| **重映射** | 全动作可重绑，可视化按住Weave显示绑定 | `AccessibilitySubsystem::SetHoldToWeave` |
| **单手模式** | 单摇杆：移动+视角合并，长按Weave切换；锚点自动吸附最近 | `SetSingleStick(true)`，测试：单手通关前2h |
| **Hold切换** | Weave/Anchor 支持 Hold ↔ Toggle，用户可选 | `SetHoldToWeave` |
| **震动替代** | 缝合张力通过屏幕织线绷紧+声音表现，不依赖震动 | HUD ring + MetaSounds |

## 感知无障碍
| 需求 | 实现 |
|------|------|
| **色盲** | 三生态形状区分（Forge尖锐/Frostvein圆润/Canopy有机）+ 高对比织线黄/紫模式 + 织纹图标非纯色 | 
| **色盲预览** | Editor `ColorBlindPreview` (CommonUI)，模拟Deuteranopia/Protanopia/Tritanopia |
| **字幕** | 全对白字幕 + 方向声波圈 + 织造提示视觉化 | 
| **高对比** | UI 120%缩放，高对比织线，发光缝线 2.0 emissive | 
| **FOV** | 90固定，Weave拖动不改FOV（防晕），可选黑边缩窄 | 
| **音频** | 方位字幕，MetaSounds参数可视化（Stability ring） | 

## 认知无障碍
- **每屏≤3信息**：HUD仅环+pips，提示3秒淡出
- **无文字教学**：环境引导+幽灵示范+线灵慢动作
- **可回放**：神殿织机可重看教程
- **安全网**：超时20s示意角度，超时降低S要求30%

## 测试
- **色盲**：3种模式下POI可读性 >95%
- **单手**：测试员单手完成 5分钟分镜
- **听障**：关闭声音通关主线

# 多人/社交系统

## 网络同步策略

- **Authority**：Dedicated Server 权威 (Weave 稳定性、谜题解算、World Partition 持久化)。
- **RPC 聚合**：`Server_UpdateDrag` 每 0.05s 聚合一次，减少 80% 包。
- **Iris**：自适应频率——Weaving 时 30Hz，闲置 10Hz。`UWeaveComponent` 的 `Stability` 用 `ReplicatedUsing` 插值。
- **MassAI**：仅同步首领 Elk，其余客户端预测 (StateTree 相同种子)。

## 合作机制设计

| 机制 | 人数 | 规则 |
|------|------|------|
| 锚点 | 1-4 | 每多一锚点 +0.3 B，角度误差 <15° 才满分 |
| 耦合物理 | 2-4 | 桥/河/藤的物理张力由所有锚点平均拉力决定 |
| 复活 | - | 跌落 → 队友 2s 内 Interact 拉回 (参考双人成行)，无惩罚 |
| 语音 | - | EOS Voice 队伍 + 轮盘表情 (无 mic 也可) |

## 异步社交 (死亡搁浅式共享世界)

- **幽灵层**：你的编织以 DataLayer 幽灵 (低 HLOD) 存于 `Iris` 的 `SparseReplication`，他人世界每 30s 拉取前 20 个高赞幽灵。
- **点亮**：他人可 Interact 点亮你的幽灵，你收线币 + 通知 (MetaHuman 感谢信)。
- **市集**：Plaza (50 人) 展示全服 Top10 编织 (投票)，可进入其原始坐标参观 (传送)。
- **反悲伤**：幽灵不可破坏他人谜题，仅装饰层；举报 → 隐藏。

## 反作弊 (如竞技元素)

- 无 PvP 竞技，仅合作 + 速通榜。
- 速通榜：服务器重放校验 (Weave 路径 + 时间)，异常 (WeaveReach >4km) 标记人工审核。
- 经济：线币仅外观，不可交易为现实货币，无 Pay-to-Win 诱因。

## 详细带宽预算

| 通道 | 频率 | 大小 | 备注 |
|------|------|------|------|
| Weave RPC | 20Hz 聚合 | 24 bytes | 位置+法线 |
| Stability | 10Hz | 4 bytes | float |
| Mass (首领) | 10Hz | 16 bytes | pos+vel |
| 幽灵 | 0.03Hz (30s) | 1KB 批 | Top20 |

- 总计 4 人 <40KB/s 上行，符合 Iris 自适应。

## 社交礼仪

- 默认静音，轮盘 8 表情 + 4 快捷 (“来锚点”“看光”“拍照”“谢谢”)。
- 恶意：投票踢 (需 3/4 同意)，幽灵举报 3 次自动隐藏。

## 测试计划

- Gauntlet 4-client 编织同步测试：同一裂缝 4 人同时拖，校验 S 一致 (<0.02 误差)。
- 50 人 Plaza 压力：Mass 800 + 玩家 50，目标 server tick <14ms。

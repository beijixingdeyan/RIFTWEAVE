# QA 计划 — 自动化 + 人工

## 自动化
| 测试 | 频率 | 工具 | 阈值 |
|------|------|------|------|
| 资产校验 | 每提交 | validate_assets.py --all | 0 fails |
| 性能基线 | 每提交CI | Perf_Mass2000 | 16.6ms, nanite12, mass3 |
| 网络同步 | 每提交CI | Gauntlet_WeaveSync (4-client) | delta0.02, tick14ms |
| 兼容 | 每日 | Automation (PS5/XSX) | Test_Mass_2000 |
| 截图对比 | 每周 | Gauntlet screenshot | 像素 diff <2% |

## 人工
| 阶段 | 重点 | 人数 |
|------|------|------|
| Pre-prod | 垂直切片 15min | 5 |
| Y1 Q4 | Obsidian+Frostvein 2h | 10 |
| Beta | 全主线20h + 无障碍 | 20 (含色盲/单手/听障) |
| Cert | PS5/XSX TRC | 5 |

## 缺陷分级
- **S0**: 崩溃/存档丢
- **S1**: 主线阻塞, S<0.4常现
- **S2**: 视觉/音频错
- **S3**: 建议

## 无障碍专项
- 色盲3模式通关
- 单手通关5min分镜
- 听障静音通关

## �ع����
- ÿ�δ��֯��ز��ȶ���
- �Զ�����ͼ�Ա�
- �����ڲ�

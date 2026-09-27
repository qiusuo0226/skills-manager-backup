# Changelog

## 0.2.0 — 2026-09-27

记忆改为顶部概览加按话题拆分，标注来源与决策理由并落盘前自检，新增接手读取与自动交接。

- 目标：记忆 md 从按时间平铺的九节升级为「顶部概览 + 按话题拆分 + 带来源与决策理由」，并补上接手读取与自动交接两条路由
- 契约：`SKILL.md` 路由 3 → 5（+ 读一下交接文件 / 接着上次、开启 / 关闭自动交接）；硬闸 5 → 7（1、3、5 补文，新增 6 落盘前自检、7 接手先复述等确认；原 1～5 无一放宽）；description 触发词 +4，`skill.json` 同步
- 规则：`references/01-write-memory.md`（来源、决策与弯路、篇幅分层、按话题编号合并、第 7 节落盘前自检、第 8 节话题拆分、首次交接问一次是否开启自动交接）；新增 `references/02-read-memory.md`、`references/03-auto-handoff.md`；`references/README.md`
- 模板：`assets/templates/session-memory.md` 加头注「自动交接」、第 0 节概览、第 10 节话题详情、第 11 节决策与弯路、来源列（第 1～9 节编号标题不变）；新增 `assets/templates/auto-handoff-rule.md`
- 示例：新增 `examples/08`～`11`；改 `examples/01`、`05`、`README.md`；根 `README.md` 补新口令与话题拆分说明
- 测试：`tests/cases.md` 保留 0.1.0 五条，新增 T-01～T-24；全量回归见 `governance/regression-reports/RR-20260927-001.md`
- 记录：`CR-20260927-001`～`004`、`IA-20260927-001`～`004`、`upgrade-to-0.2.0.md`；基线 `governance/baselines/0.2.0/`（首次含 `examples/`）
- 治理：§13 白名单补 `examples/`（CR-D）
- 回滚：对照 `governance/baselines/0.1.0/` 恢复分发文件，删除新增的 references / 模板 / 示例，`VERSION` 改回 `0.1.0` 后跑 `sync_version.py`；已写进用户规则文件的常驻片段按 BEGIN/END 标记手动整段删

## 0.1.0 — 2026-09-04

初始化开发仓，并写入会话交接初版规则。

- 版本控制：根目录 `VERSION` + git
- 基线：`governance/baselines/0.1.0/`
- 升级记录：`CR-000-init`、`upgrade-to-0.1.0.md`
- 变更门禁与打包：见 `governance/`
- 能力：把对话收成一份记忆 markdown；落盘前问路径，也可按操作系统建议（例如 Windows 下的 Downloads）
- README 仓库栏：GitHub 与 Gitee 两个地址
- `examples/`：整份交接、路径已给、路径未指定、记住原话、合并旧文件、口令不写入、装到助手里试用

# 发布核对

目标版本：0.2.1（2026-09-08 已勾完。下一周期开始前清勾选并改目标版本。）

## 变更控制

- [x] 有 AP，用户已同意执行
- [x] 有 CR，目标可验证，没有混入无关改动（`CR-20260908-001`）
- [x] 有 IA（`IA-20260908-001`）
- [x] 有 RR（正 / 反 / 旧能力）（`RR-20260908-001`；宿主项 blocked）

## 版本与记录

- [x] 根目录 `VERSION`、`skill.json` 的 `version`、`CHANGELOG.md` 该版本段一致
- [x] 已跑 `python governance/scripts/sync_version.py`
- [x] 已写 `governance/migrations/upgrade-to-0.2.1.md`
- [x] 该版本 AP 已删除（思路在 CR / CHANGELOG / upgrade-to / 基线）

## 基线与打包

- [x] `python governance/scripts/snapshot_baseline.py` 已生成且未改历史基线（`governance/baselines/0.2.1/`）
- [x] `python governance/pack/pack.py --skill-root . --dry-run` 不含 `governance/`、`.git/`、`AGENTS.md`（29 文件，无 pdf）
- [x] `python governance/scripts/audit_release.py` 退出码 0

## Git

- [x] 已提交（`5614569`）
- [x] tag 为 `v0.2.1`
- [x] 已推远程（人指令）：`origin`（Gitee）与 `github` 的 `master` + `v0.2.1`
- [x] 发布包：`C:\Users\qiusuo\Downloads\job-research-analyst-Skill-v0.2.1.zip`

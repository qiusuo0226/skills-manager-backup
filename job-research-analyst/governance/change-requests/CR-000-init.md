# Change Request

## Basic Info

| Field | Value |
|---|---|
| CR ID | CR-000-init |
| Current Version | （无，从空仓诞生） |
| Requester | 仇索 |
| Created At | 2026-09-04 |
| Change Type | feature |
| Priority | P2 |
| Status | completed |

## Change Goal

将空文件夹初始化为 Skill `job-research-analyst`（求职调研分析）的开发仓，版本 0.1.0。建立开发基线（版本控制、冻结基线、升级记录、变更门禁、打包与发布审计），并从豆包本地用户技能拷入求职调研规则与使用示例。

## Problem Statement

尚无仓库。

## Scope

初始化写入的仓根文件与 `governance/`（见 `governance/README.md`）。业务规则来自豆包 `job-research-analyst`（`SKILL.md` 与 `references/` 三份细则）。使用示例写在 `examples/`。

## Non-goals

- 不安装到 `~/.grok/skills/`
- 不配置终端用户自动升级
- 不在未确认清单前写盘（本 CR 对应已确认的初始化）

## Acceptance Criteria

1. 根目录有 `SKILL.md`、`VERSION`=`0.1.0`、`skill.json`、`CHANGELOG.md`
2. `governance/baselines/0.1.0/` 存在
3. `governance/rules/skill-governance.md` 存在
4. 发布审计可通过

## Approval

- [x] approved（初始化确认清单）

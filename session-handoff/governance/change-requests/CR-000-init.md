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

将空文件夹初始化为 Skill `session-handoff`（会话交接）的开发仓，版本 0.1.0。建立开发基线（版本控制、冻结基线、升级记录、变更门禁、打包与发布审计），并写入初版业务规则：把对话收成一份记忆 markdown。

## Problem Statement

尚无仓库。会话一长，下一场接不上；需要一份可复用的交接记忆写法。

## Scope

初始化写入的仓根文件与 `governance/`（见 `governance/README.md`）。初版规则：`SKILL.md`、`references/01-write-memory.md`、`assets/templates/session-memory.md`。

## Non-goals

- 不安装到 `~/.grok/skills/`
- 不配置终端用户自动升级
- 不代替用户建远程空仓库（远程地址由用户提供后再挂、再推）

## Acceptance Criteria

1. 根目录有 `SKILL.md`、`VERSION`=`0.1.0`、`skill.json`、`CHANGELOG.md`
2. `governance/baselines/0.1.0/` 存在
3. `governance/rules/skill-governance.md` 存在
4. 发布审计可通过
5. 开口「会话交接 / 帮我记录一下上下文 / 生成记忆 md / 帮我记住下面的话」能路由到写记忆规则

## Approval

- [x] approved（初始化确认清单）

---
name: chainlinker-fe-sync-dev-to-prod
description: >
  只服务 chainLinker-fe 前端：把 development 的新提交同步到 preRelease 并推远程，工作区始终留在 development。同步时检查两边业务代码完全一致；preRelease 的 VUE_APP_REDIRECT_LOGIN 必须为 true，否则改为 true。以后可增加同步规则。触发：新提交了代码、提交了代码、同步预发布、把 development 同步到 preRelease、/chainlinker-fe-sync-dev-to-prod。不要用于其他仓库。
---

# 全链通PC测试分支同步预发布分支（chainlinker-fe-sync-dev-to-prod）

## 身份

只服务 chainLinker-fe 前端：把 development 的新提交同步到 preRelease 并推远程，工作区始终留在 development。同步时检查两边业务代码完全一致；preRelease 的 VUE_APP_REDIRECT_LOGIN 必须为 true，否则改为 true。以后可增加同步规则。触发：新提交了代码、提交了代码、同步预发布、把 development 同步到 preRelease、/chainlinker-fe-sync-dev-to-prod。不要用于其他仓库。

## 工作区

打开本 Skill 所服务的工作目录。本文件是给 Agent 读的入口，细则放 `references/`。

## 路由

| 用户信号 | 加载 |
|---|---|
| （按实际能力填写触发说法） | `references/` 下对应文件 |
| 技能做不到 / 记成升级需求 / 这是 skill 的问题 / 技能缺口 | `references/gap-capture.md` |

细则未写之前：先问用户这个 Skill 第一步要做什么，再把规则落到 `references/`，不要把长文写进本文件。

## 硬闸

1. 未确认的破坏性改动先问。
2. 不要把 `governance/` 写进分发包（`governance/pack/pack.py` 已排除）。

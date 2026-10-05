# 全链通PC测试分支同步预发布分支（chainlinker-fe-sync-dev-to-prod）

只服务 chainLinker-fe 前端：把 development 的新提交同步到 preRelease 并推远程，工作区始终留在 development。同步时检查两边业务代码完全一致；preRelease 的 VUE_APP_REDIRECT_LOGIN 必须为 true，否则改为 true。以后可增加同步规则。触发：新提交了代码、提交了代码、同步预发布、把 development 同步到 preRelease、/chainlinker-fe-sync-dev-to-prod。不要用于其他仓库。

## 开发

本目录是 Skill **开发仓**。版本控制、基线、升级记录和打包都在 `governance/`（不进分发包）。改本 Skill 时让助手读 `governance/rules/skill-governance.md`，不必再调用 skill-devkit。

```
powershell -File governance/dev.ps1 pack
powershell -File governance/dev.ps1 release
```

## 许可证

[MIT](LICENSE) © 2026 qiusuo

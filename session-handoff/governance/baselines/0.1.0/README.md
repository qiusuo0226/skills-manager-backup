# 会话交接（session-handoff）

把当前对话里的需求、资料、进度和约束收成一份记忆 markdown，方便下一场会话接着干。落盘前询问保存位置；未指定时先识别操作系统再建议路径（例如 Windows 下的 Downloads）。触发：帮我记录一下上下文、帮我记住下面的话、会话交接、生成记忆 md。

## 开发

本目录是 Skill **开发仓**。版本控制、基线、升级记录和打包都在 `governance/`（不进分发包）。改本 Skill 时让助手读 `governance/rules/skill-governance.md`，不必再调用 skill-devkit。

```
powershell -File governance/dev.ps1 pack
powershell -File governance/dev.ps1 release
```

远程：

- https://gitee.com/qiusuo0226/session-handoff-skill.git
- https://github.com/qiusuo0226/session-handoff-skill.git

## 许可证

[MIT](LICENSE) © 2026 仇索

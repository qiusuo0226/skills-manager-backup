# 会话交接（session-handoff）

**把当前对话收成一份记忆 markdown，下一场会话只读这一份就能接着干。**

> Capture requirements, sources, progress, and constraints into one memory markdown so the next session can continue without the chat log.

落盘前询问保存位置；未指定时先识别操作系统再建议路径（例如 Windows 下的 Downloads）。

## 仓库

- GitHub：[qiusuo0226/session-handoff-skill](https://github.com/qiusuo0226/session-handoff-skill)
- Gitee：[qiusuo0226/session-handoff-skill](https://gitee.com/qiusuo0226/session-handoff-skill)

## 安装

```bash
npx skills add qiusuo0226/session-handoff-skill
```

或把本仓复制到助手的技能目录，例如 `~/.grok/skills/session-handoff/`。装好后，工作区指到**正在做的那个项目文件夹**，说「会话交接」。

[![skills.sh](https://skills.sh/b/qiusuo0226/session-handoff-skill)](https://skills.sh/qiusuo0226/session-handoff-skill)

## 它只做一件事

```mermaid
flowchart LR
    A["项目文件夹"] --> B["说：会话交接"]
    B --> C["路径已给则写；没给先问"]
    C --> D["一份记忆 markdown"]
    D --> E["下一场先读这份"]
```

不编造对话里没有的事实。口令、密钥、云方人员手机默认不写入。只维护一份记忆文件，不另存过程版本。

## 看一段真实怎么问

对话示例（项目名和人名是假的，问法是真的）：

目录：[examples/](examples/README.md)

建议先看 [01-整份会话交接.md](examples/01-整份会话交接.md)。没给路径看 [03](examples/03-路径未指定会先问.md)。只想记下原话看 [04](examples/04-记住下面的话.md)。

## 开口就能用

| 你说 | 它做 |
|---|---|
| 「帮我记录一下上下文」 | 收成一份记忆 md；没给路径则先问 |
| 「会话交接」 | 同上 |
| 「生成记忆 md」 | 同上 |
| 「会话交接，写到当前目录」 | 路径已给，直接写 |
| 「帮我记住下面的话：……」 | 原话原样追加；已有文件则只改第 9 节 |
| 「装到助手里试用」 | 你开口才拷 |

同义口令：`帮我记录一下上下文`、`帮我记住下面的话`、`会话交接`、`生成记忆 md`。

## 快速开始

1. 安装：`npx skills add qiusuo0226/session-handoff-skill`，或把本仓复制到助手的技能目录，例如 `~/.grok/skills/session-handoff/`。
2. 把助手工作区指到**正在做的项目文件夹**（不要指到本仓上）。
3. 说：「会话交接」或「帮我记录一下上下文」。
4. 没给路径时，选建议的当前目录或 Downloads，也可以自己回路径。
5. 下一场会话先读那份记忆文件。

## 本仓结构

```
session-handoff/
├── SKILL.md
├── skill.json
├── VERSION
├── CHANGELOG.md
├── references/
├── assets/templates/
├── examples/
├── tests/
└── README.md
```

## 开发

本目录是 Skill **开发仓**。版本控制、基线、升级记录和打包都在 `governance/`（不进分发包）。改本 Skill 时让助手读 `governance/rules/skill-governance.md`，不必再调用 skill-devkit。

```
powershell -File governance/dev.ps1 pack
powershell -File governance/dev.ps1 release
```

## 许可证

[MIT](LICENSE) © 2026 仇索

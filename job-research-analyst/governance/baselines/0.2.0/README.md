# 求职调研分析（job-research-analyst）

求职信息调研与职业决策分析。凡对公司、岗位、JD 的调研或求职/跳槽决策，必须使用本技能。默认产出公司深度介绍 Word、薪资福利对比 Excel、员工评价与风险 Excel。只产出可核实信息，不编造。

怎么开口见 [examples/](examples/)。随口「查一下这个公司」「看下这个 JD」也会走完整三件套；只有明确说不要文件时才口头摘要。

## 仓库

- Gitee：[qiusuo0226/job-research-analyst-skill](https://gitee.com/qiusuo0226/job-research-analyst-skill)
- GitHub：[qiusuo0226/job-research-analyst-skill](https://github.com/qiusuo0226/job-research-analyst-skill)

## 安装

```bash
npx skills add qiusuo0226/job-research-analyst-skill
```

或把本仓复制到助手的技能目录，例如 `~/.grok/skills/job-research-analyst/`。装好后，工作区指到**正在做的那个文件夹**，说「帮我调研 XX 公司」或「查一下这个公司」。

[![skills.sh](https://skills.sh/b/qiusuo0226/job-research-analyst-skill)](https://skills.sh/qiusuo0226/job-research-analyst-skill)

## 快速开始

1. 安装：`npx skills add qiusuo0226/job-research-analyst-skill`，或把本仓复制到助手的技能目录。
2. 把助手工作区指到**正在做的那个文件夹**（不要指到本仓上）。
3. 说：「帮我调研 XX 公司」「查一下这个公司」或「看下这个 JD」。
4. 助手会先声明三件套文件名；缺岗位/城市/简历时同一轮问清（记忆里已有则不二次要简历）。公开信息不够就标明，不编造。

## Qoder 广场描述（发布后手工粘贴）

广场「显示名 / 分类 / 描述」不在本仓。显示名可用「求职调研分析 / Job Research Analyst」，分类「人力招聘」。

若广场「描述」与已安装技能的激活 description **不是**同一字段，可贴稍长稿：

```
求职调研与职业决策分析。帮你查公司、看 JD、比薪资福利、看员工评价和入职风险，产出公司深度介绍 Word、薪资对比 Excel、评价与风险 Excel。只写可核实信息，不编造。适合：查一下这个公司、看下这个JD、这个岗位怎么样、值不值得去、跳槽选哪家、对比这几家、薪资多少、员工评价、有没有坑。
Job research and career decision analysis. Researches companies and JDs from public sources; salary, headcount, expansion/contraction, employee reviews; delivers deep-dive Word + salary/benefits Excel + reviews/risks Excel. Triggers: check this company, look at this JD, salary comparison, is this company worth joining.
```

若广场「描述」就是激活用的同一字段，必须与 `SKILL.md` YAML `description` **同文**（≤1024 字符，命中词不减），不要用上面稍长稿。

YAML `description` 管装上之后会不会自动触发；广场描述管有没有人点安装。正文硬闸不进入广场搜索。

## 开发

本目录是 Skill **开发仓**。版本控制、基线、升级记录和打包都在 `governance/`（不进分发包）。改本 Skill 时让助手读 `governance/rules/skill-governance.md`，不必再调用 skill-devkit。

```
powershell -File governance/dev.ps1 pack
powershell -File governance/dev.ps1 release
```

## 许可证

[MIT](LICENSE) © 2026 仇索

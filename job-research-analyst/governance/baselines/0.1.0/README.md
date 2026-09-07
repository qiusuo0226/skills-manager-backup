# 求职调研分析（job-research-analyst）

求职信息调研与职业决策分析。根据目标国家/城市、平台、公司、岗位方向、学历、经验年限、行业偏好等，检索公开来源，整理岗位薪资、公司规模、扩张/收缩信号、员工工作体验，并产出公司深度介绍、岗位薪资与福利待遇对比、员工评价与风险提示。只产出可核实信息，不编造，不把单一个人言论当事实，不把招聘平台样本误写成全市场结论。触发：XX公司怎么样、XX岗位薪资多少、帮我调研几家目标公司、跳槽选哪家、公司深度调研、薪资福利对比、员工评价、求职调研、职业决策、帮我看看这几家公司、这个岗位值不值得去。Use when the user runs /job-research-analyst.

怎么开口见 [examples/](examples/)。

## 开发

本目录是 Skill **开发仓**。版本控制、基线、升级记录和打包都在 `governance/`（不进分发包）。改本 Skill 时让助手读 `governance/rules/skill-governance.md`，不必再调用 skill-devkit。

```
powershell -File governance/dev.ps1 pack
powershell -File governance/dev.ps1 release
```

## 许可证

[MIT](LICENSE) © 2026 仇索

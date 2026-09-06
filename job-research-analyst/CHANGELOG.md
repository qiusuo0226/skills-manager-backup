# Changelog

## 0.2.0 — 2026-09-06

求职调研请求必须触发本技能并默认产出经结构校验的标准三件套；Word 骨架按焦点领动样例加厚；无记忆时询问简历。

- 契约：`SKILL.md` / `skill.json` 重写 description（中英命中词，679 字）、判定决策树、硬闸 9–14、工作流（声明→范围与简历→采集→验证→填模板→放行）
- 细则：`references/report-templates.md` 重写章节与表头；`evidence-rules.md` 补放行门槛、评价主体、浏览 ≥10 与 B 级 ≥20
- 资产：`assets/templates/company-profile.docx`、`salary-benefits.xlsx`、`reviews-risks.xlsx`
- 脚本：`scripts/validate_deliverables.py`（失败禁止交付）
- 示例：改 01/03，新增 09 事故句式
- 测试：`tests/trigger-set.md`、`tests/test_validate_deliverables.py`
- 行为不兼容：随口问薪资且未拒绝文件时改为出三件套；不要文件须明说并确认
- 回滚：重装 0.1.0 或对照 `governance/baselines/0.1.0/`
- CR：`CR-20260906-001`；升级记录：`upgrade-to-0.2.0.md`
- Qoder 广场描述须发布者在后台粘贴（见 README）；与 YAML 是否同一字段按实际上架确认（B2 O-6）

## 0.1.0 — 2026-09-04

脚手架诞生（初始化）。从豆包本地用户技能拷入求职调研规则，并写使用示例。

- 版本控制：根目录 `VERSION` + git
- 基线：`governance/baselines/0.1.0/`
- 升级记录：`CR-000-init`、`upgrade-to-0.1.0.md`
- 变更门禁与打包：见 `governance/`
- 业务规则：`SKILL.md` + `references/sources.md`、`evidence-rules.md`、`report-templates.md`
- 使用示例：`examples/`
- README 补写 Gitee、GitHub 仓库地址
- README 安装：`npx skills add qiusuo0226/job-research-analyst-skill`

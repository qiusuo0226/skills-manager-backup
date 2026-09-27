<!-- 用法：把 BEGIN～END（含两行标记）贴进 AGENTS.md / CLAUDE.md / Cursor 规则（.cursor/rules/*.mdc 需 alwaysApply: true），替换 {…}。须先经用户同意。 -->

<!-- session-handoff:auto-handoff BEGIN -->
## 自动交接已开启（session-handoff，{开启日期}）
- 记忆文件：`{记忆文件路径}`，只维护这一份，不另存。
- 检查点更新：拍板一项决定、切换话题、完成一步；约每 10 轮至多提示一次（上限，不硬计数）。
- 写前先读当前文件，只增量改受影响的话题节与 §0，保留用户手改。
- 硬闸照旧：无来源不写、不编造；不写口令/密钥等秘密；待确认不进已拍板。
- 写后只回一行：`（已更新交接：{改了什么}）`。
- 关闭：用户说「关闭自动交接」即停，并删除本段（BEGIN 到 END）。
<!-- session-handoff:auto-handoff END -->

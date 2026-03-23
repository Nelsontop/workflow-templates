# Project State Template

## 当前阶段

- 当前目标：清理不再需要的模板参考文件
- 当前切片：删除 `reference/theme.ts` 并同步目录文档
- 允许修改的文件：`reference/theme.ts`、`AGENTS.md`、`project_state.md`
- 当前端别：前端
- 是否已完成前端确认：不适用

## 已完成

- 删除 `reference/theme.ts`
- 同步更新 `AGENTS.md` 目录结构，移除 `theme.ts` 引用
- 新增 `reference/agency/upstream/`，保存筛选后的 agency Markdown 快照
- 新增 `reference/agency/build_index.py`，支持索引生成与关键词查询
- 新增 `reference/agency/index.json` 与 `reference/agency/README.md`
- 补充模板规则：agency 索引为第二优先级，仅在未明确命中本地技能时加载

## 已知问题

- 问题描述：上游快照不会自动同步，需要手动重新抓取并重建索引
- 影响范围：`reference/agency`
- 是否阻塞当前切片：否

## 下一步

- 下一切片：如有需要，补一个专门的快照刷新脚本
- 下一步验收目标：验证索引刷新流程和 README 指引足够清晰
- 是否进入后端开发：否

## 最近一次验证

- 手动验证：已检查 `theme.ts` 引用仅剩目录说明，并已同步移除
- lint：未运行，当前仓库无统一 lint 入口
- typecheck：未运行，当前切片主要为文档和 Python 脚本
- test：未运行，本次切片为文件删除与文档同步
- regression：已用生成后的 `index.json` 抽查字段结构
- preflight：不适用
- commit：未提交
- 前端确认记录：不适用

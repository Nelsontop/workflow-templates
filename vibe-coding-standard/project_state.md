# Project State Template

## 当前阶段

- 当前目标：为模板增加可动态检索的外部参考快照与索引
- 当前切片：引入 `reference/agency` 快照、索引脚本与后备加载规则
- 允许修改的文件：`reference/agency/**`、`tests/reference/agency/**`、`AGENTS.md`、`CLAUDE.md`、`ARCH.md`、`project_state.md`
- 当前端别：前端
- 是否已完成前端确认：不适用

## 已完成

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

- 手动验证：已检查快照目录、README 和索引输出结构
- lint：未运行，当前仓库无统一 lint 入口
- typecheck：未运行，当前切片主要为文档和 Python 脚本
- test：`python3 -m unittest tests/reference/agency/test_build_index.py`
- regression：已用生成后的 `index.json` 抽查字段结构
- preflight：不适用
- commit：未提交
- 前端确认记录：不适用

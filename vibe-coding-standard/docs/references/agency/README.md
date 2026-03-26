# Agency Reference Snapshot

本目录保存来自 `msitarzewski/agency-agents` 的筛选后 Markdown 快照，用作模板内的第二优先级后备参考。

## 来源

- 上游仓库：`https://github.com/msitarzewski/agency-agents`
- 快照提交：`6254154899f510eb4a4de10561fecfc1f32ff17f`
- 保留范围：适合动态加载的 `.md` agent 文档、说明文档、playbook、runbook
- 排除范围：脚本、工作流配置、Issue 模板、许可证、无关资源文件

## 目录入口

- 目录索引：[`directory-index.md`](./directory-index.md)
- 上游快照根目录：[`upstream/`](./upstream/)
- 上游说明：[`upstream/README.md`](./upstream/README.md)

## 使用原则

- `docs/references/agency` 只作第二优先级后备来源，不能覆盖已命中的本地技能。
- 如果用户或上下文已经明确指定技能，例如 `frontend-dev`、`fullstack-dev`、`ios-application-dev`，则不要再额外加载对应领域的 agency 文档。
- 每次最多读取 1 到 3 个最相关的 Markdown 文件，避免把大量外部参考塞进当前上下文。
- 这些文件只作为当前任务的临时上下文，不视为长期记忆，不应在任务结束后继续默认沿用。

## 推荐加载流程

1. 先判断当前请求是否已明确命中本地技能。
2. 若未命中，再查看 [`directory-index.md`](./directory-index.md)。
3. 按分类挑选最相关的 1 到 3 个文档。
4. 只在当前任务中临时读取这些文档。
5. 任务结束后，不把这些内容当作持久上下文继续携带。

## 维护方式

- 不再使用脚本生成索引。
- 新增或调整快照文件时，手动更新 [`directory-index.md`](./directory-index.md)。
- 如分类结构发生变化，同步更新本文件中的入口说明。

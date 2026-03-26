# Agency Reference Snapshot

本目录保存来自 `msitarzewski/agency-agents` 的筛选后 Markdown 快照，用作模板内的后备参考索引。

## 来源

- 上游仓库：`https://github.com/msitarzewski/agency-agents`
- 快照提交：`6254154899f510eb4a4de10561fecfc1f32ff17f`
- 保留范围：适合动态加载的 `.md` agent 文档、说明文档、playbook、runbook
- 排除范围：脚本、工作流配置、Issue 模板、许可证、无关资源文件

## 目录结构

```text
docs/references/agency/
├── README.md
├── build_index.py
├── index.json
└── upstream/
```

## 使用原则

- 本索引是第二优先级，只在当前请求没有明确命中已有技能时才参与检索。
- 如果用户或上下文已经明确指定技能，例如 `frontend-dev`、`fullstack-dev`、`ios-application-dev`，则不要再额外加载对应领域的 agency 文档。
- 每次最多加载 1 到 3 个最相关的 Markdown 文件，避免把大量外部参考塞进当前上下文。
- 这些文件只作为当前任务的临时上下文，不视为长期记忆，不应在任务结束后继续默认沿用。

## 索引生成

```bash
python3 docs/references/agency/build_index.py build \
  --upstream-dir docs/references/agency/upstream \
  --output docs/references/agency/index.json
```

## 索引查询

```bash
python3 docs/references/agency/build_index.py search "react dashboard ui" --limit 3
```

查询结果只返回候选文档元数据。真正加载时，应再按结果读取对应的 `.md` 文件内容。

## 推荐加载流程

1. 先判断当前请求是否已明确命中本地技能。
2. 若未命中，再查询 `docs/references/agency/index.json`。
3. 选择最相关的 1 到 3 个文档。
4. 只在当前任务中临时读取这些文档。
5. 任务结束后，不把这些内容当作持久上下文继续携带。

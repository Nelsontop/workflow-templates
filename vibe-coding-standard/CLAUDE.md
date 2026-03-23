# Claude Compatibility Entry

本文件用于兼容 Claude 系工具的规则发现方式。

请将 [AGENTS.md](/vol3/1000/workspace/workflow-templates/vibe-coding-standard/AGENTS.md) 视为主规则文件。

同步维护要求：

- 修改规则时，优先更新 `AGENTS.md`
- 同一次修改中，同步检查并更新 `CLAUDE.md`
- 如果两个入口存在冲突，以 `AGENTS.md` 为准，并立即修正另一份入口

执行时，请遵守 `AGENTS.md` 中定义的全部流程、边界、安全和文档同步要求。

当前模板的默认约定：

- 多应用目录默认使用 `apps/web` 与 `apps/server`
- 前端优先使用 `frontend-dev`
- 后端优先使用 `fullstack-dev`
- 默认启动方式使用 Docker
- 默认数据库使用 SQLite
- 开发顺序先前端，前端确认后再进入后端

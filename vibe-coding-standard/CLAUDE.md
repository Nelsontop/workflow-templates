# Claude Compatibility Entry

本文件仅用于兼容 Claude 系工具的规则发现方式。

执行时请遵守以下入口顺序：

1. [AGENTS.md](/vol3/1000/workspace/workflow-templates/vibe-coding-standard/AGENTS.md)
2. [project_state.md](/vol3/1000/workspace/workflow-templates/vibe-coding-standard/project_state.md)
3. [docs/index.md](/vol3/1000/workspace/workflow-templates/vibe-coding-standard/docs/index.md)

兼容约定：

- `AGENTS.md` 是主规则文件
- `CLAUDE.md` 只做薄入口，不重复维护长规则
- 若两者冲突，以 `AGENTS.md` 为准，并立即修正 `CLAUDE.md`

长期知识统一放在 `docs/`，不要再把 PRD、架构细节、计划正文直接堆在根目录。

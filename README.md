# workflow-templates

一组面向 AI 辅助开发的工作流模板，目标是把需求、架构、状态和执行约束沉淀为可复用文档，降低 agent 在实现过程中的失控风险。

当前仓库提供的核心模板是 `vibe-coding-standard/`，适合在新项目启动时作为基础骨架复制使用。

## 适用场景

- 你希望在 AI 编码前先锁定需求边界和架构边界
- 你希望把多轮对话中的上下文沉淀为文档，而不是只留在聊天记录里
- 你希望 agent 的改动具备可验证、可回滚、可审计的约束

## 包含内容

`vibe-coding-standard/` 目录内主要包含以下模板文件：

- `AGENTS.md`：主规则文件，定义 agent 的工作流程、边界、安全要求和提交流程
- `CLAUDE.md`：兼容 Claude 系工具的入口，要求与 `AGENTS.md` 保持同步
- `PRD.md`：产品需求模板，定义做什么、不做什么、验收口径
- `ARCH.md`：技术设计模板，定义模块边界、数据流、验证方式和风险
- `project_state.md`：当前切片、已知问题和下一步，作为短期工作上下文

## 使用方式

1. 复制 `vibe-coding-standard/` 到你的项目根目录，或按需拷贝其中的模板文件。
2. 先补齐 `PRD.md`、`ARCH.md`、`project_state.md`，再开始让 agent 改代码。
3. 将 `AGENTS.md` 作为主规则入口；如果你的工具依赖 `CLAUDE.md`，同步保留兼容入口。
4. 每完成一个可验收切片，更新 `project_state.md` 并单独提交。

## 模板约束重点

- 先读文档，再动代码
- 一次只做一个可验收切片
- 改动范围需要显式收敛
- 先验证，再提交
- 文档状态必须与代码同步

这套模板默认建议按交付物类型和实现形态选择合适技能，并把最终结果沉淀回模板文档：

- 交付物导向：`frontend-dev`、`gif-sticker-maker`、`minimax-docx`、`minimax-pdf`、`minimax-xlsx`、`pptx-generator`
- 实现形态导向：`frontend-dev`、`fullstack-dev`、`android-native-dev`、`ios-application-dev`、`shader-dev`
- 需求与架构的最终边界，仍以 `PRD.md` 和 `ARCH.md` 为准，不以技能输出直接替代文档

## 目录结构

```text
workflow-templates/
├── LICENSE
├── README.md
└── vibe-coding-standard/
    ├── AGENTS.md
    ├── ARCH.md
    ├── CLAUDE.md
    ├── PRD.md
    └── project_state.md
```

## 设计取舍

这个仓库选择的是“先约束、后执行”的路线，而不是让 agent 直接从代码表象反推需求。

可选方案至少有两种：

- 方案一：只保留口头需求，直接让 agent 编码
  取舍：启动快，但上下文容易漂移，回溯和协作成本更高。
- 方案二：先维护 `PRD.md`、`ARCH.md`、`project_state.md`，再推进切片开发
  取舍：前置成本更高，但边界更清晰，更适合多人协作和持续迭代。

如果你的项目仍处于强探索阶段，可以先轻量填写模板；如果已经进入多人协作或需要稳定交付，建议完整使用整套模板。

## License

See `LICENSE`.

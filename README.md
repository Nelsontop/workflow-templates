# workflow-templates

面向 AI 辅助开发的工作流模板仓库。

这个仓库的目标不是提供一套“提示词合集”，而是提供一套可落地的文档骨架：先把需求、架构、计划、当前状态和验证记录写进仓库，再让 agent 在明确边界内工作，减少上下文漂移、误改和不可审计的实现。

当前主模板是 `vibe-coding-standard/`。它采用 docs-first、agent-first 的组织方式，适合新项目初始化，也适合给已有项目补一层稳定的执行协议。

## 解决什么问题

很多 AI 编码协作的问题，不是模型不会写代码，而是项目没有稳定的“地图”：

- 需求只存在聊天记录里，过几轮就漂移
- 架构边界没人写清楚，agent 容易跨层改动
- 当前切片和允许改动范围不明确，修改会失控
- 做完没有验证闭环，后续很难回溯

这个仓库提供的模板，核心就是把这些信息收敛成版本化文档。

## 适用场景

- 你想让 agent 先读文档，再改代码
- 你想把长期上下文沉淀到仓库，而不是依赖会话记忆
- 你想把任务切成可验收切片，降低一次性大改风险
- 你想让需求、架构、计划、验证结果保持同步演进
- 你在做多人协作，希望后续接手的人也能快速建立上下文

## 3 分钟上手

1. 复制 `vibe-coding-standard/` 到你的项目根目录。
2. 把模板里的 `AGENTS.md`、`CLAUDE.md`、`ARCHITECTURE.md`、`project_state.md` 和 `docs/` 带过去。
3. 先补最少必要内容：
   - `project_state.md`：当前目标、当前切片、允许修改范围、最近验证
   - `docs/product-specs/prd.md`：做什么、不做什么、验收口径
   - `docs/exec-plans/active/`：当前任务计划
4. 开始新的 agent 会话时，要求它按顺序读取：
   - `AGENTS.md`
   - `project_state.md`
   - `docs/index.md`
5. 每完成一个可验收切片：
   - 更新计划和状态文档
   - 记录验证结果
   - 单独提交 commit

## 模板结构

`vibe-coding-standard/` 当前采用“根目录薄入口 + docs 长期知识树”的结构：

```text
vibe-coding-standard/
├── AGENTS.md
├── ARCHITECTURE.md
├── CLAUDE.md
├── project_state.md
└── docs/
    ├── index.md
    ├── DESIGN.md
    ├── FRONTEND.md
    ├── PLANS.md
    ├── PRODUCT_SENSE.md
    ├── QUALITY_SCORE.md
    ├── RELIABILITY.md
    ├── SECURITY.md
    ├── design-docs/
    ├── exec-plans/
    ├── generated/
    ├── product-specs/
    └── references/
```

## 每个入口文件负责什么

### 根目录

- `AGENTS.md`
  agent 的主入口。定义启动顺序、文档路由、执行协议和默认边界。
- `CLAUDE.md`
  面向 Claude 系工具的兼容入口，通常与 `AGENTS.md` 保持一致。
- `ARCHITECTURE.md`
  高层架构地图。只讲系统边界和知识树，不承载所有细节。
- `project_state.md`
  当前激活切片、阻塞项、允许改动范围、最近验证记录。

### docs/

- `docs/index.md`
  长期知识入口，告诉 agent 不同任务应该先看哪里。
- `docs/product-specs/`
  产品规格、PRD、范围边界、验收标准。
- `docs/design-docs/`
  设计原则、ADR、架构权衡、长期设计决策。
- `docs/exec-plans/`
  当前执行计划、已完成计划和技术债跟踪。
- `docs/DESIGN.md` 与 `docs/FRONTEND.md`
  前端实现、视觉和交互规则。
- `docs/PRODUCT_SENSE.md`
  需求裁剪、优先级和产品判断标准。
- `docs/QUALITY_SCORE.md` 与 `docs/RELIABILITY.md`
  验证、回归、稳定性和反熵约束。
- `docs/SECURITY.md`
  安全边界、敏感数据和高风险流程要求。
- `docs/references/`
  外部参考资料、示例和 agent 友好内容。

## 推荐工作流

建议把这个模板当成一个执行协议，而不是只拷贝几份文档：

1. 先写清当前切片，不直接让 agent 在整个仓库里自由发挥。
2. 中等及以上复杂度任务，先写 `docs/exec-plans/active/` 计划。
3. 只允许 agent 修改本次切片明确授权的文件或目录。
4. 功能、架构、状态变化发生后，文档和代码一起更新。
5. 完成后记录手动验收、lint、类型检查、测试等验证结果。

## 和传统 README 模板的区别

常见 README 更像项目说明书；这个模板更接近“协作操作系统”：

- 它强调文档路由，而不是把所有规则堆在一个文件里
- 它强调计划和状态，而不是只写静态背景介绍
- 它默认 agent 会参与开发，因此要求上下文必须版本化
- 它把“范围边界”和“验证闭环”当成一等公民

## 什么时候不适合

如果你的项目还在纯探索阶段，而且没有稳定需求、架构和交付节奏，这套模板可能偏重。此时可以只先保留：

- `AGENTS.md`
- `project_state.md`
- 一个最小的 `docs/product-specs/prd.md`
- 一个最小的 `docs/exec-plans/active/` 计划文件

等范围稳定后，再逐步补齐完整知识树。

## 使用建议

- 不要把长期约束只写在聊天里，最终都要回写到仓库。
- 不要让 `project_state.md` 变成流水账，它只记录当前最重要的状态。
- 不要把 `ARCHITECTURE.md` 写成百科全书，它应该始终保持“地图”角色。
- 如果某条规则经常被违反，优先考虑把它机械化成脚本、模板或检查项。

## License

See `LICENSE`.

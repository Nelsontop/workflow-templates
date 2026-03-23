# Examples

本目录提供可直接参考的项目文档样例，帮助你理解这套模板不是“空表格集合”，而是一套能串起需求、架构、状态、验证和回滚的工作流。

## 你可以在这里得到什么

- 一套完整填写后的 `PRD.md`
- 一套与之配对的 `ARCH.md`
- 一份反映当前切片和推进节奏的 `project_state.md`

这些示例的目标不是提供“标准答案”，而是演示文档之间如何互相约束。

## 当前包含的示例

### `minimal-saas`

一个轻量 SaaS 场景示例，主题是“团队内部反馈看板”。

适合你参考它的情况：

- 你要做一个典型的 Web 产品
- 你希望先以前端切片确认交互，再进入后端
- 你需要看清“用户流程 -> 核心工作流 -> 验证 -> 回滚”怎么落到文档

包含文件：

- `reference/examples/minimal-saas/PRD.md`
- `reference/examples/minimal-saas/ARCH.md`
- `reference/examples/minimal-saas/project_state.md`

### `minimal-mvp`

一个更轻的个人验证场景示例，主题是“把一个想法快速整理成可分享页面”。

适合你参考它的情况：

- 你是单人开发，想先验证一个想法是否值得继续
- 你不想一开始就做登录、后台、复杂权限和数据库
- 你需要的是“足够表达价值”的最小闭环，而不是可长期演进的平台

包含文件：

- `reference/examples/minimal-mvp/PRD.md`
- `reference/examples/minimal-mvp/ARCH.md`
- `reference/examples/minimal-mvp/project_state.md`

## 推荐阅读顺序

1. 先读示例 `PRD.md`
   先看目标、非目标、核心用户流程和验收口径。
2. 再读示例 `ARCH.md`
   看这些用户流程如何被翻译成核心工作流、handoff 契约、验证矩阵和回滚方式。
3. 最后读示例 `project_state.md`
   看一个真实切片如何记录“当前做什么、已完成什么、下一步做什么”。

如果你只想快速验证个人想法，优先看 `minimal-mvp`。
如果你要做一个更完整的 Web 产品，再看 `minimal-saas`。

## 如何把示例用到你自己的项目

1. 不要直接复制整份文档后只改产品名。
2. 先替换示例中的场景、目标用户和核心流程。
3. 再根据你的业务，把 `ARCH.md` 中的关键决策、工作流、验证和回滚改成真实内容。
4. 最后用 `project_state.md` 记录当前切片，而不是回顾历史。

## 复用检查清单

- 你的 `PRD.md` 是否已经写清目标、非目标、用户流程和验收？
- 你的 `ARCH.md` 是否已经写清关键技术决策、核心工作流、handoff 契约和验证方式？
- 你的 `project_state.md` 是否只记录当前切片、已知问题和下一步？
- 你的文档之间是否能连成一条链：问题 -> 目标 -> 用户流程 -> 核心工作流 -> 验证 -> 回滚？

## 后续扩展示例时的建议

- 新增示例时，优先选择和现有示例差异明显的场景
- 每个示例都应保持 `PRD.md`、`ARCH.md`、`project_state.md` 三件套
- 如果新增的是移动端、原生端或强后端场景，应突出为什么它和 `minimal-saas` 的边界不同
- 如果新增的是个人验证类项目，应像 `minimal-mvp` 一样主动删掉不影响验证速度的复杂能力

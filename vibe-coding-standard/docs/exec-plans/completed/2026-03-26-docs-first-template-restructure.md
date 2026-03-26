# Docs-First Template Restructure

状态：`done`

## 目标

把模板从“根目录堆大文档”重构为“薄入口 + docs 知识树 + 显式计划流转”的 agent-first 结构。

## 本次明确不做

- 不补新的应用代码样例
- 不引入 CI 或自动化 lint
- 不实现文档完整性检查脚本

## 允许修改范围

- `AGENTS.md`
- `CLAUDE.md`
- `ARCHITECTURE.md`
- `project_state.md`
- `docs/**`
- 原 `reference/**` 内容迁移到 `docs/references/**`

## 依赖文档

- `AGENTS.md`
- `ARCHITECTURE.md`
- `docs/PLANS.md`
- `docs/design-docs/core-beliefs.md`
- OpenAI《Harness 工程》文章

## 实施步骤

1. 建立 article 风格的 `docs/` 目录骨架
2. 将原 PRD 模板迁移到 `docs/product-specs/prd.md`
3. 将原架构规则拆成根目录架构地图与 `docs/` 中的长期知识文档
4. 将根目录 `AGENTS.md` 收缩为导航与执行协议
5. 将 `reference/examples` 与 `reference/agency` 迁移到 `docs/references/`
6. 更新 `project_state.md`，让当前状态与计划流转模型一致

## 验收标准

- 根目录不再保留厚重的 `PRD.md` 与 `ARCH.md`
- `AGENTS.md` 只保留入口协议与文档路由
- `docs/` 具备设计文档、执行计划、产品规格、参考资料四类知识入口
- 当前状态文档能指向计划文件

## 验证记录

- 手动检查：完成
- lint：未运行，当前仓库无统一 lint 入口
- typecheck：未运行，本次重构以 Markdown 模板为主
- test：未运行，本次重构以文档和目录迁移为主

## 遗留问题

- 文档链接完整性尚未机械化检查
- 旧 `reference/` 路径相关的自动化或测试如存在，后续需要统一迁移

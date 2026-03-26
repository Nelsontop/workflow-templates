# Project State

## 当前阶段

- 当前目标：将工作流模板重构为 docs-first、agent-first 的知识与计划结构
- 当前切片：完成根目录瘦身、`docs/` 知识树落地和计划流转重构
- 当前计划：`docs/exec-plans/completed/2026-03-26-docs-first-template-restructure.md`
- 允许修改的文件：`AGENTS.md`、`CLAUDE.md`、`ARCHITECTURE.md`、`project_state.md`、`docs/**`
- 当前端别：模板基础设施
- 是否已完成前端确认：不适用

## 已完成

- 新增根目录 `ARCHITECTURE.md` 作为高层架构地图
- 将原根目录 `PRD.md` 迁移为 `docs/product-specs/prd.md`
- 将原根目录 `ARCH.md` 的长期约束拆分进 `ARCHITECTURE.md` 与 `docs/**`
- 将 `AGENTS.md` 重写为薄入口、文档路由与执行协议
- 将 `CLAUDE.md` 收缩为兼容入口
- 新增 `docs/index.md`、`docs/PLANS.md`、`docs/PRODUCT_SENSE.md`、`docs/QUALITY_SCORE.md`、`docs/RELIABILITY.md`、`docs/SECURITY.md`
- 新增 `docs/DESIGN.md`、`docs/FRONTEND.md`
- 新增 `docs/design-docs/index.md` 与 `docs/design-docs/core-beliefs.md`
- 新增 `docs/exec-plans/tech-debt-tracker.md`
- 记录本次重构计划到 `docs/exec-plans/completed/2026-03-26-docs-first-template-restructure.md`
- 将 `reference/examples` 与 `reference/agency` 迁移到 `docs/references/`
- 清空 `docs/references/examples/` 下的全部示例文件，并转移到 trash
- 将旧根文档 `PRD.md`、`ARCH.md` 移到 `/vol3/1000/workspace/trash/vibe-coding-standard-2026-03-26/`

## 已知问题

- 问题描述：仓库内若存在依赖旧 `reference/` 路径的脚本、测试或外部引用，当前未做全量修复
- 影响范围：`tests/reference/**` 及潜在外部文档链接
- 是否阻塞当前切片：否

- 问题描述：文档导航、链接完整性和知识新鲜度仍未做自动检查
- 影响范围：`AGENTS.md`、`ARCHITECTURE.md`、`docs/**`
- 是否阻塞当前切片：否

- 问题描述：`docs/index.md` 仍将 `references/` 描述为包含示例，但 `docs/references/examples/` 已清空
- 影响范围：`docs/index.md`、后续模板说明
- 是否阻塞当前切片：否

## 下一步

- 下一切片：补文档完整性检查与旧路径迁移清单
- 下一步验收目标：确保 `docs/` 新路径可被自动化检查，且没有遗留旧入口漂移
- 是否进入后端开发：否

## 最近一次验证

- 手动验证：已检查根目录入口、`docs/` 目录树、计划文件、`docs/references/agency/README.md` 路径示例，以及 `docs/references/examples/` 已无文件残留
- lint：未运行，当前仓库无统一 lint 入口
- typecheck：未运行，本次切片主要为文档模板重构
- test：未运行，本次切片主要为文档与目录迁移
- regression：已抽查 `docs/index.md`、`docs/product-specs/prd.md`、`docs/design-docs/core-beliefs.md`、`docs/exec-plans/completed/2026-03-26-docs-first-template-restructure.md`
- preflight：不适用
- commit：未提交
- 前端确认记录：不适用

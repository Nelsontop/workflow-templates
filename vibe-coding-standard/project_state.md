# Project State Template

## 当前阶段

- 当前目标：统一四份根文档中“问题、目标、非目标、工作流、验收、回滚”的术语口径
- 当前切片：补齐 `PRD.md` 与 `AGENTS.md` 之间对新版 PRD 职责的描述同步
- 允许修改的文件：`PRD.md`、`AGENTS.md`、`project_state.md`
- 当前端别：前端
- 是否已完成前端确认：不适用

## 已完成

- 同步更新 `AGENTS.md`，让主规则明确新版 PRD 要包含问题证据、成功指标、非目标、开放问题和发布回滚口径
- 补充 `PRD.md` 的流程映射、切片验收与发布回滚字段，使其与新版 `ARCH.md` 的工作流和验证矩阵对齐
- 同步更新 `AGENTS.md` 与 `CLAUDE.md`，补充 `ARCH.md` 的 ADR、工作流、handoff 契约、失败恢复与结构化验证要求
- 重构 `ARCH.md`，补充架构选型取舍、ADR、运行时拓扑、核心工作流、失败恢复、handoff 契约与验证矩阵
- 强化 `ARCH.md` 与 PRD 的对齐要求，增加目标映射、非目标边界和风险跟踪
- 重构 `PRD.md`，补充问题证据、成功指标、非目标、开放问题、发布与回滚等产品章节
- 保留前后端范围拆分、默认目录骨架和前端优先开发顺序
- 删除 `reference/theme.ts`
- 同步更新 `AGENTS.md` 目录结构，移除 `theme.ts` 引用
- 新增 `reference/agency/upstream/`，保存筛选后的 agency Markdown 快照
- 新增 `reference/agency/build_index.py`，支持索引生成与关键词查询
- 新增 `reference/agency/index.json` 与 `reference/agency/README.md`
- 补充模板规则：agency 索引为第二优先级，仅在未明确命中本地技能时加载

## 已知问题

- 问题描述：上游快照不会自动同步，需要手动重新抓取并重建索引
- 影响范围：`reference/agency`
- 是否阻塞当前切片：否

## 下一步

- 下一切片：如有需要，再补一份示例项目级填写样例，演示 PRD 与 ARCH 如何配对落地
- 下一步验收目标：确认模板使用者能从四份文档直接看出“问题 -> 目标 -> 用户流程 -> 核心工作流 -> 验证 -> 回滚”的闭环
- 是否进入后端开发：否

## 最近一次验证

- 手动验证：已检查 `PRD.md` 的问题、目标、非目标、流程、验收和回滚字段与 `AGENTS.md`、`ARCH.md` 的职责说明相互呼应
- lint：未运行，当前仓库无统一 lint 入口
- typecheck：未运行，当前切片主要为文档和 Python 脚本
- test：未运行，本次切片为文档模板更新
- regression：已用生成后的 `index.json` 抽查字段结构
- preflight：不适用
- commit：未提交
- 前端确认记录：不适用

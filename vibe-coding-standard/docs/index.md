# Docs Index

`docs/` 是本模板的长期知识入口。

## 先看哪里

- 要判断做什么、不做什么、怎么验收：看 `product-specs/`
- 要理解系统边界、模块关系、trade-off：看 `../ARCHITECTURE.md` 和 `design-docs/`
- 要执行当前切片：看 `PLANS.md` 和 `exec-plans/active/`
- 要做前端页面、交互、视觉：看 `FRONTEND.md` 和 `DESIGN.md`
- 要做需求取舍或版本裁剪：看 `PRODUCT_SENSE.md`
- 要做验证、回归、反熵或技术债处理：看 `QUALITY_SCORE.md`、`RELIABILITY.md`
- 要处理认证、数据边界、密钥和敏感流程：看 `SECURITY.md`
- 要找示例或外部补充材料：看 `references/`

## 设计原则

- 目录优先于长说明
- 长期知识必须版本化
- 计划是执行入口，不是聊天记录
- 规则能机械化就尽量机械化
- 任何 agent 看不到的知识，都不应成为系统依赖

## 子目录

- `design-docs/`：设计文档、架构信念、ADR、历史权衡
- `exec-plans/`：当前与已完成的执行计划，以及技术债跟踪
- `generated/`：可再生文档，例如 schema 快照
- `product-specs/`：PRD、功能规格、验收约束
- `references/`：参考资料、示例、agent 友好文本

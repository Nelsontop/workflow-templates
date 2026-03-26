# Architecture Map

本文件只负责提供高层地图，不承载全部长期细节。

## 根目录角色

- `AGENTS.md`
  agent 入口协议与文档路由
- `CLAUDE.md`
  Claude 系工具兼容入口
- `project_state.md`
  当前激活切片、阻塞与最近验证
- `docs/`
  长期知识、计划、产品规格、参考资料

## 标准知识树

```text
docs/
├── index.md
├── design-docs/
│   ├── index.md
│   ├── core-beliefs.md
│   └── ...
├── exec-plans/
│   ├── active/
│   ├── completed/
│   └── tech-debt-tracker.md
├── generated/
│   └── db-schema.md
├── product-specs/
│   ├── index.md
│   ├── prd.md
│   └── ...
├── references/
│   ├── agency/
│   ├── examples/
│   ├── design-system-reference-llms.txt
│   ├── repo-rules-llms.txt
│   └── ...
├── DESIGN.md
├── FRONTEND.md
├── PLANS.md
├── PRODUCT_SENSE.md
├── QUALITY_SCORE.md
├── RELIABILITY.md
└── SECURITY.md
```

## 路由规则

- 需求与验收：看 `docs/product-specs/`
- 设计原则与架构 trade-off：看 `docs/design-docs/`
- 当前切片怎么做：看 `docs/exec-plans/`
- 前端实现方式：看 `docs/FRONTEND.md`
- 视觉与交互原则：看 `docs/DESIGN.md`
- 产品取舍与需求判断：看 `docs/PRODUCT_SENSE.md`
- 质量、验证、反熵：看 `docs/QUALITY_SCORE.md`、`docs/RELIABILITY.md`
- 安全边界：看 `docs/SECURITY.md`
- 外部参考与示例：看 `docs/references/`

## 默认项目边界

- 多应用项目默认采用 `apps/web` 与 `apps/server`
- 默认启动方式是 Docker
- 默认数据库是 SQLite
- 前端先行，边界确认后再进入后端

这些默认值若被覆盖，必须在 `docs/product-specs/` 和相关设计文档中写清原因、代价与回退条件。

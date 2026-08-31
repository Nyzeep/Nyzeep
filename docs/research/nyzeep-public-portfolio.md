# Nyzeep 公开作品组合：来源证据

本文记录主页精选项目与技术标签的可审计依据。数据来自 GitHub REST API 的公开仓库元数据、语言端点、根目录清单与仓库 README；不把 fork 仓库作为 Nyzeep 的原创能力证据。

## 证据采集范围

- Halo-Studio：仓库元数据、语言分布、根目录、README。
- dsh-material-file-icons：仓库元数据、许可证、语言分布、根目录、README。
- Ecoscout 与 LumiMate：仓库元数据和语言分布，用于主页中的轻量探索链接。

## 精选项目

### Halo-Studio

- 公开仓库：[Nyzeep/Halo-Studio](https://github.com/Nyzeep/Halo-Studio)
- API：<https://api.github.com/repos/Nyzeep/Halo-Studio>、<https://api.github.com/repos/Nyzeep/Halo-Studio/languages>
- 仓库描述：集成主流ai agent的开发工作平台
- 主页使用的表述“集成主流 AI Agent 的开发工作平台”直接来自该公开描述。
- 语言端点（字节）：

~~~json
{"Rust":25123836,"TypeScript":13964360,"JavaScript":3692927,"SCSS":2154565,"CSS":706514,"Python":431148,"HTML":198975,"Shell":160342,"PowerShell":37605,"Fluent":14011,"Dockerfile":9938}
~~~

- 根目录清单：

~~~text
.env.example
.gitattributes
.gitignore
CONTEXT.md
README.md
THIRD_PARTY_NOTICES.md
agents.md
docs
package-lock.json
package.json
product
scripts
~~~

- README 开头摘录（用于核对项目定位；摘录不替代完整 README）：

~~~markdown
# Halo Studio

Halo Studio 是面向本地开发者的原生开发工作台：在受信任 Git 工作区中，由 Halo Workbench Runtime 通过本机 Pi Agent（`pi --mode rpc`）执行受管编码任务，并围绕任务基线、文件写入租约、交付证据与人工审查组织可验证的编码交付。

## 当前状态

- **唯一正式产品入口**：`product/Halo Studio`（Tauri 桌面应用，bin `halo-studio`）。
- **P0 执行链**：`Halo Workbench Runtime → 受控 Pi 子进程 → pi --mode rpc → stdin/stdout JSONL`。
- **发布状态**：工单 14/15 的真实 Pi RPC 原生 UI 验收记录为 `not-run`，P0 未放行；完整验收与验证事实以 `docs/verification/` 为准。
- **上游对照**：上游（原 BitFun）源码与历史证据仅作历史/上游对照，统一标注“历史记录/上游对照（已归档）”；`BitFun-latest/` 为豁免目录，不参与构建。
- **运行时职责**：Pi 是当前唯一的 P0 生产执行 harness；DeepSeek Harness（DSH）只作为迁移参考，不进入 Halo Studio 的生产执行链。
- **受管事实**：生产 assembly 已接入独立的 Halo managed-event-facts 持久化端口与 JSON provider；任务恢复、完整生命周期事实覆盖和交付证据投影仍在后续工单中完善，不能视为已完成发布能力。

## 技术栈

[![Rust](https://img.shields.io/badge/Rust-1.95-orange?style=flat-square)](https://www.rust-lang.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8-blue?style=flat-square)](https://www.typescriptlang.org/)
[![React](https://img.shields.io/badge/React-18-61dafb?style=flat-square)](https://react.dev/)
[![Tauri](https://img.shields.io/badge/Tauri-2-6b46c1?style=flat-square)](https://tauri.app/)
[![pnpm](https://img.shields.io/badge/pnpm-10-f69220?style=flat-square)](https://pnpm.io/)
[![Vitest](https://img.shields.io/badge/Vitest-4-729b1b?style=flat-square)](https://vitest.dev/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-yes-2088ff?style=flat-square)](https://github.com/features/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](product/Halo%20Studio/LICENSE)

## 快速开始

```powershell
cd "product/Halo Studio"
pnpm install
pnpm run check:repo-hygiene
pnpm run product:check
pnpm run desktop:dev
```

完整构建/测试/打包命令与常见问题见 [docs/development/build-and-test.md](docs/development/build-and-test.md)。

## 目录说明

| 路径 | 角色 |
| --- | --- |
| `product/Halo Studio/` | 唯一正式产品源码树（Rust workspace + React 前端 + Tauri 桌面入口） |
| `docs/` | 权威文档：ADR、需求、验证、归档与开发文档 |
| `docs/development/` | 中文开发文档（架构、构建/测试、Pi RPC 适配、贡献指南） |
| `scripts/` | 根级归档脚本与仓库守卫 |
| `.agents/skills/` | 仓库开发工作流技能（to-spec、to-tickets、implement、tdd、code-review 等） |
| `BitFun-latest/` | 豁免目录：不读取、不更名、不参与构建 |

## 文档入口

- [文档地图](docs/README.md)
- [领域词汇](CONTEXT.md)
- [产品架构](docs/development/architecture.md)
- [Pi RPC 适配](docs/development/pi-rpc-adapter.md)
- [贡献指南](docs/development/contribute.md)
- [可迁移能力基线（历史）](docs/verification/mig
~~~

### dsh-material-file-icons

- 公开仓库：[Nyzeep/dsh-material-file-icons](https://github.com/Nyzeep/dsh-material-file-icons)
- API：<https://api.github.com/repos/Nyzeep/dsh-material-file-icons>、<https://api.github.com/repos/Nyzeep/dsh-material-file-icons/languages>
- 仓库描述：Material Icon Theme-inspired file and folder icons for dsh-better-sidebar in DeepSeek Harness.
- 许可证端点返回：MIT
- 主页使用的“DeepSeek Harness 文件与目录图标扩展”来自该公开描述；MIT 徽章由许可证端点支撑。
- 语言端点（字节）：

~~~json
{"TypeScript":1354962,"JavaScript":7809}
~~~

- 根目录清单：

~~~text
.gitignore
.npmrc
AGENTS.md
CONTEXT.md
LICENSE
LICENSES
README.md
README.zh-CN.md
RELEASE-CHECKLIST.md
THIRD_PARTY_NOTICES.md
cordis.patch.yml
docs
dsh.plugin.json
package.json
pnpm-lock.yaml
scripts
src
tests
tsconfig.build.json
tsconfig.json
tsdown.config.ts
vendor
vitest.config.ts
~~~

- README 开头摘录：

~~~markdown
# dsh-material-file-icons

Material Icon Theme-inspired file and folder icons for the **Files** tree in
[<code>dsh-better-sidebar</code>](https://github.com/omdsh-dev/DSH-better-sidebar)
on [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/DeepSeek-Harness).

[中文说明](README.zh-CN.md)

> **Release status — source available; npm distribution pending.** The source
> repository is public at
> [Nyzeep/dsh-material-file-icons](https://github.com/Nyzeep/dsh-material-file-icons),
> but this project has not performed an npm publication. A public
> <code>dsh-better-sidebar</code> release must first advertise the
> <code>fileIconProvider</code> capability before a normal npm installation can
> show these icons.

![Redacted local DSH Files-panel acceptance screenshot showing Material file icons](docs/assets/material-file-icons.png)

> Real local DSH Web acceptance capture. The icon nodes and Files-panel layout
> are rendered by this package; all original workspace, file, account, and
> conversation text was removed and replaced only with generic demonstration
> labels in an isolated browser context before the image was saved.

## What this plugin does

<code>dsh-material-file-icons</code> is a client-only DSH community bundle. When
the sidebar exposes the public <code>fileIconProvider</code> capability, it
registers one HMR-safe provider and replaces only the three file-tree glyph
locations:

- the workspace root directory;
- open and closed directories;
- files.

It recognizes Material Icon Theme mappings for exact file names, ordinary and
multi-part extensions, folders, roots, and path-sensitive entries. Examples
include <code>package.json</code>, <code>README.md</code>, <code>d.ts</code>,
<code>tsx</code>, <code>yaml</code>, <code>.github/workflows</code>, and
<code>.config/graphqlrc</code>.

The generated runtime is deterministic and data-driven. It contains Material
Icon Theme 5.38.1-derived data for 1,128 referenced SVGs, 2,135 file-name
mappings, 1,377 extension mappings, and 4,654 folder mappings.

## Release status and compatibility

| Environment | Expected result |
| --- | --- |
| A DSH Web runtime compatible with this package's declared client peers | The bundle can load. |
| Public <code>dsh-better-sidebar@0.16.1</code> | Safe no-op: it does **not** advertise <code>fileIconProvider</code>, so its native file-tree icons remain unchanged. |
| A future re
~~~

## 探索性作品

### Ecoscout

- 公开仓库：[Nyzeep/Ecoscout](https://github.com/Nyzeep/Ecoscout)
- API：<https://api.github.com/repos/Nyzeep/Ecoscout>、<https://api.github.com/repos/Nyzeep/Ecoscout/languages>
- 仓库描述：一个可用于社区环卫检测的项目
- 语言端点（字节）：

~~~json
{"HTML":199026,"Python":152258,"Batchfile":3089}
~~~

主页只称其为“社区环卫检测”，不从语言数据推断具体模型、算法或产品能力。

### LumiMate

- 公开仓库：[Nyzeep/LumiMate](https://github.com/Nyzeep/LumiMate)
- API：<https://api.github.com/repos/Nyzeep/LumiMate>、<https://api.github.com/repos/Nyzeep/LumiMate/languages>
- 仓库描述：一个近在眼前的伙伴
- 语言端点（字节）：

~~~json
{"Python":296107,"Vue":85839,"JavaScript":64306,"CSS":55352,"Rust":5636,"HTML":344}
~~~

主页保留其公开描述所表达的“伙伴式软件实验”定位，不额外推断产品架构。

## 技术标签映射

| 主页技术或方向 | 可审计来源 |
| --- | --- |
| Rust、TypeScript | Halo-Studio 语言端点；TypeScript 也由 dsh-material-file-icons 语言端点支撑。 |
| Python、Vue、JavaScript、CSS | LumiMate 语言端点；Python 也由 Halo-Studio 与 Ecoscout 语言端点支撑。 |
| HTML | Ecoscout 语言端点。 |
| AI Agent 工作平台 | Halo-Studio 的公开仓库描述与 README。 |
| DeepSeek Harness 扩展 / 开发者体验 | dsh-material-file-icons 的公开描述与 README。 |
| 社区环卫检测 | Ecoscout 的公开仓库描述。 |

## 主页构建路线文案映射

| README 路线 | 可审计来源 | 采用边界 |
| --- | --- | --- |
| “受管编码任务、任务基线与交付证据” | Halo-Studio README 开头摘录：本地开发工作台、受管编码任务、任务基线与交付证据。 | 不把尚未发布的能力写成已完成的产品承诺。 |
| “Files 树的 Material 风格文件与目录图标” | dsh-material-file-icons 的公开描述与 README 摘录。 | 表述为扩展定位，不承诺特定版本一定已自动安装。 |
| “社区环卫检测”与“伙伴式软件实验”的轻量探索线 | Ecoscout 与 LumiMate 的公开仓库描述。 | 不从语言或描述推断模型、算法或未公开产品细节。 |

## 主页维护边界

- 只有这里有来源的项目描述和技术标签才能留在主页核心区。
- GitHub Top Languages 卡是公开代码语言分布，不是技能或熟练度声明。
- 若某个项目描述、许可证或技术栈发生变化，应同步更新主页卡片和本证据档。

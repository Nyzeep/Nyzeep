# Nyzeep 主页重设计：实现决策

本文件记录当前主页的实现约束，并保留旧方案的历史背景。项目事实与采集边界见 [nyzeep-public-portfolio.md](nyzeep-public-portfolio.md)，早期研究见 [github-profile-readme-design.md](github-profile-readme-design.md)。

## 当前决策：2026-10-13 ZIP 工业风格

2026-10-13，用户授权按提供的 ZIP 视觉参考重做主页并删除贪吃蛇。该需求替代此前“保留贡献蛇、维护蛇生成工作流”和终端动效主视觉的决定；下方旧方案只作历史记录，不再约束当前实现。

| 项目 | 当前实现约束 | 决策理由 |
| --- | --- | --- |
| 视觉来源 | 用户提供的 `stitch_orchestella_mobile_ui_concepts.zip`；采用硬边框、非对称工业仪表盘布局 | 沿用 ZIP 的工业视觉语言，适配 GitHub Profile 的阅读路径。 |
| 色板 | 炭黑 `#121316`、信号红 `#D62828`、钴蓝 `#0047AB`、黄 `#FDBB24` | 用统一色板区分主视觉、项目与技术区域。 |
| 主视觉 | 仓库内的宽屏、窄屏两版静态 SVG，由 README 的 `<picture>` 按视口宽度选择，`<img>` 提供回退与替代文本 | 保留工业仪表盘构图，同时让窄屏文字可读；不依赖动画、外部 JS 或 CSS。 |
| 技术呈现 | 使用真实技术栈 logo：TypeScript、Python、Rust、Vue、JavaScript、Tauri、Android、Kotlin、Linux、FastAPI、Git、GitHub | 采用本轮公开资料核实的技术清单，不继承未核实的 Docker、Tailwind 标签；不把图标解释为熟练度评级。 |
| 徽章与统计卡 | 保留 5 个 Shields 徽章：仓库入口、关注、交流与两个最新提交时间；移除第三方大统计卡 | 徽章提供具体入口或仓库状态；必要信息仍由正文承载。 |
| 公开精选 | Orchestella-Studio、LumiMate、dsh-material-file-icons、Ecoscout | 按 2026-10-13 核实结果提供可公开访问的作品入口；Halo-Studio 已为私有仓库，不再作为当前公开精选或能力证据。 |
| 贡献蛇 | 从主页移除，并删除独立配置 `.github/workflows/generate-snake.yml` | 用户的新需求明确替代旧保留决定；远程 `output` 分支及历史产物不在本次清理范围。 |
| 正文与无障碍 | README 正文保留可访问的身份介绍、项目说明与项目链接 | 必要信息不只放进 SVG；图片不可用时仍能理解主页并访问作品。 |

## 当前信息架构与维护

1. 首屏：本地静态 SVG 工业仪表盘，配合正文中的简短身份与方向介绍。
2. 作品：四个公开精选项目，分别提供真实链接和有证据支持的简短描述。
3. 技术：十二个真实技术 logo，配合适量徽章；文字与图标均不宣称未经证实的能力或发布状态。
4. 导航：正文保留 GitHub 与项目入口，不依赖 SVG 内部交互。
5. 检查：验证宽屏与窄屏 `<picture>` 选择、`<img>` 回退、替代文本及正文链接；静态主视觉不需要动效回退。

项目、许可证和技术标签应以公开来源为准；本轮事实核实结论及旧证据边界记录在 [nyzeep-public-portfolio.md](nyzeep-public-portfolio.md)。当精选项目、可见性、描述或技术栈变化时，应同步更新 README、证据档与本决策记录。历史终端和蛇方案不应被当作恢复旧资产或自动化的要求。

## 历史基线：参考效果到旧实现

以下内容记录 2026-10-13 新需求之前的方案，保留它们是为了说明决策如何变化。

| 旧参考实现 | 当时的 Nyzeep 实现 | 当时的决策理由 |
| --- | --- | --- |
| 首屏打字机与 GIF 建立氛围 | 本地 `assets/nyzeep-terminal.svg` 开发工作台动效 | 用单一主题化动效建立氛围，核心资料另以 README 正文提供。 |
| 亮暗主题的贡献蛇 picture | README 末尾使用亮暗两张蛇 SVG 与 picture 回退 | 当时选择保留参考中的趣味效果，并沿用 `output` 分支发布模式；此决定已被替代。 |
| 3D 贡献图、日历、活动图、Metrics 图集 | 未加入 | 它们与蛇重复表达贡献事实，也会增加图片请求与维护负担。 |
| 多份整点运行的参考工作流 | 蛇任务采用 03:17 UTC 与 `contribution-snake-output` 并发组 | 当时用于避开整点高负载与并发写入；该独立工作流现已删除。 |
| 浮动第三方 Action 版本 | 用当时审查解析的完整 SHA 固定 | 当时保留 v3/v4 行为并减少可移动标签带来的变动。 |

旧信息架构包含两个精选项目、Ecoscout 与 LumiMate 的轻量探索链接、七个技术图标、Stats 与 Top Languages 辅助卡，以及页尾贡献蛇。旧主视觉还维护了动效版与 `prefers-reduced-motion` 静态回退版；这些数量与表现形式均为历史基线。

## 历史升级记录：极客终端与 Neofetch

下列记录描述旧终端方案的演变，不代表当前 ZIP 工业风格，也不构成本轮重新验证的在线事实。

1. **首屏升级**：将原基础 SVG 重构为原生 Linux Neofetch / Fastfetch 极客终端界面，采用 ANSI Shadow TUI 字符组装 `NYZEEP` 标题与赛博朋克渐变霓虹光效。
2. **终端遥测**：集成 Arch Linux、DeepSeek Harness 核心架构、Starship 提示符、16 色 ANSI 调色板与动态光标。
3. **统计卡调整**：当时使用统计镜像替换暂停服务的公共端点，并匹配 Tokyo Night 深色主题；此处不承诺端点当前可用。
4. **无障碍支持**：当时同步维护包含与不包含 `<animate>` 的版本，静态文件名为 `nyzeep-terminal-static.svg`。
5. **现代开发者终端与 Tokyo Night 色系升级**：
   - 由绿黑色系转向 Tokyo Night / Midnight Slate：冰川青 `#7DCFFF`、电子蓝 `#7AA2F7`、柔和紫 `#BB9AF7`、深蓝底色 `#0B0E14`。
   - 以透明度 0.22 的字符流作为背景纹理。
   - 精简正文与终端信息，聚焦平台环境、技术栈与代表作。
6. **动态彩色流光与提示符优化**：
   - 通过渐变位移动画让 `NYZEEP` 字符呈现多彩流光。
   - 精简背景颗粒流，将 Neofetch 规格表缩为两个子面板。
   - 移除假想的 `whoami` 与交互式伪命令，终端末行保留闪烁光标提示符。

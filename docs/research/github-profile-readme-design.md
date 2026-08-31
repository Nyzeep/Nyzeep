# Nyzeep GitHub Profile README：设计与性能研究

> 目标：让 `Nyzeep/Nyzeep` 成为清晰的个人作品入口，而不是功能、徽章和动态图表的陈列室。
>
> 调研范围：GitHub 官方文档、工具作者维护的第一方仓库，以及工作区内只读审阅的参考实现。本文只记录建议；不修改主页 README、已有工作流、Git 配置、Git 历史、远程或 GitHub 状态。

## 结论

Nyzeep 当前主页的基础已经比参考实现更克制：它有简短的身份区、有限色板、亮/暗主题的贡献墙贪吃蛇，以及将 SVG 静态发布到 `output` 分支的工作流。下一步不应继续叠加卡片，而应进行**替换式收敛**：

1. 用真实项目、当前方向和真实联系方式替换通用文案与泛化徽章。
2. 顶部只让一个视觉动效承担主角；蛇作为页面底部唯一大型动态视觉。
3. 将 stats、streak、Top Languages、活动图缩到一到两张不重复的卡片。
4. 保留单一蛇工作流，错开整点调度、增加并发保护，并在后续维护时将第三方 action 固定到审查过的完整 SHA。

参考 README 有 357 行、118 个含 URL 的行；它同时使用打字机、首屏 GIF、蛇、博客、WakaTime、笑话、3D 贡献图、技能墙和 Metrics 图集。五个参考工作流又都在每日 `00:00 UTC` 调度。它是组件和自动化做法的样本，不是 Nyzeep 应复制的阅读密度。

## 平台事实与设计边界

1. GitHub 只会把用户名同名的**公开仓库**根目录 README 显示为 profile README，因此 `Nyzeep/Nyzeep` 是正确的主页承载仓库。[GitHub Docs：Profile README](https://docs.github.com/en/account-and-profile/reference/profile-readme)
2. GitHub 支持用 `<picture>` 和 `prefers-color-scheme` 为图片提供亮/暗主题版本。蛇的双 SVG 方案符合这一模式。[GitHub Docs：主题图片](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/working-with-advanced-formatting#specifying-the-theme-an-image-is-shown-to)
3. GitHub 说明计划工作流在高负载时可能延迟，负载特别高时甚至可能丢弃；每小时起点属于高负载时间。公开仓库长期无活动时，计划任务也可能自动停用。[GitHub Docs：`schedule` event](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule)
4. `permissions` 控制 `GITHUB_TOKEN` 的工作流授权范围。现有蛇工作流的 job 级 `contents: write` 与发布 SVG 到 output 分支的用途相符。[GitHub Docs：`permissions`](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#permissions)
5. GitHub 的安全指南建议第三方 action 使用完整 commit SHA，且明确指出这是不可变引用；`@v3` / `@v4` 这类标签可读但可移动。[GitHub Docs：Using third-party actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-your-deployments#using-third-party-actions)
6. GitHub Actions 提供 `concurrency` 控制重叠运行。若多个触发器都可能写入同一个 `output` 分支，应用并发组避免相互争用。[GitHub Docs：Control workflow concurrency](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)

## 第一方工具研究

| 工具 | 第一方事实 | 面向 Nyzeep 的结论 |
| --- | --- | --- |
| [Platane/snk](https://github.com/Platane/snk#readme) | 官方 README 展示 `Platane/snk/svg-only@v3`、`github_user_name` 和多个 SVG 输出。 | 当前亮/暗 SVG + `output` 分支方案方向正确；保留蛇，不叠加 3D 贡献图或更多动画。 |
| [github-readme-stats](https://github.com/anuraghazra/github-readme-stats#readme) | 第一方 README 提供 Stats、Top Languages 卡和自托管路径；[Top Languages 文档](https://github.com/anuraghazra/github-readme-stats#top-languages-card) 明确它反映代码语言分布，而非技能或熟练度。 | 不把语言卡当技术实力证明；若保留，它只是一张辅助信息卡。 |
| [lowlighter/metrics](https://github.com/lowlighter/metrics#readme) | 通过 GitHub Action 生成 SVG，并以插件组合内容。 | 只有一张 SVG 能替代多张实时卡时才采用；选择 `base + 1` 个有意义插件，不与 stats、streak、activity graph 叠加。 |
| [DenverCoder1/readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg#readme) | 第一方 README 提供 URL 参数化和自部署路线。 | 适合一行克制短句。既有 Banner 和蛇时，不再增加多行循环动效。 |

## 只读审阅：参考项目与当前主页

### 借鉴而不复制

| 位置 | 已观察到的做法 | 建议 |
| --- | --- | --- |
| 用户提供的本地参考 README 开头和蛇区（不随本仓库发布） | 打字文案、主题图片和蛇动画先建立气氛。 | 保留轻动效 + 蛇的叙事，但每个区域只承担一种作用。 |
| 用户提供的本地参考 snake workflow（不随本仓库发布） | `Platane/snk/svg-only@v3`、`github.repository_owner`、亮/暗输出。 | Nyzeep 当前工作流已采用相同核心模式；无需添加第二套贡献动画。 |
| 用户提供的本地参考 metrics workflow（不随本仓库发布） | 16 个独立 Metrics 输出。 | 将它视为过量上限：Nyzeep 仅在有明确问题要回答时生成一张 SVG。 |
| 用户提供的本地参考工作流集合（不随本仓库发布） | 均使用 `0 0 * * *`；还含 `@latest` 与 `@master` 引用。 | 不复制相同整点调度和浮动依赖；遵循 GitHub 的调度与 SHA 固定建议。 |

不要复制的内容包括：重复表达贡献活动的蛇、3D 图、日历、习惯图和活动图；没有真实资料支撑的 WakaTime、Stack Overflow、博客、赞助按钮和笑话卡；以及把每个可用部件都放上去的视觉密度。

当前 [`README.md`](../../README.md) 只有 78 行、18 个含 URL 的行，比参考页更适合继续精修。当前 [`generate-snake.yml`](../../.github/workflows/generate-snake.yml) 具有每日调度、手动触发、5 分钟超时、job 级写权限和 `output` 分支发布，基础架构正确。

## 对 Nyzeep 的具体建议

| 当前区域 | 建议 | 原因 |
| --- | --- | --- |
| 波浪 Banner + 打字机 | 让一个成为主视觉；若保留 typing，就只保留一条短句、两三个轮换文本。 | 两个首屏动效会竞争注意力。 |
| 三个通用大徽章与三个理念徽章 | 最多保留 2–3 个指向真实目的地的徽章，如作品集、博客或邮箱。 | OPEN SOURCE / keep building 类措辞缺少可验证内容。 |
| 10 个技能图标 | 只留 5–7 个能被精选项目证明的核心技术。 | 工具清单会过时，也无法说明贡献。 |
| 四张统计/活动卡 | 保留 0–2 张：主 Stats 卡，或 Stats + Top Languages；去除 streak 与活动图中的多数。 | 同一事实被重复表达，且语言卡并不衡量能力。 |
| 蛇动画 | 保留在页面末尾，继续用亮/暗静态 SVG。 | 它是最有记忆点且最不重复的趣味元素。 |

### 该补的不是图表，而是真实作品入口

在 Hello, world! 后增加一个简短的 **Featured work** 区，而不是再增加仪表盘：

1. 两个精选仓库链接，每个说明项目解决的问题与技术重点。
2. 一句正在做什么，随当前项目更新。
3. 一个可选的真实联系方式或个人站入口。

这让读者在前一两屏理解 Nyzeep 的实际成果。人工精选项目比自动生成项目卡更可信，也不会新增外部服务依赖。

## 推荐的信息架构与资产预算

```text
首屏
  名字 + 一句真实定位
  1 个温和视觉锚点（Banner 或打字机）
  2–3 个真实链接

核心内容
  正在做什么（1–2 句）
  精选作品（2 个手工链接）
  核心技术（5–7 个，只列真实使用项）

证据与趣味
  0–2 张不重复的统计卡（可选）
  贡献蛇（唯一大型动态视觉）

页尾
  简短 CTA 或联系方式；不要再加图表墙
```

这是一份设计预算，不是 GitHub 硬性限制。它通过控制远程图片、重复数据表达和自动化数量，换取更短的阅读路径、更稳的页面和更低的维护成本。

## 工作流建议（本研究不实施）

1. 保留单一蛇工作流；不增加 3D 贡献图、整套 Metrics 或 WakaTime 自动更新。
2. 将 `0 0 * * *` 错开到例如 `17 3 * * *`（UTC），并保留 `workflow_dispatch`。[^schedule]
3. 为写入 `output` 分支的发布增加专属 `concurrency` group。[^concurrency]
4. 审查上游提交后，把 `Platane/snk/svg-only@v3` 和发布 action 固定到完整 SHA；定期人工升级，而不是浮动跟随标签。[^pinning]
5. 维持 `contents: write` 的最小权限边界。[^permissions]
6. 继续让 `output` 分支承载 SVG，让主分支只承载人工维护的 README 和工作流。

## 质量门槛

- 前 1–2 屏能回答：Nyzeep 是谁、正在做什么、作品在哪里。
- 每个徽章通往真实、维护中的目的地；每个技术图标都有项目佐证。
- 同一事实不由多个贡献图、streak、calendar 或 3D 图重复表达。
- 亮色与暗色各检查一次，特别是蛇的 `<picture>` 回退图与 alt 文本。
- 修改蛇工作流后手动运行一次，确认 `output` 分支含亮、暗两张 SVG。
- 新增第三方 action 前审查权限与完整 SHA；新增第三方图片服务前，先问它是否比一段正文或普通链接更有用。

## 来源

- GitHub Docs, [Profile README](https://docs.github.com/en/account-and-profile/reference/profile-readme)
- GitHub Docs, [Specifying the theme an image is shown to](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/working-with-advanced-formatting#specifying-the-theme-an-image-is-shown-to)
- GitHub Docs, [`schedule` event](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule)
- GitHub Docs, [`permissions`](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#permissions)
- GitHub Docs, [Control workflow concurrency](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)
- GitHub Docs, [Using third-party actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-your-deployments#using-third-party-actions)
- Platane, [snk — first-party README](https://github.com/Platane/snk#readme)
- lowlighter, [metrics — first-party README](https://github.com/lowlighter/metrics#readme)
- anuraghazra, [github-readme-stats — first-party README](https://github.com/anuraghazra/github-readme-stats#readme)
- DenverCoder1, [readme-typing-svg — first-party README](https://github.com/DenverCoder1/readme-typing-svg#readme)

## Scope record

- Research phase: read-only review of a user-provided local reference README and workflows (not checked into this repository), the baseline [README.md](../../README.md), and the baseline [generate-snake.yml](../../.github/workflows/generate-snake.yml).
- During the research phase, this note was the only intended file mutation. The later intentional implementation is documented in [profile-redesign-decisions.md](profile-redesign-decisions.md) and its project claims are evidenced in [nyzeep-public-portfolio.md](nyzeep-public-portfolio.md).
- The observations about the “current” README and workflow above refer to the pre-redesign baseline; they are not claims about the final implementation.

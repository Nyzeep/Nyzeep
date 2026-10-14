# Profile artwork

主页使用仓库内的静态 SVG、GitHub 支持的 HTML 与五枚 Shields 徽章。视觉方向来自用户提供的 Constructivist Mobile Workstation 设计稿：炭黑、信号红、钴蓝、黄色、直角结构和仪表盘式标签。

## 更新与预览

需要 Python 3.9+，无第三方依赖。在仓库根目录运行：

```bash
python scripts/build_profile.py
python scripts/preview_profile.py
```

打开终端输出的本地地址，默认是 <http://127.0.0.1:8765>。可加 `--port 8766` 更换端口；页面提供亮色与暗色切换，缩窄浏览器可检查移动布局。此工具使用近似 GitHub 的页面框架，最终排版仍以 GitHub 实际渲染为准。服务仅绑定本机。

- 文案与跳转链接在 `README.md`。
- 画面布局、配色和卡片文案在 `scripts/build_profile.py`；修改后重新运行生成器。
- 生成器输出到 `assets/profile/`，不要直接编辑生成文件。
- 原始品牌图标及来源、许可在 `assets/icons/`，生成时会将路径嵌入 SVG，不加载外部字体或图片。

主视觉与页脚通过 `<picture>` 在 600px 及以下切换到独立窄屏版本。项目与技术卡宽度为 400px，通过 GitHub 的 `max-width: 100%` 自然换行、缩放；避免 HTML 表格把手机页面固定成双列。图片都有替代文本，正文保留项目的普通链接。

SVG 全部静态，无脚本、`foreignObject`、滤镜或动画，减少动态效果偏好不需要单独回退。GitHub 会清洗 README 的样式与脚本，因此主页不能依赖预览页的 CSS 或 JavaScript 实现。

## 检查

```bash
python scripts/build_profile.py
python -m py_compile scripts/build_profile.py scripts/preview_profile.py
git diff --check
```

每次改版检查桌面和手机宽度、亮暗主题、图片加载、站内锚点与项目链接。技术图标描述的是公开代码中的实际使用，不表示熟练度。外部徽章可能受 Shields 缓存或服务状态影响；主视觉、项目介绍和技术栈图片不依赖它。

"""Serve the profile locally in a GitHub-like frame using only Python's stdlib."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STYLE = """
:root { color-scheme: dark; --canvas: #0d1117; --panel: #0d1117; --ink: #f0f6fc; --muted: #9198a1; --line: #3d444d; --link: #4493f8; }
:root[data-theme="light"] { color-scheme: light; --canvas: #fff; --panel: #fff; --ink: #1f2328; --muted: #59636e; --line: #d1d9e0; --link: #0969da; }
* { box-sizing: border-box; }
body { margin: 0; padding: 24px; background: var(--canvas); color: var(--ink); font: 16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif; }
.preview-bar { max-width: 898px; margin: 0 auto 16px; display: flex; gap: 14px; flex-wrap: wrap; font-size: 12px; color: var(--muted); }
.preview-bar a { color: var(--link); text-decoration: none; }
article { max-width: 898px; margin: 0 auto; padding: 32px; background: var(--panel); border: 1px solid var(--line); border-radius: 6px; overflow-wrap: break-word; }
article img { max-width: 100%; height: auto; box-sizing: content-box; vertical-align: middle; }
article h1 { font-size: 2em; margin: 24px 0 16px; font-weight: 600; padding-bottom: .3em; border-bottom: 1px solid var(--line); line-height: 1.25; }
article h2 { font-size: 1.5em; font-weight: 600; margin: 24px 0 16px; padding-bottom: .3em; border-bottom: 1px solid var(--line); line-height: 1.25; }
article p, article ul, article blockquote { margin-top: 0; margin-bottom: 16px; }
article a { color: var(--link); text-decoration: none; }
article a:hover { text-decoration: underline; }
article blockquote { color: var(--muted); padding: 0 1em; border-left: .25em solid var(--line); margin-left: 0; margin-right: 0; }
article ul { padding-left: 2em; }
article li + li { margin-top: .25em; }
article sub { font-size: 12px; }
@media (max-width: 600px) { body { padding: 12px; } article { padding: 16px; } article h1 { font-size: 1.6em; } .preview-bar { font-size: 11px; } }
"""


class PreviewHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?", 1)[0] not in ("/", "/index.html"):
            return super().do_GET()
        theme = "light" if "theme=light" in self.path else "dark"
        profile = (ROOT / "README.md").read_text(encoding="utf-8")
        document = f'''<!doctype html>
<html lang="zh-CN" data-theme="{theme}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nyzeep / Profile preview</title><style>{STYLE}</style></head>
<body><nav class="preview-bar" aria-label="Preview controls">
<span>NYZEEP / README PREVIEW</span><a href="/?theme=dark">Dark theme</a><a href="/?theme=light">Light theme</a><span>Local preview · GitHub-like layout</span>
</nav><article aria-label="GitHub profile README">{profile}</article></body></html>'''
        payload = document.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(PreviewHandler, directory=str(ROOT)))
    print(f"Profile preview: http://127.0.0.1:{args.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

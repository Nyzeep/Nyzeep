"""Build the self-contained SVG artwork used by the GitHub profile."""

from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "profile"
ICONS = ROOT / "assets" / "icons"

BG = "#121316"
PANEL = "#1B1D22"
WHITE = "#F5F4F0"
MUTED = "#ADB1BA"
LINE = "#393D46"
RED = "#D62828"
BLUE = "#0047AB"
YELLOW = "#FDBB24"
MONO = "'JetBrains Mono', 'Cascadia Code', Consolas, monospace"
SANS = "'Space Grotesk', 'Segoe UI', Arial, sans-serif"


def rect(x, y, width, height, fill, stroke=None, stroke_width=1):
    border = f' stroke="{stroke}" stroke-width="{stroke_width}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{fill}"{border}/>'


def text(x, y, value, size=14, fill=WHITE, weight=400, mono=False, **attributes):
    extra = " ".join(f'{key.replace("_", "-")}="{escape(str(value))}"' for key, value in attributes.items())
    family = MONO if mono else SANS
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{escape(value)}</text>'


def line(x1, y1, x2, y2, color=LINE, width=1):
    return f'<path d="M{x1} {y1}H{x2}" stroke="{color}" stroke-width="{width}"/>' if y1 == y2 else f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}"/>'


def cross(x, y, color=RED):
    return line(x - 5, y, x + 5, y, color) + line(x, y - 5, x, y + 5, color)


def icon(slug, x, y, size=32, color=WHITE):
    # Embed the upstream paths so image rendering needs no nested network requests.
    root = ET.parse(ICONS / f"{slug}.svg").getroot()
    paths = "".join(f'<path d="{escape(node.attrib["d"])}"/>' for node in root.iter() if node.tag.split("}")[-1] == "path")
    if not paths:
        raise ValueError(f"No brand paths in {slug}.svg")
    viewbox = root.attrib.get("viewBox", "0 0 24 24")
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="{viewbox}" fill="{color}">{paths}</svg>'


def arrow(x, y, color=WHITE):
    return f'<path d="M{x} {y + 12}l12 -12m-11 0h11v11" fill="none" stroke="{color}" stroke-width="2"/>'


def stamp(x, y, label, color=RED, width=100, dark=False):
    return rect(x, y, width, 25, color) + text(x + 10, y + 17, label, 11, BG if dark else WHITE, 700, True)


def write_svg(name, width, height, title, description, body):
    document = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(description)}</desc>
{body}
</svg>
'''
    ET.fromstring(document)
    with (OUTPUT / name).open("w", encoding="utf-8", newline="\n") as target:
        target.write(document)


def hero(mobile=False):
    w, h = (400, 464) if mobile else (1000, 412)
    b = rect(0, 0, w, h, BG)
    b += rect(1, 1, w - 2, h - 2, "none", WHITE, 2)
    b += rect(1, 1, 7, h - 2, RED)
    b += stamp(24, 20, "N / 01", RED, 72)
    b += text(108, 37, "NYZEEP / WORKSTATION", 11 if mobile else 13, WHITE, 700, True, letter_spacing=1)
    if not mobile:
        b += rect(804, 26, 7, 7, YELLOW)
        b += text(824, 37, "PUBLIC / GITHUB", 12, MUTED, 500, True)
    b += line(24, 62, w - 24, 62, LINE)

    if mobile:
        b += text(24, 91, "AI TOOLING / ANDROID / OPEN SOURCE", 10, MUTED, 500, True, letter_spacing=0.3)
        b += text(21, 169, "NYZEEP", 77, WHITE, 800, letter_spacing=-4)
        b += rect(26, 185, 64, 5, RED) + rect(96, 185, 24, 5, BLUE) + rect(126, 185, 12, 5, YELLOW)
        b += text(24, 227, "MAKE IT USEFUL.", 24, WHITE, 700, letter_spacing=-0.5)
        b += text(24, 259, "MAKE IT DELIGHTFUL.", 24, WHITE, 700, letter_spacing=-0.5)
        b += line(24, 285, 376, 285)
        for x, slug, label, color in [(24, "android", "ANDROID", RED), (144, "python", "PYTHON", YELLOW), (264, "typescript", "TS", BLUE)]:
            b += rect(x, 305, 104, 74, PANEL, LINE)
            b += icon(slug, x + 12, 317, 25, color if color != BLUE else "#70A7FF")
            b += text(x + 12, 365, label, 10, WHITE, 600, True)
        b += rect(8, 403, w - 9, 60, RED)
        b += text(24, 428, "IDEAS → TOOLS → EVERYDAY USE", 11, WHITE, 700, True)
        b += text(24, 449, "github.com/Nyzeep", 11, WHITE, 400, True)
        b += arrow(353, 423)
    else:
        b += text(32, 96, "AI TOOLING / ANDROID / OPEN SOURCE", 13, MUTED, 500, True, letter_spacing=1.5)
        b += text(24, 210, "NYZEEP", 131, WHITE, 800, letter_spacing=-7)
        b += rect(33, 230, 84, 6, RED) + rect(125, 230, 30, 6, BLUE) + rect(163, 230, 14, 6, YELLOW)
        b += text(32, 278, "MAKE IT USEFUL.", 28, WHITE, 700, letter_spacing=-0.5)
        b += text(32, 314, "MAKE IT DELIGHTFUL.", 28, WHITE, 700, letter_spacing=-0.5)
        b += line(635, 83, 635, 330)
        b += rect(661, 84, 311, 246, PANEL, WHITE)
        b += stamp(677, 100, "BUILD / EXPLORE", WHITE, 137, True)
        b += cross(972, 84)
        b += text(677, 159, "SOFTWARE FOR", 22, WHITE, 700)
        b += text(677, 188, "REAL LIFE.", 22, WHITE, 700)
        b += line(677, 207, 956, 207)
        for x, slug, label, color in [(677, "android", "ANDROID", RED), (774, "python", "PYTHON", YELLOW), (870, "typescript", "TS", "#70A7FF")]:
            b += icon(slug, x, 225, 35, color)
            b += text(x, 286, label, 11, MUTED, 500, True)
        b += rect(8, 354, w - 9, 57, RED)
        b += text(32, 388, "IDEAS → TOOLS → EVERYDAY USE", 14, WHITE, 700, True, letter_spacing=1)
        b += text(734, 388, "github.com/Nyzeep", 14, WHITE, 400, True)
        b += arrow(950, 375)
    write_svg("hero-mobile.svg" if mobile else "hero.svg", w, h, "Nyzeep — AI tooling, Android and open source", "Make it useful, then make it delightful. Personal projects in developer tools, mobile Linux and everyday AI.", b)


def stack_card(name, index, title, subtitle, items, accent):
    w, h = 400, 180
    b = rect(1, 1, w - 2, h - 2, BG, WHITE, 2)
    b += rect(1, 1, 5, h - 2, accent)
    b += text(20, 26, f"{index} / {subtitle}", 10, MUTED, 500, True, letter_spacing=1)
    b += text(20, 54, title, 21, WHITE, 700)
    b += rect(362, 20, 16, 16, accent)
    b += line(20, 69, 380, 69)
    for i, (slug, label, color) in enumerate(items):
        x = 20 + i * 122
        b += icon(slug, x, 90, 34, color)
        b += text(x, 151, label, 14, WHITE, 600)
    write_svg(name, w + 12, h + 12, title, ", ".join(item[1] for item in items) + ". Technologies and tools used across public projects; not a proficiency score.", f'<g transform="translate(6 0)">{b}</g>')


def project(name, index, title, label, slug, accent, description, stack, state):
    w, h = 400, 248
    b = rect(1, 1, w - 2, h - 2, BG, WHITE, 2)
    b += rect(1, 1, w - 2, 4, accent)
    b += rect(20, 22, 42, 42, accent)
    b += icon(slug, 29, 31, 24, BG if accent in (YELLOW, WHITE) else WHITE)
    b += text(76, 38, f"PRJ / {index}", 10, MUTED, 600, True, letter_spacing=1)
    b += text(76, 57, label, 11, WHITE, 700, True)
    b += arrow(365, 27, accent if accent != BLUE else "#70A7FF")
    b += text(20, 100, title, 23, WHITE, 700, letter_spacing=-0.5)
    for i, content in enumerate(description):
        b += text(20, 129 + i * 23, content, 16, MUTED)
    b += text(20, 185, stack, 11, WHITE, 600, True)
    b += line(20, 203, 380, 203)
    b += rect(20, 220, 6, 6, accent)
    b += text(34, 227, state, 10, MUTED, 500, True)
    b += text(294, 228, "VIEW REPO", 10, WHITE, 700, True)
    write_svg(name, w + 12, h + 12, title, " ".join(description) + " " + stack + ". " + state + ".", f'<g transform="translate(6 0)">{b}</g>')


def footer():
    b = rect(1, 1, 998, 82, BG, WHITE, 2)
    b += rect(1, 1, 7, 82, RED)
    b += rect(28, 26, 12, 12, RED) + rect(49, 26, 12, 12, YELLOW) + rect(70, 26, 12, 12, WHITE)
    b += text(112, 37, "ALWAYS CURIOUS. ALWAYS BUILDING.", 17, WHITE, 700, True)
    b += text(112, 61, "OPEN SOURCE / SHARED IDEAS / SMALL DETAILS", 10, MUTED, 500, True, letter_spacing=1)
    b += arrow(953, 35)
    write_svg("footer.svg", 1000, 84, "Always curious. Always building.", "Open source, shared ideas, and small details. Find Nyzeep on GitHub.", b)
    b = rect(1, 1, 398, 103, BG, WHITE, 2)
    b += rect(1, 1, 5, 103, RED)
    b += rect(20, 20, 10, 10, RED) + rect(37, 20, 10, 10, YELLOW) + rect(54, 20, 10, 10, WHITE)
    b += text(20, 57, "ALWAYS CURIOUS.", 19, WHITE, 700, True)
    b += text(20, 83, "ALWAYS BUILDING.", 19, WHITE, 700, True)
    b += arrow(363, 70)
    write_svg("footer-mobile.svg", 400, 105, "Always curious. Always building.", "Find Nyzeep on GitHub.", b)


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    hero()
    hero(mobile=True)
    stack_card("stack-languages.svg", "01", "Languages", "CORE LOGIC", [("typescript", "TypeScript", "#70A7FF"), ("python", "Python", YELLOW), ("rust", "Rust", WHITE)], RED)
    stack_card("stack-interfaces.svg", "02", "Interfaces", "WEB + DESKTOP", [("vuedotjs", "Vue", "#62D8A0"), ("javascript", "JavaScript", "#F7DF1E"), ("tauri", "Tauri", "#6CD9EF")], BLUE)
    stack_card("stack-systems.svg", "03", "Systems", "MOBILE + LINUX", [("android", "Android", "#67DC8B"), ("kotlin", "Kotlin", "#BB9AFF"), ("linux", "Linux", WHITE)], YELLOW)
    stack_card("stack-tools.svg", "04", "Services & tools", "BUILD + COLLABORATE", [("fastapi", "FastAPI", "#4DD4C2"), ("git", "Git", "#F47760"), ("github", "GitHub", WHITE)], WHITE)
    project("project-orchestella.svg", "01", "Orchestella Studio", "MOBILE WORKSTATION", "android", RED, ["无需 Root 的 Android Linux 运行环境", "把移动设备变成随身工作站。"], "ANDROID / KOTLIN / LINUX", "IN DEVELOPMENT")
    project("project-lumimate.svg", "02", "LumiMate", "EVERYDAY AI", "tauri", YELLOW, ["融合本地模型与语音交互", "探索更自然的桌面 AI 陪伴。"], "PYTHON / VUE / TAURI", "EARLY EXPLORATION")
    project("project-icons.svg", "03", "Material File Icons", "DEVELOPER EXPERIENCE", "typescript", BLUE, ["为 DeepSeek Harness 文件树", "带来清晰、一致的 Material 图标。"], "TYPESCRIPT / FILE ICONS", "SOURCE AVAILABLE")
    project("project-ecoscout.svg", "04", "Ecoscout", "APPLIED VISION", "python", WHITE, ["面向社区环卫场景", "构建图像与视频视觉检测后端。"], "PYTHON / FASTAPI / COMPUTER VISION", "PROJECT EXPLORATION")
    footer()
    print(f"Built 12 SVG assets in {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

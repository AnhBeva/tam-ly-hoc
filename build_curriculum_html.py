from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Giao-trinh-tam-ly-hoc-50-tap.html"


GROUPS = [
    ("Nền Tảng Cá Nhân", "Bản đồ gốc, cảm xúc, quyết định và thói quen cá nhân.", range(1, 5)),
    ("Lãnh Đạo, Giao Tiếp Và Dùng Người", "Quyền lực, thuyết phục, nhân sự, quan hệ, tiền bạc và trưởng thành nội tâm.", range(5, 11)),
    ("Não Bộ, Phát Triển Và Hành Vi", "Neuroscience, tuổi thơ, lâm sàng, thiết kế thay đổi và kinh tế học hành vi.", range(11, 16)),
    ("Hệ Thống, Văn Hóa Và Đạo Đức", "Tổ chức, văn hóa Á Đông, coaching, nhóm, đạo đức và trách nhiệm khi tác động đến con người.", range(16, 21)),
    ("Các Tầng Sâu Của Con Người", "Tiến hóa, đo lường, học tập, đạo đức nội tâm, xã hội, ý nghĩa, công nghệ, sang chấn và đọc nghiên cứu.", range(21, 31)),
    ("Vô Thức, Thân Mật Và Nửa Sau Cuộc Đời", "Động cơ ẩn, tự ái, thao túng, tình yêu, giới, khủng hoảng, sáng tạo, bản sắc, trung niên và tâm linh.", range(31, 41)),
    ("Xã Hội, Luật Pháp Và Sức Khỏe", "Ý thức hệ, tâm-thân, pháp lý, tội phạm và điều kiện xã hội tác động lên con người.", range(41, 44)),
    ("Hiệu Suất, Biểu Tượng Và Không Gian", "Hiệu suất đỉnh cao, nghệ thuật, câu chuyện, biểu tượng và môi trường sống.", range(44, 47)),
    ("Cộng Đồng, Gia Đình, Tổ Chức Và Tích Hợp", "Chữa lành tập thể, giáo dục gia đình, tổ chức nâng cao và bản đồ tối hậu 50 tập.", range(47, 51)),
]


def chapter_number(path: Path) -> int:
    if path.name == "Giao-trinh-hieu-con-nguoi-tu-goc.md":
        return 1
    match = re.match(r"Tap-(\d+)-", path.name)
    return int(match.group(1)) if match else 999


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    return text[:90] or "section"


def inline_md(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    return escaped


def parse_table(lines: list[str]) -> str:
    rows = []
    for line in lines:
        cells = [inline_md(cell.strip()) for cell in line.strip().strip("|").split("|")]
        rows.append(cells)

    header = rows[0]
    body = rows[2:] if len(rows) > 2 else []
    out = ["<div class=\"table-wrap\"><table>"]
    out.append("<thead><tr>")
    for cell in header:
        out.append(f"<th>{cell}</th>")
    out.append("</tr></thead>")
    if body:
        out.append("<tbody>")
        for row in body:
            out.append("<tr>")
            for cell in row:
                out.append(f"<td>{cell}</td>")
            out.append("</tr>")
        out.append("</tbody>")
    out.append("</table></div>")
    return "\n".join(out)


def render_mermaid_flowchart(code: str) -> str:
    labels: dict[str, str] = {}
    order: list[str] = []
    edges: list[tuple[str, str]] = []

    for line in code.splitlines():
        match = re.search(r"([A-Za-z0-9_]+)(?:\[\"(.+?)\"\])?\s*-->\s*([A-Za-z0-9_]+)(?:\[\"(.+?)\"\])?", line.strip())
        if not match:
            continue
        source, source_label, target, target_label = match.groups()
        if source_label and source not in labels:
            labels[source] = source_label
        if source not in order:
            order.append(source)
        if target_label and target not in labels:
            labels[target] = target_label
            order.append(target)
        if target not in order:
            order.append(target)
        edges.append((source, target))

    if not order:
        escaped = html.escape(code)
        return (
            "<figure class=\"diagram-card\">"
            "<figcaption>Mô hình trực quan</figcaption>"
            f"<pre class=\"code-block\"><code>{escaped}</code></pre>"
            "</figure>"
        )

    items = []
    for index, node in enumerate(order, 1):
        label = labels.get(node, node)
        items.append(
            "<div class=\"flow-step\">"
            f"<span>{index:02d}</span>"
            f"<strong>{html.escape(label)}</strong>"
            "</div>"
        )
        if index < len(order):
            items.append("<div class=\"flow-arrow\">→</div>")

    return (
        "<figure class=\"diagram-card visual-flow\">"
        "<figcaption>Mô hình trực quan</figcaption>"
        f"<div class=\"flow-grid\">{''.join(items)}</div>"
        "</figure>"
    )


def render_text_block(code: str) -> str:
    raw_lines = [line.rstrip() for line in code.splitlines() if line.strip()]
    if not raw_lines:
        return ""

    if len(raw_lines) == 1 and "=" in raw_lines[0] and " + " in raw_lines[0]:
        left, right = raw_lines[0].split("=", 1)
        chips = "".join(
            f"<span>{html.escape(part.strip())}</span>"
            for part in right.split("+")
            if part.strip()
        )
        return (
            "<div class=\"formula-card\">"
            f"<strong>{html.escape(left.strip())}</strong>"
            "<em>=</em>"
            f"<div>{chips}</div>"
            "</div>"
        )

    rows = []
    for line in raw_lines:
        numbered = re.match(r"^(\d+)\.\s*(.+)$", line.strip())
        if numbered:
            marker, content = numbered.groups()
            rows.append(
                "<div class=\"practice-line\">"
                f"<span>{html.escape(marker)}</span>"
                f"<p>{inline_md(content)}</p>"
                "</div>"
            )
        else:
            rows.append(
                "<div class=\"practice-line\">"
                "<span>•</span>"
                f"<p>{inline_md(line.strip())}</p>"
                "</div>"
            )

    return (
        "<div class=\"practice-card\">"
        "<div class=\"practice-label\">Ghi nhớ / áp dụng</div>"
        f"<div class=\"practice-lines\">{''.join(rows)}</div>"
        "</div>"
    )


def convert_markdown(md: str, chapter_id: str) -> tuple[str, list[tuple[str, str, int]]]:
    lines = md.splitlines()
    output: list[str] = []
    toc: list[tuple[str, str, int]] = []
    i = 0
    in_code = False
    code_lang = ""
    code_lines: list[str] = []
    list_stack: list[str] = []
    seen_anchors: dict[str, int] = {}

    def close_lists() -> None:
        while list_stack:
            output.append(f"</{list_stack.pop()}>")

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            if not in_code:
                close_lists()
                in_code = True
                code_lang = stripped[3:].strip() or "text"
                code_lines = []
            else:
                escaped = html.escape("\n".join(code_lines))
                if code_lang == "mermaid":
                    output.append(render_mermaid_flowchart("\n".join(code_lines)))
                elif code_lang in {"text", "txt"}:
                    output.append(render_text_block("\n".join(code_lines)))
                else:
                    output.append(
                        f"<pre class=\"code-block\"><code>{escaped}</code></pre>"
                    )
                in_code = False
                code_lang = ""
                code_lines = []
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if not stripped:
            close_lists()
            i += 1
            continue

        if stripped == "---":
            close_lists()
            output.append("<hr>")
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and re.match(
            r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[i + 1]
        ):
            close_lists()
            table_lines = [line, lines[i + 1]]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            output.append(parse_table(table_lines))
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            close_lists()
            level = len(heading.group(1))
            text = heading.group(2).strip()
            if level == 1:
                i += 1
                continue
            base_anchor = f"{chapter_id}-{slugify(text)}"
            count = seen_anchors.get(base_anchor, 0)
            seen_anchors[base_anchor] = count + 1
            anchor = base_anchor if count == 0 else f"{base_anchor}-{count + 1}"
            toc.append((text, anchor, level))
            output.append(
                f"<h{level} id=\"{anchor}\"><a class=\"anchor\" href=\"#{anchor}\">{inline_md(text)}</a></h{level}>"
            )
            i += 1
            continue

        if stripped.startswith(">"):
            close_lists()
            quote = stripped.lstrip(">").strip()
            output.append(f"<blockquote>{inline_md(quote)}</blockquote>")
            i += 1
            continue

        ordered = re.match(r"^\d+\.\s+(.+)$", stripped)
        unordered = re.match(r"^[-*]\s+(.+)$", stripped)
        if ordered or unordered:
            tag = "ol" if ordered else "ul"
            content = ordered.group(1) if ordered else unordered.group(1)
            if not list_stack or list_stack[-1] != tag:
                close_lists()
                output.append(f"<{tag}>")
                list_stack.append(tag)
            output.append(f"<li>{inline_md(content)}</li>")
            i += 1
            continue

        close_lists()
        output.append(f"<p>{inline_md(stripped)}</p>")
        i += 1

    close_lists()
    return "\n".join(output), toc


def chapter_intro(md: str) -> tuple[str, str]:
    lines = [line.strip() for line in md.splitlines() if line.strip()]
    title = lines[0].lstrip("#").strip() if lines else "Chương"
    subtitle = ""
    for line in lines[1:8]:
        if line.startswith("**") and line.endswith("**"):
            subtitle = line.strip("*").strip()
            break
    return title, subtitle


def display_title(title: str, number: int) -> str:
    return title.replace("Tập " + str(number) + ": ", "")


def main() -> None:
    files = sorted(
        [ROOT / "Giao-trinh-hieu-con-nguoi-tu-goc.md", *ROOT.glob("Tap-*.md")],
        key=chapter_number,
    )
    chapters = []
    all_toc = []
    for file in files:
        number = chapter_number(file)
        md = file.read_text(encoding="utf-8")
        title, subtitle = chapter_intro(md)
        chapter_id = f"tap-{number}"
        content, toc = convert_markdown(md, chapter_id)
        chapters.append(
            {
                "number": number,
                "id": chapter_id,
                "title": title,
                "subtitle": subtitle,
                "content": content,
                "word_count": len(md.split()),
            }
        )
        all_toc.append((number, title, subtitle, toc))

    by_number = {c["number"]: c for c in chapters}
    nav_sections = []
    for group_index, (group_title, _group_desc, number_range) in enumerate(GROUPS, 1):
        links = []
        for number in number_range:
            c = by_number.get(number)
            if not c:
                continue
            links.append(
                f"<a class=\"nav-item\" href=\"#{c['id']}\" data-chapter=\"{c['number']}\" data-title=\"{html.escape(c['title'].lower())} {html.escape(c['subtitle'].lower())}\">"
                f"<span>{c['number']:02d}</span><strong>{html.escape(display_title(c['title'], c['number']))}</strong></a>"
            )
        if links:
            nav_sections.append(
                f"<div class=\"nav-section\"><div class=\"nav-heading\">Chương {group_index:02d}<b>{html.escape(group_title)}</b></div>{''.join(links)}</div>"
            )
    nav_items = "\n".join(nav_sections)

    group_sections = []
    for group_index, (group_title, group_desc, number_range) in enumerate(GROUPS, 1):
        cards = []
        for number in number_range:
            c = by_number.get(number)
            if not c:
                continue
            cards.append(
                f"<a class=\"chapter-card\" href=\"#{c['id']}\" data-card-title=\"{html.escape(c['title'].lower())} {html.escape(c['subtitle'].lower())}\">"
                f"<span class=\"chapter-number\">Tập {c['number']:02d}</span>"
                f"<h3>{html.escape(display_title(c['title'], c['number']))}</h3>"
                f"<p>{html.escape(c['subtitle'])}</p>"
                f"<small>{c['word_count']:,} từ</small>"
                "</a>"
            )
        group_sections.append(
            f"<section class=\"theme-section\" data-theme=\"{group_index}\">"
            f"<div class=\"theme-heading\"><span>Chương {group_index:02d}</span><h3>{html.escape(group_title)}</h3><p>{html.escape(group_desc)}</p></div>"
            f"<div class=\"card-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    overview_cards = "\n".join(group_sections)

    chapter_html = "\n".join(
        f"<article class=\"chapter\" id=\"{c['id']}\" data-chapter=\"{c['number']}\">"
        f"<div class=\"chapter-hero\"><span>Tập {c['number']:02d}</span><h1>{html.escape(display_title(c['title'], c['number']))}</h1>"
        f"<p>{html.escape(c['subtitle'])}</p>"
        f"<button class=\"complete-btn\" data-complete=\"{c['number']}\">Đánh dấu đã học</button></div>"
        f"<div class=\"chapter-body\">{c['content']}</div>"
        "</article>"
        for c in chapters
    )

    html_doc = f"""<!doctype html>
<html lang=\"vi\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>Giáo Trình Tâm Lý Học 50 Tập</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f5f5f7;
      --panel: rgba(255,255,255,.78);
      --panel-solid: #fff;
      --text: #1d1d1f;
      --muted: #6e6e73;
      --line: rgba(0,0,0,.09);
      --blue: #0071e3;
      --blue-2: #54a3ff;
      --green: #30d158;
      --shadow: 0 18px 60px rgba(0,0,0,.08);
      --radius: 22px;
      --content: 920px;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, \"SF Pro Display\", \"SF Pro Text\", \"Segoe UI\", sans-serif;
      background:
        radial-gradient(circle at 10% 0%, rgba(0,113,227,.12), transparent 30%),
        radial-gradient(circle at 90% 5%, rgba(48,209,88,.10), transparent 24%),
        linear-gradient(180deg, #fbfbfd 0%, var(--bg) 30%, #fff 100%);
      color: var(--text);
      letter-spacing: 0;
    }}
    a {{ color: inherit; text-decoration: none; }}
    .top-progress {{
      position: fixed; inset: 0 0 auto 0; height: 4px; z-index: 20;
      background: linear-gradient(90deg, var(--blue), var(--green));
      transform-origin: left center; transform: scaleX(0);
    }}
    .app {{ display: grid; grid-template-columns: 320px minmax(0,1fr); min-height: 100vh; }}
    aside {{
      position: sticky; top: 0; height: 100vh; padding: 22px; overflow: auto;
      border-right: 1px solid var(--line);
      background: rgba(245,245,247,.72);
      backdrop-filter: blur(22px) saturate(1.25);
      -webkit-backdrop-filter: blur(22px) saturate(1.25);
    }}
    .brand {{ display: flex; gap: 12px; align-items: center; margin-bottom: 18px; }}
    .brand-mark {{
      width: 42px; height: 42px; border-radius: 12px;
      background: linear-gradient(145deg, #111 0%, #4b5563 100%);
      color: #fff; display: grid; place-items: center; font-weight: 800;
      box-shadow: 0 10px 24px rgba(0,0,0,.18);
    }}
    .brand h1 {{ font-size: 16px; line-height: 1.15; margin: 0; }}
    .brand p {{ margin: 3px 0 0; color: var(--muted); font-size: 12px; }}
    .search {{
      width: 100%; border: 1px solid var(--line); border-radius: 14px; padding: 12px 14px;
      background: rgba(255,255,255,.72); outline: none; font-size: 14px;
      box-shadow: inset 0 1px 0 rgba(255,255,255,.8);
    }}
    .study-panel {{
      margin: 14px 0; padding: 14px; border-radius: 18px; background: var(--panel-solid);
      border: 1px solid var(--line); box-shadow: 0 10px 30px rgba(0,0,0,.05);
    }}
    .study-panel strong {{ font-size: 13px; }}
    .meter {{ height: 8px; border-radius: 999px; background: #e8e8ed; overflow: hidden; margin: 10px 0 8px; }}
    .meter span {{ display: block; height: 100%; width: 0; background: linear-gradient(90deg, var(--blue), var(--green)); }}
    .progress-text {{ color: var(--muted); font-size: 12px; }}
    nav {{ display: grid; gap: 14px; }}
    .nav-section {{ display: grid; gap: 6px; }}
    .nav-heading {{
      display: grid; gap: 3px; padding: 8px 10px 4px; color: var(--muted);
      font-size: 11px; font-weight: 800; text-transform: uppercase;
    }}
    .nav-heading b {{
      color: #424245; font-size: 12px; font-weight: 700; text-transform: none; line-height: 1.25;
    }}
    .nav-item {{
      display: grid; grid-template-columns: 34px 1fr; align-items: center; gap: 8px;
      padding: 10px; border-radius: 13px; color: #424245; font-size: 13px;
    }}
    .nav-item:hover, .nav-item.active {{ background: rgba(0,113,227,.10); color: var(--text); }}
    .nav-item.done span {{ background: rgba(48,209,88,.16); color: #168a36; }}
    .nav-item span {{
      width: 30px; height: 26px; border-radius: 9px; display: grid; place-items: center;
      background: #fff; font-size: 11px; color: var(--muted); border: 1px solid var(--line);
    }}
    .nav-item strong {{ font-weight: 600; line-height: 1.2; }}
    main {{ min-width: 0; }}
    .hero {{
      min-height: 72vh; display: grid; align-items: center; padding: 84px 6vw 42px;
      border-bottom: 1px solid var(--line);
    }}
    .hero-inner {{ max-width: 1120px; }}
    .eyebrow {{ color: var(--blue); font-weight: 700; font-size: 14px; margin: 0 0 14px; }}
    .hero h1 {{
      margin: 0; font-size: clamp(48px, 7vw, 104px); line-height: .94; letter-spacing: -0.02em;
      max-width: 980px;
    }}
    .hero .lead {{
      margin: 28px 0 0; max-width: 760px; color: #424245; font-size: clamp(19px, 2vw, 28px);
      line-height: 1.35;
    }}
    .hero-stats {{
      display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 14px;
      max-width: 760px; margin-top: 34px;
    }}
    .stat {{
      background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 18px; box-shadow: var(--shadow); backdrop-filter: blur(16px);
    }}
    .stat strong {{ display: block; font-size: 28px; }}
    .stat span {{ color: var(--muted); font-size: 13px; }}
    .overview {{ padding: 54px 6vw; }}
    .section-title {{ max-width: var(--content); margin: 0 auto 24px; }}
    .section-title h2 {{ margin: 0; font-size: clamp(30px,4vw,54px); letter-spacing: -0.02em; }}
    .section-title p {{ color: var(--muted); font-size: 18px; line-height: 1.5; }}
    .card-grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(240px,1fr)); gap: 14px;
      max-width: 1280px; margin: 0 auto;
    }}
    .theme-stack {{ display: grid; gap: 28px; max-width: 1280px; margin: 0 auto; }}
    .theme-section {{
      border: 1px solid var(--line); border-radius: 30px; padding: clamp(18px,3vw,28px);
      background: rgba(255,255,255,.62); box-shadow: 0 14px 42px rgba(0,0,0,.045);
    }}
    .theme-heading {{ max-width: 820px; margin-bottom: 18px; }}
    .theme-heading span {{ color: var(--blue); font-weight: 800; font-size: 12px; }}
    .theme-heading h3 {{ margin: 8px 0 8px; font-size: clamp(26px,3vw,38px); letter-spacing: -0.02em; }}
    .theme-heading p {{ margin: 0; color: var(--muted); font-size: 16px; line-height: 1.5; }}
    .chapter-card {{
      background: var(--panel-solid); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 20px; min-height: 210px; box-shadow: 0 14px 40px rgba(0,0,0,.06);
      transition: transform .2s ease, box-shadow .2s ease;
      display: flex; flex-direction: column;
    }}
    .chapter-card:hover {{ transform: translateY(-4px); box-shadow: var(--shadow); }}
    .chapter-number {{ color: var(--blue); font-size: 12px; font-weight: 800; }}
    .chapter-card h3 {{ margin: 12px 0 8px; font-size: 21px; line-height: 1.16; letter-spacing: -0.01em; }}
    .chapter-card p {{ margin: 0; color: var(--muted); line-height: 1.45; font-size: 14px; }}
    .chapter-card small {{ margin-top: auto; color: #86868b; padding-top: 14px; }}
    .chapter {{
      display: none;
      max-width: calc(var(--content) + 96px); margin: 0 auto; padding: 42px 24px 70px;
      border-top: 1px solid var(--line);
    }}
    .chapter.active-chapter {{ display: block; }}
    .chapter-hero {{
      background: linear-gradient(160deg, rgba(255,255,255,.96), rgba(245,245,247,.86));
      border: 1px solid var(--line); border-radius: 32px; padding: clamp(28px,5vw,56px);
      box-shadow: var(--shadow); margin-bottom: 28px;
    }}
    .chapter-hero span {{ color: var(--blue); font-weight: 800; }}
    .chapter-hero h1 {{ margin: 12px 0; font-size: clamp(34px,5vw,64px); line-height: 1; letter-spacing: -0.025em; }}
    .chapter-hero p {{ max-width: 760px; color: #424245; font-size: 19px; line-height: 1.45; }}
    .complete-btn {{
      border: 0; border-radius: 999px; background: var(--text); color: #fff;
      padding: 12px 18px; font-weight: 700; cursor: pointer; font-size: 14px;
    }}
    .complete-btn.done {{ background: #e8f8ed; color: #168a36; }}
    .chapter-body {{
      background: rgba(255,255,255,.74); border: 1px solid var(--line); border-radius: 28px;
      padding: clamp(24px,4vw,54px); box-shadow: 0 10px 42px rgba(0,0,0,.045);
    }}
    .chapter-body h2 {{ margin: 46px 0 14px; font-size: clamp(28px,3.2vw,44px); letter-spacing: -0.02em; line-height: 1.08; }}
    .chapter-body h2:first-child {{ margin-top: 0; }}
    .chapter-body h3 {{ margin: 28px 0 10px; font-size: 23px; letter-spacing: -0.01em; }}
    .chapter-body p, .chapter-body li {{ font-size: 17px; line-height: 1.68; color: #2f2f32; }}
    .chapter-body p {{ margin: 10px 0; }}
    .chapter-body ul, .chapter-body ol {{ padding-left: 24px; margin: 12px 0 18px; }}
    .chapter-body strong {{ color: var(--text); }}
    .chapter-body code {{
      background: #f1f1f4; border: 1px solid var(--line); border-radius: 7px; padding: 2px 6px;
      font-family: \"SF Mono\", Menlo, Consolas, monospace; font-size: .9em;
    }}
    blockquote {{
      margin: 22px 0; padding: 22px 24px; border-radius: 20px;
      background: linear-gradient(135deg, rgba(0,113,227,.10), rgba(48,209,88,.08));
      border: 1px solid rgba(0,113,227,.16); font-size: 20px; font-weight: 700;
    }}
    .table-wrap {{ overflow: auto; margin: 20px 0; border-radius: 18px; border: 1px solid var(--line); }}
    table {{ width: 100%; border-collapse: collapse; background: #fff; font-size: 15px; }}
    th, td {{ padding: 13px 15px; text-align: left; border-bottom: 1px solid var(--line); vertical-align: top; line-height: 1.45; }}
    th {{ background: #f5f5f7; font-weight: 800; color: #1d1d1f; }}
    tr:last-child td {{ border-bottom: 0; }}
    .code-block, .diagram-card pre {{
      overflow: auto; white-space: pre-wrap; overflow-wrap: anywhere;
      padding: 20px 22px; border-radius: 18px; background: #f7f9fc; color: #1d1d1f;
      border: 1px solid rgba(0,113,227,.16);
      box-shadow: inset 0 1px 0 rgba(255,255,255,.95);
      font-family: \"SF Mono\", Menlo, Consolas, monospace; font-size: 15px; line-height: 1.75;
    }}
    .diagram-card {{
      margin: 24px 0; padding: 20px; border: 1px solid var(--line); border-radius: 22px; background: #fff;
    }}
    .diagram-card figcaption {{ color: var(--muted); font-size: 13px; font-weight: 700; margin: 0 0 14px; }}
    .flow-grid {{
      display: flex; align-items: stretch; gap: 10px; flex-wrap: wrap;
    }}
    .flow-step {{
      flex: 1 1 190px; min-width: 170px; display: grid; gap: 10px;
      padding: 16px; border-radius: 18px; background: linear-gradient(180deg, #fff, #f6faff);
      border: 1px solid rgba(0,113,227,.18);
      box-shadow: 0 10px 28px rgba(0,0,0,.055);
    }}
    .flow-step span {{
      width: 34px; height: 28px; border-radius: 10px; display: grid; place-items: center;
      background: rgba(0,113,227,.10); color: var(--blue); font-size: 12px; font-weight: 800;
    }}
    .flow-step strong {{ font-size: 16px; line-height: 1.35; letter-spacing: 0; }}
    .flow-arrow {{
      display: grid; place-items: center; color: var(--blue); font-size: 24px; font-weight: 800;
      min-width: 24px;
    }}
    .practice-card {{
      margin: 22px 0; padding: clamp(18px,3vw,26px); border-radius: 24px;
      background:
        linear-gradient(135deg, rgba(0,113,227,.10), rgba(48,209,88,.08)),
        #fbfdff;
      border: 1px solid rgba(0,113,227,.18);
      box-shadow: 0 16px 42px rgba(0,0,0,.06), inset 0 1px 0 rgba(255,255,255,.95);
    }}
    .practice-label {{
      display: inline-flex; align-items: center; min-height: 28px; padding: 6px 10px;
      border-radius: 999px; background: rgba(255,255,255,.78); color: var(--blue);
      border: 1px solid rgba(0,113,227,.14); font-size: 12px; font-weight: 800;
      margin-bottom: 14px;
    }}
    .practice-lines {{ display: grid; gap: 10px; }}
    .practice-line {{
      display: grid; grid-template-columns: 36px minmax(0,1fr); gap: 12px; align-items: start;
      padding: 13px 14px; border-radius: 16px; background: rgba(255,255,255,.82);
      border: 1px solid rgba(0,0,0,.055);
    }}
    .practice-line span {{
      width: 32px; height: 32px; display: grid; place-items: center; border-radius: 11px;
      background: #1d1d1f; color: #fff; font-size: 13px; font-weight: 800;
      box-shadow: 0 8px 18px rgba(0,0,0,.12);
    }}
    .practice-line p {{
      margin: 1px 0 0; color: #1d1d1f; font-size: 18px; line-height: 1.5; font-weight: 650;
      overflow-wrap: anywhere;
    }}
    .formula-card {{
      margin: 22px 0; display: grid; gap: 14px; padding: clamp(20px,3vw,28px);
      border-radius: 24px; background: linear-gradient(135deg, #f7fbff, #f1fff6);
      border: 1px solid rgba(0,113,227,.18); box-shadow: 0 16px 42px rgba(0,0,0,.06);
    }}
    .formula-card strong {{ font-size: clamp(22px,3vw,32px); letter-spacing: -0.01em; }}
    .formula-card em {{
      width: 38px; height: 38px; display: grid; place-items: center; border-radius: 13px;
      background: var(--blue); color: #fff; font-style: normal; font-size: 22px; font-weight: 900;
    }}
    .formula-card div {{ display: flex; flex-wrap: wrap; gap: 10px; }}
    .formula-card span {{
      display: inline-flex; align-items: center; min-height: 40px; padding: 9px 13px;
      border-radius: 14px; background: #fff; border: 1px solid rgba(0,0,0,.07);
      color: #1d1d1f; font-size: 16px; font-weight: 750;
    }}
    hr {{ border: 0; border-top: 1px solid var(--line); margin: 38px 0; }}
    .anchor:hover {{ color: var(--blue); }}
    .no-results {{ display: none; text-align: center; padding: 34px; color: var(--muted); }}
    footer {{ padding: 42px 6vw 70px; text-align: center; color: var(--muted); }}
    @media (max-width: 980px) {{
      .app {{ display: block; }}
      aside {{ position: relative; height: auto; max-height: 70vh; }}
      .hero {{ min-height: auto; padding-top: 46px; }}
      .hero-stats {{ grid-template-columns: 1fr; }}
    }}
    @media print {{
      aside, .complete-btn, .top-progress, .overview {{ display: none !important; }}
      .app {{ display: block; }}
      .chapter {{ display: block !important; page-break-before: always; }}
      body {{ background: #fff; }}
      .chapter-body, .chapter-hero {{ box-shadow: none; }}
    }}
  </style>
</head>
<body>
  <div class=\"top-progress\" id=\"topProgress\"></div>
  <div class=\"app\">
    <aside>
      <div class=\"brand\">
        <div class=\"brand-mark\">{len(chapters)}</div>
        <div>
          <h1>Hiểu Con Người Từ Gốc</h1>
          <p>Giáo trình tâm lý học thực dụng</p>
        </div>
      </div>
      <input class=\"search\" id=\"search\" placeholder=\"Tìm tập, chủ đề, khái niệm...\">
      <div class=\"study-panel\">
        <strong>Tiến độ học tập</strong>
        <div class=\"meter\"><span id=\"meterFill\"></span></div>
        <div class=\"progress-text\" id=\"progressText\">0/{len(chapters)} tập đã học</div>
      </div>
      <nav id=\"nav\">{nav_items}</nav>
    </aside>
    <main>
      <section class=\"hero\" id=\"top\">
        <div class=\"hero-inner\">
          <p class=\"eyebrow\">Bản HTML tổng hợp từ {len(chapters)} tập</p>
          <h1>Hiểu con người rõ hơn. Lãnh đạo sâu hơn. Sống tỉnh hơn.</h1>
          <p class=\"lead\">Một trải nghiệm đọc gọn, đẹp và có hệ thống: từ cảm xúc, quyết định, thói quen, quyền lực, quan hệ, văn hóa, neuroscience đến bản đồ tích hợp về con người.</p>
          <div class=\"hero-stats\">
            <div class=\"stat\"><strong>{len(chapters)}</strong><span>Tập học có cấu trúc</span></div>
            <div class=\"stat\"><strong>4 tuần</strong><span>Lộ trình thực hành mỗi tập</span></div>
            <div class=\"stat\"><strong>1 file</strong><span>Dễ đọc, tìm kiếm, in/PDF</span></div>
          </div>
        </div>
      </section>
      <section class=\"overview\">
        <div class=\"section-title\">
          <h2>Bản đồ học tập</h2>
          <p>Chọn một Chương hoặc một tập để bắt đầu. {len(chapters)} tập được sắp xếp theo 9 Chương: từ nền tảng cá nhân, lãnh đạo, não bộ, hệ thống, tầng sâu đến xã hội, gia đình, tổ chức và bản đồ tích hợp.</p>
        </div>
        <div class=\"theme-stack\" id=\"cardGrid\">{overview_cards}</div>
        <div class=\"no-results\" id=\"noResults\">Không tìm thấy nội dung phù hợp.</div>
      </section>
      {chapter_html}
      <footer>Thiết kế để học sâu: đọc một tập, ghi một insight, áp dụng một hành vi nhỏ.</footer>
    </main>
  </div>
  <script>
    const total = {len(chapters)};
    const completed = new Set(JSON.parse(localStorage.getItem('curriculumCompleted') || '[]'));
    const navItems = [...document.querySelectorAll('.nav-item')];
    const cards = [...document.querySelectorAll('.chapter-card')];
    const buttons = [...document.querySelectorAll('.complete-btn')];
    const chapters = [...document.querySelectorAll('.chapter')];
    const themeSections = [...document.querySelectorAll('.theme-section')];
    const navSections = [...document.querySelectorAll('.nav-section')];
    const search = document.getElementById('search');
    const progressText = document.getElementById('progressText');
    const meterFill = document.getElementById('meterFill');
    const topProgress = document.getElementById('topProgress');

    function saveProgress() {{
      localStorage.setItem('curriculumCompleted', JSON.stringify([...completed]));
      const pct = completed.size / total * 100;
      meterFill.style.width = pct + '%';
      progressText.textContent = `${{completed.size}}/${{total}} tập đã học`;
      navItems.forEach(item => item.classList.toggle('done', completed.has(item.dataset.chapter)));
      buttons.forEach(btn => {{
        const isDone = completed.has(btn.dataset.complete);
        btn.classList.toggle('done', isDone);
        btn.textContent = isDone ? 'Đã học xong' : 'Đánh dấu đã học';
      }});
    }}

    buttons.forEach(btn => btn.addEventListener('click', () => {{
      const id = btn.dataset.complete;
      completed.has(id) ? completed.delete(id) : completed.add(id);
      saveProgress();
    }}));

    search.addEventListener('input', () => {{
      const q = search.value.trim().toLowerCase();
      let visible = 0;
      navItems.forEach(item => {{
        const show = !q || item.dataset.title.includes(q);
        item.style.display = show ? '' : 'none';
      }});
      navSections.forEach(section => {{
        const hasVisibleItem = [...section.querySelectorAll('.nav-item')]
          .some(item => item.style.display !== 'none');
        section.style.display = hasVisibleItem ? '' : 'none';
      }});
      cards.forEach(card => {{
        const show = !q || card.dataset.cardTitle.includes(q);
        card.style.display = show ? '' : 'none';
        if (show) visible++;
      }});
      themeSections.forEach(section => {{
        const hasVisibleCard = [...section.querySelectorAll('.chapter-card')]
          .some(card => card.style.display !== 'none');
        section.style.display = hasVisibleCard ? '' : 'none';
      }});
      document.getElementById('noResults').style.display = visible ? 'none' : 'block';
    }});

    function showChapter(hash, shouldScroll = true) {{
      const requested = /^#tap-\\d+$/.test(hash || '') ? hash : '#tap-1';
      const target = document.querySelector(requested) || document.querySelector('#tap-1');
      chapters.forEach(chapter => chapter.classList.toggle('active-chapter', chapter === target));
      navItems.forEach(item => item.classList.toggle('active', item.getAttribute('href') === '#' + target.id));
      document.title = `${{target.querySelector('.chapter-hero h1').textContent}} | Giáo Trình Tâm Lý Học 50 Tập`;
      if (shouldScroll) {{
        target.scrollIntoView({{ block: 'start' }});
      }}
    }}

    function openChapter(event) {{
      const link = event.currentTarget;
      const href = link.getAttribute('href');
      if (!href || !href.startsWith('#tap-')) return;
      event.preventDefault();
      if (location.hash !== href) {{
        history.pushState(null, '', href);
      }}
      showChapter(href, true);
    }}

    navItems.forEach(item => item.addEventListener('click', openChapter));
    cards.forEach(card => card.addEventListener('click', openChapter));
    window.addEventListener('hashchange', () => showChapter(location.hash, true));

    window.addEventListener('scroll', () => {{
      const max = document.documentElement.scrollHeight - innerHeight;
      const pct = max > 0 ? scrollY / max : 0;
      topProgress.style.transform = `scaleX(${{pct}})`;
    }});

    saveProgress();
    showChapter(location.hash || '#tap-1', false);
  </script>
</body>
</html>"""

    OUTPUT.write_text(html_doc, encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    print(f"Chapters: {len(chapters)}")


if __name__ == "__main__":
    main()

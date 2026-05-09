from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Giao-trinh-tam-ly-hoc-60-tap.html"


GROUPS = [
    ("Nền Tảng Cá Nhân", "Bản đồ gốc, cảm xúc, quyết định và thói quen cá nhân.", range(1, 5)),
    ("Lãnh Đạo, Giao Tiếp Và Dùng Người", "Quyền lực, thuyết phục, nhân sự, quan hệ, tiền bạc và trưởng thành nội tâm.", range(5, 11)),
    ("Não Bộ, Phát Triển Và Hành Vi", "Neuroscience, tuổi thơ, lâm sàng, thiết kế thay đổi và kinh tế học hành vi.", range(11, 16)),
    ("Hệ Thống, Văn Hóa Và Đạo Đức", "Tổ chức, văn hóa Á Đông, coaching, nhóm, đạo đức và trách nhiệm khi tác động đến con người.", range(16, 21)),
    ("Các Tầng Sâu Của Con Người", "Tiến hóa, đo lường, học tập, đạo đức nội tâm, xã hội, ý nghĩa, công nghệ, sang chấn và đọc nghiên cứu.", range(21, 31)),
    ("Vô Thức, Thân Mật Và Nửa Sau Cuộc Đời", "Động cơ ẩn, tự ái, thao túng, tình yêu, giới, khủng hoảng, sáng tạo, bản sắc, trung niên và tâm linh.", range(31, 41)),
    ("Xã Hội, Luật Pháp Và Sức Khỏe", "Ý thức hệ, tâm-thân, pháp lý, tội phạm và điều kiện xã hội tác động lên con người.", range(41, 44)),
    ("Hiệu Suất, Biểu Tượng Và Không Gian", "Hiệu suất đỉnh cao, nghệ thuật, câu chuyện, biểu tượng và môi trường sống.", range(44, 47)),
    ("Cộng Đồng, Gia Đình, Tổ Chức Và Tích Hợp", "Chữa lành tập thể, giáo dục gia đình, tổ chức nâng cao và bản đồ tích hợp.", range(47, 51)),
    ("Nền Tảng Khoa Học Và Ứng Dụng Mở Rộng", "Đại cương, nhận thức nâng cao, động cơ, tham vấn, học đường, tiêu dùng, UX, truyền thông, tích cực và thực nghiệm.", range(51, 61)),
]


COMMON_REFERENCES = [
    ("APA Psychology Topics", "Bản đồ chủ đề chính thức của American Psychological Association.", "https://www.apa.org/topics/"),
    ("OpenStax Psychology 2e", "Sách nhập môn tâm lý học mở, có cấu trúc đại học.", "https://openstax.org/books/psychology-2e/pages/index"),
    ("Noba Project - Introduction to Psychology", "Kho học liệu mở do các học giả tâm lý học biên soạn.", "https://nobaproject.com/textbooks/introduction-to-psychology-the-full-noba-collection"),
    ("MIT OpenCourseWare - Introduction to Psychology", "Khóa nhập môn tâm lý học miễn phí từ MIT OCW.", "https://ocw.mit.edu/courses/9-00-introduction-to-psychology-fall-2004/"),
]


REFERENCE_THEMES = {
    "learning": [
        ("Learning How to Learn - Coursera", "Khóa học phổ biến về cách học, trí nhớ và luyện tập.", "https://www.coursera.org/learn/learning-how-to-learn"),
    ],
    "social": [
        ("Social Psychology - Coursera/Wesleyan", "Khóa học về ảnh hưởng xã hội, thuyết phục và hành vi nhóm.", "https://www.coursera.org/learn/social-psychology"),
    ],
    "behavior": [
        ("Designing for Behavior Change - Google Books", "Sách ứng dụng behavioral science vào thiết kế sản phẩm và thay đổi hành vi.", "https://books.google.com/books/about/Designing_for_Behavior_Change.html?id=nu_pDwAAQBAJ"),
    ],
    "ux": [
        ("The Design of Everyday Things - Google Books", "Sách nền về cognitive design, affordance, feedback và lỗi người dùng.", "https://books.google.com/books/about/The_Design_of_Everyday_Things.html?id=nVQPAAAAQBAJ"),
    ],
    "marketing": [
        ("Influence: The Psychology of Persuasion - Google Books", "Sách kinh điển về thuyết phục và ảnh hưởng xã hội.", "https://books.google.com/books/about/Influence.html?id=5dfv0HJ1TEoC"),
    ],
    "science": [
        ("APA Dictionary of Psychology", "Từ điển thuật ngữ tâm lý học của APA.", "https://dictionary.apa.org/"),
        ("APA PsycInfo", "Cơ sở dữ liệu học thuật chuyên ngành tâm lý học.", "https://www.apa.org/pubs/databases/psycinfo"),
    ],
}


CHAPTER_REFERENCE_THEMES = {
    **{n: ["learning", "science"] for n in [1, 3, 22, 23, 29, 51, 52, 60]},
    **{n: ["behavior", "marketing"] for n in [4, 6, 14, 15, 27, 33, 41, 56, 58]},
    **{n: ["social", "science"] for n in [5, 7, 8, 16, 17, 18, 19, 20, 24, 25, 34, 35, 47, 48, 49, 54, 55]},
    **{n: ["ux", "behavior"] for n in [27, 46, 57]},
    **{n: ["learning", "behavior"] for n in [11, 12, 13, 21, 28, 42, 43, 44, 53, 59]},
}


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
    escaped = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener">\1</a>',
        escaped,
    )
    return escaped


def chapter_references(number: int) -> str:
    refs = list(COMMON_REFERENCES)
    for theme in CHAPTER_REFERENCE_THEMES.get(number, ["science"]):
        refs.extend(REFERENCE_THEMES.get(theme, []))

    seen = set()
    items = []
    for title, desc, url in refs:
        if url in seen:
            continue
        seen.add(url)
        items.append(
            "<a class=\"reference-link\" target=\"_blank\" rel=\"noopener\" "
            f"href=\"{html.escape(url)}\">"
            f"<strong>{html.escape(title)}</strong>"
            f"<span>{html.escape(desc)}</span>"
            "</a>"
        )

    return (
        "<section class=\"reference-card\">"
        "<div><span>Nguồn kiểm chứng</span><h2>Tài Liệu Tham Khảo, Sách Và Khóa Học</h2>"
        "<p>Các link này là nguồn nền để đối chiếu khái niệm, thuật ngữ và hướng học tiếp. "
        "Nội dung giáo trình là bản diễn giải thực dụng, không thay thế đào tạo/hành nghề chuyên môn.</p></div>"
        f"<div class=\"reference-grid\">{''.join(items)}</div>"
        "<p class=\"reference-note\">Cập nhật kiểm tra link: 07/05/2026.</p>"
        "</section>"
    )


def extract_final_sentence(md: str) -> str:
    blockquotes = [
        line.lstrip(">").strip()
        for line in md.splitlines()
        if line.strip().startswith(">")
    ]
    if blockquotes:
        return blockquotes[-1]

    for line in md.splitlines():
        stripped = line.strip()
        if stripped.startswith("**Một câu cần nhớ:**"):
            return stripped.replace("**Một câu cần nhớ:**", "").strip()
    return "Hiểu đúng bản chất, chọn một hành vi nhỏ để áp dụng và đo lại trong đời sống thật."


def extract_application_questions(md: str, title: str) -> list[str]:
    questions: list[str] = []
    seen = set()
    topic = re.sub(r"^Tập\s+\d+:\s*", "", title).strip()
    cleaned = re.sub(r"\[[^\]]+\]\([^)]+\)", "", md)

    candidates: list[str] = []
    for raw_line in cleaned.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(("#", "```", "---")):
            continue
        parts = [cell.strip() for cell in line.strip("|").split("|")] if "|" in line else [line]
        for part in parts:
            if "?" not in part:
                continue
            for match in re.finditer(r"([^?]{10,150}\?)", part):
                candidate = match.group(1)
                candidate = re.sub(r"^[\s\-*>\d.]+", "", candidate).strip()
                candidate = re.sub(r"\*\*|`|###?", "", candidate).strip()
                candidate = candidate.strip("| ").strip()
                if candidate:
                    candidates.append(candidate)

    for question in candidates:
        if question in seen:
            continue
        lowered = question.lower()
        if lowered.startswith(("http", "www", "vì sao c-level", "first principles")):
            continue
        if question.startswith(("#", "##")) or "##" in question:
            continue
        if len(question) < 16:
            continue
        seen.add(question)
        questions.append(question)
        if len(questions) >= 4:
            break

    fallback = [
        f"Trong tuần này, tình huống nào liên quan trực tiếp đến {topic}?",
        "Trong bản thân tôi, cảm xúc, hành vi hoặc quyết định nào đang lặp lại?",
        "Trong công việc hoặc đội nhóm, chủ đề này đang xuất hiện ở đâu?",
        "Tôi đang có giả định nào cần kiểm chứng bằng dữ kiện thay vì cảm giác?",
        "Một câu hỏi, ranh giới hoặc hành vi nhỏ nào tôi có thể thử trong 7 ngày tới?",
        "Ai sẽ được lợi nếu tôi áp dụng tốt bài học này?",
        "Nếu áp dụng sai, rủi ro đạo đức, quan hệ hoặc hệ thống là gì?",
        "Tôi sẽ đo sự thay đổi bằng dấu hiệu cụ thể nào?",
    ]
    for question in fallback:
        if len(questions) >= 8:
            break
        if question not in seen:
            questions.append(question)
            seen.add(question)

    return questions


def chapter_learning_card(chapter: dict) -> str:
    title = display_title(chapter["title"], chapter["number"])
    final = chapter["final"]
    questions = chapter["questions"]
    summary_items = [
        ("Bản chất", chapter["subtitle"] or "Nắm bản chất trước khi áp dụng kỹ thuật."),
        ("Cần nhớ", final),
        ("Áp dụng", "Chọn một tình huống thật, viết lại bằng khái niệm của tập này, rồi thử một hành vi nhỏ."),
        ("Kiểm chứng", "Quan sát dữ kiện trước-sau thay vì chỉ dựa vào cảm giác hiểu bài."),
    ]
    summary_html = "".join(
        "<div class=\"summary-tile\">"
        f"<span>{html.escape(label)}</span>"
        f"<p>{html.escape(text)}</p>"
        "</div>"
        for label, text in summary_items
    )
    question_html = "".join(
        "<li>"
        f"<span>{index:02d}</span>"
        f"<p>{html.escape(question)}</p>"
        "</li>"
        for index, question in enumerate(questions, 1)
    )
    return (
        "<section class=\"learning-card\">"
        "<div class=\"learning-head\">"
        f"<span>Tóm tắt ứng dụng - Tập {chapter['number']:02d}</span>"
        f"<h2>{html.escape(title)}</h2>"
        "<p>Đọc phần này trước để có khung nhớ nhanh, sau đó dùng câu hỏi ứng dụng để nối bài học với đời sống thật.</p>"
        "</div>"
        f"<div class=\"summary-grid\">{summary_html}</div>"
        "<div class=\"application-questions\">"
        "<h3>5-10 câu hỏi ứng dụng</h3>"
        f"<ol>{question_html}</ol>"
        "</div>"
        "</section>"
    )


def chapter_reader_card(chapter: dict) -> str:
    return (
        "<div class=\"reader-card\" data-reader-card>"
        "<div class=\"reader-head\">"
        "<div>"
        "<span>Giọng đọc tiếng Việt</span>"
        f"<h2>Nghe toàn bộ Tập {chapter['number']:02d}</h2>"
        "<p>Phát từ đầu bài, gồm phần tóm tắt ứng dụng và nội dung chính của tập.</p>"
        "</div>"
        "<div class=\"reader-status\" data-reader-status>Chưa phát</div>"
        "</div>"
        "<div class=\"reader-controls\">"
        f"<button class=\"reader-btn reader-primary\" type=\"button\" data-reader-action=\"play\" data-reader-target=\"tap-{chapter['number']}\">▶ Đọc bài</button>"
        f"<button class=\"reader-btn\" type=\"button\" data-reader-action=\"pause\" data-reader-target=\"tap-{chapter['number']}\" disabled>⏸ Tạm dừng</button>"
        f"<button class=\"reader-btn\" type=\"button\" data-reader-action=\"stop\" data-reader-target=\"tap-{chapter['number']}\" disabled>■ Dừng</button>"
        "<div class=\"reader-voice-lock\">"
        "<span>Giọng cố định</span>"
        "<strong data-reader-voice-name>Đang kiểm tra giọng vi-VN</strong>"
        "</div>"
        "<label class=\"reader-select-wrap reader-rate-wrap\">"
        "<span>Tốc độ</span>"
        "<select class=\"reader-select\" data-reader-rate aria-label=\"Chọn tốc độ đọc\">"
        "<option value=\"0.85\">0.85x</option>"
        "<option value=\"1\" selected>1x</option>"
        "<option value=\"1.15\">1.15x</option>"
        "<option value=\"1.3\">1.3x</option>"
        "<option value=\"1.5\">1.5x</option>"
        "</select>"
        "</label>"
        "</div>"
        "<div class=\"reader-progress\"><span data-reader-progress></span></div>"
        "</div>"
    )


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
                "final": extract_final_sentence(md),
                "questions": extract_application_questions(md, title),
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
    nav_items = (
        "<a class=\"nav-item home-link active\" href=\"#home\" data-chapter=\"home\" "
        "data-title=\"trang chủ giới thiệu tổng quan tâm lý học ứng dụng cấu trúc lộ trình\">"
        "<span>⌂</span><strong>Trang Chủ & Tổng Quan</strong></a>"
        + "\n"
        + "\n".join(nav_sections)
    )

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
        f"{chapter_reader_card(c)}"
        f"<button class=\"complete-btn\" data-complete=\"{c['number']}\">Đánh dấu đã học</button></div>"
        f"{chapter_learning_card(c)}"
        f"<div class=\"chapter-body\">{c['content']}</div>"
        f"{chapter_references(c['number'])}"
        "</article>"
        for c in chapters
    )

    html_doc = f"""<!doctype html>
<html lang=\"vi\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>Giáo Trình Tâm Lý Học 60 Tập</title>
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
    .home-view.is-hidden {{ display: none; }}
    .intro-band {{ padding: 58px 6vw 18px; }}
    .intro-shell {{ max-width: 1280px; margin: 0 auto; display: grid; gap: 18px; }}
    .intro-panel {{
      background: rgba(255,255,255,.78); border: 1px solid var(--line); border-radius: 32px;
      padding: clamp(24px,4vw,46px); box-shadow: 0 18px 58px rgba(0,0,0,.06);
    }}
    .intro-panel h2 {{ margin: 0; font-size: clamp(34px,5vw,68px); line-height: .98; letter-spacing: -0.025em; }}
    .intro-panel > p {{ max-width: 880px; color: #424245; font-size: clamp(18px,2vw,24px); line-height: 1.45; }}
    .principle-grid, .path-grid, .structure-grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap: 14px;
    }}
    .principle-card, .path-card, .structure-card {{
      background: #fff; border: 1px solid var(--line); border-radius: 22px; padding: 20px;
      box-shadow: 0 12px 34px rgba(0,0,0,.045);
    }}
    .principle-card span, .path-card span, .structure-card span {{
      color: var(--blue); font-size: 12px; font-weight: 900; text-transform: uppercase;
    }}
    .principle-card h3, .path-card h3, .structure-card h3 {{ margin: 8px 0; font-size: 22px; letter-spacing: -0.01em; }}
    .principle-card p, .path-card p, .structure-card p {{ margin: 0; color: var(--muted); line-height: 1.5; }}
    .path-card {{ display: grid; gap: 10px; align-content: start; }}
    .path-card a {{
      justify-self: start; display: inline-flex; align-items: center; min-height: 36px; padding: 8px 12px;
      border-radius: 999px; background: #1d1d1f; color: #fff; font-size: 13px; font-weight: 800;
    }}
    .learning-card {{
      background: #fff; border: 1px solid var(--line); border-radius: 28px;
      padding: clamp(22px,4vw,42px); margin: 0 0 28px; box-shadow: 0 12px 38px rgba(0,0,0,.05);
    }}
    .learning-head span {{
      color: var(--blue); font-size: 12px; font-weight: 900; text-transform: uppercase;
    }}
    .learning-head h2 {{ margin: 8px 0; font-size: clamp(28px,3.4vw,46px); line-height: 1.04; letter-spacing: -0.02em; }}
    .learning-head p {{ margin: 0; color: var(--muted); font-size: 16px; line-height: 1.5; max-width: 820px; }}
    .summary-grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap: 12px; margin: 20px 0;
    }}
    .summary-tile {{
      border: 1px solid rgba(0,0,0,.07); border-radius: 18px; padding: 16px;
      background: linear-gradient(180deg, #fbfdff, #f7f9fb);
    }}
    .summary-tile span {{ color: var(--blue); font-size: 12px; font-weight: 900; }}
    .summary-tile p {{ margin: 8px 0 0; color: #2f2f32; line-height: 1.5; font-size: 15px; }}
    .application-questions {{
      border-radius: 22px; padding: 18px; background: linear-gradient(135deg, rgba(0,113,227,.08), rgba(48,209,88,.07));
      border: 1px solid rgba(0,113,227,.13);
    }}
    .application-questions h3 {{ margin: 0 0 12px; font-size: 22px; }}
    .application-questions ol {{ display: grid; gap: 10px; margin: 0; padding: 0; list-style: none; }}
    .application-questions li {{
      display: grid; grid-template-columns: 38px minmax(0,1fr); gap: 12px; align-items: start;
      padding: 12px; border-radius: 15px; background: rgba(255,255,255,.82); border: 1px solid rgba(0,0,0,.055);
    }}
    .application-questions li span {{
      width: 34px; height: 30px; display: grid; place-items: center; border-radius: 10px;
      background: #1d1d1f; color: #fff; font-size: 12px; font-weight: 900;
    }}
    .application-questions li p {{ margin: 2px 0 0; color: #1d1d1f; line-height: 1.45; font-weight: 650; }}
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
    .reader-card {{
      margin: 26px 0 18px; padding: clamp(16px,3vw,22px); border-radius: 24px;
      background: rgba(255,255,255,.82); border: 1px solid rgba(0,113,227,.16);
      box-shadow: 0 14px 38px rgba(0,0,0,.055), inset 0 1px 0 rgba(255,255,255,.92);
    }}
    .reader-head {{
      display: grid; grid-template-columns: minmax(0,1fr) auto; align-items: start; gap: 16px;
      margin-bottom: 16px;
    }}
    .reader-head span {{
      color: var(--blue); font-size: 12px; font-weight: 900; text-transform: uppercase;
    }}
    .reader-head h2 {{
      margin: 6px 0 4px; font-size: clamp(22px,2.6vw,32px); line-height: 1.08; letter-spacing: -0.01em;
    }}
    .reader-head p {{ margin: 0; max-width: 680px; color: var(--muted); font-size: 15px; line-height: 1.45; }}
    .reader-status {{
      min-width: 120px; min-height: 34px; display: grid; place-items: center; padding: 8px 11px;
      border-radius: 999px; background: #f5f5f7; border: 1px solid var(--line);
      color: #424245; font-size: 12px; font-weight: 800; text-align: center;
    }}
    .reader-status.is-playing {{ background: rgba(0,113,227,.10); color: var(--blue); border-color: rgba(0,113,227,.20); }}
    .reader-status.is-paused {{ background: #fff8e5; color: #946200; border-color: rgba(148,98,0,.18); }}
    .reader-controls {{
      display: grid; grid-template-columns: repeat(3, max-content) minmax(180px,1fr) 130px; gap: 10px;
      align-items: end;
    }}
    .reader-btn {{
      min-height: 42px; border: 1px solid rgba(0,0,0,.10); border-radius: 14px;
      background: #fff; color: #1d1d1f; padding: 10px 13px; font-size: 14px; font-weight: 800;
      cursor: pointer; white-space: nowrap;
    }}
    .reader-btn:hover:not(:disabled) {{ border-color: rgba(0,113,227,.38); color: var(--blue); }}
    .reader-btn:disabled {{ cursor: not-allowed; color: #a1a1a6; background: #f5f5f7; }}
    .reader-primary {{ background: #1d1d1f; color: #fff; border-color: #1d1d1f; }}
    .reader-primary:hover:not(:disabled) {{ color: #fff; background: #000; }}
    .reader-select-wrap, .reader-voice-lock {{ display: grid; gap: 5px; min-width: 0; }}
    .reader-select-wrap span {{ color: var(--muted); font-size: 11px; font-weight: 900; text-transform: uppercase; }}
    .reader-voice-lock span {{ color: var(--muted); font-size: 11px; font-weight: 900; text-transform: uppercase; }}
    .reader-voice-lock strong {{
      min-height: 42px; display: flex; align-items: center; border: 1px solid rgba(0,0,0,.10);
      border-radius: 14px; background: #fff; color: #1d1d1f; padding: 9px 11px;
      font-size: 14px; line-height: 1.2; overflow-wrap: anywhere;
    }}
    .reader-select {{
      width: 100%; min-height: 42px; border: 1px solid rgba(0,0,0,.10); border-radius: 14px;
      background: #fff; color: #1d1d1f; padding: 9px 11px; font-size: 14px; outline: none;
    }}
    .reader-progress {{
      height: 7px; border-radius: 999px; background: #e8e8ed; overflow: hidden; margin-top: 14px;
    }}
    .reader-progress span {{
      display: block; height: 100%; width: 0; border-radius: inherit;
      background: linear-gradient(90deg, var(--blue), var(--green)); transition: width .2s ease;
    }}
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
    .reference-card {{
      background: #fff; border: 1px solid var(--line); border-radius: 28px;
      padding: clamp(22px,4vw,42px); box-shadow: 0 12px 38px rgba(0,0,0,.05);
      margin: 28px 0 0;
    }}
    .reference-card > div:first-child span {{
      color: var(--blue); font-size: 12px; font-weight: 900; text-transform: uppercase;
    }}
    .reference-card h2 {{
      margin: 8px 0 8px; font-size: clamp(26px,3vw,40px); line-height: 1.08; letter-spacing: -0.02em;
    }}
    .reference-card p {{ color: var(--muted); font-size: 16px; line-height: 1.55; max-width: 840px; }}
    .reference-grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(230px,1fr)); gap: 12px; margin-top: 18px;
    }}
    .reference-link {{
      display: grid; gap: 8px; align-content: start; min-height: 124px; padding: 16px;
      border-radius: 18px; background: linear-gradient(180deg, #fbfdff, #f6f8fb);
      border: 1px solid rgba(0,0,0,.075); transition: transform .18s ease, border-color .18s ease;
    }}
    .reference-link:hover {{ transform: translateY(-2px); border-color: rgba(0,113,227,.32); }}
    .reference-link strong {{ color: #1d1d1f; font-size: 16px; line-height: 1.25; }}
    .reference-link span {{ color: var(--muted); font-size: 13px; line-height: 1.4; }}
    .reference-note {{ margin-bottom: 0; font-size: 13px !important; }}
    hr {{ border: 0; border-top: 1px solid var(--line); margin: 38px 0; }}
    .anchor:hover {{ color: var(--blue); }}
    .no-results {{ display: none; text-align: center; padding: 34px; color: var(--muted); }}
    footer {{ padding: 42px 6vw 70px; text-align: center; color: var(--muted); }}
    @media (max-width: 980px) {{
      .app {{ display: block; }}
      aside {{ position: relative; height: auto; max-height: 70vh; }}
      .hero {{ min-height: auto; padding-top: 46px; }}
      .hero-stats {{ grid-template-columns: 1fr; }}
      .reader-head {{ grid-template-columns: 1fr; }}
      .reader-status {{ justify-self: start; }}
      .reader-controls {{ grid-template-columns: 1fr 1fr; }}
      .reader-primary, .reader-select-wrap, .reader-voice-lock {{ grid-column: 1 / -1; }}
    }}
    @media print {{
      aside, .complete-btn, .reader-card, .top-progress, .overview {{ display: none !important; }}
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
      <div class=\"home-view\" id=\"homeView\">
        <section class=\"hero\" id=\"home\">
          <div class=\"hero-inner\">
            <p class=\"eyebrow\">Trang chủ giáo trình tâm lý học ứng dụng</p>
            <h1>Hiểu tâm lý học để hiểu người, hiểu mình và hành động đúng hơn.</h1>
            <p class=\"lead\">Tâm lý học là khoa học giúp ta đọc các tầng của con người: não bộ, cảm xúc, nhận thức, động cơ, thói quen, quan hệ, văn hóa, tổ chức, xã hội và ý nghĩa. Giáo trình này biến bản đồ rộng đó thành 60 bài học ngắn gọn, trực quan và có thể áp dụng ngay.</p>
            <div class=\"hero-stats\">
              <div class=\"stat\"><strong>{len(chapters)}</strong><span>Tập học có cấu trúc</span></div>
              <div class=\"stat\"><strong>{len(GROUPS)}</strong><span>Chương lớn để chọn theo mục tiêu</span></div>
              <div class=\"stat\"><strong>1 hành vi</strong><span>Áp dụng nhỏ sau mỗi bài</span></div>
            </div>
          </div>
        </section>
        <section class=\"intro-band\">
          <div class=\"intro-shell\">
            <div class=\"intro-panel\">
              <h2>Giá trị cốt lõi của giáo trình</h2>
              <p>Không học tâm lý để gắn nhãn người khác. Học để nhìn đúng tầng vấn đề, bớt phản ứng tự động, thiết kế môi trường tốt hơn, giao tiếp rõ hơn, lãnh đạo có trách nhiệm hơn và sống sâu hơn.</p>
              <div class=\"principle-grid\">
                <div class=\"principle-card\"><span>01</span><h3>Hiểu bản chất</h3><p>Mỗi bài bắt đầu từ first principles: con người đang cần gì, sợ gì, tin gì và hệ thống đang thưởng điều gì.</p></div>
                <div class=\"principle-card\"><span>02</span><h3>Dễ áp dụng</h3><p>Mỗi bài có công cụ, câu hỏi và lộ trình 4 tuần để chuyển hiểu biết thành hành vi cụ thể.</p></div>
                <div class=\"principle-card\"><span>03</span><h3>Có kiểm chứng</h3><p>Mỗi tập có nguồn tham khảo, sách hoặc khóa học nền để người đọc học sâu và đối chiếu thuật ngữ.</p></div>
                <div class=\"principle-card\"><span>04</span><h3>Có đạo đức</h3><p>Hiểu tâm lý phải làm con người rõ hơn và tự chủ hơn, không phải để thao túng hoặc kiểm soát.</p></div>
              </div>
            </div>
            <div class=\"intro-panel\">
              <h2>Chọn lộ trình theo mục tiêu</h2>
              <p>Không cần đọc tuần tự nếu bạn có một mục tiêu cụ thể. Hãy chọn đường vào phù hợp, rồi quay lại bản đồ tổng thể khi cần.</p>
              <div class=\"path-grid\">
                <div class=\"path-card\"><span>Bản thân</span><h3>Hiểu mình và tự điều chỉnh</h3><p>Tập 1-4, 10, 31, 38, 59.</p><a href=\"#tap-1\">Bắt đầu</a></div>
                <div class=\"path-card\"><span>Lãnh đạo</span><h3>Dùng người, giao tiếp, văn hóa</h3><p>Tập 5-7, 16, 19, 36, 49.</p><a href=\"#tap-5\">Bắt đầu</a></div>
                <div class=\"path-card\"><span>Gia đình</span><h3>Quan hệ, con cái, tuổi thiếu niên</h3><p>Tập 8, 12, 34, 48, 55.</p><a href=\"#tap-8\">Bắt đầu</a></div>
                <div class=\"path-card\"><span>Sản phẩm</span><h3>Hành vi, UX, AI, marketing</h3><p>Tập 14, 27, 56, 57, 58.</p><a href=\"#tap-14\">Bắt đầu</a></div>
                <div class=\"path-card\"><span>Khoa học</span><h3>Đo lường, đọc nghiên cứu, kiểm chứng</h3><p>Tập 22, 29, 51, 52, 60.</p><a href=\"#tap-22\">Bắt đầu</a></div>
                <div class=\"path-card\"><span>Chiều sâu</span><h3>Ý nghĩa, vô thức, trung niên, tâm linh</h3><p>Tập 26, 31, 38, 39, 40, 50.</p><a href=\"#tap-26\">Bắt đầu</a></div>
              </div>
            </div>
            <div class=\"intro-panel\">
              <h2>Cách học để nhớ và dùng được</h2>
              <div class=\"structure-grid\">
                <div class=\"structure-card\"><span>Bước 1</span><h3>Đọc tóm tắt nhanh</h3><p>Nắm bản chất, câu cần nhớ và câu hỏi ứng dụng trước khi đọc chi tiết.</p></div>
                <div class=\"structure-card\"><span>Bước 2</span><h3>Gắn với một tình huống thật</h3><p>Chọn một người, một cuộc họp, một quyết định hoặc một thói quen đang diễn ra.</p></div>
                <div class=\"structure-card\"><span>Bước 3</span><h3>Viết một insight</h3><p>Không ghi nhiều. Chỉ ghi một điều làm bạn nhìn vấn đề khác đi.</p></div>
                <div class=\"structure-card\"><span>Bước 4</span><h3>Thử một hành vi nhỏ</h3><p>Đổi một câu hỏi, một ranh giới, một nhịp phản hồi hoặc một thiết kế môi trường.</p></div>
                <div class=\"structure-card\"><span>Bước 5</span><h3>Review sau 7 ngày</h3><p>Điều gì đổi? Điều gì không đổi? Tầng nào cần học tiếp?</p></div>
              </div>
            </div>
          </div>
        </section>
        <section class=\"overview\" id=\"learning-map\">
          <div class=\"section-title\">
            <h2>Bản đồ học tập</h2>
            <p>Chọn một Chương hoặc một tập để bắt đầu. {len(chapters)} tập được sắp xếp theo {len(GROUPS)} Chương: từ nền tảng cá nhân, lãnh đạo, não bộ, hệ thống, tầng sâu đến ứng dụng mở rộng, UX, truyền thông và tư duy khoa học.</p>
          </div>
          <div class=\"theme-stack\" id=\"cardGrid\">{overview_cards}</div>
          <div class=\"no-results\" id=\"noResults\">Không tìm thấy nội dung phù hợp.</div>
        </section>
      </div>
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
    const homeView = document.getElementById('homeView');
    const search = document.getElementById('search');
    const progressText = document.getElementById('progressText');
    const meterFill = document.getElementById('meterFill');
    const topProgress = document.getElementById('topProgress');
    const supportsSpeech = 'speechSynthesis' in window && 'SpeechSynthesisUtterance' in window;
    const readerCards = [...document.querySelectorAll('[data-reader-card]')];
    const readerRateSelects = [...document.querySelectorAll('[data-reader-rate]')];
    const readerButtons = [...document.querySelectorAll('[data-reader-action]')];
    let readerVoices = [];
    let lockedVietnameseVoice = null;
    let readerRunId = 0;
    let readerState = {{
      chapter: null,
      chunks: [],
      index: 0,
      status: 'idle',
      rate: 1,
      voice: null,
      stopRequested: false,
      runId: 0,
    }};

    function getReaderCard(chapter) {{
      return chapter ? chapter.querySelector('[data-reader-card]') : null;
    }}

    function setReaderStatus(card, text, mode = '') {{
      if (!card) return;
      const status = card.querySelector('[data-reader-status]');
      status.textContent = text;
      status.classList.toggle('is-playing', mode === 'playing');
      status.classList.toggle('is-paused', mode === 'paused');
    }}

    function setReaderProgress(card, pct) {{
      if (!card) return;
      const bar = card.querySelector('[data-reader-progress]');
      bar.style.width = Math.max(0, Math.min(100, pct)) + '%';
    }}

    function updateReaderControls() {{
      readerCards.forEach(card => {{
        const chapter = card.closest('.chapter');
        const isCurrent = chapter && readerState.chapter === chapter;
        const isPlaying = isCurrent && readerState.status === 'playing';
        const isPaused = isCurrent && readerState.status === 'paused';
        const hasVietnameseVoice = Boolean(selectedReaderVoice());
        card.querySelectorAll('[data-reader-action]').forEach(button => {{
          const action = button.dataset.readerAction;
          if (!supportsSpeech) {{
            button.disabled = true;
            return;
          }}
          if (action === 'play') {{
            button.disabled = !hasVietnameseVoice;
            button.textContent = isPaused ? '▶ Tiếp tục' : isPlaying ? '↻ Đọc lại' : '▶ Đọc bài';
          }}
          if (action === 'pause') {{
            button.disabled = !isPlaying && !isPaused;
            button.textContent = isPaused ? '▶ Tiếp tục' : '⏸ Tạm dừng';
          }}
          if (action === 'stop') {{
            button.disabled = !isPlaying && !isPaused;
          }}
        }});
      }});
    }}

    function isStrictVietnameseVoice(voice) {{
      return (voice?.lang || '').toLowerCase() === 'vi-vn';
    }}

    function rankVietnameseVoice(voice) {{
      const name = (voice.name || '').toLowerCase();
      if (name === 'linh') return 0;
      if (name.includes('linh')) return 1;
      if (name.includes('hoaimy') || name.includes('hoài') || name.includes('an')) return 2;
      return 3;
    }}

    function populateReaderVoices() {{
      readerVoices = supportsSpeech ? speechSynthesis.getVoices() : [];
      lockedVietnameseVoice = readerVoices
        .filter(isStrictVietnameseVoice)
        .sort((a, b) => rankVietnameseVoice(a) - rankVietnameseVoice(b))[0] || null;
      readerCards.forEach(card => {{
        const voiceName = card.querySelector('[data-reader-voice-name]');
        if (!supportsSpeech) {{
          voiceName.textContent = 'Trình duyệt không hỗ trợ đọc';
          setReaderStatus(card, 'Không hỗ trợ');
        }} else if (!readerVoices.length) {{
          voiceName.textContent = 'Đang tải giọng vi-VN';
          setReaderStatus(card, 'Đang tải giọng');
        }} else if (!lockedVietnameseVoice) {{
          voiceName.textContent = 'Không tìm thấy giọng vi-VN';
          setReaderStatus(card, 'Thiếu giọng Việt');
        }} else {{
          voiceName.textContent = `${{lockedVietnameseVoice.name}} (${{lockedVietnameseVoice.lang}})`;
          setReaderStatus(card, 'Sẵn sàng');
        }}
      }});
      updateReaderControls();
    }}

    function selectedReaderVoice() {{
      return lockedVietnameseVoice && isStrictVietnameseVoice(lockedVietnameseVoice) ? lockedVietnameseVoice : null;
    }}

    function selectedReaderRate(card) {{
      const select = card.querySelector('[data-reader-rate]');
      const rate = Number(select.value);
      return Number.isFinite(rate) ? rate : 1;
    }}

    function cleanReaderText(text) {{
      return text
        .replace(/\\s+/g, ' ')
        .replace(/([.!?])(?=\\S)/g, '$1 ')
        .trim();
    }}

    function splitReaderText(text, maxLength = 260) {{
      const sentences = cleanReaderText(text).match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [];
      const chunks = [];
      let current = '';
      sentences.forEach(sentence => {{
        const part = sentence.trim();
        if (!part) return;
        if ((current + ' ' + part).trim().length <= maxLength) {{
          current = (current + ' ' + part).trim();
          return;
        }}
        if (current) chunks.push(current);
        if (part.length <= maxLength) {{
          current = part;
          return;
        }}
        for (let i = 0; i < part.length; i += maxLength) {{
          chunks.push(part.slice(i, i + maxLength));
        }}
        current = '';
      }});
      if (current) chunks.push(current);
      return chunks;
    }}

    function collectReaderChunks(chapter) {{
      const selectors = [
        '.chapter-hero h1',
        '.chapter-hero > p',
        '.learning-head h2',
        '.learning-head > p',
        '.summary-tile p',
        '.application-questions li p',
        '.chapter-body h2',
        '.chapter-body h3',
        '.chapter-body p',
        '.chapter-body li',
        '.chapter-body blockquote',
        '.chapter-body th',
        '.chapter-body td',
        '.chapter-body .formula-card strong',
        '.chapter-body .formula-card span',
        '.chapter-body .flow-step strong',
      ];
      const segments = selectors
        .flatMap(selector => [...chapter.querySelectorAll(selector)])
        .map(element => cleanReaderText(element.textContent || ''))
        .filter(Boolean);
      return splitReaderText(segments.join('. '));
    }}

    function resetReaderCards(exceptCard = null) {{
      readerCards.forEach(card => {{
        if (card === exceptCard) return;
        setReaderProgress(card, 0);
        if (supportsSpeech && selectedReaderVoice()) setReaderStatus(card, 'Sẵn sàng');
      }});
    }}

    function stopReader(clearProgress = false) {{
      if (!supportsSpeech) return;
      readerRunId += 1;
      readerState.stopRequested = true;
      speechSynthesis.cancel();
      const card = getReaderCard(readerState.chapter);
      if (card) {{
        setReaderStatus(card, clearProgress ? 'Đã dừng' : 'Sẵn sàng');
        if (clearProgress) setReaderProgress(card, 0);
      }}
      readerState.status = 'idle';
      readerState.chapter = null;
      readerState.chunks = [];
      readerState.index = 0;
      readerState.runId = readerRunId;
      updateReaderControls();
    }}

    function speakNextReaderChunk(runId = readerState.runId) {{
      if (runId !== readerState.runId) return;
      if (!supportsSpeech || readerState.stopRequested || !readerState.chapter) return;
      const card = getReaderCard(readerState.chapter);
      if (readerState.index >= readerState.chunks.length) {{
        setReaderProgress(card, 100);
        setReaderStatus(card, 'Hoàn tất');
        readerState.status = 'idle';
        readerState.chapter = null;
        updateReaderControls();
        return;
      }}
      const utterance = new SpeechSynthesisUtterance(readerState.chunks[readerState.index]);
      if (!isStrictVietnameseVoice(readerState.voice)) {{
        setReaderStatus(card, 'Sai giọng đọc');
        stopReader(true);
        return;
      }}
      utterance.lang = 'vi-VN';
      utterance.rate = readerState.rate;
      utterance.pitch = 1;
      utterance.voice = readerState.voice;
      utterance.onstart = () => {{
        if (runId !== readerState.runId) return;
        const pct = readerState.chunks.length ? readerState.index / readerState.chunks.length * 100 : 0;
        setReaderProgress(card, pct);
        setReaderStatus(card, `Đang đọc ${{readerState.index + 1}}/${{readerState.chunks.length}}`, 'playing');
        updateReaderControls();
      }};
      utterance.onend = () => {{
        if (runId !== readerState.runId || readerState.stopRequested) return;
        readerState.index += 1;
        setReaderProgress(card, readerState.index / readerState.chunks.length * 100);
        speakNextReaderChunk(runId);
      }};
      utterance.onerror = () => {{
        if (runId !== readerState.runId || readerState.stopRequested) return;
        setReaderStatus(card, 'Lỗi giọng đọc');
        readerState.status = 'idle';
        updateReaderControls();
      }};
      speechSynthesis.speak(utterance);
    }}

    function playReader(chapter) {{
      if (!supportsSpeech) return;
      const card = getReaderCard(chapter);
      if (readerState.chapter === chapter && readerState.status === 'paused') {{
        speechSynthesis.resume();
        readerState.status = 'playing';
        setReaderStatus(card, `Đang đọc ${{readerState.index + 1}}/${{readerState.chunks.length}}`, 'playing');
        updateReaderControls();
        return;
      }}
      stopReader(false);
      const voice = selectedReaderVoice();
      if (!voice) {{
        setReaderStatus(card, 'Thiếu giọng Việt');
        updateReaderControls();
        return;
      }}
      const chunks = collectReaderChunks(chapter);
      if (!chunks.length) {{
        setReaderStatus(card, 'Không có nội dung');
        return;
      }}
      readerRunId += 1;
      readerState = {{
        chapter,
        chunks,
        index: 0,
        status: 'playing',
        rate: selectedReaderRate(card),
        voice,
        stopRequested: false,
        runId: readerRunId,
      }};
      resetReaderCards(card);
      setReaderProgress(card, 0);
      speakNextReaderChunk(readerState.runId);
    }}

    function pauseOrResumeReader(chapter) {{
      if (!supportsSpeech || readerState.chapter !== chapter) return;
      const card = getReaderCard(chapter);
      if (readerState.status === 'playing') {{
        speechSynthesis.pause();
        readerState.status = 'paused';
        setReaderStatus(card, 'Đã tạm dừng', 'paused');
      }} else if (readerState.status === 'paused') {{
        speechSynthesis.resume();
        readerState.status = 'playing';
        setReaderStatus(card, `Đang đọc ${{readerState.index + 1}}/${{readerState.chunks.length}}`, 'playing');
      }}
      updateReaderControls();
    }}

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

    readerButtons.forEach(button => button.addEventListener('click', () => {{
      const chapter = document.getElementById(button.dataset.readerTarget);
      if (!chapter) return;
      const action = button.dataset.readerAction;
      if (action === 'play') playReader(chapter);
      if (action === 'pause') pauseOrResumeReader(chapter);
      if (action === 'stop') stopReader(true);
    }}));

    readerRateSelects.forEach(select => select.addEventListener('change', () => {{
      const chapter = select.closest('.chapter');
      if (chapter && readerState.chapter === chapter) {{
        readerState.rate = selectedReaderRate(getReaderCard(chapter));
      }}
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

    function showHome(shouldScroll = true) {{
      if (readerState.chapter) stopReader(true);
      chapters.forEach(chapter => chapter.classList.remove('active-chapter'));
      homeView.classList.remove('is-hidden');
      navItems.forEach(item => item.classList.toggle('active', item.getAttribute('href') === '#home'));
      document.title = 'Giáo Trình Tâm Lý Học 60 Tập | Trang Chủ';
      if (shouldScroll) {{
        homeView.scrollIntoView({{ block: 'start' }});
      }}
    }}

    function showChapter(hash, shouldScroll = true) {{
      if (!/^#tap-\\d+$/.test(hash || '')) {{
        showHome(shouldScroll);
        return;
      }}
      const requested = hash;
      const target = document.querySelector(requested) || document.querySelector('#tap-1');
      if (readerState.chapter && readerState.chapter !== target) stopReader(true);
      homeView.classList.add('is-hidden');
      chapters.forEach(chapter => chapter.classList.toggle('active-chapter', chapter === target));
      navItems.forEach(item => item.classList.toggle('active', item.getAttribute('href') === '#' + target.id));
      document.title = `${{target.querySelector('.chapter-hero h1').textContent}} | Giáo Trình Tâm Lý Học 60 Tập`;
      if (shouldScroll) {{
        target.scrollIntoView({{ block: 'start' }});
      }}
    }}

    function openChapter(event) {{
      const link = event.currentTarget;
      const href = link.getAttribute('href');
      if (!href || (!href.startsWith('#tap-') && href !== '#home')) return;
      event.preventDefault();
      if (location.hash !== href) {{
        history.pushState(null, '', href);
      }}
      href === '#home' ? showHome(true) : showChapter(href, true);
    }}

    navItems.forEach(item => item.addEventListener('click', openChapter));
    cards.forEach(card => card.addEventListener('click', openChapter));
    document.querySelectorAll('.path-card a').forEach(link => link.addEventListener('click', openChapter));
    window.addEventListener('hashchange', () => showChapter(location.hash, true));

    window.addEventListener('scroll', () => {{
      const max = document.documentElement.scrollHeight - innerHeight;
      const pct = max > 0 ? scrollY / max : 0;
      topProgress.style.transform = `scaleX(${{pct}})`;
    }});

    saveProgress();
    populateReaderVoices();
    if (supportsSpeech) {{
      speechSynthesis.onvoiceschanged = populateReaderVoices;
      window.addEventListener('beforeunload', () => speechSynthesis.cancel());
    }}
    showChapter(location.hash || '#home', false);
  </script>
</body>
</html>"""

    OUTPUT.write_text(html_doc, encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    print(f"Chapters: {len(chapters)}")


if __name__ == "__main__":
    main()

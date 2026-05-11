# Giáo Trình Tâm Lý Học 60 Tập

Website học tập tiếng Việt về tâm lý học ứng dụng cho người trưởng thành, quản lý và C-level.

- GitHub Pages: https://anhbeva.github.io/tam-ly-hoc/
- File website chính: `index.html`
- Bản HTML đầy đủ: `Giao-trinh-tam-ly-hoc-60-tap.html`
- Nội dung nguồn: các file Markdown `Tap-*.md`
- Bảng thuật ngữ: `Thuat-ngu-tam-ly-hoc.md`
- Script build: `build_curriculum_html.py`

## Nội dung

- 60 tập tâm lý học ứng dụng, sắp xếp theo các chương lớn từ nền tảng cá nhân, lãnh đạo, não bộ, hệ thống, quan hệ, xã hội đến tư duy khoa học.
- Mỗi tập có tóm tắt ứng dụng, câu hỏi thực hành, bảng first principles và nguồn tham khảo.
- Phụ lục **Bảng Thuật Ngữ Cốt Lõi** gồm hơn 180 thuật ngữ quan trọng như hành vi, ego/cái tôi, quyền lực, niềm tin, lãnh đạo, ảnh hưởng, stress, sang chấn, thiên kiến, nhân quả và đo lường.

## GitHub Pages

Website được publish từ `index.html` trên nhánh `main`. Sau khi cập nhật nội dung, build lại HTML rồi push lên GitHub; GitHub Pages sẽ tự phục vụ bản mới tại URL ở trên.

## Cập nhật HTML

```bash
python3 build_curriculum_html.py
cp Giao-trinh-tam-ly-hoc-60-tap.html index.html
```

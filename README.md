# 日本語 学習 — Japanese Vocabulary

Ứng dụng học từ vựng tiếng Nhật với giao diện PyQt6 hiện đại, dark-theme.

## Cài đặt

```bash
pip install PyQt6
python main.py
```

## Tính năng

| Tab | Mô tả |
|-----|-------|
| 📚 Nhập liệu | Thêm / xoá từ vựng theo cấu trúc: Từ Nhật – Romaji/Hiragana – Nghĩa tiếng Việt |
| 🃏 Flashcard | Học qua thẻ ghi nhớ; nhấn thẻ để lật, duyệt tuần tự hoặc trộn thẻ |
| ✏️ Kiểm tra | Trắc nghiệm 4 đáp án, có hiển thị điểm số |
| 🤖 Hỏi đáp AI | Gia sư AI cá nhân hoá dùng Gemini API (cần API Key) |

## AI Chat

1. Lấy API Key miễn phí tại: https://aistudio.google.com/app/apikey
2. Nhập key vào ô "Gemini API Key" trong tab Hỏi đáp AI
3. Bắt đầu hỏi về tiếng Nhật!

Dữ liệu từ vựng được lưu tự động vào `vocab_data.json` cùng thư mục.

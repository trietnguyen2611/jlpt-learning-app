# JLPT Learning App✨

Ứng dụng học từ vựng tiếng Nhật dạng Desktop App, chạy trực tiếp trên macOS như một phần mềm độc lập (không cần mở trình duyệt). Tích hợp trợ lý AI Gemini giúp nâng cao hiệu quả ôn luyện JLPT.

---

## 🌟 Tính năng:

- 📚 **Quản lý từ vựng** — Thêm, xoá từ vựng trực quan. Dữ liệu lưu tự động vào file `vocab_data.json`.
- 🃏 **Flashcard** — Thẻ ghi nhớ lật 3D mượt mà, hỗ trợ trộn thẻ ngẫu nhiên và thanh tiến trình.
- ✏️ **Kiểm tra** — Tự động tạo câu hỏi 4 đáp án từ danh sách từ vựng cá nhân.
- 🤖 **Học với AI - Tính năng thử nghiệm** — Tích hợp **Gemini 2.0 Flash** giúp giải thích ngữ pháp, phân biệt từ vựng, dịch thuật.
- 🌓 **Dark / Light Mode** — Giao diện Liquid Glass sang trọng.

---

## 🛠️ Công nghệ:

| Thành phần | Chi tiết |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3 (Glassmorphism), Vanilla JS |
| Desktop | pywebview (cửa sổ native macOS) |
| AI | Google Gemini API (`gemini-2.0-flash`) |
| Đóng gói | PyInstaller |

---

## 🚀 Cài đặt & Chạy:

### 1. Clone dự án
```bash
git clone https://github.com/trietnguyen2611/jlpt-learning-app.git
cd jlpt-learning-app
```

### 2. Tạo môi trường ảo Conda (hoặc có thể chạy Base - tùy bạn) và cài thư viện
```bash
conda create -n jlpt python=3.13 -y
conda activate jlpt
pip install -r requirements.txt
```

> [!IMPORTANT]
> Thư viện cửa sổ desktop là **`pywebview`** (không phải `webview`). File `requirements.txt` đã khai báo đúng, chỉ cần chạy `pip install -r requirements.txt`.

### 3. Chạy ứng dụng
```bash
python app.py
```
Một cửa sổ phần mềm sẽ mở lên ngay trên màn hình — không cần mở trình duyệt.

---

## 🤖 Cấu hình mục Học với AI:

1. Tạo API Key miễn phí tại [Google AI Studio](https://aistudio.google.com/app/apikey) - lưu ý khi sử dụng API này sẽ mất phí.
2. Mở ứng dụng → tab **🤖 Học với AI** → dán API Key vào ô nhập liệu.
3. Bắt đầu đặt câu hỏi và trao đổi với AI.

---

## 📁 Cấu trúc dự án:

```
jlpt-learning-app/
├── app.py              # Server Flask + pywebview desktop window
├── requirements.txt    # flask, requests, pywebview
├── vocab_data.json     # Dữ liệu từ vựng (tự động tạo)
├── templates/
│   └── index.html      # Giao diện SPA (HTML + CSS + JS)
├── icon/
│   └── app.ico         # Icon ứng dụng (.ico - dành riêng cho Windows)
    └── app.png
    └── app.icns        # Icon ứng dụng (.icns - dành riêng cho macOS)
└── README.md
```

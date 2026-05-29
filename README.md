# JLPT Learning App 🇯🇵✨

Ứng dụng học từ vựng tiếng Nhật dạng Desktop App, chạy trực tiếp trên macOS như một phần mềm độc lập (không cần mở trình duyệt). Tích hợp trợ lý AI Gemini giúp nâng cao hiệu quả ôn luyện JLPT.

---

## 🌟 Tính năng:

- 📚 **Quản lý từ vựng** — Thêm, xoá từ vựng trực quan. Dữ liệu lưu tự động vào file `vocab_data.json`.
- 🃏 **Flashcard 3D** — Thẻ ghi nhớ lật 3D mượt mà, hỗ trợ trộn thẻ ngẫu nhiên và thanh tiến trình.
- ✏️ **Trắc nghiệm** — Tự động tạo câu hỏi 4 đáp án từ danh sách từ vựng cá nhân.
- 🤖 **Gia sư AI** — Tích hợp **Gemini 2.0 Flash** giúp giải thích ngữ pháp, phân biệt từ vựng, dịch thuật.
- 🌓 **Dark / Light Mode** — Giao diện Glassmorphism sang trọng, chuyển đổi chủ đề mượt mà.

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

### 2. Tạo môi trường ảo Conda và cài thư viện
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

## 📦 Đóng gói thành Desktop App:

Để tạo file chạy độc lập (không cần cài Python):

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --clean --add-data "templates:templates" --add-data "icon:icon" --icon "icon/app.ico" app.py
```

Kết quả nằm trong thư mục `dist/` — click đúp để chạy.

---

## 🤖 Cấu hình AI Chat:

1. Tạo API Key miễn phí tại [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Mở ứng dụng → tab **Hỏi đáp AI 🤖** → dán API Key vào ô nhập liệu.
3. Bắt đầu đặt câu hỏi!

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
│   └── app.ico         # Icon ứng dụng (ICO format)
└── README.md
```

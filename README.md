# JLPT Learning App 🇯🇵✨

Ứng dụng học từ vựng tiếng Nhật Single Page Application (SPA) hiện đại, trực quan và tích hợp trợ lý AI thông minh giúp nâng cao hiệu quả ôn luyện JLPT.

---

## 🌟 Tính năng nổi bật

- 📚 **Quản lý từ vựng thông minh (Vocabulary Management):** Thêm mới, xóa từ vựng trực quan. Toàn bộ dữ liệu được lưu trữ tự động và an toàn trong tệp JSON (`vocab_data.json`).
- 🃏 **Thẻ ghi nhớ Flashcard 3D:** Giao diện lật thẻ 3D mượt mà với hiệu ứng động cao cấp. Hỗ trợ trộn thẻ ngẫu nhiên, xem tuần tự và có thanh tiến trình trực quan.
- ✏️ **Trắc nghiệm ôn luyện (Quiz):** Tự động tạo câu hỏi trắc nghiệm 4 đáp án dựa trên danh sách từ vựng cá nhân, hiển thị điểm số và kết quả ngay lập tức.
- 🤖 **Gia sư AI cá nhân (AI Assistant):** Tích hợp mô hình ngôn ngữ lớn **Gemini 2.0 Flash** siêu tốc giúp giải thích ngữ pháp, phân biệt từ vựng, dịch thuật hoặc trò chuyện tiếng Nhật theo ngữ cảnh.
- 🌓 **Giao diện Glassmorphism Sang Trọng:** Thiết kế dạng "Floating Design" (giao diện nổi) hiện đại, hỗ trợ chuyển đổi chủ đề **Sáng (Light Mode) / Tối (Dark Mode)** cực mượt mà.

---

## 🛠️ Công nghệ sử dụng

- **Backend:** Python, Flask, Requests.
- **Frontend:** HTML5, CSS3 (Vanilla CSS với biến CSS, Glassmorphism, animations nâng cao), Vanilla JavaScript (Ajax, API interaction).
- **AI Integration:** Google Gemini API (`gemini-2.0-flash` model).

---

## 🚀 Hướng dẫn cài đặt & Chạy ứng dụng

Làm theo các bước đơn giản sau để chạy ứng dụng trên máy tính của bạn:

### 1. Tải dự án về máy
```bash
git clone https://github.com/trietnguyen2611/jlpt-learning-app.git
cd jlpt-learning-app
```

### 2. Cài đặt các thư viện cần thiết
Dự án chỉ sử dụng các thư viện gọn nhẹ là `Flask` và `requests`. Cài đặt bằng lệnh:
```bash
pip install -r requirements.txt
```

### 3. Khởi chạy ứng dụng
Chạy server local bằng file `app.py`:
```bash
python app.py
```

### 4. Truy cập giao diện web
Mở trình duyệt bất kỳ và truy cập địa chỉ sau:
```text
http://127.0.0.1:5000
```

---

## 🤖 Hướng dẫn cấu hình AI Chat

Để sử dụng tính năng **Gia sư AI cá nhân**:
1. Truy cập [Google AI Studio](https://aistudio.google.com/app/apikey) và tạo một API Key miễn phí.
2. Mở ứng dụng, chuyển sang tab **Hỏi đáp AI 🤖**.
3. Dán API Key của bạn vào ô nhập liệu ở đầu trang và bắt đầu đặt câu hỏi học tập (ví dụ: *"Giải thích cách dùng ngữ pháp N3 ～うちに"*).

---

## 📁 Cấu trúc thư mục dự án

```text
jlpt-learning-app/
│
├── app.py                # Server Flask xử lý API và lưu trữ dữ liệu
├── requirements.txt      # Danh sách thư viện phụ thuộc (Flask, requests)
├── vocab_data.json       # Cơ sở dữ liệu từ vựng cục bộ dạng JSON
├── README.md             # Tài liệu hướng dẫn dự án
│
└── templates/
    └── index.html        # Giao diện SPA chính (HTML, CSS Glassmorphism, JS Logic)
```

Chúc bạn học tốt tiếng Nhật! 頑張ってください！ 🎉

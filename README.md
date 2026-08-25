# JLPT Learning App – Japanese Vocabulary Desktop App with AI

A free **JLPT vocabulary learning app** for Windows and macOS. Learn Japanese words with flashcards, quizzes, and Google Gemini AI. No browser needed – it runs as a real desktop software.

Perfect for JLPT N5 to N1 students who want a simple, offline-friendly Japanese vocabulary trainer with AI help.

---

## 🌟 Key Features

- 📚 **Japanese Vocabulary Manager** — Add, edit, and delete words easily. All data saves automatically to `vocab_data.json`.
- 🃏 **3D Flashcards** — Smooth flip cards with random shuffle and progress tracking. Great for daily JLPT practice.
- ✏️ **Auto Quiz Generator** — Creates multiple-choice questions from your own word list.
- 🤖 **AI Learning Assistant (Gemini)** — Ask about grammar, word differences, and translations using **Google Gemini 2.0 Flash**.
- 🌓 **Dark & Light Mode** — Modern Liquid Glass interface that looks good on any screen.

---

## 🛠️ Tech Stack

| Part | Technology |
|---|---|
| Backend | Python + Flask |
| Frontend | HTML5, CSS3 (Glassmorphism), Vanilla JavaScript |
| Desktop Window | pywebview (native on Windows & macOS) |
| AI | Google Gemini API (`gemini-2.0-flash`) |
| Packaging | PyInstaller |

---

## 🚀 How to Install & Run

### 1. Clone the repository
```bash
git clone https://github.com/trietnguyen2611/jlpt-learning-app.git
cd jlpt-learning-app
```

### 2. Create virtual environment and install packages
```bash
conda create -n jlpt python=3.13 -y
conda activate jlpt
pip install -r requirements.txt
```

> [!IMPORTANT]
> Use **`pywebview`** (not `webview`). The correct package is already listed in `requirements.txt`.

### 3. Start the app
```bash
python app.py
```
A native desktop window will open. You do not need a browser.

---

## 🤖 Set Up the AI Feature

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Open the app → go to the **Learn with AI** tab → paste your API key.
3. Start asking questions about Japanese grammar and vocabulary.

---

## 📁 Project Structure

```
jlpt-learning-app/
├── app.py              # Flask server + pywebview desktop window
├── requirements.txt    # flask, requests, pywebview
├── vocab_data.json     # Vocabulary data (auto created)
├── templates/
│   └── index.html      # Single page app (HTML + CSS + JS)
├── icon/
│   ├── app.ico         # Windows icon
│   ├── app.png
│   └── app.icns        # macOS icon
└── README.md
```

---

## Keywords

`JLPT` `Japanese vocabulary` `flashcards` `language learning` `desktop app` `Python` `Flask` `pywebview` `Gemini AI` `Japanese study tool`

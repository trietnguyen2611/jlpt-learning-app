# JLPT Learning App✨

A desktop app for learning Japanese vocabulary. It runs directly on Windows and macOS like a normal software (no need to open a browser). It also has an AI helper (Gemini) to make practice better.

---

## 🌟 Main Features:

- 📚 **Vocabulary Management** — Add or delete words easily. Data is saved automatically in the file `vocab_data.json`.
- 🃏 **Flashcards** — Smooth 3D flip cards. You can shuffle the cards and see a progress bar.
- ✏️ **Quiz** — The app creates 4-choice questions from your own word list.
- 🤖 **Learn with AI - Experimental** — Uses **Gemini 2.0 Flash** to explain grammar, compare words, and translate.
- 🌓 **Dark / Light Mode** — Nice Liquid Glass design.

---

## 🛠️ Technologies:

| Part | Details |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3 (Glassmorphism), Vanilla JS |
| Desktop | pywebview (native window on macOS) |
| AI | Google Gemini API (`gemini-2.0-flash`) |
| Packaging | PyInstaller |

---

## 🚀 Install & Run:

### 1. Clone the project
```bash
git clone https://github.com/trietnguyen2611/jlpt-learning-app.git
cd jlpt-learning-app
```

### 2. Create a Conda virtual environment (or use Base) and install libraries
```bash
conda create -n jlpt python=3.13 -y
conda activate jlpt
pip install -r requirements.txt
```

> [!IMPORTANT]
> The desktop window library is **`pywebview`** (not `webview`). The file `requirements.txt` already has the correct name. Just run `pip install -r requirements.txt`.

### 3. Run the app
```bash
python app.py
```
A software window will open on your screen — no browser needed.

---

## 🤖 Set up Learn with AI:

1. Create a free API Key at [Google AI Studio](https://aistudio.google.com/app/apikey) - note that using this API may cost money.
2. Open the app → go to the **🤖 Learn with AI** tab → paste your API Key.
3. Start asking questions and talk with the AI.

---

## 📁 Project Structure:

```
jlpt-learning-app/
├── app.py              # Flask server + pywebview desktop window
├── requirements.txt    # flask, requests, pywebview
├── vocab_data.json     # Vocabulary data (created automatically)
├── templates/
│   └── index.html      # SPA interface (HTML + CSS + JS)
├── icon/
│   └── app.ico         # App icon (.ico - for Windows only)
    └── app.png
    └── app.icns        # App icon (.icns - for macOS only)
└── README.md
```

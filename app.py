import json
import os
import sys
import threading

import requests
import webview
from flask import Flask, jsonify, render_template, request

# ---------------------------------------------------------------------------
# App & Path Configuration
# ---------------------------------------------------------------------------

if getattr(sys, "frozen", False):
    # Running as a PyInstaller bundle
    _base_dir = sys._MEIPASS
    _data_dir = os.path.join(os.path.expanduser("~"), ".jlpt_learning_app")
    if not os.path.exists(_data_dir):
        os.makedirs(_data_dir)
else:
    # Running as a normal Python script
    _base_dir = os.path.dirname(os.path.abspath(__file__))
    _data_dir = _base_dir

app = Flask(__name__, template_folder=os.path.join(_base_dir, "templates"))
DATA_FILE = os.path.join(_data_dir, "vocab_data.json")

SYSTEM_INSTRUCTION = (
    "Bạn là gia sư tiếng Nhật chuyên nghiệp, thân thiện và kiên nhẫn. "
    "Chuyên giúp người Việt học tiếng Nhật. "
    "Hãy trả lời bằng tiếng Việt, kèm ví dụ tiếng Nhật (có romaji và nghĩa) khi cần. "
    "Giải thích ngữ pháp, từ vựng, văn hoá Nhật Bản một cách dễ hiểu và sinh động. "
    "Dùng emoji phù hợp để tạo không khí vui vẻ. "
    "Khi dạy từ vựng, luôn cung cấp: chữ Kanji/Kana, romaji, và nghĩa tiếng Việt."
)

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.0-flash:generateContent?key={api_key}"
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_vocab():
    """Load vocabulary list from the JSON data file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_vocab(data):
    """Persist vocabulary list to the JSON data file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Serve the single-page application."""
    return render_template("index.html")


@app.route("/api/vocab", methods=["GET"])
def get_vocab():
    """Return the full vocabulary list."""
    return jsonify(load_vocab())


@app.route("/api/vocab", methods=["POST"])
def add_vocab():
    """Add a new vocabulary item and return the updated list."""
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Invalid JSON body"}), 400

    jp = body.get("jp", "").strip()
    romaji = body.get("romaji", "").strip()
    vn = body.get("vn", "").strip()

    if not jp or not vn:
        return jsonify({"error": "Fields jp and vn are required"}), 400

    vocab = load_vocab()
    vocab.append({"jp": jp, "romaji": romaji, "vn": vn})
    save_vocab(vocab)
    return jsonify(vocab), 201


@app.route("/api/vocab/<int:idx>", methods=["DELETE"])
def delete_vocab(idx):
    """Delete a vocabulary item by index and return the updated list."""
    vocab = load_vocab()

    if idx < 0 or idx >= len(vocab):
        return jsonify({"error": "Index out of range"}), 404

    vocab.pop(idx)
    save_vocab(vocab)
    return jsonify(vocab)


@app.route("/api/chat", methods=["POST"])
def chat():
    """Proxy a chat request to the Gemini AI API."""
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Invalid JSON body"}), 400

    api_key = body.get("api_key", "").strip()
    history = body.get("history", [])
    message = body.get("message", "").strip()

    if not api_key:
        return jsonify({"error": "api_key is required"}), 400
    if not message:
        return jsonify({"error": "message is required"}), 400

    # Build conversation contents from the last 10 history messages
    contents = [
        {
            "role": "user" if entry.get("role") == "user" else "model",
            "parts": [{"text": entry.get("content", "")}],
        }
        for entry in history[-10:]
    ]
    contents.append({"role": "user", "parts": [{"text": message}]})

    payload = {
        "system_instruction": {"parts": [{"text": SYSTEM_INSTRUCTION}]},
        "contents": contents,
        "generationConfig": {"temperature": 0.8, "maxOutputTokens": 1024},
    }

    try:
        resp = requests.post(
            GEMINI_URL.format(api_key=api_key), json=payload, timeout=30
        )
    except requests.RequestException as e:
        return jsonify({"error": f"Request to Gemini failed: {e}"}), 502

    if resp.status_code != 200:
        return jsonify({"error": f"Gemini API error: {resp.text}"}), resp.status_code

    data = resp.json()
    try:
        text = data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        return jsonify({"error": "Unexpected Gemini response format"}), 502

    return jsonify({"response": text})


# ---------------------------------------------------------------------------
# Entry point — Desktop window via pywebview
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Start Flask in a background daemon thread
    threading.Thread(
        target=lambda: app.run(port=5000, debug=False, use_reloader=False),
        daemon=True,
    ).start()

    # Launch native desktop window
    webview.create_window(
        title="JLPT Learning App",
        url="http://127.0.0.1:5000",
        width=1280,
        height=800,
        min_size=(900, 600),
        resizable=True,
    )
    webview.start()

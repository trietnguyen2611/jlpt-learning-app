import json
import os
import sys

import requests
from flask import Flask, jsonify, render_template, request

# Determine paths when running as a packaged executable (PyInstaller)
if getattr(sys, 'frozen', False):
    # PyInstaller temporary extraction folder for static files
    template_folder = os.path.join(sys._MEIPASS, "templates")
    app = Flask(__name__, template_folder=template_folder)
    # Writable directory of the actual executable to persist vocabulary data
    executable_dir = os.path.dirname(sys.executable)
else:
    app = Flask(__name__)
    executable_dir = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(executable_dir, "vocab_data.json")

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
    try:
        return jsonify(load_vocab())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/vocab", methods=["POST"])
def add_vocab():
    """Add a new vocabulary item and return the updated list."""
    try:
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
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/vocab/<int:idx>", methods=["DELETE"])
def delete_vocab(idx):
    """Delete a vocabulary item by index and return the updated list."""
    try:
        vocab = load_vocab()

        if idx < 0 or idx >= len(vocab):
            return jsonify({"error": "Index out of range"}), 404

        vocab.pop(idx)
        save_vocab(vocab)

        return jsonify(vocab)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/chat", methods=["POST"])
def chat():
    """Proxy a chat request to the Gemini AI API."""
    try:
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
        contents = []
        for entry in history[-10:]:
            role = "user" if entry.get("role") == "user" else "model"
            contents.append({"role": role, "parts": [{"text": entry.get("content", "")}]})

        # Append current user message
        contents.append({"role": "user", "parts": [{"text": message}]})

        payload = {
            "system_instruction": {
                "parts": [{"text": SYSTEM_INSTRUCTION}],
            },
            "contents": contents,
            "generationConfig": {
                "temperature": 0.8,
                "maxOutputTokens": 1024,
            },
        }

        url = GEMINI_URL.format(api_key=api_key)
        resp = requests.post(url, json=payload, timeout=30)

        if resp.status_code != 200:
            return jsonify({"error": f"Gemini API error: {resp.text}"}), resp.status_code

        data = resp.json()
        try:
            text = data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return jsonify({"error": "Unexpected Gemini response format"}), 502

        return jsonify({"response": text})
    except requests.RequestException as e:
        return jsonify({"error": f"Request to Gemini failed: {str(e)}"}), 502
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5000)

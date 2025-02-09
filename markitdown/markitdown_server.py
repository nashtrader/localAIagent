from flask import Flask, request, jsonify
from markitdown import MarkItDown
import os

app = Flask(__name__)
markitdown = MarkItDown()  # MarkItDown-Objekt erstellen

@app.route("/", methods=["POST"])
def convert_markdown():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    # Speichert die Datei temporär
    temp_path = f"/tmp/{file.filename}"
    file.save(temp_path)

    try:
        # MarkItDown zur Konvertierung nutzen
        result = markitdown.convert(temp_path)
        return jsonify({"markdown": result.text_content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.remove(temp_path)  # Löscht die temporäre Datei nach der Verarbeitung

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)

from __future__ import annotations

import os
from pathlib import Path

from flask import Flask, abort, send_from_directory


BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = "amaresam_portfolio_v4.html"

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(BASE_DIR, HTML_FILE)


@app.route("/<path:asset_path>")
def serve_asset(asset_path: str):
    file_path = BASE_DIR / asset_path
    if not file_path.is_file():
        abort(404)
    return send_from_directory(BASE_DIR, asset_path)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5500"))
    debug = os.getenv("FLASK_DEBUG", "1") == "1"
    app.run(host="127.0.0.1", port=port, debug=debug)

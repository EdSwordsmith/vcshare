import os
from flask import Flask, send_file
from markupsafe import escape

from .config import VCShareConfig


def create_app(config: VCShareConfig):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello, World"

    @app.get("/file/<path:file_path>")
    def get_file(file_path: str):
        if not config.download:
            # TODO: Send a better response
            return "File download not allowed"

        return send_file(os.path.join(config.directory, escape(file_path)))

    return app

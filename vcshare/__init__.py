import os
from flask import Flask, render_template, send_file
from markupsafe import escape

from .config import VCShareConfig


def create_app(config: VCShareConfig):
    app = Flask(__name__)

    def get_dir_contents(path: str | None = None) -> tuple[list[str], list[str]]:
        directory = config.directory
        if path is not None:
            directory = os.path.join(config.directory, path)

        content = os.listdir(directory)
        files = [
            item for item in content if os.path.isfile(os.path.join(directory, item))
        ]
        folders = [
            item for item in content if os.path.isdir(os.path.join(directory, item))
        ]

        return files, folders

    @app.route("/")
    def index():
        files, folders = get_dir_contents()
        return render_template("index.html", folder="", files=files, folders=folders)

    @app.get("/dir/<path:dir_path>")
    def dir(dir_path: str):
        files, folders = get_dir_contents(dir_path)
        return render_template(
            "index.html", folder=f"{dir_path}", files=files, folders=folders
        )

    @app.get("/file/<path:file_path>")
    def get_file(file_path: str):
        if not config.download:
            # TODO: Send a better response
            return "File download not allowed"

        return send_file(os.path.join(config.directory, escape(file_path)))

    return app

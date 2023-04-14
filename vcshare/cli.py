import click
import os

from . import create_app
from .config import VCShareConfig


@click.command()
@click.argument(
    "dir", type=click.Path(exists=True, dir_okay=True, file_okay=False), default="."
)
@click.option(
    "--upload",
    "-u",
    is_flag=True,
    default=False,
    required=False,
    help="Allow file upload to the directory",
)
@click.option(
    "--download",
    "-d",
    is_flag=True,
    default=False,
    required=False,
    help="Allow file download from the directory",
)
@click.option(
    "--port",
    "-p",
    type=int,
    default=5000,
    required=False,
    help="Port where the server should run",
)
def main(dir: str, upload: bool, download: bool, port: int):
    directory = os.path.abspath(dir)
    config = VCShareConfig(directory, upload, download)
    app = create_app(config)
    app.run(port=port)

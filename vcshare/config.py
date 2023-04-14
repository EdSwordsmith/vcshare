from dataclasses import dataclass


@dataclass
class VCShareConfig:
    """Class for passing the cli args to the web server as config"""

    directory: str
    upload: bool
    download: bool

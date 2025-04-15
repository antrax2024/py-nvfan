import os
from typing import Any
from confz import BaseConfig, FileSource
from rich.console import Console


APP_NAME = "py-nvfan"
VERSION = "0.1.4"
cl = Console()


def pc(message: str, variable: Any) -> None:
    cl.print(f"[bold yellow]{message}[/bold yellow]: {variable}")


def printAsciiArt() -> None:
    asciiArt = r"""
                               __             
 _ __  _   _       _ ____   __/ _| __ _ _ __  
| '_ \| | | |_____| '_ \ \ / / |_ / _` | '_ \ 
| |_) | |_| |_____| | | \ V /|  _| (_| | | | |
| .__/ \__, |     |_| |_|\_/ |_|  \__,_|_| |_|
|_|    |___/                
    """
    print(asciiArt)


class AppConfig(BaseConfig):
    CONFIG_SOURCES = FileSource(
        file=os.path.join(
            os.path.expanduser(path="~"), ".config", f"{APP_NAME}", "config.yaml"
        )
    )

    targetTemps: list[int]
    targetDuties: list[int]

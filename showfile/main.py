import sys

from rich.console import Console
from rich.syntax import PygmentsSyntaxTheme, Syntax

from showfile.theme import MonokaiProStyle

from .theme import MonokaiProStyle


def run():
    console = Console()
    syntax = Syntax.from_path(sys.argv[1])
    syntax._theme = PygmentsSyntaxTheme(MonokaiProStyle)
    console.print(syntax)

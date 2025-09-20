from rich.console import Console
from rich.text import Text
from rich.layout import Layout
from loguru import logger



def test_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header"),
        Layout(name="content")
    )

    layout["header"].update(Text("Trading Game", style="bold blue"))
    layout["content"].update(Text("This is content area."))

    console = Console()
    console.print(layout)
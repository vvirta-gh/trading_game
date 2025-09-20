from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.layout import Layout  # KORJATTU: rich.layout.Layout
from rich.text import Text
from app.utils.constants import Emojis
from app.models.stock import Stock


class GameLayout:
    """Pelin käyttöliittymä"""
    
    def __init__(self):
        self.console = Console()
        self.layout = Layout()
        self._setup_layout()

    def _setup_layout(self):
        """Luo layoutin rakenteen"""
        # Jaetaan ruutu pystysuunnassa kahteen osaan
        self.layout.split_column(
            Layout(name="header"), # Header (3 riviä)
            Layout(name="main")    # Pääsisältö
        )

        # Asetetaan headerin koko
        self.layout["header"].size = 3

        # Jaetaan pääsisältö vaakasuunnassa kahteen osaan
        self.layout["main"].split_row(
            Layout(name="left"), # Pääsisältö vasen (main_left)
            Layout(name="right") # Pääsisältö oikea (main_right)
        )

        # Jaetaan vasen puoli pystysuunnassa kahteen osaan
        self.layout["left"].split_column(
            Layout(name="stocks", ratio=2), # Osakkeet (2/3)
            Layout(name="actions", ratio=1) # Toiminnot (1/3)
        )

        # Jaetaan oikea puoli pystysuunnassa kahteen osaan
        self.layout["right"].split_column(
            Layout(name="portfolio", ratio=2), # Portfolio (2/3)
            Layout(name="status", ratio=1) # Status (1/3)
        )


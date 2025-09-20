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
            Layout(name="stocks", ratio=3),  # 3/4 tilasta
            Layout(name="actions", ratio=1)  # 1/4 tilasta
        )

        # Jaetaan oikea puoli pystysuunnassa kahteen osaan
        self.layout["right"].split_column(
            Layout(name="portfolio", ratio=2), # Portfolio (2/3)
            Layout(name="status", ratio=1) # Status (1/3)
        )

    def update_header(self, title="Trading Game"):
        header_text = f"[bold blue]{Emojis.CHART_UP} {title} {Emojis.CHART_DOWN}[/bold blue]"
        self.layout["header"].update(Panel(header_text, style="blue"))
        
    def update_stocks(self, stocks_table):
        """Updates stocks table on the left side of the screen"""
        # stocks_table on Rich Table -objekti (UIComponents.create_stocks_table() palauttaa)
        self.layout["stocks"].update(stocks_table)
        
    def update_portfolio(self, portfolio_table):
        """Updates portfolio table on the right side of the screen"""
        self.layout["portfolio"].update(portfolio_table)
        
    def update_actions(self, actions_text="Actions coming soon..."):
        """Updates actions table on the left side of the screen"""
        self.layout["actions"].update(actions_text)
        
    def update_status(self, status_text="Status info..."):
        """Updates status table on the right side of the screen"""
        self.layout["status"].update(status_text)
        
    def render(self):
        """Renders the entire layout"""
        self.console.print(self.layout)


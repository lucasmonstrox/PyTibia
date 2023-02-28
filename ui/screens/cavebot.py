from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen



class CavebotScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            use_pagination=False,
            check=False,
            column_data=[
                ("ID", dp(25)),
                ("Tipo", dp(15)),
                ("X", dp(15)),
                ("Y", dp(15)),
                ("Z", dp(15)),
                ("Opções", dp(15)),
            ],
            row_data=[
                (
                    "1",
                    "walk",
                    "33214",
                    "32459",
                    "8",
                    "...",
                ),
                (
                    "2",
                    "walk",
                    "33214",
                    "32459",
                    "8",
                    "...",
                ),
            ],
            sorted_on="ID",
            sorted_order="ASC",
            elevation=0,
        )
        layout.add_widget(self.data_tables)
        self.add_widget(layout)
    
    def addWaypoint(self):
        self.data_tables.add_row(("3", "4", "3", "4", "3", "4"))

from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class HealingScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDLabel(text='Tela de healing'))
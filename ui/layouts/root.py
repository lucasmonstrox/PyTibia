from kivymd.uix.boxlayout import BoxLayout
from ..menus.horizontal import HorizontalMenu
from ..screenManager import ScreenManagement


class RootLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        menu = HorizontalMenu()
        screenManager = ScreenManagement()
        self.add_widget(menu)
        self.add_widget(screenManager)
        self.ids.screen_manager = screenManager
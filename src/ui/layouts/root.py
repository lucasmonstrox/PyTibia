from kivymd.uix.boxlayout import BoxLayout
from ..menus.horizontal import HorizontalMenu
from ..menus.mainBar import MainBar
from ..screenManager import ScreenManagement


class RootLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        mainBar = MainBar()
        menu = HorizontalMenu()
        screenManager = ScreenManagement()
        self.add_widget(mainBar)
        self.add_widget(menu)
        self.add_widget(screenManager)
        self.ids.screen_manager = screenManager

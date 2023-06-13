from kivy.uix.button import Button
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
import re
import win32gui


class SetupScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        setupButton = Button(text='Setup', size_hint=(0.2, 0.2))
        self.button = self.add_widget(setupButton)
        self.menu = MDDropdownMenu(
            caller=self.button,
            items=[],
            width_mult=4,
            position='center',
        )
        self.getAllTibiaWindows()

    def menu_callback(self, text_item):
        print(text_item)

    def getAllTibiaWindows(self):
        windowsList = []
        win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), windowsList)
        windowsNames = list(map(lambda hwnd: win32gui.GetWindowText(hwnd), windowsList))
        regex = re.compile(r'Tibia - .*')
        windowsFilter = list(filter(lambda windowName: regex.match(windowName), windowsNames))
        menu_items = [
            {
                "text": tibiaWindow.title,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=tibiaWindow.title: self.menu_callback(x),
            } for tibiaWindow in windowsFilter
        ]
        print('self.menu.items', self.menu.items)
        self.menu.items = menu_items
        print('self.menu.items', self.menu.items)

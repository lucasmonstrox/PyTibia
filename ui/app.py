from kivymd.app import MDApp
from kivy.config import Config
from .layouts.root import RootLayout


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.title = "PyTibia"
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '800')
        return RootLayout()
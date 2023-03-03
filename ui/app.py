import kivy.context
from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window
from .layouts.root import RootLayout


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.title = "PyTibia"
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '800')
        return RootLayout()
    
    def on_start(self):
        Window.bind(on_restore=self.onRestore)
    
    def onRestore(self, _):
        gameContext = kivy.context.get_current_context()['game']
        gameContext.pause()
        
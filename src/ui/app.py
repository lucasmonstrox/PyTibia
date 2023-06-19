import kivy.context
from kivy.core.window import Window
from kivymd.app import MDApp
from .layouts.root import RootLayout


class MyApp(MDApp):
    def build(self):
        self.resizable = False
        self.size = (1280, 960)
        self.theme_cls.theme_style = 'Dark'
        self.title = 'PyTibia'
        return RootLayout()

    def on_start(self):
        Window.bind(on_restore=self.onRestore)

    def onRestore(self, _):
        context = kivy.context.get_current_context()['game']
        context.pause()

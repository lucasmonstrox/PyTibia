import kivy.context
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = 'menu'
        self.height = 50
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.spacing = 10
        playButton = Button(text='Play', size_hint=(None, 1))
        playButton.bind(on_press=self.play)
        stopButton = Button(text='Pause', size_hint=(None, 1))
        stopButton.bind(on_press=self.pause)
        self.add_widget(playButton)
        self.add_widget(stopButton)

    def play(self, _):
        context = kivy.context.get_current_context()['game']
        self.parent.parent.parent.minimize()
        context.play()

    def pause(self, _):
        context = kivy.context.get_current_context()['game']
        context.pause()

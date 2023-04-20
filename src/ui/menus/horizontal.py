from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class HorizontalMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = 'menu'
        self.height = 50
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.spacing = 10
        setupButton = Button(text='Setup', size_hint=(None, 1))
        setupButton.bind(on_press=lambda _: self.parent.ids.screen_manager.switch_screen('setup_screen'))
        cavebotButton = Button(text='Cavebot', size_hint=(None, 1))
        cavebotButton.bind(on_press=lambda _: self.parent.ids.screen_manager.switch_screen('cavebot_screen'))
        targetButton = Button(text='Targeting', size_hint=(None, 1))
        targetButton.bind(on_press=lambda _: self.parent.ids.screen_manager.switch_screen('targeting_screen'))
        healerButton = Button(text='Healing', size_hint=(None, 1))
        healerButton.bind(on_press=lambda _: self.parent.ids.screen_manager.switch_screen('healing_screen'))
        spellsButton = Button(text='Spells', size_hint=(None, 1))
        spellsButton.bind(on_press=lambda _: self.parent.ids.screen_manager.switch_screen('spells_screen'))
        self.add_widget(setupButton)
        self.add_widget(cavebotButton)
        self.add_widget(targetButton)
        self.add_widget(healerButton)
        self.add_widget(spellsButton)

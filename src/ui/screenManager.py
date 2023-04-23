from kivy.uix.screenmanager import NoTransition, ScreenManager
from .screens.cavebot import CavebotScreen
from .screens.healing.screen import HealingScreen
from .screens.setup import SetupScreen
from .screens.spells import SpellsScreen
from .screens.targeting import TargetingScreen


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = 'screen_manager'
        self.transition = NoTransition()
        self.add_widget(SetupScreen(name='setup_screen'))
        self.add_widget(CavebotScreen(name='cavebot_screen'))
        self.add_widget(TargetingScreen(name='targeting_screen'))
        self.add_widget(HealingScreen(name='healing_screen'))
        self.add_widget(SpellsScreen(name='spells_screen'))

    def switch_screen(self, screen_name):
        self.current = screen_name

from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabs
from .tabs.potions import PotionsTab
from .tabs.priority import PriorityTab
from .tabs.spells import SpellsTab


class HealingScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        tabs = MDTabs(anim_duration=0, lock_swiping=True)
        tabs.add_widget(PriorityTab(title='Priority'))
        tabs.add_widget(PotionsTab(title='Potions'))
        tabs.add_widget(SpellsTab(title='Spells'))
        self.add_widget(tabs)

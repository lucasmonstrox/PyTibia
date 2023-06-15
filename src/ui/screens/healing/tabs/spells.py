from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from ..cards.criticalHealing import CriticalHealingCard
from ..cards.lightHealing import LightHealingCard


class SpellsTab(MDFloatLayout, MDTabsBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(padding=[20, 20, 20, 20], spacing=20)
        firstRow = BoxLayout()
        firstRow.add_widget(CriticalHealingCard(labelText='Critical Healing'))
        firstRow.add_widget(LightHealingCard(labelText='Medium Healing'))
        firstRow.add_widget(LightHealingCard(labelText='Light Healing'))
        layout.add_widget(firstRow)
        self.add_widget(layout)

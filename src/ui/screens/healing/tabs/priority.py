from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from ..cards.healthFood import HealthFoodCard
from ..cards.manaFood import ManaFoodCard


class PriorityTab(MDFloatLayout, MDTabsBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(padding=[20, 20, 20, 20], spacing=20)
        firstRow = BoxLayout(orientation='horizontal')
        firstRow.add_widget(HealthFoodCard())
        firstRow.add_widget(ManaFoodCard())
        layout.add_widget(firstRow)
        self.add_widget(layout)

from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase


class PriorityTab(MDFloatLayout, MDTabsBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

import kivy.context
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.selectioncontrol.selectioncontrol import MDCheckbox
from kivymd.uix.screen import MDScreen


class SpellsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spells = []
        self.data_tables = MDDataTable(
            use_pagination=False,
            check=False,
            column_data=[
                ('Spell', dp(15)),
            ],
            row_data=[
            ],
            elevation=0,
        )
        self.add_widget(self.data_tables)

    def addSpell(self):
        pass

    def moveUpSpellByIndex(self, index):
        pass

    def moveDownSpellByIndex(self, index):
        pass

    def removeSpellByIndex(self, index):
        pass
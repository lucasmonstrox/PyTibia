from kivy.context import get_current_context
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from ..cards.healthPotion import HealthPotionCard
from ..cards.manaPotion import ManaPotionCard


class HealingScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gameContext = get_current_context()['game']
        layout = BoxLayout(padding=[20, 20, 20, 20], spacing=20)
        firstColumn = BoxLayout(orientation='vertical')
        firstColumn.add_widget(HealthPotionCard(healthPotionType='firstHealthPotion', labelText='Health Potion 1'))
        firstColumn.add_widget(HealthPotionCard(healthPotionType='secondHealthPotion', labelText='Health Potion 2'))
        firstColumn.add_widget(HealthPotionCard(healthPotionType='thirdHealthPotion', labelText='Health Potion 3'))
        secondColumn = BoxLayout(orientation='vertical')
        secondColumn.add_widget(ManaPotionCard(healthPotionType='firstManaPotion', labelText='Mana Potion 1'))
        secondColumn.add_widget(ManaPotionCard(healthPotionType='secondManaPotion', labelText='Mana Potion 2'))
        secondColumn.add_widget(ManaPotionCard(healthPotionType='thirdManaPotion', labelText='Mana Potion 3'))
        layout.add_widget(firstColumn)
        layout.add_widget(secondColumn)
        self.add_widget(layout)

    def toggleSecondHealthPotion(self, _, enabled):
        self.gameContext.toggleSecondHealthPotion(enabled)

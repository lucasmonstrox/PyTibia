from kivy.context import get_current_context
from kivy.uix.switch import Switch
from kivymd.toast import toast
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.slider.slider import MDSlider
from kivy.uix.textinput import TextInput


class MyTextInput(TextInput):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        self.callback(self, window, keycode, text, modifiers)

class HealthFoodCard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, orientation='vertical')
        self.context = get_current_context()['game']
        self.healthPotionType = 'healthFood'
        header = BoxLayout()
        label = MDLabel(text='Health Food')
        switch = Switch()
        switch.bind(active=self.toggleHealthPotion)
        header.add_widget(label)
        header.add_widget(switch)
        self.add_widget(header)
        card = MDCard()
        content = BoxLayout(orientation='vertical', padding=[10, 10, 10, 10], spacing=5)
        hpLabel = MDLabel(text='HP% less than:', theme_text_color='Error')
        hpContent = BoxLayout(orientation='vertical')
        hpContent.add_widget(hpLabel)
        slider = MDSlider(color='red', hint_bg_color='red', hint_text_color='white', thumb_color_active='red', thumb_color_inactive='red', min=10, step=10)
        slider.bind(value=self.onHpPercentageChange)
        hpContent.add_widget(slider)
        cardHeader = BoxLayout()
        # cardHeader.add_widget(FitImage(source='src/repositories/actionBar/images/cooldowns/attack.png'))
        cardHeader.add_widget(hpContent)
        content.add_widget(cardHeader)
        bottom = BoxLayout(padding=[10, 10, 10, 10])
        bottom.add_widget(MDLabel(text='Hotkey:'))
        # text = MDTextField(readonly=True, on_key_down=self.keyboard_on_key_down)
        text = MyTextInput(readonly=True, callback=self.keyboard_on_key_down)
        bottom.add_widget(text)
        content.add_widget(bottom)
        card.add_widget(content)
        self.add_widget(card)

    def toggleHealthPotion(self, _, enabled):
        self.context.toggleHealingPotionsByKey(self.healthPotionType, enabled)

    def onHpPercentageChange(self, _, value):
        self.context.setHealthPotionHpPercentageLessThanOrEqual(self.healthPotionType, value)

    def keyboard_on_key_down(self, instance, window, keyCode, text, modifiers):
        _, hotkey = keyCode
        allowedHotkeys = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']
        isNotAllowedHotkey = hotkey not in allowedHotkeys
        if isNotAllowedHotkey:
            # TODO: improve phrase
            toast('Invalid hotkey')
            return
        if hotkey and not modifiers:
            context = get_current_context()['game']
            context.setHealthPotionHotkeyByKey(self.healthPotionType, hotkey)
            instance.text = hotkey

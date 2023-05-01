# from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window
# from kivymd.theming import ThemeManager
from kivymd.app import MDApp

from kivy.lang import Builder

Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (360, 640)


class Container(GridLayout):
    action = None
    def btNum(self, number):
        if self.text_input.text == "0":
            self.text_input.text = ''
            self.text_input.text = str(number)
        else:
            self.text_input.text = self.text_input.text + str(number)

    def btClear(self):
        self.text_input.text = "0"

    def btPlus(self):
        action = self.text_input.text
        if action is None:
            action = self.text_input.text
            self.text_input.text = "0"
        else:  self.text_input.text = action + self.text_input.text



class CalcApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Калькулятор"
        # self.theme_cls.theme_style = "Light"
        super().__init__(**kwargs)

    def build(self):
        return Container()


if __name__ == "__main__":
    CalcApp().run()

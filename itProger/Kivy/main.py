# from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window
# from kivymd.theming import ThemeManager
from kivymd.app import MDApp

from kivy.lang import Builder

Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (360, 640)

Builder.load_string('''
<MyOwnLabel@MDLabel>
    font_size: '25sp'
    halign: 'left'
    walign: 'middle'
    text_size: self.size

<Container>:
    rows: 3
    text_input: text_input
    label_hours: label_hours
    label_minits: label_minits
    label_second: label_second
    label_m_second: label_m_second
    label_weeks: label_weeks

    AnchorLayout:
        anchor_y: 'top'
        size_hint: 1, 0.15
        padding: 30

        MDTextField:
            text: ''
            id: text_input
            font_size: '45sp'
            input_filter: 'int'
            input_type: 'number'
            multiline: False
            hint_text: "Введите число"

    GridLayout:
        cols: 2
        padding: [40, 0, 0, 0]

        BoxLayout:
            orientation: 'vertical'
            MyOwnLabel:
                text: 'Часы'
            MyOwnLabel:
                text: 'Минуты'
            MyOwnLabel:
                text: 'Секунды'
            MyOwnLabel:
                text: 'Милисекунды'
            MyOwnLabel:
                text: 'Недели'

        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.5, 1
            MyOwnLabel:
                text: '0'
                id: label_hours
            MyOwnLabel:
                text: '0'
                id: label_minits
            MyOwnLabel:
                text: '0'
                id: label_second
            MyOwnLabel:
                text: '0'
                id: label_m_second
            MyOwnLabel:
                text: '0'
                id: label_weeks

    BoxLayout:
        size_hint: 0.9, 0.15
        padding: [30,20,30,20]
        MDRaisedButton:
            text: 'Погнали'
            size_hint: 1, 0.9
            on_release:
                root.convert()
''')

class Container(GridLayout):
    def convert(self):
        try:
            number = int(self.text_input.text)
        except Exception:
            number = 0
        self.label_hours.text = str(number * 24)
        self.label_minits.text = str(number * 24 * 60)
        self.label_second.text = str(number * 24 * 60 * 60)
        self.label_m_second.text = str(number * 24 * 60 * 60 * 60)
        try:
            self.label_weeks.text = str("%.2f" % round(number / 7, 2))
        except Exception:
            self.label_weeks.text = 'Ошибка'

class DuckyApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "конвертор"
        # self.theme_cls.theme_style = "Light"
        super().__init__(**kwargs)

    def build(self):
        return Container()

if __name__ == "__main__":
    DuckyApp().run()

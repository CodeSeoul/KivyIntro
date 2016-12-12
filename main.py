from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MainPage(Widget):
    pass


class UpdateButton(Button):
    output_label = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def on_press(self):
        self.output_label.text = self.text_input.text


class IntroApp(App):
    def build(self):
        root = MainPage()
        return root

if __name__ == '__main__':
    IntroApp().run()
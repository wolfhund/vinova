import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import label


class MyApp(App):
    def build(self):
        return Label(text='Hello')


if __name__ == '__main__':
    MyApp().run()
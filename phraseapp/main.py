import threading
import webbrowser
from functools import partial
from random import random

from kivy.app import App
from kivy.core.image import Image
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
import data_p
from kivy.uix.screenmanager import ScreenManager, Screen
import db
from kivy.core.window import Window

import sound

Window.clearcolor = (1, 1, 1, 1)


class MainWindowScreen(Screen):
    pass


class HistoryScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


class WrappedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1] + 20))


class MainWindow(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        self.layout = GridLayout(cols=1, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.scroll = ScrollView(size_hint=(1, None), size=(Window.width, 270))
        self.scroll.add_widget(self.layout)

        self.add_widget(self.scroll)

        self.add_widget(
            Label(text='Find Phrase App', color=[0, 0, 0, 1], size_hint=(1.0, 0.05), bold=True))

    def find_phrase(self, phrase):
        print(phrase)
        if not phrase:
            return

        data = data_p.parse_phrase(phrase)

        if len(data):

            for element in self.layout.children:
                print(element)
                self.layout.remove_widget(element)

            for el in data:
                print(el)
                btn = WrappedButton(text=str(el), size_hint_y=None,
                                    background_color=[62 / 255.0, 204 / 255.0, 237 / 255.0, 1.0],
                                    font_size=20, font_name='Arial',
                                    on_press=partial(sound.pronounce, el))
                self.layout.add_widget(btn)

            for element in self.layout.children:
                print(element)

            db.add_note(phrase, data)

        else:
            self.add_widget(Label(text='No results', color=[62 / 255.0, 204 / 255.0, 237 / 255.0, 1.0]))


class History(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        self.layout = GridLayout(cols=1, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.scroll = ScrollView(size_hint=(1, None), size=(Window.width, 270))
        self.scroll.add_widget(self.layout)

        self.add_widget(self.scroll)

        self.load_history_list()

    def load_history_list(self):
        data = db.get_history()


        if len(data):

            for element in self.layout.children:
                print(element)
                self.layout.remove_widget(element)

            for el in data:
                print(el)
                btn = WrappedButton(text=str(el['title']), size_hint_y=None,
                                    background_color=[62 / 255.0, 204 / 255.0, 237 / 255.0, 1.0],
                                    font_size=20, font_name='Arial')

                dropdown = DropDown()
                for sentence in el['data']:
                    dropdown.add_widget(WrappedButton(text=str(el['title']), size_hint_y=None,
                                                      background_color=[235 / 255.0, 107 / 255.0, 52 / 255.0, 1.0],
                                                      font_size=20, font_name='Arial',
                                                      on_press=partial(sound.pronounce, el)))

                btn.on_release = dropdown.open
                self.layout.add_widget(btn)

            for element in self.layout.children:
                print(element)

        else:
            self.add_widget(Label(text='No results', color=[62 / 255.0, 204 / 255.0, 237 / 255.0, 1.0]))


kv = Builder.load_file("main.kv")


class FindPhraseApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    FindPhraseApp().run()

import urllib
from functools import partial

import pyperclip
import requests
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import data_p
from kivy.uix.screenmanager import ScreenManager, Screen
import db
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
import sound
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatIconButton, MDIconButton, MDRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from settings import *

Window.clearcolor = (1, 1, 1, 1)


class MainWindowScreen(Screen):
    def __init__(self, **kwargs):
        super(MainWindowScreen, self).__init__(**kwargs)

        self.language_code = None

        self.layout = GridLayout(cols=1, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.60))
        self.scroll.add_widget(self.layout)

        self.add_widget(self.scroll)

    def change_language(self, language):
        print(language)

        for item in LANGUAGES:
            if item['lang'] == language:
                self.language_code = item['code']

        print(self.language_code)

    def find_phrase(self, phrase, key='search'):
        print(phrase)
        if not phrase:
            return

        data = data_p.parse_phrase(phrase, self.language_code)
        self.layout.clear_widgets()

        if len(data):
            for el in data:
                print(el)
                btn = WrappedButton(text=str(el), size_hint_y=None,
                                    background_color=[74 / 255, 213 / 255, 237 / 255, 1],
                                    font_size=20, font_name='Arial',
                                    on_press=partial(sound.pronounce, el))
                self.layout.add_widget(btn)

            for element in self.layout.children:
                print(element)

            if key == 'search':
                db.add_note(phrase, data)  # add to db
            # HistoryScreen().load_history_list()  # and update the list of history

        else:
            self.layout.add_widget(Label(text='No results', color=[62 / 255.0, 204 / 255.0, 237 / 255.0, 1.0]))


class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super(HistoryScreen, self).__init__(**kwargs)

        print('History().__init__')

        self.layout = GridLayout(cols=2, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.scroll = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height * 0.60))
        self.scroll.add_widget(self.layout)

        self.add_widget(self.scroll)

        self.load_history_list()

    def load_history_list(self):
        print('load_history_list 1')

        data = db.get_history()

        # cleaning list of history
        self.layout.clear_widgets()

        print('load_history_list 2')

        if len(data):
            print(len(data))
            for el in data:
                print('->', el)
                btn = WrappedButton(text=f'{el["title"]} {"(completed)" if el["repetitions"] == 6 else ""}', size_hint_y=None,
                                    background_color=COLORS[str(el['repetitions'])],
                                    font_size=20, font_name='Arial',
                                    on_press=partial(sound.pronounce, el['title']))
                print(COLORS[str(el['repetitions'])])


                btn.bind(on_release=partial(self.open_dropdown, el['title']))

                self.layout.add_widget(btn)
                self.layout.add_widget(MDIconButton(icon='delete',
                                                    on_press=partial(self.delete_from_history, el['title']),
                                                    size_hint=(0.25, None)))
        else:
            self.layout.add_widget(Label(text='No results', color=[62 / 255.0, 204 / 255.0, 237 / 255.0, 1.0]))

    def open_dropdown(self, title, *args):
        db.phrase_repetitions_increase(title)
        self.manager.current = 'main'
        self.manager.get_screen('main').ids.phrase_field.text = title
        self.manager.get_screen('main').find_phrase(title, 'redirect')

        self.load_history_list()



    def delete_from_history(self, title, *args):
        print(title)
        db.delete_request(title)
        self.load_history_list()


class ScreenManagement(ScreenManager):
    pass


class WrappedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1] + 20))


class FindPhraseApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Find Phrase App"
        super().__init__(**kwargs)


    def updateHistory(self):
        self.root.get_screen('history').load_history_list()

    def build(self):
        self.items = ['English', 'Spanish', 'German', 'Italian', 'Portuguese', 'French']
        sm = Builder.load_file("main.kv")
        return sm


if __name__ == "__main__":
    FindPhraseApp().run()

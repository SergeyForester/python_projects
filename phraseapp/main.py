from functools import partial

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

Window.clearcolor = (1, 1, 1, 1)


class MainWindowScreen(Screen):
    def __init__(self, **kwargs):
        super(MainWindowScreen, self).__init__(**kwargs)

        self.language_code = None
        self.languages = [{'lang':'English','code': 0},
                          {'lang': 'Spanish', 'code': 2},
                          {'lang': 'German', 'code': 3},
                          {'lang': 'Italian', 'code': 4},
                          {'lang': 'French', 'code': 1},
                          {'lang': 'Portuguese', 'code': 5}]


        self.layout = GridLayout(cols=1, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.60))
        self.scroll.add_widget(self.layout)

        self.add_widget(self.scroll)


    def change_language(self, language):
        print(language)

        for item in self.languages:
            if item['lang'] == language:
                self.language_code = item['code']

        print(self.language_code)

    def find_phrase(self, phrase):

        print(phrase)
        if not phrase:
            return

        data = data_p.parse_phrase(phrase, self.language_code)

        if len(data):
            for element in self.layout.children:
                print(element)
                self.layout.remove_widget(element)

            for el in data:
                print(el)
                btn = WrappedButton(text=str(el), size_hint_y=None,
                                    background_color=[33 / 255.0, 150 / 255.0, 243 / 255.0, 1.0],
                                    font_size=20, font_name='Arial',
                                    on_press=partial(sound.pronounce, el))
                self.layout.add_widget(btn)

            for element in self.layout.children:
                print(element)

            db.add_note(phrase, data)  # add to db
            HistoryScreen().load_history_list()  # and update the list of history

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
        for element in self.layout.children:
            print('deleting load_history_list ->', element)
            self.layout.remove_widget(element)

        print('load_history_list 2')

        if len(data):
            print(len(data))
            for el in data:
                print('->', el)
                btn = WrappedButton(text=str(el['title']), size_hint_y=None,
                                    background_color=[252 / 255.0, 249 / 255.0, 240 / 255.0, 1.0],
                                    font_size=20, font_name='Arial')

                self.dropdown = DropDown(size_hint=(1.0, None))
                self.dropdown.dismiss()
                for sentence in el['data']:
                    print(sentence)
                    self.dropdown.add_widget(WrappedButton(text=str(sentence), size_hint_y=None,
                                                      background_color=[252 / 225.0, 249 / 225.0, 240 / 255.0, 1.0],
                                                      size_hint=(0.65, None),
                                                      font_size=20, font_name='Arial',
                                                      on_press=partial(sound.pronounce, sentence)))

                btn.bind(on_release=self.dropdown.open)
                self.layout.add_widget(btn)
                self.layout.add_widget(MDIconButton(icon='delete',
                                                    on_press=partial(self.delete_from_history, el['title']),
                                                    size_hint=(0.3, None)))
                self.layout.add_widget(self.dropdown)

            self.layout.add_widget(Widget())


        else:
            self.layout.add_widget(Label(text='No results', color=[62 / 255.0, 204 / 255.0, 237 / 255.0, 1.0]))

    def dropdown_open(self, *args):
        try:
            print(self.dropdown)
            self.dropdown.open(self)
        except RecursionError:
            print('rec')

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

    def build(self):
        self.items = ['English', 'Spanish', 'German', 'Italian', 'Portuguese', 'French']
        self.root = Builder.load_file("main_.kv")


if __name__ == "__main__":
    FindPhraseApp().run()

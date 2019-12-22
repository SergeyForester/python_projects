import time

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.audio import SoundLoader
from kivymd.toast import toast
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
import threading

class ScreenManagement(ScreenManager):
    pass


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.play_stop = False  # sound is not playing
        self.sound = None
        self.second = 0

        Window.bind(on_dropfile=self.file_drop)

        self.sound_slider = MDSlider(min=0, max=100, value=0)

        self.add_widget(self.sound_slider)

    def file_drop(self, window, file_path):
        self.load_sound(str(file_path.decode('utf-8')))

    def load_sound(self, path):
        print(path)
        try:
            self.sound = SoundLoader.load(path)
            self.second = 0

            print(self.sound.length)

            self.sound_slider.max = self.sound.length
            # self.sound_slider.max = 100

            toast('Sound loaded successfully')
        except Exception as e:
            print(e)

    def control_sound_slider(self, *args):
        if self.sound.get_pos():
            self.sound_slider.value = self.sound.get_pos()
            print('v ->',self.sound_slider.value)

    def play_sound(self, play_btn):
        try:
            if self.play_stop:  # if sound is playing
                print('stopping...')
                try:

                    self.second = self.sound.get_pos()

                    self.sound.stop()

                    play_btn.icon = 'play'
                    self.play_stop = False
                except Exception as err:
                    print(err)


            else:
                print('playing...')

                self.sound.play()
                self.sound.seek(self.second)

                play_btn.icon = 'pause'
                self.play_stop = True
                Clock.schedule_interval(self.control_sound_slider, 1.0)


            print(self.sound_slider)
        except AttributeError as err:
            popup = Popup(title='Error',
                          content=Label(text=f"ERROR: We can't play this file \n {err}", color=[1, 1, 1, 1]),
                          size_hint=(None, None), size=(250, 250))
            popup.open()


class AudioPlayerApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Audio Player"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_file("main_.kv")


AudioPlayerApp().run()

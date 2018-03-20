from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

from kivy.config import Config
Config.set('graphics', 'width', '225')
Config.set('graphics', 'height', '370')

class LoadingScreen(Screen):
	pass

class HomeScreen(Screen):
	pass

class HintScreen(Screen):
	pass

class MagicScreen(Screen):
	pass

class ScreenManagement(ScreenManager):
	pass

class MyButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = 'checkbox_off'

    def on_press(self):
        self.source = 'checkbox_on'

    def on_release(self):
        self.source = 'checkbox_off'

utheve = Builder.load_file('utheve.kv')


class MainApp(App):
	def build(self):
		return utheve

if __name__ == '__main__':
	MainApp().run()

from kivy.animation import Animation
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class Home(Screen):
    app = MDApp.get_running_app()

    def click(self, *args):
        print(args)

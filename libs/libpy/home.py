from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

image_path = "assets/images/"


class Home(Screen):
    app = MDApp.get_running_app()
    clock = None

    def click(self, *args):
        print(args)

    def update_rv_data(self, rv):
        if not rv.data:
            self.clock = Clock.schedule_once(lambda x: self.clock_add_data(rv), 0.5)

    @staticmethod
    def clock_add_data(rv):
        data = []
        for i in range(10):
            data.append({"source": f"{image_path}shoes.jpg"})
        rv.data.extend(data)

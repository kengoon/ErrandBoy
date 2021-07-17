import os
from functools import partial
from threading import Thread
from time import sleep

from kivy import platform
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.loader import Loader
from kivy.clock import Clock, mainthread
from kivymd.app import MDApp
from kivy.lang import Builder
from tools.iconfonts import register
from kivy.animation import Animation
from kivymd_extensions.akivymd.uix.statusbarcolor import change_statusbar_color
# from classes.miracle import TopLayer, MiddleLayer, FloatingButton, LayerContent, ScrollLayer
font_folder = "assets/fonts/"
# Loader.loading_image = "assets/images/loader.gif"
r = Factory.register
# r("TopLayer", cls=TopLayer)
# r("MiddleLayer", cls=MiddleLayer)
# r("FloatingButton", cls=FloatingButton)
# r("LayerContent", cls=LayerContent)
# r("ScrollLayer", cls=ScrollLayer)
register("icon", f"{font_folder}MaterialIconsRound-Regular.otf", f"{font_folder}googleIconRound.fontd")


class ErrandBoy(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.screen_length = (1 / (len(os.listdir("libs/libkv")))) * 100
        self.progress_total = self.screen_length * len(os.listdir("libs/libkv"))
        self.next_screen = 0
        self.major_screens = []
        self.clock_add = None
        Window.softinput_mode = 'below_target'
        self.theme_cls.font_styles.update(
            {
                "H1": [f"{font_folder}DINAlternate-bold", 96, False, -1.5],
                "H2": [f"{font_folder}DINAlternate-bold", 60, False, -0.5],
                "H3": [f"{font_folder}DINAlternate-bold", 48, False, 0],
                "H4": [f"{font_folder}DINAlternate-bold", 34, False, 0.25],
                "H5": [f"{font_folder}DINAlternate-bold", 24, False, 0],
                "H6": [f"{font_folder}DINAlternate-bold", 20, False, 0.15],
                "Button": [f"{font_folder}DINAlternate-bold", 14, True, 1.25],
                "Body1": [f"{font_folder}DINAlternate-bold", 16, False, 0.5],
                "Body2": [f"{font_folder}DINAlternate-bold", 14, False, 0.25],
            }
        )

    def build(self):
        return Builder.load_file("manager.kv")

    def on_start(self):
        change_statusbar_color(self.theme_cls.primary_color)
        Thread(target=self._initiate_server_connection).start()

    def _initiate_server_connection(self):
        from classes.m_cardtextfield import M_CardTextField
        from kivymd.uix.snackbar import Snackbar
        r("Snackbar", cls=Snackbar)
        r("M_CardTextField", cls=M_CardTextField)

        for modules in os.listdir("libs/libpy"):
            exec(f"from libs.libpy import {modules.split('.')[0]}")
        file_dir = os.listdir("libs/libkv")
        file_dir.sort(reverse=True)
        file_dir[file_dir.index("home.kv")], file_dir[-1] = (file_dir[-1], file_dir[file_dir.index("home.kv")])
        for files in file_dir:
            Builder.load_file(f"libs/libkv/{files}")
            if files == "widgets.kv" or "2" in files:
                sleep(0.5)
                self.root.ids.progress_bar.current_percent += self.screen_length
                if self.root.ids.progress_bar.current_percent == self.progress_total:
                    Clock.schedule_once(lambda x: exec("self.root.current = 'home'", {"self": self}), 1)
                    break
                continue
            files = files.split(".")[0].capitalize()
            if "_" in files:
                files = "".join(file.capitalize() for file in files.split("_")).split(".")[0]
            self.major_screens.append(files)
        self.clock_add = Clock.schedule_interval(lambda x: self.add_screen(self.major_screens[self.next_screen]), 1)

    @mainthread
    def add_screen(self, widget):
        widget_obj = eval(f"Factory.{widget}()")
        self.root.add_widget(widget_obj)
        self.root.ids.update({widget.lower(): widget_obj})
        self.next_screen += 1
        if self.next_screen == len(self.major_screens):
            self.clock_add.cancel()
        Clock.schedule_once(lambda x: self.change_screen(widget), 1)

    def change_screen(self, widget):
        self.root.ids.progress_bar.current_percent += self.screen_length
        if widget.lower() == "home":
            Clock.schedule_once(lambda x: exec("self.root.current = 'home'", {"self": self}), 1)

    @staticmethod
    def on_focus(value):
        """if platform == "android":
            from kvdroid import activity
            from android.runnable import run_on_ui_thread

            @run_on_ui_thread
            def fix_back_button():
                activity.onWindowFocusChanged(False)
                activity.onWindowFocusChanged(True)

            if not value:
                fix_back_button()"""


ErrandBoy().run()

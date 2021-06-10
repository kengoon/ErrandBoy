import os
from threading import Thread
from time import sleep

from kivy import platform
from kivy.factory import Factory
from kivy.loader import Loader
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd_extensions.akivymd.uix.statusbarcolor import change_statusbar_color
from tools.iconfonts import font_folder, register
from classes.m_cardtextfield import M_CardTextField
from classes.miracle import TopLayer, MiddleLayer, FloatingButton, LayerContent, ScrollLayer

Loader.loading_image = "assets/images/loader.gif"
r = Factory.register
r("TopLayer", cls=TopLayer)
r("MiddleLayer", cls=MiddleLayer)
r("FloatingButton", cls=FloatingButton)
r("LayerContent", cls=LayerContent)
r("ScrollLayer", cls=ScrollLayer)
r("M_CardTextField", cls=M_CardTextField)
register("icon", f"{font_folder}MaterialIconsRound-Regular.otf", f"{font_folder}googleIconRound.fontd")


class ErrandBoy(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.screen_length = (1 / (len(os.listdir("libs/libkv")) - 1)) * 100
        change_statusbar_color(self.theme_cls.primary_color)
        self.theme_cls.font_styles.update(
            {
                "H1": [f"{font_folder}DINAlternate-bold", 96, False, -1.5],
                "H2": [f"{font_folder}DINAlternate-bold", 60, False, -0.5],
                "H3": [f"{font_folder}DINAlternate-bold", 48, False, 0],
                "H4": [f"{font_folder}DINAlternate-bold", 34, False, 0.25],
                "H5": [f"{font_folder}DINAlternate-bold", 24, False, 0],
                "H6": [f"{font_folder}DINAlternate-bold", 20, False, 0.15],
                "Body1": [f"{font_folder}DINAlternate-bold", 16, False, 0.5],
                "Body2": [f"{font_folder}DINAlternate-bold", 14, False, 0.25],
            }
        )

    def build(self):
        return Builder.load_file("manager.kv")

    def on_start(self):
        Thread(target=self._initiate_server_connection).start()

    def _initiate_server_connection(self):
        sleep(5)
        for modules in os.listdir("libs/libpy"):
            exec(f"from libs.libpy import {modules.rstrip('.pyc')}")
        for files in os.listdir("libs/libkv"):
            Builder.load_file(f"libs/libkv/{files}")
            if files == "widgets.kv":
                continue
            Clock.schedule_once(lambda x: self.add_screen(files.split(".")[0].capitalize()), 0.5)

    def add_screen(self, widget):
        widget_obj = eval(f"Factory.{widget}()")
        self.root.add_widget(widget_obj)
        self.root.ids.update({widget.lower(): widget_obj})
        self.root.ids.progress_bar.current_percent += self.screen_length
        if self.root.ids.progress_bar.current_percent == 100:
            Clock.schedule_once(lambda x: exec("self.root.current = 'home'", {"self": self}), 5)

    @staticmethod
    def on_focus(value):
        if platform == "android":
            from kvdroid import activity
            from android.runnable import run_on_ui_thread

            @run_on_ui_thread
            def fix_back_button():
                activity.onWindowFocusChanged(False)
                activity.onWindowFocusChanged(True)

            if not value:
                fix_back_button()


ErrandBoy().run()

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.textinput import TextInput as TI
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.stencilview import StencilView
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase

app = MDApp.get_running_app()


class ItemPagination(ThemableBehavior, Widget):
    current_index = NumericProperty(0)
    color_round_not_active = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.color_round_not_active:
            self.color_round_not_active = get_color_from_hex("#757575")


class CarouselLayout(MDBoxLayout, StencilView):
    def __draw_shadow__(self, origin, end, context=None):
        pass

    @staticmethod
    def swipe_pagnitors(instance, index):
        for pagnitor in instance.pagnitors:
            if instance.pagnitors[index] == pagnitor:
                Animation(rgba=app.theme_cls.primary_color, d=0.3).start(pagnitor.canvas.children[0])
                continue
            Animation(rgba=pagnitor.color_round_not_active, d=0.3).start(pagnitor.canvas.children[0])


class Tab(MDBoxLayout, MDTabsBase):
    def __draw_shadow__(self, origin, end, context=None):
        pass


class TextInput(TI):
    def insert_text(self, substring, from_undo=False):
        print(substring)
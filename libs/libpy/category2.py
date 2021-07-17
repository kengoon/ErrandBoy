from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.app import App


class Category(Screen):
    data_len = 5
    counter = 0
    clock = None
    app = App.get_running_app()
    scroll_data = 4

    def update_rv_data(self, rv):
        if not rv.data:
            self.clock = Clock.schedule_once(lambda x: self.clock_add_data(rv), 0.5)

    @staticmethod
    def clock_add_data(rv):
        data = []
        for i in range(10):
            data.append({})
        rv.data.extend(data)

    def change_screen(self, parent, instance):
        instance_index = parent.children.index(instance)
        self.ids.manager.current = instance.text.lower().split(" ")[1]
        for child in parent.children:
            if child == instance:
                if child.md_bg_color == self.app.theme_cls.primary_color:
                    return
                continue
            if child.md_bg_color == self.app.theme_cls.primary_color:
                former_active_child = parent.children.index(child)
            child.md_bg_color = [1, 1, 1, 1]
            child.text_color = self.app.theme_cls.primary_color
        instance.md_bg_color = self.app.theme_cls.primary_color
        instance.text_color = [1, 1, 1, 1]
        if parent.children.index(instance) < former_active_child:
            if parent.children.index(instance) == 0:
                return
            self.ids.sv.scroll_to(parent.children[instance_index - 1])
        else:
            try:
                self.ids.sv.scroll_to(parent.children[instance_index + 1])
            except IndexError:
                pass





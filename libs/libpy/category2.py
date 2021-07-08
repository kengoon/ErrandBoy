from kivy.clock import Clock
from kivy.uix.screenmanager import Screen


class Category(Screen):
    data_len = 5
    counter = 0
    clock = None

    def update_rv_data(self, rv):
        if not rv.data:
            self.clock = Clock.schedule_once(lambda x: self.clock_add_data(rv), 0.5)

    def clock_add_data(self, rv):
        # if self.counter == self.data_len:
        #     self.counter = 0
        #     self.clock.cancel()
        #     return
        data = []
        for i in range(10):
            data.append({})
        rv.data.extend(data)
        # self.counter += 1

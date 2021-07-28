from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock


# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


Builder.load_file('myKivy/main.kv')
Builder.load_file('myKivy/about.kv')
Builder.load_file('myKivy/settings.kv')
Builder.load_file('myKivy/bluetooth.kv')
Builder.load_file('myKivy/run.kv')


# Declare both screens
class Menu(Screen):
    pass

class Settings(Screen):
    def on_enter(self):
        text = self.ids.input.text
        print(text)

class About(Screen):
    pass

class Run(Screen):
    def update_bar(self, dt=None):
        obj_label = self.ids.pb.value
        self.ids.pb.value = obj_label + 2

        obj_label = self.ids.pb1.value
        self.ids.pb1.value = obj_label + 5

        obj_label = self.ids.pb2.value
        self.ids.pb2.value = obj_label + 3

    def on_update_bar(self, dt=None):
        obj_label = self.ids.pb.value
        self.ids.pb.value = obj_label - 2

        obj_label = self.ids.pb1.value
        self.ids.pb1.value = obj_label - 5

        obj_label = self.ids.pb2.value
        self.ids.pb2.value = obj_label - 3

    def on_start(self):
        obj_label = self.ids.pb2.value
        self.ids.pb2.value = obj_label - 3
        Clock.schedule_interval(self.ids.pb2.value, 60 ** -1)

class Bluetooth(Screen):
    pass

class SeedsApp(App):

    def build(self):

        # Create the screen manager
        sm = ScreenManager()

        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Settings(name='settings'))
        sm.add_widget(About(name='about'))
        sm.add_widget(Run(name='run'))
        sm.add_widget(Bluetooth(name='bluetooth'))

        return sm


if __name__ == '__main__':
    SeedsApp().run()
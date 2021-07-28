import sys
from random import random

from kivy.app import App, Widget
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
Builder.load_file('myKivy/my_run.kv')


# Declare both screens
class Menu(Screen, Widget):
    pass

class Settings(Screen, Widget):
    def on_enter(self):
        text = self.ids.input.text
        print(text)

class About(Screen, Widget):
    pass

class My_run(Screen, Widget):

    def update(self, dp=0.3):

        if self.ids.stop.state == 'down':
            raise Exception

        obj_label = random() * 50 + 50
        self.ids.pb.value = obj_label
        labal_1 = str(int(obj_label)) + ' %'
        self.ids.num1.text = labal_1

        obj_label = random() * 50 +40
        self.ids.pb1.value = obj_label
        labal_2 = str(int(obj_label)) + ' %'
        self.ids.num2.text = labal_2

        obj_label = random() * 50 +45
        self.ids.pb2.value = obj_label
        labal_3 = str(int(obj_label)) + ' %'
        self.ids.num3.text = labal_3

    def update_bar(self, dp=0.1):
        Clock.schedule_interval(self.update, dp)
        try:
            self.update()
        except Exception:
            sys.exc_clear()


    def on_update_bar(self):
        obj_label = self.ids.pb.value
        self.ids.pb.value = obj_label - 2
        obj_label = self.ids.pb1.value
        self.ids.pb1.value = obj_label - 5
        obj_label = self.ids.pb2.value
        self.ids.pb2.value = obj_label - 3


class Bluetooth(Screen, Widget):
    pass

class SeedsApp(App):

    def build(self):

        # Create the screen manager
        sm = ScreenManager()

        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Settings(name='settings'))
        sm.add_widget(About(name='about'))
        sm.add_widget(My_run(name='my_run'))
        sm.add_widget(Bluetooth(name='bluetooth'))

        return sm



if __name__ == '__main__':
    SeedsApp().run()
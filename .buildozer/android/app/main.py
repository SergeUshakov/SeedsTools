from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

Builder.load_file('myKivy/main.kv')
Builder.load_file('myKivy/about.kv')
Builder.load_file('myKivy/settings.kv')
Builder.load_file('myKivy/bluetooth.kv')
Builder.load_file('myKivy/run.kv')

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class RunScreen(Screen):
    pass

class BluetoothScreen(Screen):
    pass



class SeedsApp(App):

     def build(self):
        # Create the screen manager
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(RunScreen(name='run'))
        sm.add_widget(BluetoothScreen(name='bluetooth'))

        return sm

if __name__ == '__main__':
    SeedsApp().run()
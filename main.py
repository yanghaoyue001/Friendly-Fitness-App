from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import requests
import json

class HomeScreen(Screen):
    pass

class ImageButton(ButtonBehavior,Image):
    pass

class SettingsScreen(Screen):
    pass

GUI = Builder.load_file("main.kv")

class MainApp(App):
    my_friend_id = 1
    def build(self):
        return GUI

    def on_start(self):
        # Get database data
        result = requests.get("https://friendly-fitness-97308.firebaseio.com/" + str(self.my_friend_id) + ".json")
        print("Was is okay?", result.ok)
        data = json.loads(result.content.decode())
        print(data)
        workouts = data['workout'][1:]
        for workout in workouts:
            # print(workout)
            print(workout['workout_image'])
            print(workout['units'])

        # Populate workout grid in home screen



    def change_screen(self, screen_name):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition
        screen_manager.current = screen_name
        #screen_managr = self.root.ids

MainApp().run()
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from workoutbanner import WorkoutBanner
import requests
import json

class HomeScreen(Screen):
    pass

class LabelButton(ButtonBehavior,Label):
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
        # Get and update avatar image
        avatar_image = self.root.ids['avatar_image']
        avatar_image.source = "icons/avatars/" + data['avatar']

        # Get and update streak label
        streak_label = self.root.ids['home_screen'].ids['streak_label']
        streak_label.text = str(data['streak']) + " DAY STREAK!"

        # Get and update friend id label
        friend_id_label = self.root.ids['settings_screen'].ids['friend_id_label']
        friend_id_label.text = "Friend ID:" + str(self.my_friend_id)

        banner_grid = self.root.ids['home_screen'].ids['banner_grid']
        workouts = data['workout'][1:]
        for workout in workouts:
            for i in range(5):
                # Populate workout grid in home screen
                W = WorkoutBanner(workout_image=workout['workout_image'], description=workout['description'],
                                  type_image=workout['type_image'], number=workout['number'], units=workout['units'],
                                  likes=workout['likes'])
                banner_grid.add_widget(W)


    def change_screen(self, screen_name):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition
        screen_manager.current = screen_name
        #screen_managr = self.root.ids

MainApp().run()
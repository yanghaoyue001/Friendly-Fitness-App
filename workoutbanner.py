from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

class WorkoutBanner(GridLayout):
    rows = 1

    def __init__(self, **kwargs):
        super().__init__()

        # Need left FloatLayout
        left = FloatLayout()
        left_image = Image(source = "icons/workouts/" + kwargs['workout_image'], size_hint = (1, 0.8), pos_hint = {"top": 1,"right": 1})
        left_label = Label(text=kwargs['description'], size_hint=(1, .2), pos_hint={"top": .2, "right": 1})
        left.add_widget(left_image)
        left.add_widget(left_label)

        # Need middle FloatLayout
        middle = FloatLayout()
        middle_image = Image(source="icons/" + kwargs['type_image'], size_hint = (1, 0.8), pos_hint = {"top": 1,"right": 1})
        middle_label = Label(text=str(kwargs['number'])+" "+kwargs['units'], size_hint=(1, .2), pos_hint={"top": .2, "right": 1})
        middle.add_widget(middle_image)
        middle.add_widget(middle_label)

        # Need right FloatLayout
        right = FloatLayout()
        right_image = Image(source="icons/likes.png", size_hint = (1, 0.8), pos_hint = {"top": 1,"right": 1})
        right_label = Label(text=str(kwargs['likes']) + " fist bumps", size_hint=(1, .2), pos_hint={"top": .2, "right": 1})
        right.add_widget(right_image)
        right.add_widget(right_label)


        self.add_widget(left)
        self.add_widget(middle)
        self.add_widget(right)




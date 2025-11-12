from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label   #
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 0, 1)   # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)


class DynamicLabelsApp(App):
    name_display = StringProperty()

    def __init__(self, **kwargs):
        """Initialise construct"""
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0499999999"}

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Creates label from dictionary"""
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            temp_label.color = NEW_COLOUR
            self.root.ids.label_box.add_widget(temp_label)
            # add_widget() is a method is used to add a child widget to a parent widget
            # It allows to build complex layouts by nesting widgets inside others
            # Here's a breakdown of how add_widget() works within the context:
            # Parent Widget: The widget to which you want to add another widget.
            # Child Widget: The widget that you want to add to the parent.
            # Example: self.root.ids.label_box.add_widget(temp_label)
            # Parent = self.root.ids.label_box, Child = temp_label


DynamicLabelsApp().run()

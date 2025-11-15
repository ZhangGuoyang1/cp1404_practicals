from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


MAIN_COLOUR = (0, 0.5, 1, 1)     # Blue-ish
SECOND_COLOUR = (1, 0.3, 0.3, 1)  # Light Red


class DynamicLabelsApp(App):
    """Kivy App for dynamic labels."""
    name_display = StringProperty()

    def __init__(self, **kwargs):
        """Initialise construct"""
        super().__init__(**kwargs)
        self.name_to_age = {
            "Alice Aqua": "18",
            "Ben Berry": "21",
            "Cindy Coral": "25",
        }

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels (Inspired Example)"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Creates labels from dictionary"""
        for name in self.name_to_age:
            temp_label = Label(text=name)
            temp_label.color = MAIN_COLOUR
            self.root.ids.label_box.add_widget(temp_label)


DynamicLabelsApp().run()

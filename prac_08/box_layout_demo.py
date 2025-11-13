from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Create root widget to load kv file"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        """Join hello with user input name"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def press_clear(self):
        """Resets both text field and output label to blank"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()

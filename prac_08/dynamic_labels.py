from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES_LIST = ["Bob", "James", "George", "David"]


class DynamicLabelApp(App):
    """Main Program - Kivy app to demo dynamic label creation"""

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Label"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI"""
        for name in NAMES_LIST:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()

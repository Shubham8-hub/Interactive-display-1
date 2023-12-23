"""
This is the main file of the project.


"""

# importing the libraries related to the Kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


# importing the libraries related to the kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

# Common declaration
Company_name = "Yellow Matrix - CAN Dashboard"
window_height = 750
window_width = 1100

class MainApp(MDApp):
    def build(self):
        #Create root widget
        root = MDBoxLayout(orientation='vertical')

        # Add KivyMD components to the root widget
        label = MDLabel(text="Hello, Shubham", halign="center")
        root.add_widget(label)

        return root
    
    # Display the title 
    def on_start(self):
        self.title = Company_name 

        # Set the window size
        Window.size = (window_height, window_width) 
        Window.minimum_height = window_height
        Window.minimum_width = window_width
        # Window.maximum_height = window_height
        # Window.maximum_width = window_width

    
if __name__ == "__main__":
    MainApp().run()
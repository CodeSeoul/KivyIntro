from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button

# MainPage will be our root widget
# The root widget is the widget that contains all other widgets to be displayed
class MainPage(Widget):
    pass

# We've created an UpdateButton widget, inheriting from Button, that will allow
# us to take custom action for button events
class UpdateButton(Button):
    # This is how we can store references to other UI elements
    # See the kv file for more
    output_label = ObjectProperty(None)
    text_input = ObjectProperty(None)

    # on_press is a function from the Button class. It is executed when the user
    # presses on this button object
    def on_press(self):
        # We're going to set our label to the text the user set for our text input
        self.output_label.text = self.text_input.text


# The main class of your project must inherit App
# Kivy recognizes the class name IntroApp. It removes the App portion of the class name
# and looks for a kv file with the same name, in this case intro.kv
class IntroApp(App):

    # Build is the function Kivy runs when starting your application
    def build(self):
        # The build function should return your root Widget
        # The root widget is the main widget that should contain your app
        root = MainPage()
        return root

# This tells Python to construct an IntroApp object instance and execute its run method
# This is required to start your Kivy app
if __name__ == '__main__':
    IntroApp().run()
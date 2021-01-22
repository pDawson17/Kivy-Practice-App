from kivy.app import App
#from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    self.name = ObjectProperty(None)
    self.email = ObjectProperty(None) #links to KV file

    def button_press(self):
        print(self.name.text, self.email.text)

class MyApp2(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp2().run()

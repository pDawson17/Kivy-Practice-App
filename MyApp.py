from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs): #**kwargs allws use of as many variable/children as needed
        super(MyGrid, self).__init__(**kwargs) #calling our own init ig?

        self.inside = GridLayout()
        self.inside.cols = 2 #can assign variables to layouts!

        self.cols = 1
        self.inside.add_widget(Label(text="uname"))
        self.uname = TextInput(multiline=False)
        self.inside.add_widget(self.uname)

        self.inside.add_widget(Label(text="email", font_size=40))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text="password"))
        self.password = TextInput(multiline=False)
        self.inside.add_widget(self.password)

        self.add_widget(self.inside) #add layout inside layout!!

        self.submit = Button(text="submit", font_size=60)
        self.submit.bind(on_press=self.button_press)

        self.add_widget(self.submit)

    def button_press(self,instance):
        print("butttoonnn", self.uname.text, self.email.text, self.password.text)
        self.uname.text = ""
        self.email.text = ""
        self.password.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()

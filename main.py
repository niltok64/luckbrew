# import all classes of guizero cus i'm lazy to add guizero. behind all the classes
from guizero import *

app = App(title="Luckbrew")
logo = Picture(app, image="logo.png")
welcome = Text(app, text="Welcome to Luckbrew!")
app.display()
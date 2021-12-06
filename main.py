# import all classes of guizero cus i'm lazy to add guizero. behind all the classes
from guizero import *

# variables
potion_of_luck = 0
pot_o_luck = 0
luck_nut = 0
luck_bank = 0

app = App(title="Luckbrew")
logo = Picture(app, image="logo.png")
welcome = Text(app, text="Welcome to Luckbrew!")
app.display()
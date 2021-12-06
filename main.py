# import all classes of guizero cus i'm lazy to add guizero. behind all the classes
from guizero import *

# variables
potion_of_luck = 0
pot_o_luck = 0
luck_nut = 0
luck_bank = 0

# functions
def brew():
    info("Brew", ("Thank you for brewing a " + brew_options.value))

# the actual code
app = App(title="Luckbrew")
logo = Picture(app, image="logo.png")
welcome = Text(app, text="Welcome to Luckbrew!")
brew_text = Text(app, text="What would you like to brew?")
brew_options = Combo(app, options=["Potion of Luck", "Pot O\' Luck", "Luck Nut", "Luck Bank"])
brew_button = PushButton(app, text="Brew", command=brew)

app.display()
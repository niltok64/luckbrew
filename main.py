from guizero import *
app = App(title="Luckbrew")
logo = Picture(app, image="logo.png")
welcome = Text(app, text="Welcome to Luckbrew!")
app.display()
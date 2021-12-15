













import turtle as turtle_module
import random

color_list = [(244, 235, 46), (196, 12, 34), (221, 159, 69), (43, 80, 178), (238, 39, 143), (40, 215, 68)]
tim = turtle_module.Turtle()
tim_screen = turtle_module.Screen()
turtle_module.colormode(255)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


tim_screen.exitonclick()


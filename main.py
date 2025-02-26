from turtle import Turtle, Screen
import random

screen = Screen()

canvas_width = 500
canvas_height = 500
screen.screensize(canvas_width, canvas_height)  # Sets the actual drawable area
screen.setworldcoordinates(-canvas_width/2, -canvas_height/2, canvas_width/2, canvas_height/2)


user_bet = screen.textinput(title="Make you Bet", prompt="Which turtle will win the race? Enter a color: ")
is_race_on=False

colors = ["red", "orange", "yellow", "green", "blue","purple"]
y_position=[-60,-40,-20,0,20,40]

turtle_object = []

for i in range(len(colors)):
    turtle_object.append(Turtle(shape="turtle"))
    turtle_object[i].color(colors[i])
    turtle_object[i].penup()
    turtle_object[i].goto(x=-250, y=y_position[i])

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtle_object:
        steps = random.randint(0, 10)
        turtle.forward(steps)
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is winner!")
            is_race_on=False

screen.exitonclick()
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("CornflowerBlue")

for steps in range(4):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()

import turtle
from turtle import Turtle, colormode, Screen
from random import randint, choice

tim = Turtle()
tim.shape("turtle")
tim.color("CornflowerBlue")

# challenge 1
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# challenge 2
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# challenge 3 - my attempt
# 360 / side = angle
# sides = 3
# while sides < 11:
#     angle = round(360 / sides)
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#         tim.forward(100)
#     sides += 1


# challenge 3 - solution
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# def get_rand_color():
#     return tuple(randint(0, 255) for _ in range(3))
#
# challenge 5 - random colors function
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)
#     colormode(255)
#     tim.pencolor(*get_rand_color())


# Challenge 4 - faster, thicker pen, random walk
# my attempt
# tim.speed(10)
# tim.pensize(10)
# for _ in range(300):
#     tim.forward(20)
#     direction = [0, 90, 180, 360]
#     tim.right(choice(direction))
#     tim.forward(20)
#     colormode(255)
#     tim.pencolor(*get_rand_color())

# Challenge 4 - solution
# directions = [0, 90, 180, 360]
# tim.speed("fastest")
# tim.pensize(10)
colormode(255)
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     # for random direction; right, left
#     tim.setheading(choice(directions))

# challenge 6 - draw circle radius of 100, random change of tile,
# continue drawing circle
# my attempt
# tim.speed("fastest")
# for _ in range(40):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.left(10)

# challenge 6 - solution
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()

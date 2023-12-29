# import colorgram
from turtle import Turtle, colormode, Screen
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# my attempt to retrieve colors
# def rgb_colors(all_colors, list_of_colors):
#     for color in all_colors:
#         color_rgb = color.rgb
#         list_of_colors.append(tuple(color_rgb))
#     return list_of_colors

# list_of_color_tups = []
# print(rgb_colors(colors, list_of_color_tups))

# solution to retrieve colors
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, b, g)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# background colors: (233, 232, 233), (231, 237, 233), (236, 233, 231)

colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(224, 227, 233), (207, 82, 160), (54, 130, 88), (145, 40, 91), (140, 49, 26), (221, 105, 207), (132, 203, 177), (158, 83, 46), (45, 104, 55), (169, 39, 160), (129, 143, 189), (83, 44, 20), (37, 67, 43), (186, 107, 94), (187, 170, 140), (85, 180, 120), (59, 31, 39), (88, 92, 157), (78, 165, 153), (194, 73, 79), (45, 78, 74), (80, 44, 74), (161, 218, 201), (57, 121, 125), (219, 187, 175), (169, 172, 206), (219, 169, 182)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


# def horizontal_move():
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.penup()
#         tim.forward(50)
#
#
# for _ in range(10):
#     # tim.goto(0, y_pos)
#     horizontal_move()
#     # y_pos += 50

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()

#day 8 challenge 1
# paint area calculator

import math

def paint_cal(height, width, cover):
    print(f"You'll need {math.ceil((height * width) / cover)} of paint")


wall_height = int(input("Enter wall height: "))
wall_width = int(input("Enter wall width: "))
coverage = 5

paint_cal(wall_height, wall_width, coverage)

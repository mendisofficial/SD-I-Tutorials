# Cuboid Area, Perimeter, and Volume Calculator

import math

length = float(input("Enter the length of a cuboid: "))
width = float(input("Enter the width of a cuboid: "))
height = float(input("Enter the height of a cuboid: "))

area = 2 * (length * width + length * height + width * height)
perimeter_of_base = 2 * (length + width)
volume = length * width * height

print(f"Area: {area:.2f} \nPerimeter of Base: {perimeter_of_base:.2f} \nVolume: {volume:.2f}")
# Volume of a Cylinder

import math

radius = float(input("Enter the radius of a cylinder: "))
height = float(input("Enter the height of a cylinder: "))

volume = math.pi * radius ** 2 * height

print(f"Volume: {volume:.2f}")
import math

# calculates circle 
# R = radius 
# D = diameter

def circleA(size):
    circumference = (math.pi * size)
    return circumference

def circleB(size):
    area = math.pi * (size**2)
    return area



# calculates sphere
# V = volume
# SA = surface area

def sphereA(size):
    volume = (4/3) * math.pi * (size**3)
    return volume

def sphereB(size):
    surfArea = 4 * (math.pi * (size**2))
    return surfArea



# calculates square
# P = perimeter
# A = area

def squareA(size):
    perimeter = 4 * size
    return perimeter

def squareB(size):
    area = size ** 2
    return area



# calculates cube
# V = volume
# SA = surface area

def cubeA(size):
    volume = size ** 3
    return volume

def cubeB(size):
    surfArea = 6 * (size**2)
    return surfArea

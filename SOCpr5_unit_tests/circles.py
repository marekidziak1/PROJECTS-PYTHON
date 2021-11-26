import math
def circle_area(r):
    if r < 0:
        raise ValueError("Cannot be smaller then 0")
    if type(r) not in [float, int]:
        raise TypeError("only int or float")
    return math.pi*(r**2)

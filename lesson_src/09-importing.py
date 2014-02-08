# using "libraries" - other people's classes and functions

# import it
import math

# then use it!
print math.pi
print math.pow(2, 3)
print math.sqrt(4)

# we can use it to make our own classes!
class CircleArea:
    radius = 0
    def __init__(self, radius):
        self.radius = radius
    def setRadius(self, radius):
        self.radius = radius
    def getArea(self):
        return self.radius * self.radius * math.pi

area = CircleArea(7)
print area.getArea()

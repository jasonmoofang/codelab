# make a class
class TriangleArea:
    height = 10
    base = 6
    def setHeight(self, height):
        self.height = height
    def setBase(self, base):
        self.base = base
    def getArea(self):
        return self.height * self.base / 2

area = TriangleArea() # make an object of that class!
print area.getArea()  # call a member function/method
area.setHeight(5)
print area.getArea()
area.setBase(12)
print area.getArea()

class TriangleArea2:
    height = 0
    base = 0
    def __init__(self, height, weight): # use a constructor!
        self.height = height
        self.weight = weight
    def setHeight(self, height):
        self.height = height
    def setBase(self, base):
        self.base = base
    def getArea(self):
        return self.height * self.base / 2

area = TriangleArea2(5, 8) # make an object with constructor arguments!
print area.getArea()
area.setBase(12)
print area.getArea()
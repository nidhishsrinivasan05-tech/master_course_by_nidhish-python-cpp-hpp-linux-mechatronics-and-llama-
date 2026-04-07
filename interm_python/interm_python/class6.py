from dataclasses import dataclass

@dataclass
class University:
    name: str = None
    location: str = None

def relocalize(u: University):
    if u.location == "Kremlin-Bicetre":
        u.location = "Grand Paris"

dta = [University("EPITA", "Kremlin-Bicetre"), University("Sorbonne University", "Paris 5")]

print(f"name = {dta[0].name} where = {dta[0].location}")
print(dta[0])

for u in dta:
    relocalize(u)

print(f"name = {dta[0].name} where = {dta[0].location}")
print(dta[0])

#Points
import math

class Point:
    def __init__(self, xCoord = 0, yCoord = 0):
        self.__xCoord = xCoord
        self.__yCoord = yCoord

    def distance(self, second):
        x_d = self.__xCoord - second.__xCoord
        y_d = self.__yCoord - second.__yCoord
        return (x_d ** 2 + y_d ** 2) ** 0.5
    
    def __str__(self):
        return f"{self.__xCoord, self.__yCoord}"
    
pt1 = Point(0.0, 0.0)
pt2 = Point(3.0, 4.0)

print(pt1)
print(pt2)

distance = pt1.distance(pt2)
print("The distanec: ", distance)


# Circle

class Circle:
    x = 0
    y = 0
    radius = 0
    area = 0
    perimeter = 0

    def __init__(self, x, y, radius):
        self.radius = radius
        self.area = math.pi * radius * radius
        self.perimeter = 2.0 * math.pi * radius
        self.x = x
        self.y = y

    def setRadius(self, radius):
        self.radius = radius
        self.area = math.pi * radius * radius
        self.perimeter = 2.0 * math.pi * radius

    def printCircle(self):
        print(" --- Circle: (x,y) = (%.2f,%.2f): radius = %.2f : area = %.2f : perimeter = %.2f", (self.x, self.y, self.radius, self.area, self.perimeter))

x = Circle(0.0, 0.0, 3.0)
y = Circle(1.0, 2.0, 4.0)
x.printCircle()
y.printCircle()
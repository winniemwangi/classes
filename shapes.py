import math


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        a = math.pi * self.radius**2
        return a

    def circumfrence(self):
        b = 2 * math.pi * self.radius
        return b

class Square:
    def __init__(self,side):
        self.side = side

    def area (self):
        a = self.side**2
        return a
    
    def perimeter(self):
        p = 4 * self.side
        return p

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def area (self):
        a = self.width*self.length
        return a

    def perimeter(self):
        p = 2 * (self.width+self.length)
        return p

class Sphere:
    def __init__(self,radius):
        self.radius = radius

    def surface_Area(self):
        a = 4*math.pi*self.radius**2
        return a

    def volume(self):
        v = 4/3*(math.pi*self.radius**3)
        return v
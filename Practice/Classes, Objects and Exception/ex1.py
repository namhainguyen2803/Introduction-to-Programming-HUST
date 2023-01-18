import math

class Figure:
    def perimeter(self):
        pass
    
    def area(self):
        pass

# These classes are used for the purpose of raising exception, you just need to raise when necessary

class LengthException(Exception):
    pass

class InvalidTriangleException(Exception):
    pass

class Rectangle(Figure):
    def __init__(self, width, height):
        try:
            if width > 0 and height > 0:
                self.width = width
                self.height = height
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2
    
class Circle(Figure):
    def __init__(self, radius):
        try:
            if radius > 0:
                self.radius = radius
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
    def area(self):
        return math.pi * (self.radius**2)
    def perimeter(self):
        return math.pi * self.radius * 2
    
class Triangle(Figure):
    def __init__(self, a, b, c):
        try:
            if a > 0 and b > 0 and c > 0:
                if a + b > c and b + c > a and a + c > b:
                    self.a = a
                    self.b = b
                    self.c = c
                else:
                    raise InvalidTriangleException
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
        except InvalidTriangleException as e:
            print(str(type(e)) + ' was raised')
    def area(self):
        p = self.perimeter()/2
        a = self.a
        b = self.b
        c = self.c
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    def perimeter(self):
        return self.a + self.b + self.c
# rec = Rectangle(-1, 2)
# tri = Triangle(3, 4, 7)
rec = Rectangle(1, 2)
tri = Triangle(3, 4, 5)
print(rec.perimeter())
print(tri.area())
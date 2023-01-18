import math

class Figure:
    def perimeter(self):
        pass
    
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        
    def perimeter(self):
        return (self.width + self.height) * 2
    
    def area(self):
        return self.width * self.height
    
    def set_height(self,a):
        self.height = a
    def set_width(self,b):
        self.width = b
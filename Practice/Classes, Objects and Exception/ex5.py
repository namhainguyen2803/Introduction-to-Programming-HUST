from ex3 import Rectangle

class Square(Rectangle):
    def __init__(self,a):
        self.width = a
        self.height = a
    def set_height(self,b):
        self.height = b
        self.width = b
    def set_width(self, b):
        self.height = b
        self.width = b
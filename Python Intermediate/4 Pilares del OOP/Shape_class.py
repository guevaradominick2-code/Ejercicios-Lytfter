from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod    
    def get_area(self):
        pass

class Circle(Shape):
        
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Negative sizes are not allowed")
        self.radius = radius
    
    def get_area(self):
        return math.pi * (self.radius**2)
    
    def get_perimeter(self):
         return 2 *  math.pi * self.radius

class Square(Shape):
    def __init__(self, height):
        if height < 0:
            raise ValueError("Negative sizes are not allowed")
        self.height = height

    def get_perimeter(self):
        return self.height*4
    
    def get_area(self):
         return self.height**2

class Rectangle(Shape):
        
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Negative sizes are not allowed")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

circle_shape = Circle(10)
print(circle_shape.get_area())
print(circle_shape.get_perimeter())

rectangle_shape = Rectangle(10, 5)
print(rectangle_shape.get_area())
print(rectangle_shape.get_perimeter())

square_shape = Square(10)
print(square_shape.get_area())
print(square_shape.get_perimeter())
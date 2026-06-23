class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)


r_shape = Rectangle(5, 3)
print(r_shape.get_area())       # 15
print(r_shape.get_perimeter())  # 16


class Rectangle():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def get_area(self):
        while True:
            try:
                self.height = int(input('Insert rectangle height: '))
                self.width = int(input('Insert rectangle width: '))
                if self.height < 0 or self.width < 0:
                        raise ValueError
            except ValueError as ex:
                print(f"Error - Text or negative values are not allowed")
                continue
                
            return self.width * self.height
        
    
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter


r_shape = Rectangle()
print(r_shape.get_area())
print(r_shape.get_perimeter())


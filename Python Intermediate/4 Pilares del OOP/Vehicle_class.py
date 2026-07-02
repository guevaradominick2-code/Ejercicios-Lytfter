class Vehicle():

    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
        

    def get_info(self):
        return f"{self._brand} ({self._year})"

class Car(Vehicle):
    def __init__(self, brand, year, type, doors):
        super().__init__(brand, year)
        self._type = type
        self._doors = doors

    def get_info(self):
        return f"{super().get_info()} - Model: {self._type} {self._doors} doors"
    
class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self._type = type

    def get_info(self):
        return f"{super().get_info()} - Model: {self._type}"
    
car = Car("Mitsubishi", 2017, "sedan", 4)
print(car.get_info())

bike = Motorcycle("Yamaha", 2025, "Racing Sport")
print(bike.get_info())

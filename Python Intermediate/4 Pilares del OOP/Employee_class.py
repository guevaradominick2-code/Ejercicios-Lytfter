class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):    
        for letters in name:
            if letters.isdigit():
                raise ValueError("Error - Employee's name must not contain digits")
        self._name = name
        

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Error - Employee's salary must not be negative")
        self._salary = value
        

    def promote(self, increase_percentage):
        self.salary = self.salary * (1 + increase_percentage / 100)

employee_1 = Employee("Karen", 1155000)
employee_1.promote(10)
print(employee_1.salary)


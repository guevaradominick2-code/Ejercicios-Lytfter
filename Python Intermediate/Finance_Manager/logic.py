from validations import validate_date

class Category():

    def __init__(self, name, color):
        self.name = name
        self.color = color

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Invalid category name")

        self._name = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value,str) or not value.startswith("#") or len(value) != 7:
            raise ValueError("Invalid Color Format")
            
        characters_allowed = "0123456789ABCDEF"
        color_code = value[1:]

        for char in color_code.upper():
            if char not in characters_allowed:
                raise ValueError ("Invalid Color Code Format")

        self._color = value

class Movement():

    def __init__(self, title, amount, category, movement_type, date):
        self.title = title
        self.amount = amount
        self.category = category
        self.movement_type = movement_type
        self.date = date

    @property
    def title (self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Invalid Title Name, must be only text.")

        self._title = value.strip()

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, (int,float)) or isinstance(value, bool) or value <= 0:
            raise ValueError ("Invalid Amount, must be only positive numbers.")

        self._amount = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, Category):
            raise ValueError ("Invalid Category")

        self._category = value

    

    @property
    def movement_type(self):
        return self._movement_type

    @movement_type.setter
    def movement_type(self, value):

        allowed_movements = ("Income", "Expense")

        if value not in allowed_movements:
            raise ValueError ("Movement type is not defined")

        self._movement_type = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = validate_date(value)

class FinanceManager():

    def __init__(self):
        self.categories = []
        self.movements = []

    def add_category(self, category):
        if not isinstance(category, Category):
            raise ValueError ("Invalid category")

        for added_categories in self.categories:
            if category.name.strip().upper() == added_categories.name.strip().upper():
                raise ValueError ("This category already exists")

        self.categories.append(category)

    def add_movement(self, movement):

        if not isinstance(movement, Movement):
            raise ValueError("Movement is not valid")

        elif not self.categories:
            raise ValueError("No categories available")

        elif movement.category not in self.categories:
            raise ValueError("Category does not exist")

        else:
            self.movements.append(movement)

    def calculate_income(self):

        total_income = 0

        for information in self.movements:
            if information.movement_type == "Income":
                total_income += information.amount

        return total_income

    def calculate_expense(self):

        total_expense = 0

        for information in self.movements:
            if information.movement_type == "Expense":
                total_expense += information.amount

        return total_expense

    def calculate_balance (self):

        income = self.calculate_income()
        expense = self.calculate_expense()

        total_balance = income - expense

        return total_balance
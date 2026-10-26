from validations import validate_date, validate_amount


class Category:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if not isinstance(value, str) or not value.strip():
            raise ValueError(
                "Invalid category name"
            )

        self._name = value.strip()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):

        if not isinstance(value, str):
            raise ValueError(
                "Invalid Color Format"
            )

        value = value.strip().upper()

        if (
            not value.startswith("#")
            or len(value) != 7
        ):
            raise ValueError(
                "Invalid Color Format"
            )

        allowed = "0123456789ABCDEF"

        for char in value[1:]:

            if char not in allowed:
                raise ValueError(
                    "Invalid Color Code Format"
                )

        self._color = value


class Movement:

    def __init__(
        self,
        title,
        amount,
        category,
        movement_type,
        date
    ):

        self.title = title
        self.amount = amount
        self.category = category
        self.movement_type = movement_type
        self.date = date

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):

        if (
            not isinstance(value, str)
            or not value.strip()
        ):
            raise ValueError(
                "Invalid Title Name, must be only text."
            )

        self._title = value.strip()

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):

        if (
            not isinstance(value, (int, float))
            or isinstance(value, bool)
            or value <= 0
        ):
            raise ValueError(
                "Invalid Amount, must be only positive numbers."
            )

        self._amount = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):

        if not isinstance(value, Category):
            raise ValueError(
                "Invalid Category"
            )

        self._category = value

    @property
    def movement_type(self):
        return self._movement_type

    @movement_type.setter
    def movement_type(self, value):

        if value not in (
            "Income",
            "Expense"
        ):
            raise ValueError(
                "Movement type is not defined"
            )

        self._movement_type = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):

        if (
            hasattr(value, "strftime")
            and not isinstance(value, str)
        ):
            value = value.strftime(
                "%d/%m/%Y"
            )

        self._date = validate_date(value)


class FinanceManager:

    def __init__(self):
        self.categories = []
        self.movements = []

    def add_category(self, category):

        if not isinstance(category, Category):
            raise ValueError(
                "Invalid category"
            )

        for existing in self.categories:

            if (
                category.name.casefold()
                == existing.name.casefold()
            ):
                raise ValueError(
                    "This category already exists"
                )

        self.categories.append(category)

    def create_category(
        self,
        name,
        color
    ):

        category = Category(
            name,
            color
        )

        self.add_category(category)

        return category

    def find_category(
        self,
        category_name
    ):

        if (
            not isinstance(category_name, str)
            or not category_name.strip()
        ):
            raise ValueError(
                "Please select a category"
            )

        wanted = (
            category_name
            .strip()
            .casefold()
        )

        for category in self.categories:

            if (
                category.name.casefold()
                == wanted
            ):
                return category

        raise ValueError(
            "Category not found"
        )

    def add_movement(self, movement):

        if not isinstance(
            movement,
            Movement
        ):
            raise ValueError(
                "Movement is not valid"
            )

        if not self.categories:
            raise ValueError(
                "No categories available"
            )

        if (
            movement.category
            not in self.categories
        ):
            raise ValueError(
                "Category does not exist"
            )

        self.movements.append(
            movement
        )

    def create_movement(
        self,
        title,
        amount,
        category_name,
        movement_type,
        movement_date
    ):

        if not self.categories:
            raise ValueError(
                "No categories available"
            )

        numeric_amount = validate_amount(
            amount
        )

        category = self.find_category(
            category_name
        )

        movement = Movement(
            title,
            numeric_amount,
            category,
            movement_type,
            movement_date
        )

        self.add_movement(
            movement
        )

        return movement

    def filter_movements(
        self,
        start_date_text,
        end_date_text
    ):

        if (
            not isinstance(
                start_date_text,
                str
            )
            or not start_date_text.strip()
        ):
            raise ValueError(
                "Please enter the start date"
            )

        if (
            not isinstance(
                end_date_text,
                str
            )
            or not end_date_text.strip()
        ):
            raise ValueError(
                "Please enter the end date"
            )

        start_date = validate_date(
            start_date_text
        )

        end_date = validate_date(
            end_date_text
        )

        if start_date > end_date:
            raise ValueError(
                "Start date cannot be after end date"
            )

        return [
            movement
            for movement in self.movements
            if (
                start_date
                <= movement.date
                <= end_date
            )
        ]

    def calculate_income(
        self,
        movements=None
    ):

        source = (
            self.movements
            if movements is None
            else movements
        )

        return sum(
            movement.amount
            for movement in source
            if (
                movement.movement_type
                == "Income"
            )
        )

    def calculate_expense(
        self,
        movements=None
    ):

        source = (
            self.movements
            if movements is None
            else movements
        )

        return sum(
            movement.amount
            for movement in source
            if (
                movement.movement_type
                == "Expense"
            )
        )

    def calculate_balance(
        self,
        movements=None
    ):

        return (
            self.calculate_income(
                movements
            )
            -
            self.calculate_expense(
                movements
            )
        )

    def clear_history(self):
        self.movements.clear()
from datetime import date
from functools import wraps


class User():
    def __init__(self, birthday_date):
        if not isinstance(birthday_date, date):
            raise TypeError("birthday_date is in YYYY,MM,DD")

        self.birthday_date = birthday_date

    @property
    def age(self):
        today = date.today()

        age = today.year - self.birthday_date.year

        if (today.month, today.day) < (
            self.birthday_date.month,
            self.birthday_date.day
        ):
            age -= 1

        return age


def adult_required(function):
    @wraps(function)
    def wrapper(user, *args, **kwargs):

        if not isinstance(user, User):
            raise TypeError("Enter a User as first arg")

        if user.age < 18:
            raise ValueError("Error - User is under-age")

        return function(user, *args, **kwargs)

    return wrapper

@adult_required
def enter_bar(user):
    print(f"Access granted. User is {user.age} years old.")


user_1 = User(date(2001, 8, 28))
user_2= User(date(2021,1,1))

print(user_1.age)
enter_bar(user_1)

print(user_2.age)
try:
    enter_bar(user_2)
except ValueError as error:
    print(error)
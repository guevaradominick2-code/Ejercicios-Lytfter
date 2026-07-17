import numbers
import functools

def only_numbers(function):
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, numbers.Number):
                raise TypeError("Error you can not enter letters in this option")
        for i in kwargs.values():
            if not isinstance(i, numbers.Number):
                raise TypeError("Error you can not enter letters in this option")
        result = function(*args, **kwargs)
        return result
    return wrapper

@only_numbers
def number_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print(number_sum(1,2,3))
print(number_sum( x=14, y=100))
print(number_sum(12, "Once"))


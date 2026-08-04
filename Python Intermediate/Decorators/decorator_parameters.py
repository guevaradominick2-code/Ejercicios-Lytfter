def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Parameters: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print (f"Return: {result}")
        return result
    return wrapper
@log_function
def sum_decorator(a,b):
    return a + b

sum_decorator(3, 5)

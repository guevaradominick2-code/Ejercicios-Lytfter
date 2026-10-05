from datetime import datetime

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance (arg, int) and not isinstance(arg, float):
                raise Exception("Only numerical values are allowed...")
        for kwarg in kwargs.values():
            if not isinstance (kwarg, int) and not isinstance(kwarg, float):
                raise Exception("Only numerical values are allowed...")
        result =func(*args, **kwargs)
        return result
    return wrapper

def log_call(func):
    def wrapper(*args, **kwargs):
        result =func(*args, **kwargs)
        print(f"Function:{func.__name__} // Args: {args[0]},{args[1]}// Date: {datetime.now()} // Result: {result}")
        return result
    return wrapper

@log_call
@validate_numbers
def multiply(a,b):
    return a * b

result = multiply(78, 15)
print(f"Result: {result}")


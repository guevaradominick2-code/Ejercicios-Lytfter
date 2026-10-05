def repeat_twice(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

@repeat_twice
def meet(name):
    print(f"Hi, {name}" )

meet("Dom")
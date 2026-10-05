user_logged_in = False

def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise Exception("User needs to be logged first")
        result = func(*args, **kwargs)
        return result
    return wrapper

@requires_login
def view_profile():
    print("Showing user profile...")

user_logged_in = True
view_profile()

user_logged_in = False
view_profile()
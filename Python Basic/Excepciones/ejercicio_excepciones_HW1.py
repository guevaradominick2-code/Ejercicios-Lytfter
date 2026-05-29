def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("ERROR: CANNOT DIVIDE BY ZERO")
        return None
    return a / b


def show_menu():
    option = input("""
Menu:
    1. Sum
    2. Subtraction
    3. Multiplication 
    4. Division
    5. Clear
    6. Close Calculator
------------------------------------------------------------
Enter the number or name of the operation you want to perform: """).lower()
    return option


def get_number():
    try:
        number = float(input("Enter number: "))
        return number
    except ValueError:
        print("ERROR: ENTER A VALID NUMBER")
        return None


def show_result(number):
    print(f"\nCurrent number: {number}")


def calculator_logic():
    current_number = 0
    running = True
    
    while running:
        show_result(current_number)
        option = show_menu()
        
        if option == "1" or option == "sum":
            number2 = get_number()
            if number2 is not None:
                current_number = add(current_number, number2)
                print(f"Result: {current_number}")
                
        elif option == "2" or option == "subtraction":
            number2 = get_number()
            if number2 is not None:
                current_number = subtract(current_number, number2)
                print(f"Result: {current_number}")
                
        elif option == "3" or option == "multiplication":
            number2 = get_number()
            if number2 is not None:
                current_number = multiply(current_number, number2)
                print(f"Result: {current_number}")
                
        elif option == "4" or option == "division":
            number2 = get_number()
            if number2 is not None:
                result = divide(current_number, number2)
                if result is not None:
                    current_number = result
                    print(f"Result: {current_number}")
                    
        elif option == "5" or option == "clear":
            current_number = 0
            print("Result cleared")
            
        elif option == "6" or option == "close calculator":
            print("Closing calculator...")
            running = False
            
        else:
            print("The operation you requested is not in the menu")


calculator_logic()
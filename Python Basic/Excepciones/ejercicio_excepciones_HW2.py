

def ask_name():
    return input("Ingrese el nombre: ")

def ask_age():
    return input("Ingrese su edad: ")


def validate_name(name):
    
    if name.isdigit():
        return False
    return True

def validate_age(age):
    try:
        int(age)
        return True
    except ValueError:
        return False


def get_valid_name():
    while True:
        name = ask_name()
        if validate_name(name):
            return name
        print("ERROR: El nombre no puede ser un número")

def get_valid_age():
    while True:
        age = ask_age()
        if validate_age(age):
            return int(age)
        print("ERROR: La edad debe ser un número")



def main():
    name = get_valid_name()
    age = get_valid_age()
    print(f"Hola, te llamas {name} y tienes {age} años")


main()

print(60*"-")
#--------------------------------------------------------------------------------------------------------------
def ask_list():
    
    user_input = input("Inserte la lista de strings separados por un guion: ")
    return user_input.split("-")


def integer_converter(my_list):
    
    results = []
    for item in my_list:
        try:
            converted = int(item)
            results.append(f"{item} convertido a {converted}")
        except ValueError:
            results.append(f"No se pudo convertir el string: {item}")
    return results


def show_results(results):
    
    print("Resultado:")
    for line in results:
        print(line)


def main2():
    my_list = ask_list()
    results = integer_converter(my_list)
    show_results(results)


main2()
print(60*"-")
#--------------------------------------------------------------------------------------------------------------
def ask_list():
    
    user_input = input("Inserte la lista de elementos separados por un guion: ")
    return user_input.split("-")


def values_sum(my_list):
    
    new_list = []
    total_sum = 0
    for item in my_list:
        try:
            converted = float(item)
            total_sum += converted
            new_list.append(f"{converted} sumado correctamente")
        except ValueError:
            new_list.append(f"Elemento inválido: {item}")
    return new_list, total_sum


def show_results(new_list, total_sum):
    """Muestra los resultados"""
    for line in new_list:
        print(line)
    print(f"Total de la suma de floats: {total_sum}")


def main3():
    my_list = ask_list()
    new_list, total_sum = values_sum(my_list)
    show_results(new_list, total_sum)


main3()
print(f"-Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda-")
print(60*"-")
def greetings():
    print ("Hola Team")
    bye()

def bye():
    print("Adios")


greetings()
print(60*"-")
#-------------------------------------------------------------------------------------------
print("""-Experimente con el concepto de scope:
Intente acceder a una variable definida dentro de una función desde afuera.
Intente acceder a una variable global desde una función y cambiar su valor-""")
print(60*"-")
def inside_variable():
    variable_type =  "This is my inside variable"
    print(variable_type)

inside_variable()

#print(variable_type)  # Error: NameError
# Nota: La variable solo existe dentro de la función

name = "Dominick"

def global_variable_sin_global():
    name = "Andrey"  # ← Esto crea una variable LOCAL nueva
    print(f"Dentro de la función: {name}")

print(f"Antes de la función: {name}")
global_variable_sin_global()
print(f"Después de la función: {name}")
# Nota: La variable original NO cambió porque Python creó una local

# --- 2b: Variable global CON global ---
def global_variable_con_global():
    global name
    name = "Andrey"
    print(f"Dentro de la función: {name}")

global_variable_con_global()
print(f"Después de usar global: {name}")
print(60*"-")
#-------------------------------------------------------------------------------------
print(f"""Cree una función que retorne la suma de todos los números de una lista.
La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
[4, 6, 2, 29] → 41""")
print(60*"-")

number_list = [4, 6, 2, 29]

def summary_list(number_list):
    return sum(number_list)  

result = summary_list(number_list)


summary_list(number_list)

print(result)
print(60*"-")

#------------------------------------------------------------------------------------

print(f"""Cree una función que le dé la vuelta a un string y lo retorne.
#Esto ya lo hicimos en iterables.
#“Hola mundo” → “odnum aloH” """)
print(60*"-")

my_string = input("Inserte la palabra que desea ver al reves: ")

def invert_string(my_string):
    invert = (my_string[::-1])
    return invert

print(f"Tu palabra invertida es: {invert_string(my_string)}")
print(60*"-")

#-----------------------------------------------------------------------------------

print(f"""Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
I love Nación Sushi → Theres 3 upper cases and 13 lower cases""")
print(60*"-")
sentence = input("Inserte la palabra para averiguar cuantas mayusculas y minisculas tiene: ")

def upper_lower_counter(sentence):
    uppers = 0 
    lowers = 0

    for letters in sentence:
        if letters.isupper():
            uppers += 1
        elif letters.islower():
            lowers += 1
    return uppers, lowers

uppers, lowers = upper_lower_counter(sentence)

print(f"{sentence}: tiene {uppers} mayusculas y {lowers} minisculas")

upper_lower_counter(sentence)
print(60*"-")

#----------------------------------------------------------------------------------

print(f"""Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.x =  len(my_string)
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.""")
print(60*"-")

words = input("Inserte la lista de palabras que desea agregar a la lista: ")

def sentences_ordered(words):
    words_list = words.split("-")
    words_list.sort()
    new_order = "-".join(words_list)

    return new_order

print (f"El orden alfabetico de las palabras {words} es: {sentences_ordered(words)}")
print(60*"-")

#---------------------------------------------------------------------------------
print(f"""Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.""")
print(60*"-")

def number_list():
    number_list = []
    numbers_qty = int(input("Cantidad de numeros: "))
    
    for i in range(numbers_qty):
        n = int(input("Number: "))
        number_list.append(n)
    
    return number_list

def prime_number(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def primes_sort(list1):
    primes = []
    for number in list1:
        if prime_number(number):
            primes.append(number)
    return primes


my_list = number_list()
primes = primes_sort(my_list)

if primes:
    print(f"De la Lista {my_list} solo estos son primos: {primes}")
else:
    print(f"La Lista {my_list} no tiene números primos")
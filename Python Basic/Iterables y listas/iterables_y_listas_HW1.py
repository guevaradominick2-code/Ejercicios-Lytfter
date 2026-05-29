#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

index = len(first_list)

for actual_index in range(index):
    print(f"{first_list[actual_index]} {second_list[actual_index]}")

#--------------------------------------------------------------------------------
#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = "Pizza con piña"

index = len(my_string)

for actual_index in range(index - 1, -1, -1):
    print(my_string[actual_index])

#--------------------------------------------------------------------------------
#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

my_list = [4, 3, 6, 1, 7]

first_element = my_list[0]
last_element = my_list[-1]

my_list[0] = last_element
my_list[-1] = first_element

print(my_list)

#--------------------------------------------------------------------------------
#Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pair_numbers = [] 

for number in my_list:
    if number % 2 == 0: 
        pair_numbers.append(number) 

print(pair_numbers) 
#-----------------------------------------------------------------------------------
#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
number_required = 10
numbers_entered = 1
number_by_user = 0
numbers_list = []

while numbers_entered <= number_required:
    number_by_user= int(input(f"Ingrese el {numbers_entered}º numero de 10: "))
    numbers_entered += 1
    numbers_list.append (number_by_user)

highest_number = max(numbers_list)

print (f"{numbers_list}: El numero mayor de esa lista es {highest_number} ")



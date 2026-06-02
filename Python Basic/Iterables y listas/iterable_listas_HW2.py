#Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar

my_list = []

number_of_elements = int(input("¿Cuántos números desea ingresar en la lista? "))
counter = 1
number_entered = 0

while counter <= number_of_elements:
    if number_of_elements == 1 :
        number_entered = int (input(f"Inserte el numero que desea ingresar: "))
        my_list.append(number_entered)
        counter += 1
    else:
        number_entered = int(input(f"Inserte el {counter}º de los {number_of_elements} que desea ingresar: "))
        my_list.append(number_entered)
        counter += 1

search_number = int(input(f"Inserte el numero que desea buscar: "))
search_number_counter = 0

for number in my_list:
    if number == search_number:
        search_number_counter += 1


print (f"El numero {search_number} aparece {search_number_counter} veces.") 
print("--"*60)
#--------------------------------------------------------------------------------------------------------------------
#Cree un programa que verifique si todos los elementos de una lista son positivos

my_list2 = [3, 6, 0, -2, 4]

positive_check = True

for numbers in my_list2:
    if numbers <= 0:
        positive_check = False
        
        break 
    
if positive_check:
    print(f"Todos los numeros en la lista son positivos")  
else:
    print(f"Hay al menos un número negativo o cero")   

print("--"*60)

#----------------------------------------------------------------------------------------------------------------------
#Cree un programa que muestre el valor más pequeño de una lista sin usar min().

my_list3 = [9, 4, 7, 1, 5]

lower_value = my_list3[0]

for numbers3 in my_list3:
    if numbers3 < lower_value:
        lower_value = numbers3
    


print (f"{lower_value} es el numero menor en la lista")
print("--"*60)

#--------------------------------------------------------------------------------------------------------------------
#Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio
numbers_entered2 = input(f"Inserte la lista de numeros que desea incluir (separelos por un espacio): ")
numbers_divided = numbers_entered2.split()
my_list4 = list(map(int, numbers_divided))

index = len(my_list4)
sum_total = sum(my_list4)

average = sum_total / index
my_list_new = []

for values in my_list4:
    if average < values:
        my_list_new.append(values)

print(f"Promedio: {average}")
print (f"Nueva lista: {my_list_new}")
print("--"*60)     

#--------------------------------------------------------------------------------------------------------------------
#Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

my_list5 = []
counter = 1
quantity = 0
new_list_2 = []

while counter <= 5:
    sentence = input(f"Insert la {counter}ª palabra de 5: ")
    my_list5.append(sentence)
    counter += 1

for letters in my_list5:
    quantity = len(letters)
    if quantity > 4 :
        new_list_2.append(letters)

print (new_list_2) 
print("--"*60) 


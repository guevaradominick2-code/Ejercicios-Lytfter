#Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

#string + string → "Hola" + "Mundo" → "HolaMundo"
#string + int → "Hola" + 5 → Error
#int + string → 5 + "Hola" → Error
#list + list → [1, 2] + [3, 4] → [1, 2, 3, 4]
#string + list → "Hola" + [1, 2] → Error
#float + int →  3.5 + 2 → 5.5
#bool + bool → True + False → 1

#------------------------------------------------------------------------------------------------

name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))

if age <= 1:
    print(f" {name} {last_name}, eres un bebe.")
elif age <= 9:
   print (f"{name} {last_name}, eres un niño")
elif age <= 12:
    print(f" {name} {last_name}, eres un preadolescente.")
elif age <= 18:
    print(f" {name} {last_name}, eres un adolescente.")
elif age <= 25:
    print(f" {name} {last_name}, eres un adulto joven.")
elif age <= 60:
    print(f" {name} {last_name}, eres un adulto.")
else:
    print(f" {name} {last_name}, eres un adulto mayor.")

#---------------------------------------------------------------------------------
#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

import random
secret_number = random.randint(1, 10)
while True:
    Number_by_user = int(input("Adivina el numero secreto entre 1 y 10: "))
    if Number_by_user == secret_number:
        print("¡Felicidades! Has adivinado el numero secreto.")
        break
    else:
        print("Intenta de nuevo.")
#--------------------------------------------------------------------------------
#Cree un programa que le pida tres números al usuario y muestre el mayor.
number1= int(input("Ingrese el primer numero: "))
number2= int(input("Ingrese el segundo numero: "))
number3= int(input("Ingrese el tercer numero: "))

if number1 > number2 and number1 > number3:
    print(f"El numero mayor es: {number1}")
elif number2 > number1 and number2 > number3:
    print(f"El numero mayor es: {number2}")
else:
    print(f"El numero mayor es: {number3}")
#--------------------------------------------------------------------------------
#Dada n cantidad de notas de un estudiante, calcular:

total_scores = int(input("Ingrese la cantidad de notas: "))

score_count = 1
approved_scores = 0
non_approved_scores = 0

overall_score = 0

sum_approved = 0.0
sum_non_approved = 0.0

average_approved = 0.0
average_non_approved = 0.0
average_overall_scores = 0.0

while score_count <= total_scores:
    score = float(input(f"Ingrese la nota {score_count}: "))
    overall_score = overall_score + score
    score_count = score_count + 1
    
    if score >= 70:
        approved_scores = approved_scores + 1
        sum_approved = sum_approved + score
    else:
        non_approved_scores = non_approved_scores + 1
        sum_non_approved = sum_non_approved + score


if approved_scores > 0:
    average_approved = sum_approved / approved_scores
else:
    average_approved = 0 

if non_approved_scores > 0:
    average_non_approved = sum_non_approved / non_approved_scores
else:
    average_non_approved = 0 


if total_scores > 0:
    average_overall_scores = overall_score / total_scores
else:
    average_overall_scores = 0

print(f"Cantidad de notas aprobadas: {approved_scores}")
print(f"Cantidad de notas no aprobadas: {non_approved_scores}")


print(f"Promedio de notas aprobadas: {average_approved:.2f}")
print(f"Promedio de notas no aprobadas: {average_non_approved:.2f}") 


if average_overall_scores >= 70:
    
    print(f"Promedio general de notas: {average_overall_scores:.2f} - El estudiante ha aprobado el curso")
else:
    print(f"Promedio general de notas: {average_overall_scores:.2f} - El estudiante no ha aprobado el curso")





#Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#Si el precio es menor a 100, el descuento es del 2%.
#Si el precio es mayor o igual a 100, el descuento es del 10%.
#Ejemplos:
#120 → 108
#40 → 39.2

price = float(input("Ingrese el precio del producto: "))

if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10

final_price = price - discount
print(f"El precio final es: {final_price}")

#---------------------------------------------------------------------------------------------------------------
#Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos.
#Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos.
#Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.

#1040 → Mayor
#140 → 460
#600 → Igual
#599 → 1

ten_minutes = 600
seconds_in_minutes = 60
time = int(input("Ingrese el tiempo en segundos: "))

if time == ten_minutes:
    print("Igual")
elif time < ten_minutes:
    print(f"Faltan {ten_minutes - time} segundos para llegar a 10 minutos")
else:
    print("Mayor")  
 #---------------------------------------------------------------------------------------------------------------
#Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado.
#Luego muestre el resultado de la suma.

#5 → 15 (1 + 2 + 3 + 4 + 5)
#3 → 6 (1 + 2 + 3)
#12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

number = int(input("Ingrese un número: "))
total_sum = 0
counter = 1
while counter <= number:
    total_sum += counter
    counter = counter + 1

print(f"La suma de los números del 1 al {number} es: {total_sum}")

#---------------------------------------------------------------------------------------------------------------
#Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, y le pida al usuario adivinar ese número.
# El algoritmo no debe terminar hasta que el usuario adivine el numero.

import random

secret_number = random.randint(1,10)

guess = int(input("Adivina el número secreto (entre 1 y 10): "))

while guess != secret_number:
    print("¡Incorrecto! Intenta de nuevo.")
    guess = int(input("Adivina el número secreto (entre 1 y 10): "))

if guess == secret_number:
    print("¡Felicidades! Has adivinado el número secreto.")

#---------------------------------------------------------------------------------------------------------------
#Cree un diagrama de flujo que pida 3 números al usuario.
#Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.

#23, 30, 768 → Correcto (hay un 30)
#10, 15, 5 → Correcto (10 + 15 + 5 = 30)
#35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 == 30 or num2 == 30 or num3 == 30 or (num1 + num2 + num3) == 30:
    print("Correcto")
else:
    print("Incorrecto")

#----------------------------------------------------------------------------------------------------------------
###Convertidor de unidades de temperatura
#Pida al usuario ingresar una temperatura en Celsius
#Conviértala a Fahrenheit y Kelvin

#Muestre los tres valores

celsius = float(input("Ingrese la temperatura en Celsius: "))

fanhrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15

print(f"Temperatura en Celsius: {celsius}°C")
print(f"Temperatura en Fahrenheit: {fanhrenheit}°F")
print(f"Temperatura en Kelvin: {kelvin}K")

#----------------------------------------------------------------------------------------------------------------
#Tabla de multiplicar personalizada
#Pida al usuario un número del 1 al 10
#Muestre su tabla de multiplicar del 1 al 12

table = int(input("Ingrese un número del 1 al 10 para mostrar su tabla de multiplicar: "))

multiplication_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for number in multiplication_number:
    result = table * number
    print(f"{table} x {number} = {result}")


#Cree una funcion que reciba un texto y un caracter y retorne cuantas veces aparece el caracter en el texto
#-----------------------------------------------------------------------------------------------------------

text = input("Inserte el texto: ")
search = input("Inserte el caracter que desea ubicar en el texto: ")

def character_counter(text, search):
    
    counter = 0

    for character in text:
        if character.lower() == search:
            counter += 1

    return counter

total_count = character_counter(text, search)

if total_count > 0:
    print(f"El caracter que buscas aparece {total_count}")
else:
    print(f"El caracter que buscas no se ha encontrado en el texto")

#-------------------------------------------------------------------------------------------------------------------
#Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras

words = input("Introduzca todas las palabras separadas por un guion (-): ")
words_list = words.split("-")
letters = int(input("Inserte la cantidad de caracteres mínima: ")) 

def filter_by_length(words_list, letters):  
    new_list = []

    for word in words_list:
        if len(word) > letters:
            new_list.append(word)
        
    return new_list

characters_list = filter_by_length(words_list, letters)

if characters_list:
    print (f"Solo las siguientes palabras cuentan con una cantidad superior de letras a las que buscas: {characters_list}")
else:
    print ("No existen palabras con esa cantidad de letras")

#-------------------------------------------------------------------------------------------------------------------
#Cree una función que reciba un string y retorne cuántas vocales contiene

string = input("Introduzca la palabra para buscar cuantas palabras tiene: ")

def vocal_counter(string):

    v_counter = 0

    for letter in string:
        if letter.lower() in "aeiou":
            v_counter += 1

    return v_counter

total_vocals = vocal_counter(string)

if total_vocals > 0:
    print (f"La palabra {string} contiene {total_vocals} vocales")
else: 
    print (f"la palabra {string} no tiene vocales")
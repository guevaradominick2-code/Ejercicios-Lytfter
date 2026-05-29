#Cree un diccionario que guarde la siguiente información sobre un hotel:

hotels_list= {
    "name" : "New Yorker",
    "stars": 3,
    "rooms": [{"number" : 125, "floor" : 5, "price" : 149.99},
              {"number" : 135, "floor" : 5, "price" : 149.99},
              {"number" : 78, "floor" : 3, "price" : 99.99}
              ]
       
}

print(hotels_list["rooms"][2]["price"])
print(60*"__")

#--------------------------------------------------------------------------------------------------------------
#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

list_a = ["first_name", "last_name", "role"]

list_b = ["Dom", "Guevara", "Software Engineer"]

information_dict = {}

for i in range (len(list_a)):
    information_dict [list_a[i]] = list_b[i]

print(information_dict)
print(60*"__")
#--------------------------------------------------------------------------------------------------------------
#Cree un programa que use una lista para eliminar keys de un diccionario.

list_of_key = ["access_level","age" ]
employee = { "name": "John",
            "email": "jonh@ecorp.com",
            "access_level" : 5,
            "age" : 28
            }

for key in list_of_key:
    employee.pop(key)


print(employee)
print(60*"__")




def bubble_sort(numbers):
    n = len(numbers)

    # Primer ciclo: recorre la lista varias veces
    for i in range(n - 1):

        # Segundo ciclo: compara elementos vecinos
        # Al estar dentro de otro ciclo, la complejidad es O(n^2)
        for j in range(n - 1 - i):

            if numbers[j] > numbers[j + 1]:

                # Intercambio de elementos
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers


# Complejidad temporal:
# O(n^2)
# Porque existen dos ciclos anidados que dependen del tamaño de la lista.

#---------------------------------------------------------------------------------------------------
def print_numbers_times_2(numbers_list):

    # Recorre cada elemento de la lista una sola vez
    for number in numbers_list:
        print(number * 2)


# Complejidad temporal:
# O(n)
# Porque el ciclo se ejecuta una vez por cada elemento de la lista.

#-------------------------------------------------------------------------------------------------
def check_if_lists_have_an_equal(list_a, list_b):

    # Recorre todos los elementos de list_a
    for element_a in list_a:

        # Por cada elemento de list_a,
        # recorre todos los elementos de list_b
        for element_b in list_b:

            # Compara ambos elementos
            if element_a == element_b:
                return True

    return False


# Complejidad temporal:
# O(n^2), si ambas listas tienen aproximadamente el mismo tamaño.
#
# Más precisamente sería O(n * m),
# donde n es el tamaño de list_a
# y m es el tamaño de list_b.
#
# El mejor caso puede ser O(1) si encuentra
# una coincidencia inmediatamente.

#----------------------------------------------------------------------------------------
def print_10_or_less_elements(list_to_print):

    # Obtiene el tamaño de la lista
    list_len = len(list_to_print)

    # Recorre como máximo 10 elementos
    for index in range(min(list_len, 10)):
        print(list_to_print[index])


# Complejidad temporal:
# O(1)
#
# Aunque la lista tenga 100, 1000 o 1,000,000 de elementos,
# el ciclo nunca se ejecuta más de 10 veces.
#
# Por eso el número máximo de operaciones es constante.

#------------------------------------------------------------------------------
def generate_list_trios(list_a, list_b, list_c):

    result_list = []

    # Primer ciclo
    for element_a in list_a:

        # Segundo ciclo anidado
        for element_b in list_b:

            # Tercer ciclo anidado
            for element_c in list_c:

                # Genera una combinación usando un elemento de cada lista
                result_list.append(
                    f'{element_a} {element_b} {element_c}'
                )

    return result_list


# Complejidad temporal:
# O(n^3), si las tres listas tienen aproximadamente el mismo tamaño.
#
# Existen tres ciclos anidados:
# n * n * n = n^3
#
# Más precisamente sería O(a * b * c),
# dependiendo del tamaño de cada lista.

#------------------------------------------------------------------------------------
# BIG O DE LOS ALGORITMOS

# bubble_sort
# O(n^2)

# print_numbers_times_2
# O(n)

# check_if_lists_have_an_equal
# O(n^2)

# print_10_or_less_elements
# O(1)

# generate_list_trios
# O(n^3)
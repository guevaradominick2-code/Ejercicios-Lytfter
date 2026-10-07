def summary_list(number_list):
    return sum(number_list)  

#------------------------------------------------------------------------------------
def invert_string(my_string):
    invert = (my_string[::-1])
    return invert

#-----------------------------------------------------------------------------------
def upper_lower_counter(sentence):
    uppers = 0 
    lowers = 0

    for letters in sentence:
        if letters.isupper():
            uppers += 1
        elif letters.islower():
            lowers += 1
    return uppers, lowers

#----------------------------------------------------------------------------------
def sentences_ordered(words):
    words_list = words.split("-")
    words_list.sort()
    new_order = "-".join(words_list)

    return new_order

#---------------------------------------------------------------------------------
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
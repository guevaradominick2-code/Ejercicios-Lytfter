
def summary_list(number_list):
    return sum(number_list)  

#---------------------------------------------------------------------------------------------------------------def invert_string(my_string):
def invert_string(my_string):
    invert = (my_string[::-1])
    return invert

#---------------------------------------------------------------------------------------------------------------------------------------
def upper_lower_counter(sentence):
    uppers = 0 
    lowers = 0

    for letters in sentence:
        if letters.isupper():
            uppers += 1
        elif letters.islower():
            lowers += 1
    return uppers, lowers
def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n-1):
        for j in range(n - 1 - i):

            if numbers[j] > numbers [j + 1]:
                temp = numbers[j]
                numbers [j] = numbers [j + 1]
                numbers[j + 1] = temp

    return numbers
    

numbers = [5,15,20,25,10,11,12]
print(bubble_sort(numbers))


#--------------------------------------------------------------------------------------------------------------'

def bubble_sort_reverse_direction(numbers):
    n = len(numbers)

    for i in range(n - 1):

        for j in range(n - 1, i, -1):

            if numbers[j] < numbers[j - 1]:
                temp = numbers[j]
                numbers[j] = numbers[j - 1]
                numbers[j - 1] = temp

    return numbers


numbers = [5, 3, 8, 1, 4]

print(bubble_sort_reverse_direction(numbers))
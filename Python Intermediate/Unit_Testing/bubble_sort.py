def bubble_sort(numbers):
    
    n = len(numbers)

    for i in range(n-1):
        for j in range(n - 1 - i):

            if numbers[j] > numbers [j + 1]:
                temp = numbers[j]
                numbers [j] = numbers [j + 1]
                numbers[j + 1] = temp

    return numbers


'''
The function max() from exercise 1) and the function max_of_three() from exercise 2)
will only work for two and three numbers, respectively.
But suppose we have a much larger number of numbers,
or suppose we cannot tell in advance how many they are?
Write a function max_in_list() that takes a list of numbers and returns the largest one.
'''

list_numbers = [4,2,5,2121,3,2]

def max_in_list(a_list):
    max_number = 0
    for i in a_list:
        if i > max_number:
            max_number = i

    return max_number
print max_in_list(list_numbers)
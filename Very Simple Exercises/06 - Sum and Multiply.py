'''
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
'''

your_list = [1,2,3,4]
def sum(your_list):
    sum_of_list = 0
    for i in your_list:
        sum_of_list += i
    print(sum_of_list)

def multiply(your_list):
    sum_of_list = 1
    for i in your_list:
        sum_of_list *= i
    print(sum_of_list)

sum(your_list)
multiply(your_list)
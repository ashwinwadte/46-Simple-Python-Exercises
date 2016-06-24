'''
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
'''
numbers = [4,9,7]
def histogram(a_list):
    for i in a_list:
        print(i * '*')

histogram(numbers)
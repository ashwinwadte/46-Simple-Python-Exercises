'''
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
'''

def max_of_three(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    if num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)
num1 = int(input('Please input your first number'))
num2 = int(input('Please input your second number'))
num3 = int(input('Please input your third number'))

max_of_three(num1,num2,num3)
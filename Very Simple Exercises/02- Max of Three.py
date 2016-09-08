'''
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
'''
num1 = int(input('Please input your first number'))
num2 = int(input('Please input your second number'))
num3 = int(input('Please input your third number'))

def max_of_three(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    if num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print max_of_three(num1,num2,num3)
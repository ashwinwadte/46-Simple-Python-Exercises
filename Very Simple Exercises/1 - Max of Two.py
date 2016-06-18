'''
Define a function max() that takes two numbers as arguments and returns the largest of them.
Use the if-then-else construct available in Python.
(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)'''

def max(num1,num2):
    if num1 > num2:
        print (num1)
    else:
        print (num2)
num1 = int(input('Please input your first number'))
num2 = int(input('Please input your second number'))
max(num1,num2)
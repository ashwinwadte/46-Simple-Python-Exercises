'''
Define a function max() that takes two numbers as arguments and returns the largest of them.
Use the if-then-else construct available in Python.
(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)'''

num1 = int(input('Please input your first number'))
num2 = int(input('Please input your second number'))

def max(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
print max(num1,num2)
'''
Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I".
'''

str = input('Please input your string and it will reversed')
def reverse(str):
    return (str[::-1])

print reverse(str)
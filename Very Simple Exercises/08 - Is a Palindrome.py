'''
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.
'''

#I will return to this later on, will implement regular expressions to further improve this piece of code
str = input("Please enter text to see if it's a palindrome")
def is_palindrome(str):
    str.lower()
    if str == str[::-1] :
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

is_palindrome(str)

'''
Write a version of a palindrome recogniser that accepts a file name from the user,
reads each line, and prints the line to the screen if it is a palindrome.
'''
import re

def palindrome_checker(text):
    text = re.sub(r'[^a-zA-Z]', "",text).lower()
    if text == text[::-1]:
        return True
    else:
        return False

def file_opener(filename):
    f = open(filename, 'r')
    for line in f:
        if palindrome_checker(line):
            print(line)
        else:
            pass

print (file_opener('palindromes.txt'))
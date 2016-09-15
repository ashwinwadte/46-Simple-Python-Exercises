'''
According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
("Semordnilap" is itself "palindromes" spelled backwards.)
Write a semordnilap recogniser that accepts a file name
(pointing to a list of words) from the user and finds and
prints all pairs of words that are semordnilaps to the screen.
For example, if "stressed" and "desserts" is part of the word list,
the output should include the pair "stressed desserts".
Note, by the way, that each pair by itself forms a palindrome!
'''

import re

file_name = input('Please input your file name')

def semordnilap_checker(file_name):
    f = open(file_name, 'r')
    result = []
    for line in f:
        #removes all spaces,punctuations and make all characters lower cased
        line = re.sub(r'[^a-zA-Z]', "", line).lower()
        if line[::-1] in result:
            print (line, line[::-1])
        else:
            result.append(line)

semordnilap_checker(file_name)
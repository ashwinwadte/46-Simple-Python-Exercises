'''
Write a program that will calculate the average word
length of a text stored in a file (i.e the sum of all the l
engths of the word tokens in the text, divided by the number of word tokens).
'''

import re
def average_words(file_name):
    with open(file_name, 'r') as f:
        f = f.read()
        # removes all non alphabet characters
        f = re.sub(r'[^A-Za-z]', ' ', f)
        words = f.split()
        length_of_words = 0

        for word in words:
            for letter in word:
                length_of_words += 1

    # returns an integer, rather than tuple
    return int(length_of_words / len(words))

print (average_words('lorem.txt'))


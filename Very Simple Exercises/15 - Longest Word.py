'''
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
'''

list_words = ['Abraham','Sky','Astronaut','Chicken','Accelerator']

def find_longest_word(list_of_words):
    len_of_longest_word = 0
    for i in list_of_words:
        if len(i) > len_of_longest_word:
            len_of_longest_word = len(i)
    print(len_of_longest_word)

find_longest_word(list_words)
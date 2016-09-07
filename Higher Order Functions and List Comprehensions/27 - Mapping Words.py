'''
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.
'''

example = ['Chicken','Dragon','Palindromes','JackieChan']

# Mapping words using a for-loop
def length_of_words(list):
    word_lengths = []
    for word in list:
        word_lengths.append(len(word))
    return word_lengths

# Mapping words using the higher order function map()
def length_of_words1(list):
    return map(len, list)

# Mapping words using a list comprehensions
def length_of_words2(list):
    return ([len(word) for word in list])


print (length_of_words(example))
print (length_of_words1(example))
print (length_of_words2(example))

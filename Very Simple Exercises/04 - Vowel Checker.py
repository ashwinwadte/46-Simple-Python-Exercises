'''
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
'''

character = input('Please enter a character')

def is_vowel(character):
    if character in 'AaEeIiOoUU':
        return ("It's a vowel!")
    else:
        return ("It's not a vowel!")

print is_vowel(character)
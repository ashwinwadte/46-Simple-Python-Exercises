'''
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
'''

character = input('Please enter a character')

def is_vowel(character):
    character.lower()
    if character in 'AaEeIiOoUU':
        print("It's a vowel!")
    else:
        print("It's not a vowel!")

is_vowel(character)
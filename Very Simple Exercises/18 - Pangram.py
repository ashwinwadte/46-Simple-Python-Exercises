'''
A pangram is a sentence that contains all the letters of the
English alphabet at least once, for example:
The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a pangram or not.
'''

pangram = input('Input pangram')

def is_pangram(word):
    word = word.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    temp_alphabet = ''
    for i in word:
        if i not in temp_alphabet and i in alphabet:
            temp_alphabet += i
    print(temp_alphabet)
    if len(temp_alphabet) == 26:
        print("It's a pangram!")
    else:
        print("It's not a pangram!")

is_pangram(pangram)
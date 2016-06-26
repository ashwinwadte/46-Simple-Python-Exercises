'''
Write a version of a palindrome recognizer that also accepts phrase palindromes
such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets",
"Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation
"Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
'''
import re
word = input("Input text so I can check if it's a palindrome")

def palindrome_checker(text):
    text = re.sub(r'[^a-zA-Z]', "",text).lower()
    if text == text[::-1]:
        print(True)
    else:
        print(False)

palindrome_checker(word)
'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in
either the written record of a language, the works of an author, or in a single text.
Define a function that given the file name of a text will return all its hapaxes.
Make sure your program ignores capitalization.
'''
import re
def hapax_checker(file_name):
    f = open(file_name, 'r').read()
    f = re.sub(r'[^A-Za-z]', ' ', f)
    words = f.lower().split(' ')
    print(words)

    for line in f:
        words.append(line.lower().split())
    hapaxes = list(filter(lambda x: words.count(x) == 1, words))
    return hapaxes

print(hapax_checker('hapax.txt'))
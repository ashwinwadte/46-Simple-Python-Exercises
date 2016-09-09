# -*- coding: utf-8 -*-
'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
and use it to translate your Christmas cards from English into Swedish.
Use the higher order function map() to write a function translate()
that takes a list of English words and returns a list of Swedish words.
'''

swedish_english = {
    'merry':'god',
    "christmas":"jul",
    "and":"och",
    "happy":"gott",
    "new":"nytt",
    "year":"år"
}
example = ['merry','christmas','and','merry']

def translate(words):
    return map(lambda x: swedish_english[x.lower()],words)

print translate(example)


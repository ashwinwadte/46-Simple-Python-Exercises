'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
and use it to translate your Christmas cards from English into Swedish.
That is, write a function translate() that takes a list of English words and returns a list of Swedish words.
'''

swedish_english = {
    'merry':'god',
    "christmas":"jul",
    "and":"och",
    "happy":"gott",
    "new":"nytt",
    "year":"år"
}

word = ['merry','christmas','and','merry']
def translate(word):
    translated = []
    for i in word:
        try:
            translated.append(swedish_english[i])
        except:
            print('Error')
    print(' '.join(translated))

translate(word)
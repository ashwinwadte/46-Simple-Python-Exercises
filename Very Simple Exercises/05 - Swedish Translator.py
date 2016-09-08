'''
Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between.
 For example, translate("this is fun") should return the string "tothohisos isos fofunon".
'''
text_to_translate = input('Please enter your text to translate')

def translate(text):
    vowels = 'AaEeIiOoUu '
    translated = ''
    for i in text:
        translated += i
        if i not in vowels:
            translated += 'o' + i
    return translated

print translate(text_to_translate)
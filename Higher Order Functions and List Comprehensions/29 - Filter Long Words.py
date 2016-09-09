"""
Using the higher order function filter(), define a function
filter_long_words() that takes a list of words and an integer n
and returns the list of words that are longer than n.
"""
example = ['FirstWord','Jack','Red','Jackie','Superman']
n = 3
def filter_long_words(words, n):
  return filter(lambda x: len(x) > n, words)

print filter_long_words(example, n)
"""
Write a function find_longest_word() that takes a list of words and
returns the length of the longest one. Use only higher order functions.
"""
example = ['Apple','Jack','Michael']
def find_longest_word(words):
  return max(map(len, words))

print find_longest_word(example)
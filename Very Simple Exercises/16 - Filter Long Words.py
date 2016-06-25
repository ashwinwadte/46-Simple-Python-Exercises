'''
Write a function filter_long_words()
that takes a list of words and an integer n and returns the list of words that are longer than n.
'''

list_of_words = ['Apple','Chicken','Book','Jack','Max']

def filter_long_words(list_of_words,n):
    filtered_words = []
    for i in list_of_words:
        if len(i) > n:
            filtered_words.append(i)
    print(filtered_words)
filter_long_words(list_of_words,5)
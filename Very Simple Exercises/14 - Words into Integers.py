'''
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
'''

list_of_words = ['Apple','Chicken','Book','Jack','Max']

def words_to_int(list_of_words):
    converted_list = []
    for i in list_of_words:
        converted_list.append(len(i))
    return converted_list

print words_to_int(list_of_words)
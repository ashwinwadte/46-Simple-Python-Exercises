'''
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
'''

demo_list = ['s','f','s']
demo_string = 'Kratos'

def calc_length(list_or_string):
    length = 0;
    for i in list_or_string:
        length += 1
    print(length)

calc_length(demo_string)
'''
Write a procedure char_freq_table() that, when run in a terminal,
accepts a file name from the user, builds a frequency listing of the characters contained in the file,
and prints a sorted and nicely formatted character frequency table to the screen.
'''
import re
file_name = raw_input('please enter your file name')

def char_freq_table(file_name):
    frequency_dict = {
    }
    f = open(file_name,'r')
    for line in f:
        #ignores all white space
        line = re.sub(r'[\s]', "", line).lower()
        for char in line:
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[str(char)] = 1
    print 'Here are the results'
    #sorts character in a descending order - greatest to smallest
    for char in sorted(frequency_dict.items(),key=lambda x: x[1],reverse=True):
        print char[0], frequency_dict[char[0]]


#test
char_freq_table(file_name)
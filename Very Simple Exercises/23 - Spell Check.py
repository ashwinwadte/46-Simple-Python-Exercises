'''
Define a simple "spelling correction" function correct()
that takes a string and sees to it that
1) two or more occurrences of the space character is compressed into one, and
2) inserts an extra space after a period if the period is directly followed by a letter.
E.g. correct("This is very funny and cool.Indeed!") should return "This is very funny and cool.
Indeed!" Tip: Use regular expressions!
'''

import re

example = "This is very      funny and    cool.Indeed!"
def correct(a_string):
    check_space = re.sub(r'\s{2,}',' ',a_string)
    make_space = re.sub(r'(\.)(\w)', r'\1 \2',check_space)
    return make_space

print correct(example)
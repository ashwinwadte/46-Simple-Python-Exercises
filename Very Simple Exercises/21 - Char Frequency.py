'''
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
'''

a_string = 'abbabcbdbabdbdbabababcbcbab'

def char_freq(a_string):
    frequency_dict = {

    }
    for i in a_string:
        if i in frequency_dict:
            frequency_dict[i] += 1
        else:
            frequency_dict[str(i)] = 1
    return frequency_dict

print char_freq(a_string)
'''
The third person singular verb form in English is distinguished by the suffix -s,
which is added to the stem of the infinitive form: run -> runs.
A simple set of rules can be given as follows:

If the verb ends in y, remove it and add ies
If the verb ends in o, ch, s, sh, x or z, add es By default just add s
Your task in this exercise is to define a function make_3sg_form()
which given a verb in infinitive form returns its third person singular form.
Test your function with words like
try, brush, run and fix.
Note however that the rules must be regarded as heuristic,
in the sense that you must not expect them to work for all cases.
Tip: Check out the string method endswith().

'''
import re
suffixes = ('o','ch','s','sh','x','z')
examples = ['try','brush','run','fix']
def make_3sg_form(list_of_strings):
    transformed_strings = []
    for i in list_of_strings:
        if i.endswith('y'):
            transformed_strings.append(re.sub(r'y','ies',i))
        elif i.endswith(suffixes):
            i += 'es'
            transformed_strings.append(i)
        else:
            i += 's'
            transformed_strings.append(i)
    return transformed_strings

print(make_3sg_form(examples))

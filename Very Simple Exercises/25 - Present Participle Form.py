'''
In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:

If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter before adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form()
which given a verb in infinitive form returns its present participle form.
Test your function with words such as lie, see, move and hug.
However, you must not expect such simple rules to work for all cases.
'''
import re
example = ['move','try','hug','jump','catch','share','eat','eradicate']

def make_ing_form(list_of_strings):
    transformed_strings = []
    vowels = 'aeiou'
    for verb in list_of_strings:
        if verb.endswith('e'):
            transformed_strings.append(re.sub(r'e$', 'ing', verb))

        elif verb.endswith('ie'):
            transformed_strings.append(re.sub(r'ie$', 'ying', verb))

        elif verb[-1] not in vowels:
            if verb[-2] in vowels:
                if verb[-3] not in vowels:
                    transformed_strings.append(verb + verb[-1] + 'ing')
                else:
                    transformed_strings.append(verb + 'ing')
            else:
                transformed_strings.append(verb + 'ing')




    return transformed_strings

print(make_ing_form(example))



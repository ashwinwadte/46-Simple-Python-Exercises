'''
An anagram is a type of word play, the result of
rearranging the letters of a word or phrase
to produce a new word or phrase, using all the original letters exactly
once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place.
Write a Python program that, when started
1) randomly picks a word w from given list of words,
2) randomly permutes w (thus creating an anagram of w),
3) presents the anagram to the user, and
4) enters an interactive loop in which the user is invited to guess the original word.
It may be a good idea to work with (say) colour words only. The interaction with the program may look like so:
'''

# This was a bit messy, if you ever catch me awake
# tell me to improve this.
import random


def anagram_gamer(words, topic):

    anagrams = []
    done = False

    # generates anagrams for all the words given.
    for word in words:
        anagrams.append(''.join(random.sample(word, len(word))))
    current_anagram = random.randrange(len(anagrams))

    while not done:
        user_answer = input("Your topic is " + topic + ". Guess the original word for this anagram: "+ anagrams[current_anagram])
        if user_answer.lower() == words[current_anagram].lower():
            response = input("You're correct! Do you want to try again? please enter either 'y' or 'n' ?")
            if response == 'y':
                anagram_gamer(words,topic)
            else:
                done = True
        else:
            response = input("You're wrong, you want to try again? 'y' or 'n'?")
            if response == 'yes':
                anagram_gamer(words, topic)
            else:
                done = True


anagram_gamer(['cat','tiger','ostrich','elephant','kangaroo','zebra'], 'animals')
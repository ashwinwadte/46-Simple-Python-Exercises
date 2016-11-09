'''
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:

<<< import guess_number
Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!
'''
import random

def guess_game():
    user_name = input('Hello! What is your name?')
    random_number = random.randrange(1,20)
    guess = int(input("Well, " + user_name +', I am thinking of a number between 1 and 20'))
    count = 1
    while guess != random_number:
        if guess > random_number:
            guess = int(input("Well, " + user_name +', Your guess is too high, try lower: '))
        else:
            guess = int(input("Well, " + user_name + ', Your guess is too low, try higher: '))
        count += 1
    return 'Good Job ' + user_name + ', You guess my number in ' + str(count) + ' guesses'

print(guess_game())
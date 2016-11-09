'''
In a game of Lingo, there is a hidden word, five characters long.
The object of the game is to find this word by guessing,
and in return receive two kinds of clues:

1) the characters that are fully correct,
with respect to identity as well as to position, and

2) the characters that are indeed present in the word,
but which are placed in the wrong position.

Write a program with which one can play Lingo.

Use square brackets to mark characters correct in the sense of 1),

and ordinary parentheses to mark characters correct in the sense of 2).
'''


def lingo(word):
    word = list(word)
    done = False

    while not done:
        user_answer = list(input("Guess this random five letter word"))

        try:
            for i in range(0,5):
                if user_answer[i] == word[i]:
                    user_answer[i] = '[' + user_answer[i] + ']'
                elif user_answer[i] in word:
                    user_answer[i] = '(' + user_answer[i] + ')'
        except:
            print("You're answer wasn't  five letters, try again")
            lingo(word)

        if user_answer == word:
            print('You guessed correct!')
            done = True

        print(user_answer)

        # recursive until user is correct
        lingo(word)

print (lingo('tiger'))
'''
Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops.
'''

member_group_A = ['Ibrahim','Chin','Jacob','Sandra']
member_group_B = ['Jackson', 'Aaron','Jacob', 'Matthew']

def overlapping():
    overlapped = False
    for i in member_group_A:
        for j in member_group_B:
            if i == j:
                overlapped = True

    print (overlapped)

overlapping()
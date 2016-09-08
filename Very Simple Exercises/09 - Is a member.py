'''
Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a,
and returns True if x is a member of a, False otherwise.
(Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)
'''
members = ['Aaron','Jackson','Jacob']
member_name = input('Please input your name')
def is_member(member_name):
    if member_name in members:
        return True
    else:
        return False

print is_member(member_name)
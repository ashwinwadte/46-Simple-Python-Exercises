'''
Implement the higher order functions map(), filter() and reduce().
(They are built-in but writing them yourself may be a good exercise.)
'''

# The solutions below are were based on this definition from http://www.python-course.eu/lambda.php

example = ['Apple','Jack','Google']

# my implementation of the map() function
def my_map(function, sequence):
    result = []
    for i in sequence:
        result.append(function(i))
    return result

# my implementation of the filter() function

def my_filter(function, sequence):
    #returns string
    if isinstance(sequence, str):
        result = ''
    # returns tuple
    elif isinstance(sequence, tuple):
        result = ()
    else:
        result = []

    for item in sequence:
        if function(item):
            if isinstance(sequence, str):
                result += item
            elif isinstance(sequence, tuple):
                result += (item,)
            else:
                result.append(item)
    return result

# this took a while to grasp.
def my_reduce(function, sequence, start=None):
    #sets it to the starting value if start is set, else, set it to the first value
    result = start if start else sequence[0]
    if start:
        for item in sequence:
            result = function(result, item)
    else:
        for item in sequence[1:]:
            result = function(result, item)
    return result


print my_map(lambda x: x * 2, [1,2,3,4])
print my_filter(lambda x: x.endswith('le'), example)
print my_reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 5)
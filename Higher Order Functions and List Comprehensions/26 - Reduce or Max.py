'''Using the higher order function reduce(), write a function max_in_list()
that takes a list of numbers and returns the largest one.
Then ask yourself: why define and call a new function,
when I can just as well call the reduce() function directly?'''

example = [1,4,2,4,2,5,9,34,309]

def max_in_list(list):
    return reduce(lambda x, y: x if x > y else y, list)

print (max_in_list(example))
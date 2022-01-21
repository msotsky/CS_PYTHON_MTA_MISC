# COMP 1631 Lab 4 Fall 2018
# Filename: lab4pr1.py
# Names:
# Problem Description: 


def triple_threat(lst):
    """ triple_threat is a function that takes a list as
        input and returns a list of elements
        each three times as large as the original
    """

    tripled = [ 3*x for x in lst ]
    return tripled



def triple_threat_by_index(lst):
    """ triple_threat_by_index has the same input and output
        behaviour as triple_threat, but it uses the index
        of each list element, instead of the element itself.
    """

    n = len(lst)
    tripled = [ 3*lst[i] for i in list(range(n)) ]
    return tripled


def length(lst):
    """ returns the length of the provided list
    """

    # Use a list comprehension to make a 
    #  list with a 1 for every item in lst
    lc = [ 1 for item in lst ]
    # Add up the ones to determine the length
    return sum(lc)

def triple(data):
    total = 0
    for n in data:
        if n > 0:
            total += n
    return total
        
# COMP 1631 Lab 5 Fall 2018
# Filename: lab6pr1.py
# Names:
# Problem Description: 


def longest(lst):
    """ input: L, a list of strings
        returns one of the strings
        with the greatest length
    """
    LoL = [ [len(s), s] for s in lst ]
    bestpair = max(LoL)
    return bestpair[1]

print(longest(['stuck','in','hell']))
def all_longest(lst):
    LoL = [ [len(s), s] for s in lst ]
    bestpair = max(LoL)
    newlist = [s for s in lst if len(s) == bestpair[0]]
    return newlist

#>>> lis= ["a" , "aa", "aaa", "aaaa", "aaab", "aaac"]

#>>> le = max(len(x) for x in lis)   #find out the max length      

#>>> [x for x in lis if len(x) == le]  #now filter list based on that max length
#['aaaa', 'aaab', 'aaac']
        
        
    

    

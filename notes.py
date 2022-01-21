def lone_sum(a,b,c):
    count = a
    if count == b and b == c:
        return 0
    elif count == b:
        return c
    elif count == c:
        return b
    elif b == c:
        return count
    else:
        count = count + b + c
        return count 


def dog_cat(str):
    if len(str) < 6:
        return False
    else:
        countdog = [1 for x in str if x in 'dog']
        countcat = [1 for x in str if x in 'cat']
        if countdog == countcat:
            return True
        else:
            return  False

def count_pairs(str):
    if len(str) < 3:
        return 0
    elif (str[0] == str[2]):
        return 1 + count_pairs(str[1:])
    else:
        return count_pairs(str[1:])

mylist = ([2,1,2,2])

def this(mylist):
    if 2 in mylist:
        return True
    else:
        return False


def has_22(list_of_ints):
    if 2 not in list_of_ints:
        return False
    else:
        length = len(list_of_ints)
        count = 0
        answer = False
        while count != length:
            if list_of_ints[count]== 2 and list_of_ints[count+1]== 2:
                answer = True
                return answer
            else:
                count += 1
    if answer == False:
        return False


print(2//10)
print(3//12)
print(4//6)
print(3//13)
print(13//3)


def max_scrib_LOL(a_list):
    LoL = [[max_scrib_LOL(word),word]for word in a_list]
    best_pair = max(LoL)
    return best_pair[1]

def all_longest(lst):
    lol = [[len(s),s] for s in lst]
    bestpair = max(lol)
    newlist = [s for s in lst if len(s)==bestpair[0]]
    return newlist
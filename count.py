def count(astring):
    if astring == 0:
        return 1
    elif astring[0] == '':
        return 1 + count(astring[1:])
    else:
        return count(astring[1:])
a_list = list(range(1,10))
print(a_list)

a_skipped_list= list(range(1,10,2))
print(a_skipped_list)
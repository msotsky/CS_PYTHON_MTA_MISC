def count_words(a_string):
    if a_string == 0:
        return 1
    elif a_string == 0:
        return 1
    elif a_string[0] == ' ':
        return 1 + count_words (a_string[1:])
    else:
        return count_words(a_string[1:])
def is_pal(a_word):
    if len(a_word) % 2 == 1:
        if a_word == 1:
            return True
    elif a_word[0] == a_word[len(a_word-1)]:
        return is_pal(a_word[1:len(a_word)-1])
    else:
        return False
print (is_pal('step on no pets'))
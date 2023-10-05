# CONVERT BOOLEAN VALUES TO STRINGS 'YES' OR 'NO'
def bool_to_word(bool):
    return "Yes" if bool else "No"
# my solution
def bool_to_word(boolean):
    if boolean: return 'Yes'
    else: return 'No'


# SUM ARRAYS
def sum_array(a): # sum(iterable, start)
    return sum(a) # python has its own sum() function - add all items in a tuple, and return the result
# my solution
def sum_array(a):
    n = 0
    for x in a:
        n += x
    return n


# CONVERT A STRING TO A NUMBER
def string_to_number(s): # try:... except:...
    try:
        return int(s)
    except (ValueError):
        return "Input is not valid"
string_to_number = int # using an alias for the function name: int eg. string_to_number("1234") to int("1234")
# my solution
def string_to_number(s):
    return int(s)


# COUNTING SHEEP
def count_sheeps(sheep): 
    return sheep.count(True) # python has its own count() function - count the number of times the value appear in the list
# my solution
def count_sheeps(sheep):
    s = 0
    for x in sheep:
        if x == True:
            s += 1
        else:
            s += 0
    return s


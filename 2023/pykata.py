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


# GRASSHOPPER - SUMMATION
def summation(num): # range does not support float/string data type, only integer
    return sum(range(1, num + 1)) # range(start(default 0), stop(stops before this number), step(increment)) - returns a sequence of numbers
# eg. range(1, 8 + 1) will return range(1, 9) then sum() method will add all numbers in range(1, 9)
# my solution
def summation(num):
    return num * (num + 1) / 2


# REVERSED STRINGS
# my solution
def solution(string):
    return string[::-1] # [::] is slice notation/slicing - use a slice that steps backwards, -1
# eg. b = "Hello, World!" | print(b[2:5]) -> 'llo' - start from 0, only takes the string up until before the 5th character
# b = "Hello, World!" | print(b[-5:-2]) -> 'orl' - count backwards start from 1, not 0. but takes the string from left to right


# OPPOSITES ATTRACT
# my solution
def lovefunc( flower1, flower2 ):
    return flower1 % 2 != flower2 % 2
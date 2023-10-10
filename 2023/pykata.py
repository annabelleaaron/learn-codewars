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


# REMOVE FIRST AND LAST CHARACTER
# my solution
def remove_char(s):
    return s[1 : -1]
# indexes range -len(x) to (len(x) - 1)
# [0, 1, 2, 3, 4] == [-5, -4, -3, -2, -1] <- the values equal to the index of the same element
# the length of each of these lists is 5, and the values in the first list and the second list differ by exactly 5


# FAKE BINARY
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
# my solution
def fake_bin(x):
    n = ''
    for s in x:
        if int(s) >= 5:
            n += '1'
        else:
            n += '0'
    return n


# KEEP HYDRATED!
def litres(time):
    return time // 2 # floor division (//) rounds the result down to the nearest whole number
# my solution
import math
def litres(time):
    return math.floor(time * 0.5)



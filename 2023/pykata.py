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


# GET THE MIDDLE CHARACTER
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]
# my solution
import math
def get_middle(s):
    return s[math.floor(len(s)/2)] if len(s) % 2 == 1 else s[math.floor(len(s)/2-1):math.floor(len(s)/2)+1]
# without import math
def get_middle(s):
    return s[int(len(s)/2)] if len(s) % 2 == 1 else s[int(len(s)/2-1):int(len(s)/2)+1]


# SUM OF THE FIRST NTH TERM OF SERIES
def series_sum(n):
    return '{:.2f}'.format(sum(1/(3 * i + 1) for i in range(n)))
# my solution
def series_sum(n):
    sum = 0
    for i in range(n):
        sum += 1 / (1 + 3 * i)
    return "{:.2f}".format(sum)


# SENTENCE SMASH
# my solution
def smash(words):
    return ' '.join(words)


# GROWTH OF A POPULATION
# recursive function
######################## take note
def nb_year(p0, percent, aug, p, i=0):
    return i if p0>=p else nb_year(int(p0+p0*(percent/100)+aug), percent, aug, p, i+1)
# my solution
def nb_year(p0, percent, aug, p):
    n = 0
    while (p0 < p):
        p0 += int(p0 * (percent/100) + aug)
        n += 1
    return n


# MUMBLING
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
# my solution
def accum(s):
    text = ''
    for i in range(len(s)):
        j = 0
        while (j <= i):
            if j == 0:
                text += s[i].capitalize()
            else:
                text += s[i].lower()
            j += 1
        if i < len(s)-1:
            text += '-'
    return text


# DISEMVOWELING TROLLS
def disemvowel(string):
    return string.translate({ord(i):None for i in 'aeiouAEIOU'})
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
# my solution
def disemvowel(string_):
    return string_.translate(str.maketrans('', '', 'aeiouAEIOU'))


# LIST FILTERING
# my solution
def filter_list(l):
    return [x for x in l if type(x) is int]
def filter_list(l):
    return [x for x in l if isinstance(x, int)]
# isinstance() is faster but if the list contains a boolean value, it will be converted to a 0 or 1 and will be considered an integer (True)


# FRIEND OR FOE
def friend(x):
    return filter(lambda name: len(name) == 4, x)
# my solution
def friend(x):
    return [f for f in x if len(f) == 4]


# NUMBER OF PEOPLE IN THE BUS
def number(bus_stops):
    return sum(on - off for on, off in bus_stops)
# my solution
def number(bus_stops):
    return sum(p[0]-p[1] for p in bus_stops)


# TESTING 1-2-3
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
# my solution
def number(lines):
    return [f'{i + 1}: {s}' for i, s in enumerate(lines)]


# REVERSE WORDS
# regex
import re
def reverse_words(str):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)
# map
def reverse_words(str):
  return " ".join(map(lambda word: word[::-1], str.split(' ')))
# x[::-1] reverses a string
# my solution
def reverse_words(text):
    return ' '.join(x[::-1] for x in text.split(' '))


# ISOGRAMS

# my solution
def is_isogram(string):
    return len(set((string.lower()))) == len(string)


# YOU'RE A SQUARE!
def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0
# my solution
import math
def is_square(n):    
    return math.sqrt(n) % 1 == 0 if n >= 0 else False # return n > -1 and math.sqrt(n) % 1 == 0


# COUNT THE DIVISORS OF A NUMBER
def divisors(n): # not efficient
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0])
def divisors(n): # not efficient
    return sum(n%i==0 for i in range(1,n+1))
# my solution
def divisors(n):
    divs = 1
    factor = 2
    
    while factor * factor <= n:
        exponent = 0
        while n % factor == 0:
            n /= factor
            exponent += 1
        factor = 3 if factor == 2 else factor + 2
        divs *= exponent + 1
    
    if n > 1:
        divs *= 2
        
    return divs





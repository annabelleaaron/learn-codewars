# SUM ARRAYS
def sum_array(a): # sum(iterable, start)
  return sum(a) # python has its own sum() function - add all items in a tuple, and return the result
# my solution
def sum_array(a):
    n = 0
    for x in a:
        n += x
    return n

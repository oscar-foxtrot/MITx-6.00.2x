import math
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    
    mean = 0
    for i in L:
        mean += len(i)
    mean /= len(L)
    
    sumsquares = 0
    for i in L:
        sumsquares += (len(i) - mean)**2
    
    return math.sqrt(sumsquares / len(L))

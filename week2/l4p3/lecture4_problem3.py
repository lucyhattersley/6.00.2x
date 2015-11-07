def stdDevOfLengths(L):
    import statistics
    """
    Accepts a list of strings (L)
    Counts the chars in each string
    Finds the mean, calculates the variance and returns the standard deviation
    """
    if len(L) == 0:
        return float('NaN')
    L2 = []
    for t in L:
        L2.append(len(t))
    return statistics.pstdev(L2)
    
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L)
def stdDevOfLengths(L):
    """
    Accepts a list of strings (L)
    Counts the chars in each string
    Finds the mean, calculates the variance and returns the standard deviation
    """
    if not L:
        return float('NaN')
    X = []
    for t in L:
        X.append(len(t))
    
    mean = sum(X) / len(X)
    
    result = 0.0
    for t in X:
        result += (t - mean)**2
    
    return (result / len(L)) ** 0.5

#L = [] 
#L = ['a', 'z', 'p']    
#L = ['apples', 'oranges', 'kiwis', 'pineapples']
L = ['h', 'mi', 'uios', 'qkpsjixo', 'bmhiklywgy', 'ltpxfmympwwuex', 'o']
print stdDevOfLengths(L)
print "Should be 4.681705602335411"
print 4.681705602335411 == stdDevOfLengths(L)
def stdDevOfLengths(L):
    """
    Accepts a list of strings (L)
    Counts the chars in each string
    Finds the mean, calculates the variance and returns the standard deviation
    """
    if len(L) == 0:
        return float('NaN')
    X = []
    for t in L:
        X.append(len(t))
    
    mean = sum(X) / len(X)
    
    result = long(0.0)
    for t in X:
        result += (t - mean)**2
    
    result = result / len(L)
    return result ** 0.5
        
#L = ['apples', 'oranges', 'kiwis', 'pineapples']
#L = ['h', 'mi', 'uios', 'qkpsjixo', 'bmhiklywgy', 'ltpxfmympwwuex', 'o']
L = ['h', 'mi', 'uios', 'qkpsjixo', 'bmhiklywgy', 'ltpxfmympwwuex', 'o']
print stdDevOfLengths(L)


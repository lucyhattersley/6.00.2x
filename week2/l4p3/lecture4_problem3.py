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
        X.append(float(len(t)))
    
    mean = sum(X) / len(X)
    
    result = 0.0
    for t in X:
        result += (t - mean)**2
    
    result = result / len(L)
    return result ** 0.5

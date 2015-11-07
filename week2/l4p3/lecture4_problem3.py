def stdDevOfLengths(L):
    """
    Accepts a list of strings (L)
    Counts the chars in each string
    Finds the mean, calculates the variance and returns the standard deviation
    """
    ints = []
    for l in L:
        ints.append(len(l))
    
    # find mean of ints
    mean = sum(ints)/len(ints)
    return mean
    
    #find variance
    #this isn't working. I need to figure out how to sum up each item
    #in ints properly
    variance = sum((ints-mean)**2)/len(ints)
    sd = sqrt(variance)
    return sd

L = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L)
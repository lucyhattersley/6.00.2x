import numpy as np

c = [-6, -6, -4, -4, 2, 2, 2]

c1 = [2, 2, -6]
c2 = [-4, -4,2, -6]

tests = [c1, c2]
results = []

for test in tests:
    mean = np.mean(test)
    variance = 0
    for x in test:
        variance += (x - mean)**2
    results.append(variance)
    
badness = sum(results)

print "c1 is: " + str(c1)
print "Variance is: " + str(results[0])
print "c2 is: " + str(c2)
print "Variance is: " + str(results[1])
print "Badness is: " + str(badness)


# test to get plt.hist values
import numpy as np
import matplotlib.pyplot as plt

# generation some uniformly distributed  data
x = np.random.rand(1000)

# create the histogram
(n, bins, patches) = plt.hist(x, bins=10,  label='hst')

plt.show()

# inspect the counts in each bin
print n

# and we see that the bins are approximately uniformly filled.
# create a second histogram with more bins (but same input data)
(n2, bins2, patches) = plt.hist(x, bins=20, label='hst')

print n2
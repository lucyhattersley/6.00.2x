# Lecture 8 Problem 4

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
            yield combo
            
items = ['cat', 'dog', 'duck']
combos = []
comboGen = powerSet(items) 

while True:
    try:
        combo = comboGen.next()
        if combo not in combos:
            combos.append(combo)
    except:
        break

print items
print combos

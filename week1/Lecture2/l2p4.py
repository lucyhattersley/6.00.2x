import random
def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1
        
import random
def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)
    
import random
def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)
        
dist1test = []
dist2test = []

for i in range(1000):
    dist1test.append(dist1())
    dist2test.append(dist2())

dist1result = sum(dist1test) / len(dist1test)
dist2result = sum(dist2test) / len(dist2test)

print "dist1result is: " + str(dist1result)
print "dist2result is: " + str(dist2result)
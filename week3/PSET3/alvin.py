import random

trials = []

for trial in range(1000):
    alvins = []
    for i in range(10000):
        flucount = 0
        for i in range(3):
            if random.randint(1,10) == 1:
                flucount += 1
        alvins.append(flucount)
    trials.append(float(alvins.count(1)) / float(len(alvins)))

print float(sum(trials)) / float(len(trials))

#twoorthree = alvins.count(2) + alvins.count(3)
#print float(twoorthree) / float(len(alvins))


#for month in months:
#    print str(month) + ": "+ str(months[month])
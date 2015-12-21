items = ['cat', 'dog']
# 
# 
# creating file to save outputvalues
f = open('/Users/Lucy/Desktop/yieldtest.csv', 'w+')
# build header values for file
f.write('i' + ',' + 'j' + ',' + 'bin(i)' + ',' + 'bin(j)' + ',' + '(3 ** j)' + ',' + 'i // (3 ** j)) % 3' + ',' + 'bag1' + ',' + 'bag2' + '\n')
# 
# # generate all combinations of N items
# def powerSet(items):
#     N = len(items)
#     # enumerate the 2**N possible combinations
#     for i in xrange(2**N):
#         combo = []
#         for j in xrange(N):
#             # test bit jth of integer i
#             if (i >> j) % 2 == 1:
#                 combo.append(items[j])
#                 f.write(str(i) + ',' + str(j) + ',' + str(bin(i)) + ',' + str(bin(j)) + ','+ str(bin(i >> j)) + ',' + str(i >> j) + ',' + str(combo) + '\n')
#             else:
#                 f.write(str(i) + ',' + str(j) + ',' + str(bin(i)) + ',' + str(bin(j)) + ','+ str(bin(i >> j)) + ',' + str(i >> j) + ',' + 'NULL' + '\n')                
#         yield combo
# 
# comboGen = powerSet(items)
# 
# while True:
#     try:
#         x = comboGen.next()
#         print x
#     except:
#         break

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    for i  in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield(bag1, bag2)


# def yieldAllCombos(items):
#     """
#       Generates all combinations of N items into two bags, whereby each 
#       item is in one or zero bags.
# 
#       Yields a tuple, (bag1, bag2), where each bag is represented as 
#       a list of which item(s) are in each bag.
#     """
#     N = len(items)
#     for i  in xrange(3**N):
#         bag1 = []
#         bag2 = []
#         for j in xrange(N):
#             if (i // (3 ** j)) % 3 == 1:
#                 bag1.append(items[j])
#                 f.write(str(i) + ',' + str(j) + ',' + str(bin(i)) + ',' + str(bin(j)) + ','+ str(3 ** j) + ',' + str(i // (3 ** j) % 2) + ',' + str(bag1) + '\n')
# 
#             elif (i // (3 ** j)) % 3 == 2:
#                 bag2.append(items[j])
#                 f.write(str(i) + ',' + str(j) + ',' + str(bin(i)) + ',' + str(bin(j)) + ','+ str(3 ** j) + ',' + str(i // (3 ** j) % 2) + ',' + ',' + str(bag2) + '\n')
#             else:
#                 f.write(str(i) + ',' + str(j) + ',' + str(bin(i)) + ',' + str(bin(j)) + ','+ str(bin(i >> j)) + ',' + str(i >> j) + ',' + 'NULL' + ',' + 'NULL' + '\n')
#         yield(bag1, bag2)

comboGen = yieldAllCombos(items)

while True:
    try:
        x = comboGen.next()
        print x
    except:
        break

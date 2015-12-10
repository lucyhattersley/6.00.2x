mapFilename = open('mit_map.txt', 'r')
linenumber = 1
for line in mapFilename:
    items = []
    for item in line.split(" "):
        items.append(item)
    node1 = items[0]
    node2 = items[1]
    weight1 = items[2]
    weight2 = items[3]
    print "------"
    print "Line: " + str(linenumber)
    print "Node 1: " + str(node1)
    print "Node 2: " + str(node2)
    print "Weight 1: " + str(weight1)
    print "Weight 2: " + str(weight2)
    linenumber += 1
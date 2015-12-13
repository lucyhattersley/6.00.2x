# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT building
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import *

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 
# Map.txt contains lines (each with four digits). The first two are source and destination nodes. The third is distance, the fourth indoor distance.
# These correspond to the __init__ values of WeightedEdge class: (self, src, dest, weight1, weight2):

# Instantiate a WeightedDigraph object.
# Create a function to import the map.mit_map.txt file
# Examine each line of file individually. Split each value by the space
# The WeightedDigraph object inherits AddNode function from Digraph. Use  it to add the 
# first two numbers as nodes to the graph (duplicates raise a ValueError - use Try / Except) when adding nodes
# Create a WeightedEdge instance using all four values
# Use the AddEdge function in WeightedDigraph to add the edge to the graph.

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    f = open(mapFilename, "r")

    # Create a graph
    dirGraph = WeightedDigraph()

    # Spliting file into lines and matching each value to a variable
    for line in f:
        items = []
        for item in line.split(" "):
            items.append(item)
        node1 = Node(items[0])
        node2 = Node(items[1])
        weight1 = float(items[2])
        weight2 = float(items[3])

#         # Adding nodes
        try: 
            dirGraph.addNode(node1)
        except:
            pass
        try:
            dirGraph.addNode(node2)
        except:
            pass
        
        # creating weighted edge and adding to dirGraph
        weightedEdge = WeightedEdge(node1, node2, weight1, weight2)
        dirGraph.addEdge(weightedEdge)

    #returning dirGraph
    return dirGraph

#
# Problem 3: Finding the Shortest Path using Brute Force Search

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    def getAllPaths(digraph, start, end, path=[], paths=[]):
        """
        Helper function accepts start and end nodes
        Returns a list of paths (each path a list of nodes) 
        """
        start = Node(int(start))
        end = Node(int(end))
        
        path = path + [start]

        if start == end:
            paths.append(path)
        else:
            for node in digraph.childrenOf(start):
                if node not in path: #avoid cycles
                    newPath = getAllPaths(digraph,node.getName(),end.getName(),path,paths)

        return paths

    def findShortest(digraph, paths, maxTotalDist, maxDistOutdoors):
        """
        Helper function accepts all list of paths and constraints
        Returns shortest path that meets max constraints
        """
        shortest = []
        
        f = open('/Users/Lucy/Desktop/paths.txt', 'w+') # create test file
        
        for path in paths:
            pathDistance = 0
            pathOutdoorDistance = 0
            for i in range(len(path)-1):
                node1 = path[i]
                node2 = path[i+1]
                weights = digraph.getWeights(node1, node2)
                distance = int(weights[0])
                outdoorDistance = int(weights[1])
                pathDistance += distance
                pathOutdoorDistance += outdoorDistance
                f.write(str(path))
                f.write(': ')
                f.write('(')
                f.write(str(pathDistance))
                f.write(',')
                f.write(str(pathOutdoorDistance))
                f.write(')')
                f.write('\n')
                if shortest == [] or len(path) <= len(shortest):
                    if pathDistance <= maxTotalDist and pathOutdoorDistance <= maxDistOutdoors:
                        shortest = path
        if shortest != []:
            return map(str, shortest)
        else:
            raise ValueError

    paths = getAllPaths(digraph, start, end)
    return findShortest(digraph, paths, maxTotalDist, maxDistOutdoors)

# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    pass


# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
#if __name__ == '__main__':
#     Test cases
#    mitMap = load_map("/Users/Lucy/Dropbox/2_active_projects/6002x/week5/PSET5/ProblemSet5/mit_map.txt")
#     print isinstance(mitMap, Digraph)
#     print isinstance(mitMap, WeightedDigraph)
#     print 'nodes', mitMap.nodes
#     print 'edges', mitMap.edges
#     LARGE_DIST = 1000000

map5 = load_map("/Users/Lucy/Dropbox/2_active_projects/6002x/week5/PSET5/ProblemSet5/map5.txt")
print "----------"
print isinstance(map5, Digraph)
print isinstance(map5, WeightedDigraph)
print 'nodes', map5.nodes
print 'edges', map5.edges

print "Testing Map 5"
expectedPath1 = ['4', '3', '5']
brutePath1 = bruteForceSearch(map5, "4", "5", 21, 11)
print "Expected: ", expectedPath1
print "Brute-force: ", brutePath1 

#     Test case 1
#     print "---------------"
#     print "Test case 1:"
#     print "Find the shortest-path from Building 32 to 56"
#     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
# #     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#    print "DFS: ", dfsPath1
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)
# 
#     Test case 2
#     print "---------------"
#     print "Test case 2:"
#     print "Find the shortest-path from Building 32 to 56 without going outdoors"
#     expectedPath2 = ['32', '36', '26', '16', '56']
#     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#     print "Expected: ", expectedPath2
#     print "Brute-force: ", brutePath2
#     print "DFS: ", dfsPath2
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)
# 
#     Test case 3
#     print "Test case 3:"
#     print "---------------"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)
# 
#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)
# 
#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)
# 
#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)
# 
#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
#     
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
#     
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#    print "Did DFS search raise an error?", dfsRaisedErr
# 
#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#    dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
#     
# #     try:
# #         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
# #     except ValueError:
# #         dfsRaisedErr = 'Yes'
#     
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#    print "Did DFS search raise an error?", dfsRaisedErr
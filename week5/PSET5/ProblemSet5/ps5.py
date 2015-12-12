# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
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
        node1 = items[0]
        node2 = items[1]
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
#
# State the optimization problem as a function to minimize
# and what the constraints are

# first try to find a single path
# def DFS(graph, start, end, path = [], shortest = None):
#     #assumes graph is a Digraph
#     #assumes start and end are nodes in graph
#     path = path + [start]
# #    print 'Current dfs path:', printPath(path)
#     if start == end:
#         return path
#     for node in graph.childrenOf(start):
#         if node not in path: #avoid cycles
#             newPath = DFS(graph,node,end,path,shortest)
#             if newPath != None:
#                 return newPath

# This code finds shortest path
# def DFSShortest(graph, start, end, path = [], shortest = None):
#     #assumes graph is a Digraph
#     #assumes start and end are nodes in graph
#     path = path + [start]
# #    print 'Current dfs path:', printPath(path)
#     if start == end:
#         return path
#     for node in graph.childrenOf(start):
#         if node not in path: #avoid cycles
#             if shortest == None or len(path)<len(shortest):
#                 newPath = DFSShortest(graph,node,end,path,shortest)
#                 if newPath != None:
#                     shortest = newPath
#     return shortest

# Adapting DFSShortest to return all paths
# def DFSBrute(graph, start, end, path = [], paths = []):
#     #assumes graph is a Digraph
#     #assumes start and end are nodes in graph
#     path = path + [start]
#     if start == end:
#         return path
#     for node in graph.childrenOf(start):
#         if node not in path: #avoid cycles
#             newPath = DFSBrute(graph,node,end,path,paths)
#             if newPath != None:
#                 if node == end:
#                     path = path + [end]
#                     paths.append(path)
#     return paths
    
# Adapting DFSBrute to return paths and total weights
# I need to keep track of current and next nodes and add weight of each arc to totalDist
# def DFSBruteW(graph, start, end, path = [], paths = [], totalDist = 0):
#     #assumes graph is a Digraph
#     #assumes start and end are nodes in graph
#     path = path + [start]
#     if start == end:
#         return (path, totalDist)
#     for node in graph.childrenOf(start):
#         if node not in path: #avoid cycles
#             distance = graph.getWeights(start, node)
#             totalDist = totalDist + distance[0]
#             newPath = DFSBruteW(graph,node,end,path,paths,totalDist)
#             if newPath != None:
#                 if node == end:
#                     path = path + [end]
#                     paths.append((path, totalDist))
#     return paths
    
# Adapting DFSBrute to return paths, total distances and outdoor distances
# def DFSBruteW(graph, start, end, path = [], paths = [], totalDist = 0, outdoorDist = 0):
#     #assumes graph is a Digraph
#     #assumes start and end are nodes in graph
#     path = path + [start]
#     if start == end:
#         return (path, (totalDist, outdoorDist))
#     for node in graph.childrenOf(start):
#         if node not in path: #avoid cycles
#             distance = graph.getWeights(start, node)
#             totalDist = totalDist + distance[0]
#             outdoorDist = outdoorDist + distance[1]
#             newPath = DFSBruteW(graph,node,end,path,paths,totalDist, outdoorDist)
#             if newPath != None:
#                 if node == end:
#                     path = path + [end]
#                     paths.append((path, (totalDist, outdoorDist)))
#     return paths
#     
# def findShortestTotal(paths):
#     """
#     Accepts (paths). A list  of tuples. The first item in each tuple is a list of nodes. The second item is a tuple (total distance, total outdoor distance).
#     Loops through each path in paths. If distance is shorter than current, appends shortest path (the nodes, not the distance)
#     Returns the list of nodes corresponding to shortest path
#     """
#     shortest = None
#     for path in paths:
#         if shortest == None or path[1][0] < shortest[1][0]:
#             shortest = path
#     return shortest[0]
#     
# def findShortestOutdoor(paths):
#     """
#     Accepts (paths). A list  of tuples. The first item in each tuple is a list of nodes. The second item is a tuple (total distance, total outdoor distance).
#     Loops through paths and finds one with lowest outdoor distance value
#     Returns the list of nodes corrosponding to shortest outdoor path
#     """
#     shortest = None
#     for path in paths:
#         if shortest == None or path[1][1] < shortest[1][1]:
#             shortest = path
#     return shortest[0]
# 
# def findShortestDistance(paths, maxTotalDist, maxDistOutdoors):
#     """
#     (paths). A list  of tuples. The first item in each tuple is a list of nodes. The second item is a tuple (total distance, total outdoor distance).
#     (maxTotalDist) an int.
#     (maxDistOutdoors) an int.
#     Loops through paths and finds shortest one that does not exceed maxTotalDist and maxDistdoors
#     Returns list of nodes
#     """
#     shortest = None
#     for path in paths:
#         if shortest == None or path[1][0] < shortest[1][0]:
#             if path[1][0] < maxTotalDist and path[1][1] < maxDistOutdoors:
#                 shortest = path
#     if shortest != None:
#         return shortest[0]
#     else:
#         raise ValueError

# def findShortest(paths, maxTotalDist, maxDistOutdoors):
#     """
#     (paths). A list  of tuples. The first item in each tuple is a list of nodes. The second item is a tuple (total distance, total outdoor distance).
#     (maxTotalDist) an int.
#     (maxDistOutdoors) an int.
#     Loops through paths and finds shortest one that does not exceed maxTotalDist and maxDistdoors
#     Returns list of nodes
#     """
#     shortest = None
#     for path in paths:
#         if shortest == None or len(path[1]) < len(shortest[1]):
#             if path[1][0] < maxTotalDist and path[1][1] < maxDistOutdoors:
#                 shortest = path
#     if shortest != None:
#         return shortest[0]
#     else:
#         raise ValueError



# Short code to test output from functions
# #f = open('/Users/Lucy/Desktop/nodes.txt', 'w+')
# mitMap = load_map('mit_map.txt')
# paths = DFSBruteW(mitMap, '1', '13')


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
    global f #set tester file to global
    def DFSBruteW(digraph, start, end, path = [], paths = []):
        """
        Helper function accepts start and end nodes
        Returns a list of paths (each path a list of nodes) 
        """
        path = path + [start]
        f.write(str(path)) # tester code. Writes all paths taken to file
        f.write('\n' )

        if start == end:
            path = path + [end]
            paths.append(path)
        for node in digraph.childrenOf(start):
            if node not in path: #avoid cycles
                newPath = DFSBruteW(digraph,node,end,path,paths)
        return paths

    def findShortest(digraph, paths, maxTotalDist, maxDistOutdoors):
        """
        (paths). A list  of tuples. The first item in each tuple is a list of nodes. The second item is a tuple (total distance, total outdoor distance).
        (maxTotalDist) an int.
        (maxDistOutdoors) an int.
        Loops through paths and finds shortest one that does not exceed maxTotalDist and maxDistdoors
        Returns list of nodes
        """
        shortest = None
        # Calculating length of each path
        
        for path in paths:
            pathDistance  = 0
            pathOutdoorDistance = 0
            for i in range(len(path)-1):
                node1 = path[i]
                node2 = path[i+1]
                weights = digraph.getWeights(node1, node2)
                pathDistance = pathDistance + weights[0]
                pathOutdoorDistance = pathDistance + weights[1]

            if shortest == None or len(path) <= len(shortest):
                if pathDistance <= maxTotalDist and pathOutdoorDistance <= maxDistOutdoors:
                    shortest = path
        if shortest != None:
            return shortest
        else:
            return ValueError

    paths = DFSBruteW(digraph, start, end)
    return findShortest(digraph, paths, maxTotalDist, maxDistOutdoors)
#
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

# Tester file
f = open('/Users/Lucy/Desktop/paths.txt', 'w+') # create global test file

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
#     Test cases
    mitMap = load_map("/Users/Lucy/Dropbox/2_active_projects/6002x/week5/PSET5/ProblemSet5/mit_map.txt")
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    print 'nodes', mitMap.nodes
    print 'edges', mitMap.edges
# 
# 
    LARGE_DIST = 1000000

#     Test case 1
#     print "---------------"
#     print "Test case 1:"
#     print "Find the shortest-path from Building 32 to 56"
#     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#    print "DFS: ", dfsPath1
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

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

#     Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

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

#     Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
# #     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
#     
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

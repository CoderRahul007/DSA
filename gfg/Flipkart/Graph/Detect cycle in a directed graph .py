# Given a directed graph, check whether the graph contains a cycle or not.
#  Your function should return true if the given graph contains at least one cycle, else return false.

# Example: 

# Input: n = 4, e = 6 
# 0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3, 3 -> 3 
# Output: Yes 
# Explanation: 
 
# WHITE : Vertex is not processed yet. Initially, all vertices are WHITE.
# GRAY: Vertex is being processed (DFS for this vertex has started, but not 
# finished which means that all descendants (in DFS tree) of this vertex are
#  not processed yet (or this vertex is in the function call stack)
# BLACK : Vertex and all its descendants are processed. While doing DFS, if 
# an edge is encountered from current vertex to a GRAY vertex, then this edge is back edge and hence there is a cycle. 
 

# Algorithm:  

# Create a recursive function that takes the edge and color array (this can be also kept as a global variable)
# Mark the current node as GREY.
# Traverse all the adjacent nodes and if any node is marked GREY then return true as a loop is bound to exist.
# If any adjacent vertex is WHITE then call the recursive function for that node.
#  If the function returns true. Return true.
# If no adjacent node is grey or has not returned true then mark the current Node 
# as BLACK and return false.

class Solution:
    
    def DFSUtil(self, u, color , adj):
  
        color[u] = "GRAY"
    
        for v in adj[u]:
    
            if color[v] == "GRAY":
                return True
    
            if color[v] == "WHITE" and self.DFSUtil(v, color ,adj) == True:
                return True
    
        color[u] = "BLACK"
        return False
        
    def isCyclic(self, V, adj):
        # code here
        color = ["WHITE"] * V
 
        for i in range(V):
            if color[i] == "WHITE":
                if self.DFSUtil(i, color , adj) == True:
                    return True
        return False

# Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Space Complexity :O(V). 

#####################################################################################################################################

# Solution using Depth First Search or DFS

# Approach: Depth First Traversal can be used to detect a cycle in a Graph. 
# DFS for a connected graph produces a tree. There is a cycle in a graph only
#  if there is a back edge present in the graph. A back edge is an edge that is 
# from a node to itself (self-loop) or one of its ancestors in the tree produced 
# by DFS. In the following graph, there are 3 back edges, marked with a cross sign.
#  We can observe that these 3 back edges indicate 3 cycles present in the graph.
 
# Depth First Traversal to detect a cycle in a Graph

# For a disconnected graph, Get the DFS forest as output. To detect cycle,
#  check for a cycle in individual trees by checking back edges.
# To detect a back edge, keep track of vertices currently in the recursion
#  stack of function for DFS traversal. If a vertex is reached that is already
#  in the recursion stack, then there is a cycle in the tree. The edge that
#  connects the current vertex to the vertex in the recursion stack is a back edge.
#  Use recStack[] array to keep track of vertices in the recursion stack.
# Dry run of the above approach: 
 
# Dry run of Depth First Traversal to detect a cycle in a Graph

# In the above image there is a mistake node 1 is making a directed edge to 2 not with 0 please make a note.

# Algorithm: 
# Create the graph using the given number of edges and vertices.
# Create a recursive function that initializes the current index or vertex, visited,
#  and recursion stack.
# Mark the current node as visited and also mark the index in recursion stack.
# Find all the vertices which are not visited and are adjacent to the current node.
#  Recursively call the function for those vertices, If the recursive function returns true, return true.
# If the adjacent vertices are already marked in the recursion stack then return true.
# Create a wrapper class, that calls the recursive function for all the vertices and
#  if any function returns true return true. Else if for all vertices the function returns false return false.
# Implementation: 


  
from collections import defaultdict
  
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
  
    def addEdge(self,u,v):
        self.graph[u].append(v)
  
    def isCyclicUtil(self, v, visited, recStack):
  
        # Mark current node as visited and 
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
  
        # Recur for all neighbours
        # if any neighbour is visited and in 
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
  
        # The node needs to be popped from 
        # recursion stack before function ends
        recStack[v] = False
        return False
  
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False
  
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
    print( "Graph has a cycle")
else:
    print("Graph has no cycle")
  

# Output: 

# Graph contains cycle
# Complexity Analysis: 
# Time Complexity: O(V+E). 
# Time Complexity of this method is same as time complexity of DFS traversal which is O(V+E).
# Space Complexity: O(V). 
# To store the visited and recursion stack O(V) space is needed.

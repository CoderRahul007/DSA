# How to implement the above algorithm? 
# We use a boolean array mstSet[] to represent the set of vertices 
# included in MST. If a value mstSet[v] is true, then vertex v is 
# included in MST, otherwise not. Array key[] is used to store key
# values of all vertices. Another array parent[] to store indexes of 
# parent nodes in MST. The parent array is the output array which is
# used to show the constructed MST. 


# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph
 
import sys # Library for INT_MAX
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print ("Edge \tWeight")
        for i in range(1, self.V):
            print (parent[i], "-", i, "\t", self.graph[i][parent[i]])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):
 
        # Initialize min value
        min = sys.maxsize
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
 
    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):
 
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1 # First node is always the root of
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
 
            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
 
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
 
        self.printMST(parent)
 
g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
 
g.primMST()
 
# Contributed by Divyanshu Mehta
# Output: 

# Edge   Weight
# 0 - 1    2
# 1 - 2    3
# 0 - 3    6
# 1 - 4    5
# The Time Complexity of the above program is O(V^2). If the input graph is
#  represented using adjacency list, then the time complexity of Prim’s algorithm 
#  can be reduced to O(E log V) with the help of a binary heap.  In this implementation,
#   we are always considering the spanning tree to start from the root of the graph, 
# and this is the basic difference between Kruskal’s Minimum Spanning Tree and Prim’s Minimum Spanning tree.




#######################################################################################################################

# As discussed in the previous post, in Prim’s algorithm, two sets are maintained,
#  one set contains list of vertices already included in MST,
#  other set contains vertices not yet included. With adjacency list representation, 
#  all vertices of a graph can be traversed in O(V+E) time using BFS. The idea is to
#   traverse all vertices of graph using BFS and use a Min Heap to store the vertices
#    not yet included in MST. Min Heap is used as a priority queue to get the minimum 
#    weight edge from the cut. Min Heap is used as time complexity of operations like 
#    extracting minimum element and decreasing key value is O(LogV) in Min Heap.

# Following are the detailed steps. 

# Create a Min Heap of size V where V is the number of vertices in the given graph. 
# Every node of min heap contains vertex number and key value of the vertex. 
# Initialize Min Heap with first vertex as root (the key value assigned to first vertex
#  is 0). The key value assigned to all other vertices is INF (infinite). 
# While Min Heap is not empty, do following 
# Extract the min value node from Min Heap. Let the extracted vertex be u. 
# For every adjacent vertex v of u, check if v is in Min Heap (not yet included in MST). 
# If v is in Min Heap and its key value is more than weight of u-v, then update the key 
# value of v as weight of u-v.

# A Python program for Prims's MST for
# adjacency list representation of graph


import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        key = [float('inf')]*V
        vis = [False] * V
        
        par = [-1] * V
        
        key[0] = 0
        lst = []
        
        heapq.heappush(lst , (0 , 0)) # distance and vertex
        
        while lst:
            di , curr = heapq.heappop(lst)
            
            vis[curr] = True
            
            for v in adj[curr]:
                node = v[0]
                d = v[1]
                if not vis[node]  and d < key[node]:
                    par[node] = curr
                    key[node] = d
                    heapq.heappush(lst  , (key[node] , node))
        return sum(key)

# T - O(ElogV).
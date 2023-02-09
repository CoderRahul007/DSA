# A Bipartite Graph is a graph whose vertices can be divided into 
# two independent sets, U and V such that every edge (u, v) either
#  connects a vertex from U to V or a vertex from V to U. In other
#   words, for every edge (u, v), either u belongs to U and v to V, 
#   or u belongs to V and v to U. We can also say that there is no edge that connects vertices of same set.

# Algorithm to check if a graph is Bipartite: 
# One approach is to check whether the graph is 2-colorable or not using backtracking algorithm m coloring problem. 
# Following is a simple algorithm to find out whether a given graph is Bipartite or not using Breadth First Search (BFS). 
# 1. Assign RED color to the source vertex (putting into set U). 
# 2. Color all the neighbors with BLUE color (putting into set V). 
# 3. Color all neighbor’s neighbor with RED color (putting into set U). 
# 4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2. 
# 5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot be 
# colored with 2 vertices (or graph is not Bipartite) 

class Solution:

        def isBipartite(self, V, adj):
            #code here
            colorArr = [-1 for i in range(V)]

            for i in range(V):
                if colorArr[i] == -1:
                    colorArr[i] = 1
                    q = []
                    q.append(i)
                    while q:
                        u = q.pop(0)
                        for v in adj[u]:
                            if colorArr[v] == -1:
                                colorArr[v] = 0 if colorArr[u] == 1 else 1
                                q.append(v)
                            elif colorArr[v] == colorArr[u]:
                                return False
            return True

# If Graph is represented using Adjacency List .Time Complexity will be O(V+E).
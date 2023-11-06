# Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

# Notice
# Each connected component should sort by label.

class Solution:
    def countComponents(edges , n):
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            res = n
            while res != par[n]: # of its equal to res it means it is its own parent 
                par[res] = par[par[res]] # path compresion to get the grandparents
                res = par[res]
            return res
        
        def union( n1 , n2):
            p1 , p2 = find(n1) , find(n2)

            if p1 == p2:
                return 0

            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] += 1
            
            return 1
        
        connectedComponents = n
        for n1 , n2 in edges:
            connectedComponents -= union(n1 , n2)

        return connectedComponents
        

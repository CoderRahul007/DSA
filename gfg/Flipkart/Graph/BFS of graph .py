class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        bfs = []
        q = [0]
        d= {}
        d[0] = True
        
        while q:
            u = q.pop(0)
            bfs.append(u)
            for i in adj[u]:
                if i not in d:
                    q.append(i)
                    d[i] = True
        return bfs
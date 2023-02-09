class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		def checkForCycle(s , V , adj  , vis):
		    q = []
		    vis[s] = True
		    q.append([s , -1])
		    
		    while q:
		        n , parent = q.pop(0)
		        for child in adj[n]:
		            if not vis[child]:
		                vis[child] = True
		                q.append([child , n])
		            elif parent != child and vis[child]:
		                return True
		    return False
		        
		        
		vis = [False]*(V+1)
		for i in range(V):
		    if not vis[i]:
		        if checkForCycle(i , V , adj , vis):
		            return True
		return False


###########################################################################
# DFS

class Solution:
    
    #Function to detect cycle in an undirected graph.
        def dfsCycleHelper(self,node,parent,vis,adj):
            vis[node] = True
            for i in adj[node]:
                if not vis[i]:
                    if self.dfsCycleHelper(i,node,vis,adj) :
                        return True
                elif i != parent:
                    return True
            return False    
        def isCycle(self, V, adj):
            #Code here
            vis = [False for _ in range(V)]
            for i in range(V):
                if not vis[i] and self.dfsCycleHelper(i,-1,vis,adj):
                        return True
            return False
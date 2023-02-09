import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        l = []*(V+1)
        dis = [float('inf')]*V
        dis[S] = 0
        heapq.heappush(l , (0 , S))
        while l:
            di , curr = heapq.heappop(l)
            for i in adj[curr]:
                nextdis = i[1]
                nextcurr = i[0]
                
                if di + nextdis < dis[nextcurr]:
                    dis[nextcurr] = di + nextdis
                    heapq.heappush(l , (dis[nextcurr] , nextcurr))
        return dis
# 1584. Min Cost to Connect All Points
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = { i: [] for i in range(N)}

        for i in range(N):
            x1 , y1 = points[i]
            for j in range(i + 1 , N):
                x2 , y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([ dist , j])
                adj[j].append([ dist , i])
        res = 0
        minH = [[0 , 0]] # cost , node
        visit = set()

        while len(visit) < N:
            cost , node = heapq.heappop(minH)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for neiCost , nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minH , [neiCost , nei])
    
        return res
 # O(n^2 logn)        
# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

# Example 1:


# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            tmpPrices = prices[:]
            for s , d , p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        
        return prices[dst] if prices[dst] != float('inf') else -1

# O(E . V)        


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for flight in flights:
            adjList[flight[0]].append(flight[1:])

        cost = [inf] * n
        cost[src] = 0
        q = deque([(src, cost[src])])
        steps = -1
        while steps < k and len(q):
            size = len(q)
            print(q)
            while size:
                curr, curr_cost = q.popleft()
                for nei, path_cost in adjList[curr]:
                    if curr_cost + path_cost < cost[nei]:
                        q.append((nei, curr_cost + path_cost))
                        cost[nei] = curr_cost + path_cost
                size -= 1
            steps += 1
        
        if cost[dst] != inf:
            return cost[dst]
        return -1
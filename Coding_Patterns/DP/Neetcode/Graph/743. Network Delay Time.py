# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

import collections , heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v , w in times:
            edges[u].append((v , w))
                
        total = 0
        minheap = [(0 , k)]
        visit = set()

    # here we are using the minheap so that we get the shorted weight path to a node
        while minheap:
            w1 , n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            total = max(total , w1)
            visit.add(n1)

            for n2 , w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap , (w1 + w2 , n2))
        
        return total if len(visit) == n else -1
# E log v
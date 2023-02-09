# Given a Directed Acyclic Graph (DAG) with V vertices and E edges, 
# Find any Topological Sorting of that Graph.
# Output:
# 1
# Explanation:
# The output 1 denotes that the order is
# valid. So, if you have, implemented
# your function correctly, then output
# would be 1 for all test cases.
# One possible Topological order for the
# graph is 3, 2, 1, 0.

#Function to return list containing vertices in Topological order.

class Solution:
    def topoSort(self, V, adj):
        # Code here
        #create an indegree counter for each node
        #add all 0 indegree nodes to the queue
        # while queue pop from 0 and decrement the neighbors
        #if any of the neighbors is 0 add to queue
        #keep going until queue is empty
        in_degree = [0] *V
        for i in range(V):
            for to in adj[i]:
                in_degree[to] +=1
        
        queue = []
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
        index = 0
        sort = [0] *V
        while queue:
            current = queue.pop(0)
            sort[index] = current
            index +=1
            for to in adj[current]:
                in_degree[to] -=1
                if in_degree[to] == 0:
                    queue.append(to)
        if index != V:
            return False
        return sort

 # TC-O(N+E) ,SC-O(2N)
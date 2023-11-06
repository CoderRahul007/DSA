# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

import collections
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        
        def path_exists(u , v):
            if u == v:
                return True
            visited.add(u)
            
            for neigh in graph[u]:
                if neigh not in visited:
                    if path_exists( neigh , v):
                        return True
            return False
        for u, v in edges:
            visited = set()
            if path_exists(u , v):
                return [u , v]
            else:
                graph[u].append(v)
                graph[v].append(u)
        return None


# O n ^ 2 


# Union FInd ( DOne know the flow ) O(n)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = {v:-1 for v in range(1, len(edges)+1)}
        
        # ---------------------------------
        
        def find(u):
            
            if parent[u] != -1:
                # find root with path compression
                parent[u] = find(parent[u])
                return parent[u]
            
            else:
                # root node must be with -1
                return u
            
        
        # ---------------------------------
        
        def union(u, v):

           
            parent_of_u = find(u)
            parent_of_v = find(v)
            
            if parent_of_u == parent_of_v:
                
                # u and v has the same parent node
                # this edges froms a cycle in graph
                return True
            
            
            else:
                
                # after adding edge(u, v)
                # graph is still a tree without cycle
                parent[parent_of_u] = parent_of_v
                return False
            
        
        # ---------------------------------
        
        redundant = None
        for u, v in edges:
                        
            if union(u, v):
                # check if edge (u, v) forms a cycle
                redundant = [u, v]
                return redundant
        
        
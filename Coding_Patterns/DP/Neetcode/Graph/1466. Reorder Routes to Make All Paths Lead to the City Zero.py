# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = { (a,b) for a,b in connections}
        visit = set()
        changes = 0
        neighbors = { city : [] for city in range(n)}
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(city):
            nonlocal changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                
                if (neighbor , city) not in roads:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)
        
        visit.add(0)
        dfs(0)
        return changes

# O(n)
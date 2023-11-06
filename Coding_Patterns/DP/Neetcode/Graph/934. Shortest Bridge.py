# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1

# Approach:
# Perform a depth-first search (DFS) to find the first island in the grid. Mark the visited cells as you traverse through the island.
# Start a breadth-first search (BFS) from the visited cells of the first island. Keep expanding to neighboring cells until you find the second island or exhaust all possible cells.
# During the BFS, maintain the level (distance) from the first island. Return the level when you encounter the second island.
# If no second island is found, return -1 to indicate that no bridge exists between the two islands.


class Solution:
    def shortestBridge(self, grid):
        m, n = len(grid), len(grid[0])
        start_i, start_j = next((i, j) for i in range(m) for j in range(n) if grid[i][j])
        
        
        stack = [(start_i, start_j)]
        visited = set(stack)
        while stack:
            i, j = stack.pop()
            visited.add((i, j))  
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] and (ii, jj) not in visited:
                    stack.append((ii, jj))
                    visited.add((ii, jj))
        
        
        ans = 0
        queue = list(visited)
        while queue:
            new_queue = []
            for i, j in queue:
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited:
                        if grid[ii][jj] == 1:
                            return ans
                        new_queue.append((ii, jj))
                        visited.add((ii, jj))
            queue = new_queue
            ans += 1
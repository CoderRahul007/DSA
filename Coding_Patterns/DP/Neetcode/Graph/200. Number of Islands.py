# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])        
        def bfs(i, j):
            q = collections.deque([(i, j)])
            visited.add((i, j))
            while q:
                r, c = q.popleft() # for making DFS make it to pop()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr == M or nc < 0 or nc == N:
                        continue
                    if grid[nr][nc] == '0' or (nr, nc) in visited:
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
            return None

        visited = set()
        islands = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '0' or (i, j) in visited:
                    continue
                bfs(i, j)
                islands += 1
        return islands



# O(M*N)
# The time complexity of finding the number of islands in a grid is O(M*N), where M is the number of rows and N is the number of columns12. The space complexity is O((M,N))
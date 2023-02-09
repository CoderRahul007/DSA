# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
#  return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally
#  or vertically. You may assume all four edges of the grid are all surrounded by water.


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


# DFS
from collections import deque


class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        if not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        numIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(i, j, m, n, grid)
                    numIslands += 1
        return numIslands

    def dfs(self, i, j, m, n, grid):
        if grid[i][j] == '1':
            grid[i][j] = '2'
            moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for (movex, movey) in moves:
                def inBound(x, y, m, n):
                    return x >= 0 and x < m and y >= 0 and y < n

                if inBound(i + movex, j + movey, m, n):
                    self.dfs(i + movex, j + movey, m, n, grid)


# BFS


def numIslands(self, grid):
    if not grid:
        return 0
    row, col = len(grid), len(grid[0])
    s = set([(i, j) for i in range(row)
            for j in range(col) if grid[i][j] == "1"])
    num = 0
    while s:
        num += 1

        queue = deque([s.pop()])
        while queue:
            i, j = queue.popleft()
            for item in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if item in s:
                    s.remove(item)
                    queue.append(item)
    return num

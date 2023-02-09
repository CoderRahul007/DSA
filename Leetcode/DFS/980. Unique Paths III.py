# You are given an m x n integer array grid where grid[i][j] could be:

# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square,
#  that walk over every non-obstacle square exactly once.

# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.

# The idea is to recusively explore all possible paths from the starting cell '1',
# stopping exploration as soon as paths are found to be invalid. The trick to ensure
# each cell is traversed only once is to change its value from '0' to '-1' right after
#  its visited, so it is considered a wall. However, after checking valid movements in all
#   4 directions, be careful to revert grid values to 0 in order to consider previously
#   unexplored paths(if not, grid will only be traversed once).

# First, we loop through all elements of grid to(1) count all traversable cells(i.e. 1, 2 and 0s)
# and (2) find the starting point(i.e. cell '1' coordinates). This information is stored
# in to_visit and start_r, start_c respectively.

# Next, we implement the dfs function, which will construct the graph of all possible paths,
#  backtracking whenever we either(1) find a wall or a previously visited cell or (2) reach
#  the ending cell '2' without having visited all the grid's 0s.


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
            self.R, self.C = len(grid), len(grid[0])
            self.directions = (0, 1), (0, -1), (1, 0), (-1, 0)
            to_visit = 0
            for r in range(self.R):
                for c in range(self.C):
                    # count all 0s, 1 and 2 cells to be visited
                    if grid[r][c] != -1:
                        to_visit += 1
                    # find starting point i.e. cell 1
                    if grid[r][c] == 1: 
                        start_r, start_c = r, c

            return self.dfs(grid, start_r, start_c, to_visit)
        
    def dfs(self, grid, r, c, to_visit):
        # check if out of range or wall found
        if not (0 <= r < self.R and 0 <= c < self.C) or grid[r][c] == -1: 
            return 0
        
        # found end cell, valid path if all 0s visited
        if grid[r][c] == 2: 
            return to_visit == 1
        
        # valid movement, keep going
        elif grid[r][c] in [0, 1]:
            res = 0
            # mark as visited
            grid[r][c] = -1
            # check movements in all 4 directions
            for dr, dc in self.directions:
                res += self.dfs(grid, r + dr, c + dc, to_visit - 1)
            # mark prev explored cell as unvisited
            grid[r][c] = 0
        return res
###########################################################################################

class Solution:
    def dfs(self, grid: List[List[int]], x: int, y: int, emptyCell: int) -> int:
        # base cases -
        # 1. out of bounds and obstacles
        if x == -1 or x == len(grid) or y == -1 or y == len(grid[0]) or grid[x][y] == -1:
            return 0
        # 2. reached the ending square, check if it can be a valid 4-directional walk
        if grid[x][y] == 2:
            return emptyCell == 0
        # since it is an empty cell, we visit the current cell
        grid[x][y] = -1
        # do the 4-directional dfs walk from here
        walks = (self.dfs(grid, x + 1, y, emptyCell - 1)   # visit SOUTH 
               + self.dfs(grid, x - 1, y, emptyCell - 1)   # visit NORTH 
               + self.dfs(grid, x, y + 1, emptyCell - 1)   # visit EAST 
               + self.dfs(grid, x, y - 1, emptyCell - 1))  # visit WEST 
        # coming back we backtrack, un-visit the current cell
        grid[x][y] = 0
        return walks
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        emptyCell, xIdx, yIdx = 1, 0, 0
        # counting the no. of empty cells and getting the position of starting square
        # x and y coordinate of starting square are xIdx and yIdx respectively
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == 1:
                    xIdx, yIdx = i, j
                elif grid[i][j] == 0:
                    emptyCell += 1
        return self.dfs(grid, xIdx, yIdx, emptyCell)
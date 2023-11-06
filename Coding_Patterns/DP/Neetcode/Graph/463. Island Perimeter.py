# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4

# O( n * m)


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()

        def dfs(r , c):
            if (r , c) in visit:
                return 0
            if r not in ROWS or c not in COLS or grid[r][c] == 0:
                return 1

            visit.add((r,c))
            
            perim = dfs(r + 1 , c)
            perim += dfs(r - 1 , c)
            perim += dfs(r , c + 1)
            perim += dfs(r , c - 1)
            return perim
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r , c)        

# Here these blocks and they intersect at one edge. So perimeter(4+4=8) will be reduced by 2 (removing intersected edge at each square) upon each intersection. Each block in the land has four neighbours. We need to check whether the neighbour is land or not and decrement perimeter based on intersections.


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
					R,C = len(grid), len(grid[0])
					perimeter = 0
					# Traverse the grid
					for i in range(R):
						for j in range(C):
							# If it is a land block increment perimeter by 4
							if grid[i][j] == 1:
								perimeter += 4
								# Check whether top neighbour is a land and decrement it by 2
								# as it intersects
								if i > 0 and grid[i-1][j] == 1:
									perimeter -= 2
								# Check left neighbour is a land and decrement it by 2
								# as it intersects
								if j > 0 and grid[i][j-1] == 1:
									perimeter -= 2
					return perimeter


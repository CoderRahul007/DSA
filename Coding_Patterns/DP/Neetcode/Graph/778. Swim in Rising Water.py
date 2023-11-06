# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

# Example 1:


# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        minheap = [(grid[0][0], 0 , 0)] # time , row , col
        seen = set()
        seen.add((0 , 0))
        while minheap:
            t , r , c = heapq.heappop(minheap)
            if r == ROWS -1 and c == COLS - 1:
                return t
            for i , j in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (i,j) in seen or i not in range(ROWS) or j not in range (COLS):
                    continue
                heapq.heappush(minheap , [max(t , grid[i][j]) , i , j])
                seen.add((i , j))
###############################################
# O(n2 logn)
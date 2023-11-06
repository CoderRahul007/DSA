# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.


# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

# recursion
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def helper(i, j):
            if i >= m or j >= n:
                return float('inf')

            if i == m-1 and j == n-1:
                return grid[i][j]

            return grid[i][j] + min(helper(i+1, j), helper(i, j+1))

        return helper(0, 0)

# Memoization


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        cache = {}

        def helper(i, j):
            if i >= m or j >= n:
                return float('inf')

            if i == m-1 and j == n-1:
                return grid[i][j]

                # return from cache if present
            if (i, j) in cache:
                return cache[(i, j)]

                # populate cache
            cache[(i, j)] = grid[i][j] + min(helper(i+1, j), helper(i, j+1))
            return cache[(i, j)]

        return helper(0, 0)

# djikstra


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dis = [[inf] * len(grid[0]) for _ in range(len(grid))]
        dis[0][0] = grid[0][0]

        pq = [(grid[0][0], 0, 0)]
        directions = [[0, 1], [1, 0]]

        while pq:
            distance, row, col = heappop(pq)

            for dx, dy in directions:
                vis_row = row + dx
                vis_col = col + dy
                if vis_row < len(grid) and vis_row >= 0 and vis_col >= 0 and vis_col < len(grid[0]):
                    if distance + grid[vis_row][vis_col] < dis[vis_row][vis_col]:
                        dis[vis_row][vis_col] = distance + \
                            grid[vis_row][vis_col]
                        heappush(
                            pq, (distance + grid[vis_row][vis_col], vis_row, vis_col))

        return dis[-1][-1]

# In Place


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:  # We just want to skip the top-left corner of the grid
                    continue
                if r-1 < 0:  # Cases for elements in top row
                    grid[r][c] = grid[r][c] + grid[r][c-1]
                elif c-1 < 0:  # Cases for elements in leftmost column
                    grid[r][c] = grid[r][c] + grid[r-1][c]
                else:  # Normal cell
                    grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])

        # We have got the minimum path accumaled at the bottom-right corner, just return this
        return grid[rows-1][cols-1]

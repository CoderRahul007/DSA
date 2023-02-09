# You are given an m x n integer array grid. There is a robot initially located at the top-left corner
#  (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
#   The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot
#  include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

# https://leetcode.com/problems/unique-paths-ii/solutions/184772/unique-paths-ii/

##############################################################################
# Recursive
# TC -> O(mn)
# SC -> O(mn)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        brute force, bottom-up recursively with memorization
        - intuitively go through all the path with i+1 OR j+1
        - count the path which reaches to the destination coordinate (m, n)
        - cache the count of the coordinates which we have calculated before
        - if the current grid, grid[i][j], is blocked, tell its parent that this way is blocked by return 0
        - sum up all the coordinates' count

        Time    O(row*col) since we cache the intermediate coordinates, we wont go through the visited coordinates again
        Space   O(row*col) depth of recursions
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        seen = {}
        return self.dfs(obstacleGrid, 0, 0, len(obstacleGrid)-1, len(obstacleGrid[0])-1, seen)

    def dfs(self, grid, i, j, m, n, seen):

        key = str(i)+","+str(j)
        if key in seen:
            return seen[key]
        if i == m and j == n:
            if grid[i][j] == 1:
                return 0
            return 1
        elif i > m or j > n:
            return 0
        if grid[i][j] == 1:
            seen[key] = 0
            return 0

        left = self.dfs(grid, i+1, j, m, n, seen)
        right = self.dfs(grid, i, j+1, m, n, seen)

        seen[key] = left + right
        return left + right

#########################################################################################

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    R, C = len(obstacleGrid), len(obstacleGrid[0])

    @lru_cache(maxsize=None)
    def dp(r: int, c: int) -> int:
        if r == R - 1 and c == C - 1 and obstacleGrid[r][c] == 0:
            return 1
        if r >= R or c >= C or obstacleGrid[r][c] == 1:
            return 0
        return dp(r + 1, c) + dp(r, c + 1)

    return dp(0, 0)
#######################################################################################
# DP

def uniquePathsWithObstacles(self, obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    # initialization
    dp = [[0] * n for i in xrange(m)]
    for i in xrange(m):
        if obstacleGrid[i][0] == 1: break
        dp[i][0] = 1
    for j in xrange(n):
        if obstacleGrid[0][j] == 1: break
        dp[0][j] = 1
    # dp
    for i in xrange(1, m):
        for j in xrange(1, n):
            if not obstacleGrid[i][j]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        grid = [[0]*n for row in range(m)]
            
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    continue
                if row == 0 and col == 0:
                    grid[0][0] = 1
                if row - 1 >= 0 and obstacleGrid[row-1][col] == 0:
                    grid[row][col] += grid[row-1][col]
                if col - 1 >= 0 and obstacleGrid[row][col-1] == 0:
                    grid[row][col] += grid[row][col-1]
                
        return grid[-1][-1]
###########################################################################################
# Without modifying input

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        a = [0 if i == 1 else 1 for i in obstacleGrid[0]]
        b = [0] * n
        for i in range(1, len(a)):
            if a[i-1] == 0:
                a[i] = 0
        for row in range(1, m):
            for col in range(n):
                if col == 0:
                    b[col] = a[col] if obstacleGrid[row][col] == 0 else 0
                else:
                    b[col] = b[col-1] + a[col] if obstacleGrid[row][col] == 0 else 0
            a = b
            b = [0] * n
        return a[-1]


################################################################################
# Dp

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[m-1][n-1]
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).


# Example 1:


# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:


# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# Example 3:

# Input: matrix = [[1]]
# Output: 1

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS , COLS =  len(matrix) , len(matrix[0])
        dp = {}
        def dfs(r , c , prevVal):
            if ( r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prevVal):
                return 0
            key = (r,c)
            if key in dp:
                return dp[key]
            
            res = 1
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            for rowDir, colDir in directions:
                res = max(res, 1 + dfs(r + rowDir, c + colDir, matrix[r][c]))
            dp[key] = res
            return res
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r , c , -1)
        
        return max(dp.values())


# O( n * m)
# O( n * m)


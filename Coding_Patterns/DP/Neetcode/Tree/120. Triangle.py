# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0]*(len(triangle) + 1)
        
        for row in triangle[::-1]:
            for i , ele in enumerate(row):
                dp[i] = ele + min(dp[i] , dp[i + 1]) 
        return dp[0]
        # bottom up approach so that we can get the min sum

# TC- O(n^2)        
# SC - O(n)
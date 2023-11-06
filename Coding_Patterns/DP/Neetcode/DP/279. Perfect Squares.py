# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words,
# it is the product of some integer with itself. For example, 1, 4, 9, and 16 are 
# perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for target in range(1 , n + 1):
            limit = target ** 0.5
            # for all the decision tree
            for s in range(1 , int(limit) + 1):
                sq = s*s
                dp[target] = min( dp[target] , 1 + dp[target - sq]) # we are using a bottom up approach here 
                # suppose n = 12 and we got sq = 4 so we will have to get dp[4] so that we get total minimum number of sq required for the n
        return dp[n]


# O(n* n^0.5)
# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:

# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

# Time - O( n^2) 
# Space - O(n)

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = { 1 : 1}
        def dfs( num ):
            if num in dp:
                return dp[num]
            dp[num] = 0 if num == n else num # so that original problem should be broken down but not the subprpblem
            for i in range(1 , num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num] , val)
            return dp[num]
        return dfs(n)

# DP

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = { 1 : 1}
        for num in range(2 , n + 1):
            dp[num] = 0 if num == n else num # so that original problem should be broken down but not the subprpblem
            for i in range(1 , num // 2 + 1):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num] , val)
        return dp[n]

# for each number we can either break or take it as whole to produce max result that's why max(j,dp[j]), max(i-j,dp[i-j])
# i//2 because after half j and i-j will start reapeating.
# for example=>i=7
# j=2,i-j=5
# j=5,i-j=2
# Both are same

class Solution:
    def integerBreak(self, n: int) -> int:
        # Initialize dp array with 0's
        dp = [0]*(n+1)
        
        # Base case
        dp[2] = 1
        
        # Iterate from 3 to n
        for i in range(3, n+1):
            # Iterate from 1 to i//2
            for j in range(1, i//2+1):
                # Calculate the product of j and i-j
                prod = j*(i-j)
                
                # Update the maximum product in dp[i]
                dp[i] = max(dp[i], max(prod, j*dp[i-j]))
        
        # Return dp[n]
        return dp[n]

# https://www.youtube.com/watch?v=-w67-4tnH5U

# Given an integer N and a 2D array cost[][3], where cost[i][0],
#  cost[i][1], and cost[i][2] is the cost of painting ith house 
#  with colors red, blue, and green respectively, the task is to 
# find the minimum cost to paint all the houses such that no two 
# adjacent houses have the same color.

# Examples:

# Input: N = 3, cost[][3] = {{14, 2, 11}, {11, 14, 5}, {14, 3, 10}}
# Output: 10
# Explanation: 
# Paint house 0 as blue. Cost = 2. Paint house 1 as green. Cost = 5. Paint house 2 as blue. Cost = 3.
# Therefore, the total cost = 2 + 5 + 3 = 10.

# Input: N = 2, cost[][3] = {{1, 2, 3}, {1, 4, 6}}
# Output: 3

# https://www.geeksforgeeks.org/minimize-cost-of-painting-n-houses-such-that-adjacent-houses-have-different-colors/

def minCosts( costs ):
    dp = [ 0 , 0 , 0]
    for i in range(len(costs)):
        dp0 = costs[i][0] + min(dp[1] , dp[2])
        dp1 = costs[i][1] + min(dp[0] , dp[2])
        dp2 = costs[i][2] + min(dp[0] , dp[1])
        dp = [dp0 , dp1 , dp2]
    return min(dp)

# O(n)
# O(1)
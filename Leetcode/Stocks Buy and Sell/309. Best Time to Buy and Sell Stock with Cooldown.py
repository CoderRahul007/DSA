# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many 
# transactions as you like (i.e., buy one and sell one share of the stock 
# multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously 
# (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0

# Definition
# Define dp[i][state] as the max profit at the end of day i,
#  where the first dimension is the index of the day, and the second denotes its state at the end of day i:

# 0: we currently have one share of the stock, so we can sell or hold (do nothing) on the next day
# 1: we currently don’t have any share of the stock and are stamped with a 
# “cooldown” mark (meaning must cooldown next day), so we can do nothing on the next day
# 2: we currently don’t have any share of the stock and are not stamped 
# with a “cooldown” mark, so we can buy or hold on the next day
# State Transition

# 1 . dp[i][0]

# The stock on hand at the end of day icould be:

# already owned on day i-1
# bought on day i, which means we have no stock and are stamped with “cooldown” on day i-1
# so, dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])

# 2. dp[i][1]


# We currently have no stock and are stamped with “cooldown”, 
# which means we sold a share of the stock on day i and we must 
# hold one share on day i-1. So, dp[i][1] = dp[i-1][0] + prices[i]

# 3. dp[i][2]

# Have no stock and are not stamped with “cooldown”, which means we 
# have no stock on day i-1. So, the state of day i-1 could be either 
# marked as cooldown or not. So, dp[i][2] = max(dp[i-1][1], dp[i-1][2])

# The max profit during a n-day period is max(dp[n][0], dp[n][1], dp[n][2]).
#  Notice that having any share of the stock at the end of day n is not wise 
#  if we want to get the maximum profit, so the result is max(dp[n][1], dp[n][2])

# Initialization
# dp[0][0] = -prices[0], the stock on hand at the end of the first day could only be bought on this day
# dp[0][1] = 0. Even though we couldn’t be stamped as cooldown on the first day, 
# it will be harmless to initialize it as 0. Becausedp[0][1] only affects dp[1][2] 
# and dp[1][2] = max(dp[0][1], dp[0][2]), dp[1][2] must be dp[0][2], so as long as 
# dp[0][1] <= dp[0][2], it does not affect the result.
# dp[0][2] = 0, which is obvious
# Code

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0, 0, 0] for _ in xrange(n)]
        dp[0][0] = -prices[0]
        
        for i in xrange(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1][1], dp[-1][2])

# Time complexity: O(n)
# Space complexity: O(n)


# Optimization of Memory
# Notice that the states on day i depend only on those on day i-1, 
# so we don’t have to store the information before day i-1. So, we 
# just need to store dp[i-1][0], dp[i-1][1], and dp[i-1][2], and use them to update states on day i.

# Code

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        state0, state1, state2 = -prices[0], 0, 0
        
        for i in xrange(1, n):
            state00 = max(state0, state2 - prices[i])
            state11 = state0 + prices[i]
            state22 = max(state1, state2)
            state0, state1, state2 = state00, state11, state22
        return max(state1, state2)

# Time complexity: O(n)
# Space complexity: O(1)

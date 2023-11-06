
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                # State: canBuy or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, canBuy) val=max_profit

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            cooldown = dfs(i + 1, canBuy)
            if canBuy:
                buy = dfs(i + 1, not canBuy) - prices[i]
                dp[(i, canBuy)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not canBuy) + prices[i]
                dp[(i, canBuy)] = max(sell, cooldown)
            return dp[(i, canBuy)]

        return dfs(0, True)
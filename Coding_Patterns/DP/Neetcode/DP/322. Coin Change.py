# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

# Recursive
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(memo, n):
            if memo[n]: # it's already calculated, simply return it
                return memo[n]
            if n == 0:
                return 0
            memo[n] = float("inf")
            for coin in coins:
                if n - coin >= 0:
                    memo[n] = min(memo[n], dfs(memo, n-coin)+1)
            return memo[n]
        
        memo = collections.defaultdict(int)
        tmp = dfs(memo, amount)
        return tmp if tmp != float("inf") else -1
    

# Memo with pruning
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(memo, n):
            if n == 0:
                return 0
            memo[n] = float("inf")
            for coin in coins:
                if n - coin >= 0:
                    if memo[n - coin]:
                        memo[n] = min(memo[n], memo[n - coin]+1)
                    # It also stops exploring when the branch could not give a better result than already found.
                    # With the current coin value and the min number of coins,
                    #  no need to run dfs() if it can't satisfy the remaining amount.
					elif n - coin < memo[n]*coin:
                        memo[n] = min(memo[n], dfs(memo, n-coin)+1)
            return memo[n]
        
        coins.sort(reverse = True)
        memo = collections.defaultdict(int)
        tmp = dfs(memo, amount)
        return tmp if tmp != float("inf") else -1    


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        numCoins = len(coins)
        
        # Values in this array equal the number of coins needed to achieve the cost of the index
        minCoins = [amount + 1] * (amount + 1)
        minCoins[0] = 0
        
        # Loop through every needed amount
        for i in range(amount + 1):
            # Loop through every coin value
            for coin in coins:
                # Check that the coin is not bigger than the current amount
                if coin <= i:
                    # minCoins[i]: number of coins needed to make amount i
                    # minCoins[i-coin]: number of coins needed to make the amount before adding 
                    #                   the current coin to it (+1 to add the current coin)
                    minCoins[i] = min(minCoins[i], minCoins[i-coin] + 1)
        
        # Check if any combination of coins was found to create the amount
        if minCoins[amount] == amount + 1:
            return -1
        
        # Return the optimal number of coins to create the amount
        return minCoins[amount]

########################################
#         
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        if not amount:
            return 0

        
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for v in range(1 , amount + 1):
            for c in coins:
                if c <= v:
                    dp[v] = min( dp[v] , 1 + dp[v-c]) # dp[v-c] means if we have another sol with [v-c] 
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]


        
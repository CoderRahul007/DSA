# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money
#  cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

 

# Example 1:

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

class Solution:
    
    def brute(self, coins, i, target):
        if target == 0:
            return 1
        
        if i >= len(coins):
            return 0
        
        coin = coins[i]
        c1 = 0
        if (target - coin) >= 0:
            c1 = self.brute(coins, i, target - coin)
        
        c2 = self.brute(coins, i + 1, target)
        
        return c1 + c2

    def change(self, amount: int, coins: List[int]) -> int:
        return self.brute(coins, 0, amount)


##############
# memo

def coin_change(amount  , coins):
    dp = {}
    def memo(i , a):
        if a == amount:
            return 1
        if a > amount:
            return 0
        if i >= len(coins):
            return 0
        key = (i,a)

        include = memo(i , a + coins[i])
        exclude = memo( i + 1 , a)
        dp[key] =  include + exclude

        return dp[key]
    
    return memo(0 , 0)

###
# 2 D array

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for j in range(len(coins) + 1)] for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1 , amount + 1):
            for i in range(len(coins)-1 , -1 , -1):
                dp[a][i] = dp[a][i+1] # exclude 
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a-coins[i]][i] # include
        return dp[amount][0]

####
# 1 D memory
class Solution:

    def change(self, target: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]
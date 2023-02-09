# You are given an integer array coins representing coins of different denominations and
#  an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount
#  of money cannot be made up by any combination of the coins, return -1.

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

### Greedy approach wont work link is below

##########################################################
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        q = deque()
        q.append((amount, 0))
        visited = set()
        visited.add(amount)

        while q:
            curr_amt, level = q.popleft()
            if curr_amt == 0:
                return level
            for c in coins:
                new_amt = curr_amt - c
                if new_amt >= 0 and new_amt not in visited:
                    q.append((new_amt, level+1))
                    visited.add(new_amt)
        return -1

#########################################################################

# https://dev.to/shivams136/leetcode-322-coin-change-solution-4kmd

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
                    dp[v] = min( dp[v] , 1 + dp[v-c])
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]


        
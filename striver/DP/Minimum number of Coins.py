# Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } 
# and a target value N.
# Find the minimum number of coins and/or notes needed to make the change for Rs N.


# Example 1:

# Input: N = 43
# Output: 20 20 2 1
# Explaination: 
# Minimum number of coins and notes needed 
# to make 43. 

class Solution:
    def minPartition(self, amount):
        # code here
        denominations = [1, 2, 5, 10, 20, 50, 100,200, 500, 2000]
        c = 0
        arr=[]
        for denomination in reversed(denominations):
            if amount >= denomination:
                temp = amount // denomination
                while temp:
                    arr.append(denomination)
                    temp-=1
            amount %= denomination
        return arr

################################################

# for count of min number of coins
denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    c = 0
    for denomination in reversed(denominations):
        c += amount // denomination
        amount %= denomination
    return c

#########################################

# We maintain a vector ‘dp’ of size AMOUNT+1 and initialize it to a maximum value (say AMOUNT + 1).
# Here, dp[i] stores the minimum number of coins needed to change an amount ‘i’. 

 

# Algorithm

 

#     We set dp[0] to 0 as minimum coins to change an amount of ‘0’ is 0.
#     We then traverse denominations from beginning to end (loop variable i).
#         We loop from denominations[i] to amount (loop variable j).
#             Now, if we pick the i-th coin, we will be interested in minimum coins needed to make a 
#             change of amount j - denominations[i].
#             So, we set dp[j] to the minimum of dp[j] and dp[j - denominations[i]] + 1.
#     Finally, we return dp[amount] as answer.
# USing DP
'''
    Time Complexity: O(AMOUNT * N)
    Space Complexity: O(AMOUNT)

    where AMOUNT is the given amount to be changed
    and N is the size of DENOMINATIONS array/list.
'''


denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    n = len(denominations)

    maxVal = amount + 1

    dp =  [maxVal] * (amount + 1)

    dp[0] = 0

    # Pick each coin
    for i in range(n):
        for j in range(denominations[i], amount + 1):
                dp[j] = min(dp[j], dp[j - denominations[i]] + 1)

    return dp[amount]
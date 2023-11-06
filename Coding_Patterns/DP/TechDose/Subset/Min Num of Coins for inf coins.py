
# For example, consider S = { 1, 3, 5, 7 }.
# If the desired change is 15, the minimum number of coins required is 3
 
# (7 + 7 + 1) or (5 + 5 + 5) or (3 + 5 + 7)
 
 
# If the desired change is 18, the minimum number of coins required is 4
 
# (7 + 7 + 3 + 1) or (5 + 5 + 5 + 3) or (7 + 5 + 5 + 1) 

import sys
 
 
# Function to find the minimum number of coins required
# to get a total of `target` from set `S`
def findMinCoins(S, target , n):
 
    # if the total is 0, no coins are needed
    if target == 0:
        return 0
 
    # return infinity if total becomes negative
    if target < 0 or n < 0:
        return sys.maxsize
 
    return min(findMinCoins(S, target , n-1), findMinCoins(S, target - S[n] , n) + 1)

def findMinCoinsDp(arr , target) :
    dp = [[0 for i in range(target+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[0][i] = 0
    for i in range(1 , target+1):
        dp[0][i] = sys.maxsize
    for i in range(1 , n+1):
        for j in range(1 , target+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j] , dp[i][j-arr[i-1]] + 1)
    return dp[n][target]

# here dp[i][j-arr[i-1]] i is not decremented bcz we can select a coin inf times so we are staying after decrementing target
 
 

#findMinCoins(S, target - S[n] , n) means include the coin and dont change the coin
#dont include coin and change coin findMinCoins(S, target , n-1)

 
 
if __name__ == '__main__':
 
    # coins of given denominations
    S = [1, 3, 5, 7]
 
    # total change required
    target = 15
    n = len(S) -1
 
    coins = findMinCoins(S, target , n)
    
    if coins != sys.maxsize:
        print('The minimum number of coins required to get the desired change is',
            coins)

    print(findMinCoinsDp(S,target))
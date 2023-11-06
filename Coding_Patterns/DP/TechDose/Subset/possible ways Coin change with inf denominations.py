# find the number of possible ways to form a given amount using the 
# given coin denominations having infinite instances of each
#  coin denomination.We can solve this problem using recursion but the time 
#  complexity will be exponential

# let coins = [1 , 2 ,5 ] sum = 5
# so either we include or exclude the coins
# if we include we have to minus the amount by coin and stay in that coin since its have inf denomintaions

# for recursive call max depth = amount/least_val_coin
# Time complexity Number of coin ^ max_level



# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n
def countWays(S, n, target):
    # if the total is 0, return 1 (solution found)
    if target == 0:
        return 1
 
    # return 0 (solution does not exist) if total becomes negative,
    # no elements are left
    if target < 0 or n < 0:
        return 0
 
    # Case 1. Include current coin `S[n]` in solution and recur
    # with remaining change `target-S[n]` with the same number of coins
    incl = countWays(S, n, target - S[n])
 
    # Case 2. Exclude current coin `S[n]` from solution and recur
    # for remaining coins `n-1`
    excl = countWays(S, n - 1, target)
 
    # return total ways by including or excluding current coin
    return incl + excl

def countUsingLookUp(S, n, target, lookup):
 
    # if the total is 0, return 1 (solution found)
    if target == 0:
        return 1
 
    # return 0 (solution does not exist) if total becomes negative,
    # no elements are left
    if target < 0 or n < 0:
        return 0
 
    # construct a unique key from dynamic elements of the input
    key = (n, target)
 
    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
 
        # Case 1. Include current coin `S[n]` in solution and recur
        # with remaining change `target-S[n]` with the same number of coins
        include = countUsingLookUp(S, n, target - S[n], lookup)
 
        # Case 2. Exclude current coin `S[n]` from solution and recur
        # for remaining coins `n-1`
        exclude = countUsingLookUp(S, n - 1, target, lookup)
 
        # assign total ways by including or excluding current coin
        lookup[key] = include + exclude
 
    # return solution to the current subproblem
    return lookup[key]

def countUsingDp(S, target):
 
    n = len(S)
 
    T = [[0] * (target + 1) for _ in range(n + 1)]
 
    for i in range(n + 1):  #target 0 then 1
        T[i][0] = 1
 
    for i in range(1, n + 1):
        for t in range(1, target + 1):
            if S[i - 1] > t:
                T[i][t] = T[i - 1][t] # exclude
            else:
                T[i][t] = T[i - 1][t] + T[i][t - S[i - 1]]
 
    return T[n][target]

def ReducedSpace(coins, target):
 
    dp = [0] * (target + 1)
    dp[0] = 1
 
    for i in range(len(coins)):
        t = coins[i]
        while t <= target:

            dp[t] += dp[t - coins[i]]
            print("dp[t]" , t ,  dp[t] , dp)
            t = t + 1
 
    return dp[target]
 
 

# Driver program to test above function
arr = [1, 2, 3]
n = len(arr)
target = 4
print(countWays(arr, n-1, 4))
print(ReducedSpace(arr , target))
lookup = {}
print('The total number of ways to get the desired change is',countUsingLookUp(arr, len(arr) - 1, target, lookup))


print(countUsingDp(arr , target))

# This code is contributed by Smitha Dinesh Semwal

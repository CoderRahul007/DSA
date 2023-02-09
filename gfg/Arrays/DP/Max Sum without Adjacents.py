# Given an array Arr of size N containing positive integers. 
# Find the maximum sum of a subsequence such that no two numbers in the sequence 
# should be adjacent in the array.

# Example 1:

# Input:
# N = 6
# Arr[] = {5, 5, 10, 100, 10, 5}
# Output: 110
# Explanation: If you take indices 0, 3
# and 5, then Arr[0]+Arr[3]+Arr[5] =
# 5+100+5 = 110.

# Example 2:

# Input:
# N = 4
# Arr[] = {3, 2, 7, 10}
# Output: 13
# Explanation: 3 and 10 forms a non
# continuous  subsequence with maximum
# sum.

# T - O(n)  Space - O(n)

	
def findMaxSum(arr, n):
    # code here
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr)
    dp = [0]*n
    
    dp[0] = arr[0]
    dp[1] = max(arr[:2])
    
    for i in range(2 , n):
        dp[i] = max(arr[i]+dp[i-2] , dp[i-1])
    return dp[-1]

def recursive( dp , ind , arr):
    if ind == 0:
        return arr[0]
    if ind < 0: 
        return 0
    if dp[ind] != -1:
        return dp[ind]
    take = arr[ind] + recursive(dp, ind -2 , arr)
    nottake = 0 + recursive(dp, ind-1, arr)

    dp[ind] = max(take , nottake)
    return dp[ind]

def findMaxSum(arr , n):
    dp = [-1]*(n+1)
    return recursive(dp, n-1, arr)

def optimal(arr , n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    x = arr[0]
    y = max(arr[:2])

    for i in range(2 , n):
        temp = y
        y = max(y , x + arr[i])
        x = temp
    return y


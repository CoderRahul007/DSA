def countSubsetRecursion(arr , i , sum):
    if sum == 0 : # empty sum is always true 
        return 1
    if i < 0:
        return 0
    if arr[i] > sum:
        return countSubsetRecursion(arr, i-1 , sum)
    else:
        return countSubsetRecursion(arr, i-1 , sum) + countSubsetRecursion(arr, i-1 , sum-arr[i])

def count_subsets_with_sum(arr, k):
    n = len(arr)

    # Create a 2D table to store the counts of subsets
    # dp[i][s] represents the number of subsets of arr[:i] with sum equal to s
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Initialize the first column with 1 since an empty subset has a sum of 0
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill the table using bottom-up DP
    for i in range(1, n + 1):
        for s in range(1, k + 1):
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s] + dp[i - 1][s - arr[i - 1]] # excude and include
            else:
                dp[i][s] = dp[i - 1][s] # exclude 

    return dp[n][k]


arr = [1,2,1]
sum = 3
i = len(arr) -1
print(countSubsetRecursion(arr , i , sum))
print(count_subsets_with_sum(arr  , sum))

def countSubsetRecursion(arr , i , sum):
    if sum == 0 : # empty sum is always true 
        return 1
    if i < 0:
        return 0
    if arr[i] > sum:
        return countSubsetRecursion(arr, i-1 , sum)
    else:
        return countSubsetRecursion(arr, i-1 , sum) + countSubsetRecursion(arr, i-1 , sum-arr[i])

def countSubsetDp(arr,n , sum):
    dp = [[0 for i in range(sum+1)] for j in range(n+1)] 
    for i in range(n + 1):  # If sum is 0, then answer is 1 , this is row
        dp[i][0] = 1
    for i in range(1 ,sum + 1): # If sum is not 0 and set is empty, then answer is 0 , this is column
        dp[0][i] = 0    
    for i in range(1 , n+1):
        for j in range(1 , sum +1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0 and j != 0:
                dp[i][j] = 0
            elif j == 0 and i != 0:
                dp[i][j] = 1
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    print(dp)
    return dp[n][sum]



arr = [1,2,1]
sum = 3
i = len(arr) -1
print(countSubsetRecursion(arr , i , sum))
print(countSubsetDp(arr , len(arr) , sum))

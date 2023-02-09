# Let sum of subset 1 be s1 and subset 2 with s2
# s1 - s2 = diff (given)
# s1 + s2=sum of array (logical)
# Therefore adding both eq we get :
# 2s1= diff + sum of array
# s1= (diff + sum of array)/2;
# Problem reduces to find no of subsets with given sum**

def findNumberOfSubsetsWithDiffRecur(arr , i , sum ):
    if sum == 0 : #means sum is found since we are decrementing sum
        return 1
    if i < 0 : # means sum is not 0 and we are out of bound of list
        return 0 
    if arr[i] >  sum :
        return findNumberOfSubsetsWithDiffRecur(arr , i-1 , sum)
    else :
        return findNumberOfSubsetsWithDiffRecur(arr, i-1 , sum) + findNumberOfSubsetsWithDiffRecur(arr , i-1 , sum - arr[i])

def findNumberOfSubsetsWithDiffDp(arr , n , sum):
    dp = [[0 for i in range(sum+1)] for j in range(n+1)] 
    for i in range(n + 1):  # If sum is 0, then answer is 1 , this is row
        dp[i][0] = 1
    for i in range(1 ,sum + 1): # If sum is not 0 and set is empty, then answer is 0 , this is column
        dp[0][i] = 0    
    for i in range(1 , n+1):
        for j in range(1 , sum +1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    return dp[n][sum]

arr = [5 , 2 , 6 , 4]
diff = 3
sum = (diff + sum(arr)) // 2
print(findNumberOfSubsetsWithDiffRecur(arr , len(arr)-1 , sum))

print(findNumberOfSubsetsWithDiffDp(arr , len(arr) , sum))
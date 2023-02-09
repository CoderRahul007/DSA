# https://www.geeksforgeeks.org/maximize-sum-of-all-elements-which-are-not-a-part-of-the-longest-increasing-subsequence/

# Given an array arr[], the task is to find the maximum sum of all the elements
#  which are not a part of the longest increasing subsequence. 

# Examples: 

# Input: arr[] = {4, 6, 1, 2, 3, 8} 
# Output: 10 
# Explanation: 
# Elements are 4 and 6 

# Input: arr[] = {5, 4, 3, 2, 1} 
# Output: 14 
# Explanation: 
# Elements are 5, 4, 3, 2  

# Approach: 

# The idea is to find the longest increasing subsequence with the minimum sum
#  and then subtract it from the sum of all elements.
# To do this we will use the concept of LIS using Dynamic Programming and store
#  the sum along with the length of the subsequences and update the minimum sum accordingly.
# Below is the implementation of the above approach.


 
# Function to find maximum sum
def findSum(arr, n):
 
    totalSum = 0
 
    # Find total sum of array
    for i in range(n):
        totalSum += arr[i]
 
    # Maintain a 2D array
    dp = [[0] * n for i in range(2)]
 
    for i in range(n):
        dp[0][i] = 1
        dp[1][i] = arr[i]
 
    # Update the dp array along
    # with sum in the second row
    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j]):
 
                # In case of greater length
                # update the length along
                # with sum
                if (dp[0][i] < dp[0][j] + 1):
                    dp[0][i] = dp[0][j] + 1
                    dp[1][i] = dp[1][j] + arr[i]
 
                # In case of equal length
                # find length update length
                # with minimum sum
                elif (dp[0][i] == dp[0][j] + 1):
                    dp[1][i] = min(dp[1][i],
                                   dp[1][j] +
                                     arr[i])
 
    maxm = 0
    subtractSum = 0
 
    # Find the sum that need to
    # be subtracted from total sum
    for i in range(n):
        if (dp[0][i] > maxm):
            maxm = dp[0][i]
            subtractSum = dp[1][i]
 
        elif (dp[0][i] == maxm):
            subtractSum = min(subtractSum,
                              dp[1][i])
 
    # Return the sum
    return totalSum - subtractSum
 
# Driver code
arr = [ 4, 6, 1, 2, 3, 8 ]
n = len(arr)
 
print(findSum(arr, n))
 
# Output: 
# 10
 

# Time Complexity: O(N2) where N is the length of the array arr[]
# Auxiliary Space: O(N)

#################################################################################################
class Solution:
    def maxSumLis(self, arr, n):
        # code here
        if n ==1 :
            return 0
        s = 0
        ans = float('inf')
        maxLen = 0
        dp = []
        for i in range(n):
            s += arr[i]
            dp.append([1 , arr[i]])
        #first = length
        # second = sum
        for i in range(1 , n):
            for j in range(0 , i):
                if arr[i] > arr[j] and ( dp[i][0] < dp[j][0] + 1) or (dp[i][0] == dp[j][0] + 1 and  dp[i][1] > dp[j][1] + arr[i]) :
                    dp[i] = [dp[j][0] + 1  , dp[j][1] + arr[i]]
            if maxLen < dp[i][0] or maxLen == dp[i][0] and ans > dp[i][1] :
                maxLen = dp[i][0]
                ans = dp[i][1]
        return s - ans
        
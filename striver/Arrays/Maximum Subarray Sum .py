# Problem Statement
# You are given an array (ARR) of length N, consisting of integers. 
# You have to find the sum of the subarray (including empty subarray)
#  having maximum sum among all subarrays.
# A subarray is a contiguous segment of an array. In other words, a 
# subarray can be formed by removing 0 or more integers from the beginning, 
# and 0 or more integers from the end of an array.

#  Brute Force Approach

# Let us check for all possible subarrays of the array. For this, 
# we run two loops, where the outer loop points to the left boundary
#  and the inner loop points to the outer boundary of the subarray. 

# Using another loop inside, find the sum of this subarray. Compare
#  it with the maximum subarray sum obtained so far. After checking all 
#  the subarrays, simply return the maximum sum found.
# Time Complexity

# O(N^3), where N is the length of the array.
# There are N*(N+1)/2 subarrays in total, and for each subarray, we find its sum in O(N) time.

# https://www.codingninjas.com/codestudio/problems/maximum-subarray-sum_630526?topList=striver-sde-sheet-problems&leftPanelTab=2

############################################################################

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

    curSum = [0 for i in range(n)] 
    maxSum = 0
    for i in range(n) :

        if(i == 0) :
            curSum[i] = max(curSum[i], arr[i])
        
        else :

            curSum[i] = max(curSum[i], curSum[i-1] + arr[i])
        
        maxSum = max(maxSum, curSum[i])
    
    return maxSum


#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
##################################################################################################################3
#  Inplace Approach

# Looking at the previous approach,we realize that to compute curSum[i], we only require the value of curSum[i-1]. 
# Hence, instead of maintaining a whole array, we can simply keep track of the previous value only.
# Time Complexity

# O(N), where N is the length of the array.

# Traversing the array once takes O(N) time.
# Space Complexity

# O(1), as constant extra space is required.

'''
    Time complexity : O(N)
    Space complexity : O(1)

    where N is the size of array
'''

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

    curSum = 0
    preSum = 0
    maxSum = 0
    for i in range(n) :

        if(i == 0) :
            curSum = arr[i]
        
        else :

            curSum = max(arr[i], preSum + arr[i])
        
        preSum = curSum
        maxSum = max(maxSum, curSum)
    
    return maxSum


#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))

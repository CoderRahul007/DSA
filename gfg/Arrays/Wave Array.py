# Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it
# In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

# If there are multiple solutions, find the lexicographically smallest one.

# Example 1:

# Input:
# n = 5
# arr[] = {1,2,3,4,5}
# Output: 2 1 4 3 5
# Explanation: Array elements after 
# sorting it in wave form are 
# 2 1 4 3 5.

def convertToWave( n , a ):
    # code here
    for i in range(0 , n-1 , 2):
        a[i],a[i+1] = a[i+1] , a[i]
    print(*a)
import sys
class Solution:
    def closestToZero (self,arr, n):
        # your code here
        arr.sort()
        i = 0
        j = n-1
        m = arr[i] + arr[j]
        
        while i < j:
            s = arr[i] + arr[j]
            if s == 0:
                return 0
            if s < 0:
                i+=1
            else:
                j-=1
            if abs(s) < abs(m):
                m =  s
            if abs(s) == abs(m):
                m = max(m , s)
            
        return m



# Given an integer array of N elements. You need to find the maximum sum of two elements such that sum is
#  closest to zero.

# Example 1:

# Input:
# N = 3
# arr[] = {-8 -66 -60}
# Output: -68
# Explanation: Sum of two elements closest to 
# zero is -68 using numbers -60 and -8.

# â€‹Example 2:

# Input: 
# N = 6
# arr[] = {-21 -67 -37 -18 4 -65}
# Output: -14
# Explanation: Sum of two elements closest to
# zero is -14 using numbers -18 and 4.
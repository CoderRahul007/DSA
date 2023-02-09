# Given two sorted arrays A and B of size M and N respectively. 
# Each array may have some elements in common with the other array. 
# Find the maximum sum of a path from the beginning of any array to the end of any of the two arrays.
#  We can switch from one array to another array only at the common elements.Both the arrays are sorted.
# Note: Only one repeated value is considered in the valid path sum.


# Example 1:

# Input:
# M = 5, N = 4
# A[] = {2,3,7,10,12}
# B[] = {1,5,7,8}
# Output: 35
# Explanation: The path will be 1+5+7+10+12
# = 35.


# Example 2:

# Input:
# M = 3, N = 3
# A[] = {1,2,3}
# B[] = {3,4,5}
# Output: 15
# Explanation: The path will be 1+2+3+4+5=15.

class Solution:
    def maxSumPath(self, arr1, arr2, m, n):
        #code here
        i = 0
        j = 0
        res = 0
        s1 = 0
        s2 = 0
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                s1 += arr1[i]
                i +=1
            elif arr1[i] > arr2[j]:
                s2 += arr2[j]
                j +=1
            else:
                res += max(s1 , s2) + arr1[i]
                s1 = s2 = 0
                i +=1
                j +=1
        
        while i < m:
            s1 += arr1[i]
            i+=1
        while j < n:
            s2 += arr2[j]
            j+=1
        
        res += max(s1 , s2)
        return res
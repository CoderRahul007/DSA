# The hiring team aims to find 3 candidates who are great collectively. 
# Each candidate has his or her ability expressed as an integer. 
# 3 candidates are great collectively if product of their abilities is maximum.
#  Given abilities of N candidates in an array arr[],
#  find the maximum collective ability from the given pool of candidates.


# Example 1:

# Input:
# N = 5
# Arr[] = {10, 3, 5, 6, 20}
# Output: 1200
# Explanation:
# Multiplication of 10, 6 and 20 is 1200.

# Example 2:

# Input:
# N = 5
# Arr[] = {-10, -3, -5, -6, -20}
# Output: -90
# Explanation:
# Multiplication of -3, -5 and -6 is -90.



# Scan the array and compute Maximum, second maximum and third maximum element present in the array.
# Scan the array and compute Minimum and second minimum element present in the array.
# Return the maximum of product of Maximum, second maximum and third maximum and product of Minimum, second minimum and Maximum element.

import sys
class Solution:
    def maxProduct(self, arr, n):
        # code here
        mx1 = -sys.maxsize
        mx2 = -sys.maxsize
        mx3 = -sys.maxsize
        
        mn1 = sys.maxsize
        mn2 = sys.maxsize
        
        for i in arr:
            if i > mx1:
                mx3 = mx2
                mx2 =  mx1
                mx1 = i
            elif i > mx2:
                mx3 = mx2
                mx2 = i
            elif i > mx3:
                mx3 = i
            if i < mn1:
                mn2 = mn1
                mn1 = i
            elif i < mn2:
                mn2 = i
        return max(mn1*mn2*mx1 , mx1 *mx2* mx3)
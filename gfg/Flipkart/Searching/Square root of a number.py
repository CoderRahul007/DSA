# Given an integer x, find the square root of x. If x is not a perfect square, then return floor(√x).

 

# Example 1:

# Input:
# x = 5
# Output: 2
# Explanation: Since, 5 is not a perfect 
# square, floor of square_root of 5 is 2.

# Example 2:

# Input:
# x = 4
# Output: 2
# Explanation: Since, 4 is a perfect 
# square, so its square root is 2.

 
class Solution:
    def floorSqrt(self, x): 
        #Your code here
        l = 0
        h = x
        while l <= h:
            m = (l+h)//2
            if m*m == x:
                return m
            elif m*m > x:
                h= m -1
            else:
                l = m+1
        return l-1

# For Input: 
# 5
                                     
# Your Output: 
                                        
# m 2
# l 3
# m 4
# h 3
# m 3
# h 2
# 3 2

# ouput - 2

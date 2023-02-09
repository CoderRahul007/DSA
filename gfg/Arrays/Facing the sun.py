# Given an array H representing heights of buildings.
#  You have to count the buildings which will see the sunrise 
# (Assume : Sun rise on the side of array starting point).

# Example 1:

# Input: 
# N = 5
# H[] = {7, 4, 8, 2, 9}
# Output: 3
# Explanation: As 7 is the first element, it
# can see the sunrise. 4 can't see the
# sunrise as 7 is hiding it.  8 can see.
# 2 can't see the sunrise. 9 also can see
# the sunrise.

class Solution:
    
    def countBuildings(self,arr, n):
        # code herel
        leftM = 0
        c = 0
        for i in range(n):
            if arr[i] > leftM:
                leftM = max(arr[i] , leftM)
                c +=1
        return c
# Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.

# Example 1:

# Input:
# R=4
# C=5
# M=[[1,2,-1,-4,-20],
# [-8,-3,4,2,1],
# [3,8,10,1,3],
# [-4,-1,1,7,-6]]
# Output:
# 29
# Explanation:
# The matrix is as follows and the
# blue rectangle denotes the maximum sum
# rectangle.

# https://www.youtube.com/watch?v=yCQN096CwWM

def kadane(arr):
    ans = -float('inf')
    temp = 0
    for i in range(len(arr)):
        temp += arr[i]
        ans = max(ans,temp)
        temp = max(temp , 0)
    return ans
    
class Solution:
    def maximumSumRectangle(self,R,C,M):
        #code here
        ans = -float('inf')
        for i in range(C):
            t = [0]*R
            for j in range(i , C):
                for k in range(R):
                    t[k]+=M[k][j]
                ans = max(ans , kadane(t))
        return ans
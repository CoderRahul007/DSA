# Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s. 

# Example: 

# Input:
# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0
# Output :
# 8
# Explanation : 
# The largest rectangle with only 1's is from 
# (1, 0) to (2, 3) which is
# 1 1 1 1
# 1 1 1 1 

# Input:
# 0 1 1
# 1 1 1
# 0 1 1      
# Output:
# 6
# Explanation : 
# The largest rectangle with only 1's is from 
# (0, 1) to (2, 2) which is
# 1 1
# 1 1
# 1 1
# Recommended Practice
# Max Rectangle
# Try It!

# There is already an algorithm discussed a dynamic programming based solution for finding the largest square with 1s. 

# Approach: In this post, an interesting method is discussed that uses largest rectangle under histogram as a subroutine. 
# If the height of bars of the histogram is given then the largest area of the histogram can be found. This way in each row, the largest area of bars of the histogram can be found. To get the largest rectangle full of 1’s, update the next row with the previous row and find the largest area under the histogram, i.e. consider each 1’s as filled squares and 0’s with an empty square and consider each row as the base.

# Illustration: 

# Input :
# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0
# Step 1: 
# 0 1 1 0  maximum area  = 2
# Step 2:
# row 1  1 2 2 1  area = 4, maximum area becomes 4
# row 2  2 3 3 2  area = 8, maximum area becomes 8
# row 3  3 4 0 0  area = 6, maximum area remains 8
# Algorithm: 

# Run a loop to traverse through the rows.
# Now If the current row is not the first row then update the row as follows, if matrix[i][j] is not zero then matrix[i][j] = matrix[i-1][j] + matrix[i][j].
# Find the maximum rectangular area under the histogram, consider the ith row as heights of bars of a histogram. This can be calculated as given in this article Largest Rectangular Area in a Histogram
# Do the previous two steps for all rows and print the maximum area of all the rows.
# Note: It is strongly recommended to refer to this post first as most of the code is taken from there. 

# Implementation 


# Python3 program to find largest rectangle
# with all 1s in a binary matrix
 
# Finds the maximum area under the
# histogram represented
# by histogram. See below article for details.
 
 
class Solution():
    def maxHist(self, row):
        # Create an empty stack. The stack holds
        # indexes of hist array / The bars stored
        # in stack are always in increasing order
        # of their heights.
        stack = []
 
        # Top of stack
        top_val = 0
 
        # Initialize max area in current
        max_area = 0
        # row (or histogram)
 
        area = 0  # Initialize area with current top
 
        # Run through all bars of given
        # histogram (or row)
        i = 0
        while (i < len(row)):
 
            # If this bar is higher than the
            # bar on top stack, push it to stack
            if (len(stack) == 0) or (row[stack[-1]] <= row[i]):
                stack.append(i)
                i += 1
            else:
 
                # If this bar is lower than top of stack,
                # then calculate area of rectangle with
                # stack top as the smallest (or minimum
                # height) bar. 'i' is 'right index' for
                # the top and element before top in stack
                # is 'left index'
                top_val = row[stack.pop()] # 3
                area = top_val * i # i is the right smaller since its less than the top of stack left smaller will  be 0 since stack is empty
 
                if (len(stack)):
                    area = top_val * (i - stack[-1] - 1) # since the stack elements are in
                    # increasing order so left smaller will be the top of stack
                    # i right smaller  and stack[-1] is the left smaller
                max_area = max(area, max_area)
 
        # Now pop the remaining bars from stack
        # and calculate area with every popped
        # bar as the smallest bar
        while (len(stack)):
            top_val = row[stack.pop()]
            area = top_val * i
            if (len(stack)):
                area = top_val * (i - stack[-1] - 1)
 
            max_area = max(area, max_area)
 
        return max_area
 
    # Returns area of the largest rectangle
    # with all 1s in A
    def maxRectangle(self, A):
 
        # Calculate area for first row and
        # initialize it as result
        result = self.maxHist(A[0])
 
        # iterate over row to find maximum rectangular
        # area considering each row as histogram
        for i in range(1, len(A)):
 
            for j in range(len(A[i])):
 
                # if A[i][j] is 1 then add A[i -1][j]
                if (A[i][j]):
                    A[i][j] += A[i - 1][j]
 
            # Update result if area with current
            # row (as last row) of rectangle) is more
            result = max(result, self.maxHist(A[i]))
 
        return result
 
 
# Driver Code
if __name__ == '__main__':
    A = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
    ans = Solution()
 
    print("Area of maximum rectangle is",
          ans.maxRectangle(A))
 
#  Complexity Analysis:  

# Time Complexity: O(R x C). 
# Only one traversal of the matrix is required, so the time complexity is O(R X C)
# Space Complexity: O(C). 
# Stack is required to store the columns, so space complexity is O(C)

##################################################################################################
# Another Solution

# https://www.youtube.com/watch?v=0do2734xhnU
from collections import deque

class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)

        def leftsmaller(nums):
            stack = deque()
            res = []
            for i, val in enumerate(nums):
                while stack and val <= stack[-1][1]: # if smaller elements is nums[i] then larger elements are popped from stack 
                    stack.pop()
                if not stack:
                    res.append(-1)
                else:
                    res.append(stack[-1][0]) # if larger elements is nums[i] then it will store the top of stack in res

                stack.append((i, val))
            return res

        def rightsmaller(nums):
            stack = deque()
            res = []
            for i in range(len(nums)-1, -1, -1):
                while stack and nums[i] <= stack[-1][1]: # if smaller elements is nums[i] then larger elements are popped from stack 
                    stack.pop()
                if not stack:
                    res.append(n)
                else:
                    res.append(stack[-1][0]) # if larger elements is nums[i] then it will store the top of stack in res

                stack.append((i, nums[i]))
            return res[::-1]

        l, r = leftsmaller(heights), rightsmaller(heights)
        res = 0
        for i in range(n):
            res = max(res, (r[i]-l[i]-1)*heights[i])
        return res
    
    def maxArea(self,mat, n, m):
        # code here
        array = list()
        for j in range(m):
            array.append(mat[0][j])
        maxi = self.largestRectangleArea(array)
        for i in range(1,n):
            for j in range(m):
                if mat[i][j]==0:
                    array[j]=0
                else:
                    array[j]+=mat[i][j]
            maxi = max(maxi,self.largestRectangleArea(array))
        return maxi
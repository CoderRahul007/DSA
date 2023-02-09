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

# There is already an algorithm discussed a dynamic programming based solution
# for finding the largest square with 1s.

# Approach: In this post, an interesting method is discussed that uses largest
#  rectangle under histogram as a subroutine.
# If the height of bars of the histogram is given then the largest area of the
# histogram can be found. This way in each row, the largest area of bars of the
# histogram can be found. To get the largest rectangle full of 1’s, update the
#  next row with the previous row and find the largest area under the histogram,
# i.e. consider each 1’s as filled squares and 0’s with an empty square and consider each row as the base.

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
# Now If the current row is not the first row then update the row as follows,
#  if matrix[i][j] is not zero then matrix[i][j] = matrix[i-1][j] + matrix[i][j].
# Find the maximum rectangular area under the histogram, consider the ith row as
# heights of bars of a histogram. This can be calculated as given in this article
#  Largest Rectangular Area in a Histogram
# Do the previous two steps for all rows and print the maximum area of all the rows.
# Note: It is strongly recommended to refer to this post first as most of the code is taken from there.

# Implementation


# Python3 program to find largest rectangle
# with all 1s in a binary matrix

# Finds the maximum area under the
# histogram represented
# by histogram. See below article for details.


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxHistoArea(heights):
            heights.append(0)
            st = []
            res = 0
            for i,height in enumerate(heights):
                while st and height < heights[st[-1]]:
                    h = heights[st.pop()]
                    left = st[-1] if st else -1
                    w = i-left-1
                    res = max(res , h * w)
                st.append(i)
            return res

        array = [int(i) for i in matrix[0]]

        n = len(matrix)
        m = len(matrix[0])

        maxi = maxHistoArea(array)
        for i in range(1, n): # O(n * m)
            for j in range(m):
                if matrix[i][j] == "0":
                    array[j] = 0
                else:
                    array[j] += int(matrix[i][j])
            maxi = max(maxi, maxHistoArea(array))
        return maxi

# O(n * (m + n))
# O(n)

##################################################################################################
# Another Solution


# https://www.youtube.com/watch?v=0do2734xhnU


class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)

        def leftsmaller(nums):
            stack = deque()
            res = []
            for i, val in enumerate(nums):
                # if smaller elements is nums[i] then larger elements are popped from stack
                while stack and val <= stack[-1][1]:
                    stack.pop()
                if not stack:
                    res.append(-1)
                else:
                    # if larger elements is nums[i] then it will store the top of stack in res
                    res.append(stack[-1][0])

                stack.append((i, val))
            return res

        def rightsmaller(nums):
            stack = deque()
            res = []
            for i in range(len(nums)-1, -1, -1):
                # if smaller elements is nums[i] then larger elements are popped from stack
                while stack and nums[i] <= stack[-1][1]:
                    stack.pop()
                if not stack:
                    res.append(n)
                else:
                    # if larger elements is nums[i] then it will store the top of stack in res
                    res.append(stack[-1][0])

                stack.append((i, nums[i]))
            return res[::-1]

        l, r = leftsmaller(heights), rightsmaller(heights)
        res = 0
        for i in range(n):
            res = max(res, (r[i]-l[i]-1)*heights[i])
        return res

    def maxArea(self, mat, n, m):
        # code here
        array = mat[0]
        maxi = self.largestRectangleArea(array)
        for i in range(1, n): # O(n * m)
            for j in range(m):
                if mat[i][j] == 0:
                    array[j] = 0
                else:
                    array[j] += mat[i][j]
            maxi = max(maxi, self.largestRectangleArea(array))
        return maxi
# O(n * m)
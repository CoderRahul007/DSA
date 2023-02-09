# Given an array of integers heights representing the histogram's bar
#  height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4

#################################################################################################

# To get the bigest rectangle area, we should check every rectangle with lowest point at i=1...n.

# Define Si := the square with lowest point at i.
# To calculate faster this Si , we have to use a stack stk which stores some indices.

# The elements in stk satisfy these properties:

# the indices as well as the corresponding heights are in ascending order
# for any adjecent indices i and j (eg. s=[...,i,j,...]), any index k between
# i and j are of height higher than j:
# height[k]>height[j]
# We loop through all indices, when we meet an index k with height lower than
# elements in stk (let's say, lower than index i in stk), we know that the right
#  end of square Si is just k-1. And what is the left end of this square? Well
#  it is just the index to the left of i in stk !

# Another important thing is that we should append a 0 to the end of height,
# so that all indices in stk will be checked this way.

class Solution(object):

    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """        
        # here stack contains lineraly incresing element from bottom to top and
        # each will be the smaller element from the current element index 
        # which will become left 
        # right will be the next smaller element

        # 1. while iterating if we find ele > stack top then push to stack 
        # 2 . else if the ele < stack top then that ele will be right smaller or right boundary
        # and the stack top-1 will be left smaller or left boundary

        heights.append(0)
        stack = []

        result = 0
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:  # 1. step
                h = heights[stack.pop()] # element or h
                left = stack[-1] if stack else -1 # left boundary which is top-1 or -1 if empty
                w = i - left - 1 # width
                result = max(result, h*w)
            stack.append(i)
        return result

##################################################


def twoArraySolution(height):
    n = len(height)
    prevSmall = getPrevSmall(height)
    nextSmall = getNextSmall(height)

    maxArea = 0
    for i in range(n):
        currArea = (nextSmall[i] - prevSmall[i] - 1) * height[i]
        maxArea = max(maxArea, currArea)
    print(maxArea)


def getPrevSmall(height):
    stack = []
    prevSmall = [0]*len(height)

    for i in range(len(height)):
        # while top element of stack is >= current height
        while stack and height[stack[-1]] >= height[i]:
            stack.pop()
        if not stack:
            prevSmall[i] = -1  # prev small is 0
        else:
            prevSmall[i] = stack[-1]  # else previosu small is top element

        stack.append(i)
    return prevSmall


def getNextSmall(height):
    stack = []
    nextSmall = [0]*len(height)

    for i in range(len(height) - 1, -1, -1):
        while stack and height[stack[-1]] >= height[i]:
            stack.pop()
        if not stack:
            nextSmall[i] = len(height)
        else:
            nextSmall[i] = stack[-1]

        stack.append(i)
    return nextSmall


arr = [2, 1, 5, 6, 2, 3]

# oneStack(arr)
(twoArraySolution(arr))

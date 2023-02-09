# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# we need max of left and right boundary height


class Solution:
    def maxArea(self, height: List[int]) -> int:
        mxArea = 0
        left = 0
        right = len(height)-1


        while left < right :
            if height[left] <= height[right]:
               res = height[left] * ( right - left)
               left +=1 # left is smaller or equal so we move forward
            else:
                res = height[right] * (right - left)
                right -=1 # right is smaller or equal so we move backward
            if res > mxArea:
                mxArea = res            
        return mxArea

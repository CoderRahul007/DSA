# Given an integer array nums, move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

# Optimal but more writes image all are 0s then write is to be done more
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        for i in range(len(nums)):
            char = nums[i]
            if char != 0:
                nums[lastNonZero] = char
                lastNonZero +=1
        for i in range(lastNonZero , len(nums)):
            nums[i] = 0

####################################################################################################
# More Optimal

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
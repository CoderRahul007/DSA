# Given an integer array nums, in which exactly two elements appear only once 
# and all the other elements appear exactly twice. Find the two elements that appear only once.
#  You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# Example 2:

# Input: nums = [-1,0]
# Output: [-1,0]
# Example 3:

# Input: nums = [0,1]
# Output: [1,0]

import math
class Solution:
    '''
        say nums = [1,2,1,3,2,5]
        x = XOR(nums) -> 6
        Binary form of 6 is 110

        find the first set bit position and divide the array into 2 based on that bit position
        why?
            Becoz 6 is the result obtained after 3^5 -> if we can throw these numbers into different parts 
            then our smaller arrays looks like -> [find the number that will appear exactly once and 
            remaining elements appear twice]

        Based on 2nd bit position if we partition the array it looks like

        Array1 -> [1,1,5]
        Array2 -> [2,3,2]

        Apply XOR for each part -> TADA!!!! We got what we want

    '''
        
    def checkBit(self, n, i):
        return (n & (1<<i))!=0
    
    def getSetBitPos(self, n):
        for i in range(32):
            if self.checkBit(n, i):
                return i
    
    def singleNumber(self, nums: List[int]) -> List[int]:
        x,n = 0,len(nums)
        if n==2:
            return nums
        
        for i in range(n):
            x^=nums[i]
        
        pos = self.getSetBitPos(x)
        x1,x2 = 0,0
        for i in range(n):
            if self.checkBit(nums[i],pos):
                x1^=nums[i]
            else:
                x2^=nums[i]
        
        return [x1, x2]


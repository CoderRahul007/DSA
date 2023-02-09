# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# You may assume the input array always has a valid answer.


# Example 1:

# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]
# Explanation: [1,4,1,5,1,6] is also accepted.
# Example 2:

# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]


def wiggleSort(self, nums):
    for i, num in enumerate(sorted(nums)[::-1]):
        nums[(1+2*i) % (len(nums) | 1)] = num


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Init
        nums_copy = sorted(nums)
        mid = (len(nums)+1)//2
        left, right = mid-1, len(nums)-1

        # Wiggle sort
        idx = 0
        while left >= 0 or right >= mid:
            if left >= 0:
                nums[idx] = nums_copy[left]
                left -= 1
                idx += 1
            if right >= mid:
                nums[idx] = nums_copy[right]
                right -= 1
                idx += 1
        return

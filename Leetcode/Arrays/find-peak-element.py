# https://leetcode.com/problems/find-peak-element/solutions/127550/find-peak-element/

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        while low <= high:
            if low == high:
                return low
            mid = (low + high) / 2
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid

        return mid

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1
                
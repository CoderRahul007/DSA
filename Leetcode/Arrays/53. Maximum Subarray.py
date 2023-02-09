# Given an integer array nums, find the 
# subarray
#  which has the largest sum and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23

# kadane algo
def maxSubArray(nums):
    sum = res = nums[0]
    for i in range(1,len(nums)):
        sum = max(nums[i], sum+nums[i])
        res = max(res, sum)
    return res

# DP Solution

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums.copy()
        
        for i in range(1, len(nums)):
            prev = dp[i-1]
            cur = dp[i]
            
            if prev + cur > cur:
                dp[i] += prev
        
        return max(dp)    
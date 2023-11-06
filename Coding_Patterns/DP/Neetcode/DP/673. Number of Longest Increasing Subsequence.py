# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

# Constraints:

# 1 <= nums.length <= 2000
# -106 <= nums[i] <= 106

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        maxLIS , res = 0 , 0 #lenght of LIS , count of LIS
        for i in range(len(nums) - 1 , -1  , -1):
            maxLen , mxCount = 1 , 1
            for j in range(i + 1 , len(nums)):
                if nums[j] > nums[i]: # if increasing sequence
                    length , count = dp[j]
                    if length + 1 > maxLen:
                        maxLen , mxCount = length + 1 , count
                    elif length + 1 == maxLen:
                        mxCount += count
            if maxLen > maxLIS:
                maxLIS  , res = maxLen  , mxCount
            elif maxLen == maxLIS:
                res += mxCount
            dp[i] = [maxLen  , mxCount]
        
        return res

# Time  O(n*2 )
# Space O(n)
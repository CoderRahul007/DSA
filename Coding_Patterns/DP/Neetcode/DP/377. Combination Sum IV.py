# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = { 0: 1 }
        for total in range(1, target + 1):
            dp[total] = 0 # this is a new total we dont know about it and will calculate below
            for n in nums:
                dp[total] += dp.get(total - n  , 0) # if we make a decision tree for each n in nums we will find that the 
                # each dp[4] = dp[1] + dp[2] + dp[3]
                # where 4 is target and nums = [ 1 , 2 , 3]
                # so if we cachche the computed value we will make use in future

        return dp[target]
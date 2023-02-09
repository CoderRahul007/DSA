# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you 
# from robbing each of them is that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
#  return the maximum amount of money you can rob tonight without alerting the police.
 
# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

############################################################
# Recurive

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(index):
            if index == len(nums)-1:
                return nums[-1]
            if index > len(nums)-1:
                return 0
            include = helper(index+2) + nums[index]
            exclude = helper(index+1)

            return max(include , exclude)
        return helper(0)

##########################################################
# Memoization

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def helper(index):
            if index == len(nums)-1:
                return nums[-1]
            if index > len(nums)-1:
                return 0
            if index in dp:
                return dp[index]
            include = helper(index+2) + nums[index]
            exclude = helper(index+1)

            dp[index] =  max(include , exclude)
            return dp[index]
            
        return helper(0)

###########################################################
## DP

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums) 

        nums[2] += nums[0]

        for i in range(3,len(nums)):
            nums[i] = nums[i] + max(nums[i-2], nums[i-3])
        
        return max(nums[-1], nums[-2])

def rob(nums):
    if len(nums) == 0:
        return 0
    memo = [0]*(len(nums) + 1)
    memo[0] = 0
    memo[1] = nums[0]

    for i in range(1 , len(nums)):
        val = nums[i]
        memo[i+1] = max(memo[i] , memo[i-1] + val)
    return memo[len(nums)]


         
            
#####################################################
# # Optimizee

# We can notice that in the previous step we use only memo[i] and memo[i-1], 
# so going just 2 steps back. We can hold them in 2 variables instead.
#  This optimization is met in Fibonacci sequence creation and some other problems [to paste links].        

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
        [1,2,3,1]
        max(1 + [3,1] , 2 + [1])
        max(1 + max(3, [1]), 2 + 1)
        max(1 + 3 , 3)
        max(4, 3)
        => 4
        => rob = max( arr[0] + rob[2:n], rob[1:n] )
        '''

        rob1, rob2 = 0, 0

        for num in nums:
            tmp = rob1
            rob1 = max(num + rob2 , rob1)
            rob2 = tmp

        return rob1
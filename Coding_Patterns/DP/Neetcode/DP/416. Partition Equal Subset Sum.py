# Given an integer array nums, return true if you can partition the array into two subsets such
# that the sum of the elements in both subsets is equal or false otherwise.


# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

### Backtrackking Sol ##################

# Let's try solving it using brute-force approach. We need to partition the array into two subsets. This means that for each element of the array, we can either place it in 1st subset, or place it in 2nd subset.

# Since we are only concerned with the sums of subset being equal, we will maintain 1st subset's sum: sum1 & 2nd subset's sum: sum2. For each element, we try both possible options of either placing it in 1st subset and increasing sum1 or placing it in 2nd subset & increasing sum2. Finally, once we reach the end of array, we can check if the current placements gave equal sum. If none of the possible placements give equal sum, we will return false.

class Solution:
    def canPartition(self, nums, i=0, sum1=0, sum2=0):
        if i >= len(nums):
            return sum1 == sum2
        return self.canPartition(nums, i+1, sum1 + nums[i], sum2) or self.canPartition(nums, i+1, sum1, sum2 + nums[i])

# Slightly optimise


class Solution:
    def canPartition(self, nums):
        def subsetSum(s, i=0):
            if s == 0:
                return True
            if i >= len(nums) or s < 0:
                return False
            return subsetSum(s-nums[i], i+1) or subsetSum(s, i+1)
        total_sum = sum(nums)
        return total_sum & 1 == 0 and subsetSum(total_sum // 2)

##############################################################
# Solution - II (Dynamic Programming - Memoization)

# The above solution times out because we were performing repeated calculations over and over unnecessarily. The result for a given parameters sum, i (can we achieve subset sum = sum starting from i index?) will always be the same. So once we have calculated it, we dont need to repea the whole calculation again when it is called from another recursive branch. Instead we can save the result for this state and return it whenever we called again.

# Thus, we can use dynamic programming here. We use a dp array where dp[i][sum] denotes whether subset-sum = sum can be achieved or not starting from the ith index.

# Initially all elements in dp are initialized to -1 denoting that we have not computed that state
# If dp[i][sum] == 1 means that we can achieve sum starting from ith index
# If dp[i][sum] == 0 means we cant achieve that sum starting from the ith index

class Solution:
    def canPartition(self, nums):
        @cache
        def subsetSum(s, i):
            if s == 0: return True
            if i >= len(nums) or s < 0: return False
            return subsetSum(s-nums[i], i+1) or subsetSum(s, i+1)
        total_sum = sum(nums)
        return total_sum & 1 == 0 and subsetSum(total_sum // 2, 0)

# Time Complexity : O(N*sum), where N is the number of elements in nums & sum is the sum of all elements in nums.
# Space Complexity : O(N*sum), required by dp


#########################################################################
#  Solution - IV (Dynamic Programming - Tabulation)

# We can convert the dp approach to iterative version. Here we will again use dp array, where dp[sum] will denote whether sum is achievable or not. Initially, we have dp[0] = true since a 0 sum is always achievable. Then for each element num, we will iterate & find if it is possible to form a sum j by adding num to some previously formable sum.

# One thing to note that it is essential to iterate from right to left in the below inner loop to avoid marking multiple sum, say j1 as achievable and then again using that result to mark another bigger sum j2 (j2=j1+num) as achievable. This would be wrong since it would mean choosing num multiple times. So we start from right to left to avoid overwriting previous results updated in the current loop.

class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum & 1: return False
        half_sum = total_sum // 2
        dp = [True] + [False]*half_sum
        for num in nums:
            for j in range(half_sum, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[half_sum]


# Time Complexity : O(N*sum)
# Space Complexity : O(sum)
##############################
# Optimised one we are storing all the sums and will find if the target exist or not


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) & 1:
            return False
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for j in dp:
                nextDP.add(nums[i] + j)
                nextDP.add(j)
            dp = nextDP
        return target in dp

# O(n * sum(n))

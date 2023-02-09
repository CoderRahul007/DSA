# https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326552/optimization-from-brute-force-to-dynamic-programming-explained/?orderBy=most_votes


# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence


# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

###########################################################################

def lengthOfLIS( nums ):
    def solve( nums , i , prev ):
        if i >= len(nums) :
            return 0                                # cant pick any more elements
        take = 0 
        dontTake = solve(nums, i + 1, prev);           # try skipping the current element
        if nums[i] > prev:
            take = 1 + solve(nums, i + 1, nums[i])   # or pick it if it is greater than previous picked element
        return max(take, dontTake);                                  # return whichever choice gives max LIS
    
    return solve(nums, 0, -float('inf'))

# Time Complexity : O(2^N), where N is the size of nums.
#  At each index, we have choice to either take or not take the element and 
#  we explore both ways. So, we 2 * 2 * 2...N times = O(2^N)
# Space Complexity : O(N), max recursive stack depth.
#########################################################################

def lengthOfLIS( nums ):
    def solve( nums , i , prev_i ):
        if i >= len(nums) :
            return 0     
        if dp[prev_i + 1] != -1:
            return dp[prev_i + 1]

        take = 0 
        dontTake = solve(nums, i + 1, prev);           # try skipping the current element
        if nums[i] > num[prev_i] or prev_i == -1 :
            take = 1 + solve(nums, i + 1, i)   # or pick it if it is greater than previous picked element
        dp[prev_i + 1] = max(take , dontTake)
        return dp[prev_i + 1]
    
    dp = [-1] * (len(nums) + 1)
    return solve(nums, 0, -1)

# Time Complexity : O(N^2), where N is the size of nums.

# Space Complexity : O(N), max recursive stack depth.
###################################################################################

# We can solve it iteratively as well. Here, we use dp array where dp[i] denotes the LIS 
# ending at index i. We can always pick a single element and hence all dp[i] will be initialized to 1.

# For each element nums[i], if there's an smaller element nums[j] before it, the result will 
# be maximum of current LIS length ending at i: dp[i], and LIS ending at that j + 1: dp[j] + 1.
#  +1 because we are including the current element and extending the LIS ending at j.

def lengthOfLIS( nums ):
    ans = 1 
    n = len(nums)
    dp = [1] * n
    for i in range(0 , n):
        for j in range(0 , i):
            if nums[i] > nums[j] :
                dp[i] = max( dp[i] , dp[j] + 1 )
                ans = max( ans , dp[i])
    return ans


################################################################################

# tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
# For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

# len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
# len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
# len = 3   :      [4, 5, 6]            => tails[2] = 6
# We can easily prove that tails is a increasing array. Therefore it is possible 
# to do a binary search in tails array to find the one needs update.

# Each time we only do one of the two:

# (1) if x is larger than all tails, append it, increase the size by 1
# (2) if tails[i-1] < x <= tails[i], update tails[i]
# Doing so will maintain the tails invariant. The the final answer is just the size.
def lengthOfLIS(self, nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

# Runtime: 48 ms nlogn
# https://leetcode.com/problems/longest-increasing-subsequence/solutions/74824/java-python-binary-search-o-nlogn-time-with-explanation/?orderBy=most_votes&languageTags=python

############################################################

class Solution:     # Suppose, for example:
                    #           nums = [1,8,4,5,3,7],
                    # for which the longest strictly increasing subsequence is arr = [1,4,5,7],
                    # giving len(arr) = 4 as the answer
                    #
                    # Here's the plan:
                    #   1) Initiate arr = [num[0]], which in this example means arr = [1]
                    #     
                    #   2) Iterate through nums. 2a) If n in nums is greater than arr[-1], append n to arr. 2b) If 
                    #      not, determine the furthest position in arr at which n could be placed so that arr
                    #      remains strictly increasing, and overwrite the element at that position in arr with n.

                    #   3) Once completed, return the length of arr.

                    # Here's the iteration for the example:

                    #       nums = [ _1_, 8,4,5,3,7]     arr = [1]              (initial step)
                    #       nums = [1, _8_, 4,5,3,7]     arr = [1, 8]           (8 > 1, so    append 8)
                    #       nums = [1,8, _4_, 5,3,7]     arr = [1, 4]           (4 < 8, so overwrite 8)
                    #       nums = [1_8,4, _5_, 3,7]     arr = [1, 4, 5]        (5 > 4, so    append 5)
                    #       nums = [1_8,4,5, _3_, 7]     arr = [1, 3, 5]        (3 < 5, so overwrite 4)
                    #       nums = [1_8,4,5,3, _7_ ]     arr = [1, 3, 5, 7]     (7 > 5, so    append 7)    

                    # Notice that arr is not the sequence given above as the correct seq. The ordering for [1,3,5,7]
                    # breaks the "no changing the order" rule. Cheating? Maybe... However len(arr) = 4 is the 
                    # correct answer. Overwriting 4 with 3 did not alter the sequence's length.
                                
    def lengthOfLIS(self, nums: list[int]) -> int:

        arr = [nums.pop(0)]                  # <-- 1) initial step
 
        for n in nums:                       # <-- 2) iterate through nums
            
            if n > arr[-1]:                  # <--    2a)
                arr.append(n)

            else:                            # <--    2b)
                arr[bisect_left(arr, n)] = n 

        return len(arr)                      # <-- 3) return the length of arr
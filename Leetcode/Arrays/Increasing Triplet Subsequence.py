# Given an integer array nums, return true if there exists a 
# triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
#  If no such indices exists, return false.


# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3: 
            return False
        # we can use two thresholds to divide the subsquence length
        # everything between threshold1 and threshold2 will form doublets
        # everything above threshold2 will form a triplet
        # dynamically change these two thresholds
        
        threshold1 = threshold2 = float("inf")
        for num in nums:
            # lower threshold1
            if num <= threshold1:
                threshold1 = num
            # lower threshold2
            elif num <= threshold2:
                threshold2 = num
            # if greater than both thresholds (note equal doesn't count)
            else:
                return True
        return False
        


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        return self.increasingKlet(nums, 3)

    def increasingKlet(self, nums: List[int], k) -> bool:
        '''
        Approach: start with k-1 very large values, as soon as we 
        find a number bigger than all k-1, return true.
        Time: O(n*k)
        Space: O(k)
        this is the generic solution for this problem
        '''
        small_arr = [math.inf] * (k - 1)

        for num in nums:
            for i in range(k-1):
                if num <= small_arr[i]:
                    small_arr[i] = num
                    break

            if num > small_arr[-1]:
                return True

        return False
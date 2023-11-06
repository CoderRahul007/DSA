# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


# this is very similar to the " max cumulative sum subarray" problem. here you keep 2 values: the max cumulative product UP TO current element starting from SOMEWHERE in the past, and the minimum cumuliative product UP TO current element . it would be easier to see the DP structure if we store these 2 values for each index, like maxProduct[i],minProduct[i] .

# at each new element, u could either add the new element to the existing product, or start fresh the product from current index (wipe out previous results), hence the 2 Math.max() lines.

# if we see a negative number, the "candidate" for max should instead become the previous min product, because a bigger number multiplied by negative becomes smaller, hence the swap()

class Solution:
    def maxProduct(self, nums) :
        ans = nums[0]
        minPro = nums[0] # if only single element
        maxPro = nums[0] # if only single element

    # we are keeping the max and min so that if we encounter -ve and our current min is - then together it will be positive
        for i in range(1 , len(nums)):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if nums[i] < 0:
                maxPro , minPro = minPro , maxPro
           
            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            maxPro = max( maxPro * nums[i] , nums[i])
            minPro = min(minPro * nums[i]  , nums[i])
            
            ans = max(ans , maxPro)

        return ans

obj = Solution()
# obj.maxProduct([-2,0,-1])
obj.maxProduct([2 , 3 , -2 ,  0 ,4])
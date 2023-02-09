# Two Pointer Solution:
# We know our input is always sorted. So the largest squared values are on 
# left and right sides of the input. So we can use 2 pointers (l, r) to compared
#  the left and right most values and insert the larger ones to the resultant list.
# But when we add larger ones first, we have a list that's in descending order. 
# We want the result to be in ascending order. We can simply reverse the resultant list to get that.
# This 2 pointer approach will give us a O(n) solutions.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1 # Initialise 2 pointers
        res = [] # initialise the result list

        while l <= r: # continue the loop untill we go through all values, either with left pointer or with right pointer
            if abs(nums[l]) > abs(nums[r]):
				# If the absolute value at left pointer is bigger, we know the square of left value will be bigger than the right one
                res.append(nums[l]**2)
                l += 1 # increment pointer because we can now look at the next value
            else:
				# If left is not bigger, it's either equal or right value is bigger. In both cases, we can add right value to the result.
                res.append(nums[r]**2)
                r -= 1 # decrement pointer to go to the previous value
        return res[::-1]

# Minor optimisation:
# In the above algorithm, we reverse the output which is a O(n) operation. 
# Which can be avoided by creating a result list of the same length with dummy
#  values (I'm taking 0s here but this doesn't actually matter). The thing to keep
#   in mind is that, we're finding the largest values one by one. So we have to fill
#    the result from the right end, or the starting index will be len(nums) - 1.
#     We keep decrementing this value as we add more values to the result.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums) # create a result list with dummy values
        i = len(nums) - 1 # index on which we will fill the result

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l]**2
                l += 1
            else:
                res[i] = nums[r]**2
                r -= 1
            i -= 1 # we have filled the result on this index, now we go to the index one lesser than this
        return res
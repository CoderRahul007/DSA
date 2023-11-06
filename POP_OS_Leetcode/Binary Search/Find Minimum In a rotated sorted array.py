# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.
class Solution:

    def findMin(self, nums: List[int]) -> int:
        l ,r= 0 ,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m] >nums[r]:
                l=m+1
            else:
                r=m
        return nums[l]## when left == right

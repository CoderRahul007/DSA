# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

#     For example, for arr = [1,2,3], the following are considered permutations of
#  arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].

# The next permutation of an array of integers is the next lexicographically greater
#  permutation of its integer. More formally, if all the permutations of the array 
# are sorted in one container according to their lexicographical order, then the next 
# permutation of that array is the permutation that follows it in the sorted container. I
# f such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

#     For example, the next permutation of arr = [1,2,3] is [1,3,2].
#     Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
#     While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not 
# have a lexicographical larger rearrangement.

# Given an array of integers nums, find the next permutation of nums.

###########################################################################################################################

# The replacement must be in place and use only constant extra memory.
# First, we observe that for any given sequence that is in descending order, no next larger permutation is possible. 
# For example, no next permutation is possible for the following array:

# [9, 5, 4, 3, 1]

# We need to find the first pair of two successive numbers a[i]a[i]a[i] and a[i−1]a[i-1]a[i−1], from the right,
#  which satisfy a[i]>a[i−1]a[i] > a[i-1]a[i]>a[i−1]. Now, no rearrangements to the right of a[i−1]a[i-1]a[i−1] 
#  can create a larger permutation since that subarray consists of numbers in descending order. Thus, we need to 
#  rearrange the numbers to the right of a[i−1]a[i-1]a[i−1] including itself.

# Now, what kind of rearrangement will produce the next larger number? We want to create the permutation just 
# larger than the current one. Therefore, we need to replace the number a[i−1]a[i-1]a[i−1] with the number which 
# is just larger than itself among the numbers lying to its right section, say a[j]a[j]a[j].

# Next Permutation

# We swap the numbers a[i−1]a[i-1]a[i−1] and a[j]a[j]a[j]. We now have the correct number at index i−1i-1i−1. But still the current
#  permutation isn't the permutation that we are looking for. We need the smallest permutation that can be formed by using the
#   numbers only to the right of a[i−1]a[i-1]a[i−1]. Therefore, we need to place those numbers in ascending order to get their 
#   smallest permutation.

# But, recall that while scanning the numbers from the right, we simply kept decrementing the index until we found the pair a[i]a[i]a[i]
#  and a[i−1]a[i-1]a[i−1] where, a[i]>a[i−1]a[i] > a[i-1]a[i]>a[i−1]. Thus, all numbers to the right of a[i−1]a[i-1]a[i−1] were already
#   sorted in descending order. Furthermore, swapping a[i−1]a[i-1]a[i−1] and a[j]a[j]a[j] didn't change that order. Therefore, we simply
#    need to reverse the numbers following a[i−1]a[i-1]a[i−1] to get the next smallest lexicographic permutation.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = e = len(nums)-1
        while k > 0 and nums[k-1] >= nums[k]:
            k -= 1
        if k == 0:           # nums are in descending order
            nums.reverse()
            return  
        while nums[k-1] >= nums[e] :   # find the last "ascending" position
            e -= 1
        nums[k-1], nums[e] = nums[e], nums[k-1] 
        nums[:] = nums[0:k] + list(reversed(nums[k:]))
        
       
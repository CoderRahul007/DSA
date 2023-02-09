# Input: A[] = [1, 2, 3]
# Output: [1, 3, 2]
# Explanation: The lexicographically greater permutation than A[] is [1, 3, 2]

# Input:  A[] = [4, 3, 2, 1]

# Output: [1, 2, 3, 4]
# Approach 1: Brute Force

# A simple approach to solve this problem is to generate all the permutations of the given
#  array and return the permutation which is just greater than the given array.
# But this approach is very naive and won’t work for N > 10.


# Time Complexity: O(N * N!), since total possible permutations are N!
# Space Complexity: O(N), since the permutation is stored.


# Efficient Approach 

# Idea 
# The idea is to find the longest non-increasing(decreasing) suffix and swap it with the pivot element found.
#  Pivot element is the index where A[i] < A[i + 1]. At last reversing the suffix, gives us the next greater permutation.

# Traverse the array from end and find the first index, idx such that A[i] < A[i + 1].
# Again traverse the array from the end and find the first index, idx such that A[i] > A[idx].
# Swap A[idx] and A[ind].
# Reverse the array from idx + 1 till N.
# The base case would be, if the array is in decreasing order, no next permutation will be found, hence return the array in sorted order.

def nextPermutation( nums):
    i = len(nums) - 1
  
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    if i == 0:
        nums.reverse()
        return
    k = i - 1 # pivot element
    j = len(nums) - 1
    while nums[j] <= nums[k]: # Again traverse the array from the end and find the first index, idx such that A[i] > A[idx].
        j -= 1
    nums[k], nums[j] = nums[j], nums[k] # Swap A[idx] and A[i].

    l = k + 1 # start of suffix
    r = len(nums) - 1
    while l < r: # reversing
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

#  https://www.interviewbit.com/blog/next-permutation-problem/
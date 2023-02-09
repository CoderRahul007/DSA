# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost 
# or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array 
# for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.


# You are given an integer array nums and an integer x. In one operation, you can either remove
#  the leftmost or the rightmost element from the array nums and subtract its value from x.
#   Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

def lenOfLongestSubarrayWithSum(arr, n, k):
    prevsums = {}
    total = 0
    maxLen = 0
    for i in range(n):
        total += arr[i]
        if (total == k):
            maxLen = i + 1
        elif (total - k) in prevsums:
            maxLen = max(maxLen, i - prevsums[total - k])
        if total not in prevsums:
            prevsums[total] = i
    return maxLen


def minOperations( nums, x):
    n = len(nums)
    total = sum(nums)
    if total == x:  # if all the elements sum is x then the min operation is length of array else we have to find the maxium subarray of diff of total -x
        return n
    k = lenOfLongestSubarrayWithSum(nums, n, total - x)
    if k == 0:
        return -1
    return n - k  # total - maxium subarray size 
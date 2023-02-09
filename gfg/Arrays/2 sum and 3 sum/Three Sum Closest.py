import sys
class Solution:
    def threeSumClosest (self, arr, target):
    # Your Code Here
        arr.sort()
        n = len(arr)
        m = sys.maxsize
        s = 0
        for i in range(n-2):
            j = i+1
            k = n-1
            
            while j < k:
                s = arr[i]+arr[j]+arr[k]
                if s == target:
                    return s
                    
                elif s > target:
                    k-=1
                else:
                    j+=1
                
                if abs(m-target) > abs(s-target):
                    m = s
                elif abs(s-target) == abs(m-target) and s > m:
                    m = s
        return m

# Given an array, Arr of N numbers, and another number target, find three integers in the array such that the sum is closest to the target. Return the sum of the three integers.

# Note: If there are multiple solutions, print the maximum one.

# Example 1:

# Input:
# N = 6, target = 2
# A[] = {-7,9,8,3,1,1}
# Output: 2
# Explanation: There is one triplet with sum
# 2 in the array. Triplet elements are -7,8,
# 1 whose sum is 2.

# Example 2:

# Input:
# N = 4, target = 13
# A[] = {5,2,7,5}
# Output: 14
# Explanation: There is one triplet with sum
# 12 and other with sum 14 in the array.
# Triplet elements are 5, 2, 5 and 2, 7, 5
# respectively. Since abs(13-12) ==
# abs(13-14) maximum triplet sum will be
# preferred i.e 14.        
# https://www.youtube.com/watch?v=muDPTDrpS28

class Solution:
    def canReach(self, A, N):
        # code here 
        rec = 0
        for i in range(N):
            if rec < i:  # if we reach an index which we cant move from reachability then return False
                return 0
            rec = max(rec , A[i] + i)
        return 1

# Given an positive integer N and a list of N integers A[]. 
# Each element in the array denotes the maximum length of jump you can cover.
#  Find out if you can make it to the last index if you start at the first index of the list.


# Example 1:

# Input:
# N = 6
# A[] = {1, 2, 0, 3, 0, 0} 
# Output:
# 1
# Explanation:
# Jump 1 step from first index to
# second index. Then jump 2 steps to reach 
# 4th index, and now jump 2 steps to reach
# the end.

# Example 2:

# Input:
# N = 3
# A[] =  {1, 0, 2}
# Output:
# 0
# Explanation:
# You can't reach the end of the array.

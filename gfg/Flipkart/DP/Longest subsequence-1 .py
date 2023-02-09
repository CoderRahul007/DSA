# Given an array A[] of size N, find the longest subsequence
#  such that difference between adjacent elements is one.


# Example 1:

# Input: N = 7
# A[] = {10, 9, 4, 5, 4, 8, 6}
# Output: 3
# Explaination: The three possible subsequences 
# {10, 9, 8} , {4, 5, 4} and {4, 5, 6}.


# Example 2:

# Input: N = 5
# A[] = {1, 2, 3, 4, 5}
# Output: 5
# Explaination: All the elements can be 
# included in the subsequence.

class Solution:
    def longestSubsequence(self, N, A):
        # code here
        dp = [1]*N
        for i in range(1 , N):
            for j in range(0 , i):
                if abs(A[i] -  A[j]) == 1:
                    dp[i] = max(dp[j] + 1  , dp[i])
        return max(dp)

# O(n^2) solution 

#################################################
# O(n) solution using hashmap
# https://www.youtube.com/watch?v=opjyzmiTp1I
class Solution:
    def longestSubsequence(self, N, A):
        # code here
        mp = {}
        ma = 0
        for i in A:
            l = 0
            if i - 1 in mp :
                l = mp[i-1]
            if i+1 in mp and mp[i+1] > l:
                l = mp[i+1]
            mp[i] = l+1
            ma = max(mp[i] , ma)
        return ma
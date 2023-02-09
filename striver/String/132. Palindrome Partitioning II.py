# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

# Example 2:

# Input: s = "a"
# Output: 0

# Example 3:

# Input: s = "ab"
# Output: 1

# Approach:

# How to apply DP?

# Lets say we have a palindrome from a to i and to calculate minimum palindrome counts till index i,
# the dp equation will be
# min_count[i] = min (min_count[i], 1+ min_count[a-1] )

# To apply DP equation, for every i we need a list of a (ie indices from where palindrome starts),
# lets call this p_start

# if p_start[i] = [a,b,c] it represents palindromes:

#     from a to i (inclusive),
#     from b to i (inclusive),
#     from c to i (inclusive)

# Eg:
# for aba

# p_start = [
#     [0],
#     [1],
#     [0, 2]
# ]

# Now our DP equation for aba and i=2:

#     dp[2] = min(dp[2], 1+dp[-1]) --> for palindome aba (j=0)
#     dp[2] = min(dp[2], 1+dp[1]) --> for palindrome a (j=2)

# Solution:

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        p_start = [[] for _ in range(n)]

        # odd palindromes
        for i in range(n):
            j = 0
            while i + j < n and i - j >= 0:
                if s[i + j] == s[i - j]:
                    p_start[i + j].append(i - j)
                else:
                    break
                j += 1

        # even palindromes
        for i in range(n):
            j = 0
            while i + j < n and i - j - 1 >= 0:
                if s[i + j] == s[i - j - 1]:
                    p_start[i + j].append(i - j - 1)
                else:
                    break
                j += 1

        min_counts = [math.inf for _ in range(n)]
        for i in range(n):
            for j in p_start[i]:
                min_counts[i] = min(
                    min_counts[i], 1 + (min_counts[j - 1] if j > 0 else 0)
                )

        return min_counts[n - 1] - 1

# Time complexity: O(n^2)

#########################################################################################
# start from back
    def minCut(self, s: str) -> int:
        n=len(s)
        # return self.f(0,n,s)-1
        dp=[0 for i in range(n+1)]
        dp[n]=0
        for i in range(n-1,-1,-1):
            minicost=float("inf")
            for j in range(i,n):
                if s[i:j+1]==s[i:j+1][::-1]:
                    cost = 1+ dp[j+1]
                    minicost = min(minicost,cost)
            dp[i]=minicost
        return dp[0]-1

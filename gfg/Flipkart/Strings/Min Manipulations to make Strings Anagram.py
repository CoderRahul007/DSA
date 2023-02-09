# Given two strings in lowercase, your task is to find minimum number of
#  manipulations required to make two strings anagram without deleting any character. 
# If two strings contains same data set in any order then strings are called Anagrams.

# Example 1:

# Input:
# S1 = "aba", S2 = "baa", N = 3
# Output: 0
# Explanation: Both the strings are already
# anagrams.

# â€‹Example 2:

# Input: 
# S1 = "ddcf", S2 = "cedk", N = 4
# Output: 2
# Explanation: We can change 'e' and 'k' in
# S2 to 'd' and 'f' to make both the strings
# anagram. 


# Note that any pair of difference of characters 
# in both the strings can be resolved in one manipulation.
# For example, if S1 = "abc", S2 = "cbb". Here, only 1
#  pair of characters is different and this can be resolved in
#   one manipulation (by either converting 'a' in S1 to 'b' or
#    converting 'b' in S2 to 'a').

class Solution:
    def minManipulation(self, N, S1, S2): 
        # code here
        cnt = [0]*26
        for i in range(N):
            t1 = ord(S1[i])-ord('a')
            t2 = ord(S2[i])-ord('a')
            cnt[t1]+=1
            cnt[t2]-=1
        steps = 0
        for i in cnt:
            steps+=abs(i)
        return steps//2
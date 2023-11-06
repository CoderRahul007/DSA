# Given a string s, return the longest
# palindromic

# substring
#  in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        mx = 0
        for i in range(len(s)):
            l , r = i , i # odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > mx:
                    res = s[l : r+1]
                    mx = r-l+1
                l-=1
                r+=1
            
            l , r = i , i+1 # even
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > mx:
                    res = s[l : r+1]
                    mx = r-l+1
                l-=1
                r+=1
        return res


# O(n^2)
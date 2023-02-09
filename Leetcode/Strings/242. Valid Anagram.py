# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dp = [0]*256
        for i in range(len(s)):
            schar = s[i]
            tchar =  t[i]
            
            dp[ord(schar)] +=1
            dp[ord(tchar)] -=1
            
        for i in dp:
            if i < 0:
                return False
        return True
        
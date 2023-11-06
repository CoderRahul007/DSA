# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        if len(p)==1:
            res=[]
            for i in range(len(s)):
                if s[i]==p[0]:
                    res.append(i)
            return res
        res=[]
        scount=[0]*26
        pcount=[0]*26
        for i in range(len(p)):
            scount[ord(s[i])-97]+=1
            pcount[ord(p[i])-97]+=1
        for i in range(len(p),len(s)):
            if scount == pcount:
                res.append(i-len(p))
            scount[ord(s[i])-97]+=1
            scount[ord(s[i-len(p)])-97]-=1
        if scount == pcount:
            res.append(len(s)-len(p))
        return res
                 

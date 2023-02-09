# Suppose we have a string s; we have to find the length of the longest substring 
# t that has at most 2 distinct characters.

# So, if the input is like "eceba", then the output will be 3 as t is "ece" which 
# its length is 3.


# The problem can be solved in O(n). Idea is to maintain a window and add elements 
# to the window till it contains less or equal k, update our result if required while 
# doing so. If unique elements exceeds than required in window, start removing the elements from left side. 
# Below are the implementations of above. The implementations assume that the input 
# string alphabet contains only 26 characters (from ‘a’ to ‘z’). The code can be easily extended to 256 c

from collections import defaultdict
def lengthOfLongestSubstringKDistinct( s , k):
    ans = 0
    mp = defaultdict(int)
    n = len(s)
    uniqueNumber = 0
    left = 0
    for right in range(n):
        ch = s[right]
        mp[ch] += 1

        if mp[ch] == 1:
            uniqueNumber += 1
        while uniqueNumber > k and left <= right:
            m[ch] -= 1
            if mp[ch] == 0:
                uniqueNumber -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

# O(n)


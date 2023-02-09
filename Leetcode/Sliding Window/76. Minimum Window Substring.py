# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.


# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Given two strings S and P. Find the smallest window in the string S consisting of all
#  the characters(including duplicates) of the string P.  Return "-1" in case there is
#  no such window present. In case there are multiple such windows of same length, return
# the one with the least starting index.

# Example 1:

# Input:
# S = "timetopractice"
# P = "toc"
# Output:
# toprac
# Explanation: "toprac" is the smallest
# substring in which "toc" can be found.

# Example 2:

# Input:
# S = "zoomlazapzo"
# P = "oza"
# Output:
# apzo
# Explanation: "apzo" is the smallest
# substring in which "oza" can be found.

# https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
####################################################################################################################

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        
        if n > m :
            return ""
        
        shash = defaultdict(lambda : 0)
        thash =  defaultdict(lambda : 0)
        
        for chart in t:
            thash[chart] += 1
        
        counter = 0
        begin = 0        
        startIndex = -1
        length = 0
        minLength = float('inf')
        
        for i ,chars in enumerate(s):
            shash[chars] += 1
            
            if thash[chars] != 0 and shash[chars] <= thash[chars]: # if chars is present in p and count of chars in s is <= t
                counter +=1
            
            if counter == len(t):     # if counter is = len t           
                
                while shash[s[begin]] > thash[s[begin]] or thash[s[begin]] == 0:
                    if shash[s[begin]] > thash[s[begin]]:
                        shash[s[begin]]-=1
                    begin +=1
                
                length = i - begin + 1
                
                if length < minLength:
                    startIndex = begin
                    minLength = length
                    
        if startIndex == -1:
            return ""
        return s[startIndex : startIndex + minLength]

############################################################################################################################
class Solution:

    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    def smallestWindow(self, s, p):

        # if length of string p is greater than string s then we return -1.
        if(len(p) > len(s)):
            return -1

        # using hash tables to store the count of characters in strings.
        shash = [0 for i in range(26)]
        phash = [0 for i in range(26)]

        # storing the count of characters in string p in hash table.
        for char in p:
            phash[ord(char)-ord('a')] += 1

        counter = 0
        begin = 0
        startindex = -1
        length = 0
        minlength = 1e10

        for i in range(len(s)):

            character = ord(s[i])-ord('a')

            # storing the count of characters in string s in hash table.
            shash[character] += 1

            # if count of current character in string s is equal to or less
            # than in string p, we increment the counter.
            if (phash[character] != 0 and
                        shash[character] <= phash[character]):

                    counter += 1

            # if all the characters are matched
            if(counter == len(p)):

                    # we try to minimize the window.                    

                    while (shash[ord(s[begin])-ord('a')] > phash[ord(s[begin])-ord('a')] or phash[ord(s[begin])-ord('a')] == 0):

                        if(shash[ord(s[begin])-ord('a')] > phash[ord(s[begin])-ord('a')]): # if count is more we can decrerease it 
                            shash[ord(s[begin])-ord('a')] -= 1

                        begin += 1

                    # updating window size.
                    length = i-begin+1

                    if(length < minlength):

                        # if new minimum sub-string is found, we store value
                        # of its starting index for new found window.
                        startindex = begin
                        minlength = length

        # returning the smallest window or -1 if no such window is present.
        if(startindex == -1):
            return "-1"
        else:
            return s[startindex: startindex + minlength]

# Time Complexity:  O(N), where N is the length of string. 
# Auxiliary Space: O(1)

######################################################################################################################


def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1

        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

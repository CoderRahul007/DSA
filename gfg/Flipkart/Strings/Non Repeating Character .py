from collections import Counter
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        freq = Counter(s)
        for i in s:
            if freq[i]==1:
                return i
        for i in s:
            if freq[i]!=1:
                return "$"
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


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        
        #if length of string p is greater than string s then we return -1.
    	if(len(p)>len(s)):
    		return -1
    		
    	#using hash tables to store the count of characters in strings.
    	shash=[0 for i in range(26)]
    	phash=[0 for i in range(26)]
    
        #storing the count of characters in string p in hash table.
    	for char in p:
    		phash[ord(char)-ord('a')] += 1
    
    	counter = 0
    	begin = 0
    	startindex = -1
    	length = 0
    	minlength = 1e10
    
    	for i in range(len(s)):
    	    
    	    #storing the count of characters in string s in hash table.
    		shash[ord(s[i])-ord('a')]+=1
            
            #if count of current character in string s is equal to or less 
            #than in string p, we increment the counter.
    		if (phash[ord(s[i])-ord('a')] != 0 and
    		shash[ord(s[i])-ord('a')] <= phash[ord(s[i])-ord('a')] ):
    		    
    			counter += 1
    
            #if all the characters are matched
    		if(counter == len(p)):
    		    
    		    #we try to minimize the window.
    			while (shash[ord(s[begin])-ord('a')] > phash[ord(s[begin])-ord('a')] or phash[ord(s[begin])-ord('a')] == 0):
    				if(shash[ord(s[begin])-ord('a')]  > phash[ord(s[begin])-ord('a')]):
    					shash[ord(s[begin])-ord('a')] -= 1
    					begin += 1
    					
    			#updating window size.
    			length = i-begin+1
    
    			if(length < minlength):
    			    
    			    #if new minimum sub-string is found, we store value
                    #of its starting index for new found window.
    				startindex = begin
    				minlength = length
    
        #returning the smallest window or -1 if no such window is present.
    	if(startindex == -1):
    		return "-1"
    	else:
    		return s[startindex : startindex + minlength]
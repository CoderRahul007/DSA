# Given a string A and a dictionary of n words B, 
# find out if A can be segmented into a space-separated sequence of dictionary words.

# Note: From the dictionary B each word can be taken any number of times and in any order.
# Example 1:

# Input:
# n = 12
# B = { "i", "like", "sam",
# "sung", "samsung", "mobile",
# "ice","cream", "icecream",
# "man", "go", "mango" }
# A = "ilike"
# Output:
# 1
# Explanation:
# The string can be segmented as "i like".


# Example 2:

# Input:
# n = 12
# B = { "i", "like", "sam",
# "sung", "samsung", "mobile",
# "ice","cream", "icecream", 
# "man", "go", "mango" }
# A = "ilikesamsung"
# Output:
# 1
# Explanation:
# The string can be segmented as 
# "i like samsung" or "i like sam sung".

# Recursive
# Recursive implementation of
# word break problem in Python

# returns True if the word can be segmented into parts such
# that each part is contained in dictionary
def wordBreak(word):
	
	global dictionary

	size = len(word)

	# base case
	if (size == 0):
		return True

	# else check for all words
	for i in range(1,size + 1):
		# Now we will first divide the word into two parts ,
		# the prefix will have a length of i and check if it is
		# present in dictionary ,if yes then we will check for
		# suffix of length size-i recursively. if both prefix and
		# suffix are present the word is found in dictionary.

		if (word[0:i] in dictionary and wordBreak(word[i: size])):
			return True

	# if all cases failed then return False
	return False

# set to hold dictionary values
dictionary = set()

# array of strings to be added in dictionary set.
temp_dictionary = [ "mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i","like", "ice", "cream" ]

# loop to add all strings in dictionary set
for temp in temp_dictionary:
	dictionary.add(temp)

# sample input cases
print("Yes" if wordBreak("ilikesamsung") else "No")
print("Yes" if wordBreak("iiiiiiii") else "No")
print("Yes" if wordBreak("") else "No")
print("Yes" if wordBreak("ilikelikeimangoiii") else "No")
print("Yes" if wordBreak("samsungandmango") else "No")
print("Yes" if wordBreak("samsungandmangok") else "No")

#################################################
# Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def memoize(i):
            if i in dp:
                return dp[i]
            if i == 0:
                return True
            for j in range(i):
                if s[j : i] in wordDict and memoize(j) == True:
                    dp[i] = True
                    return dp[i]
            dp[i] = False
            return dp[i]

        
        return memoize(len(s))
        
##########################################################################################
# dynamic Solution

def wordBreak(s, dictionary):
	
	# create a dp table to store results of subproblems
	# value of dp[i] will be true if string s can be segmented
	# into dictionary words from 0 to i.
	dp = [False for i in range(len(s) + 1)]

	# dp[0] is true because an empty string can always be segmented.
	dp[0] = True

	for i in range(len(s) + 1):
		for j in range(0 , i):
			if dp[j] and s[j: i] in dictionary:
				dp[i] = True
				break
	
	return dp[len(s)]

# driver code
dictionary = [ "mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice", "cream" ]

dict = set()
for s in dictionary:
	dict.add(s)

if (wordBreak("ilikesamsung", dict)):
	print("Yes")
else :
	print("No")



##########################################################################
# Dynamic programming with memoization. The big difference from other approaches 
# is I also keep a set of possible word lengths to reduce look ahead possibilities 
# and avoid needing to build new strings.

from typing import List
from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Turn word dict into a set for O(1) lookups
        wordDict = set(wordDict)

        # Keep a set of possible lengths for all words in dict
        lens = set()
        for w in wordDict:
            lens.add(len(w))

        # DP list - i-th index = reached i-th letter in s
        # True = reachable, False = unreachable
        dp = [False for _ in range(len(s) + 1)]
        # Base case where 0 letters is reachable
        dp[0] = True

        for i in range(len(s)):
            # At each letter, check if it is reachable
            if dp[i] == True:
                # If current letter reached, we loop through looking ahead each length
                # and see if next l letters forms a word in wordDict
                for l in lens:
                    # handle case where we reach end. We can break early and return True
                    if i+l == len(s) and s[i:i+l] in wordDict:
                        return True

                    # Handle case where next l letters in wordDict but we haven't reached end
                    # Set look ahead DP to True
                    elif i+l < len(s) and s[i:i+l] in wordDict:
                        dp[i+l] = True
        
        return False
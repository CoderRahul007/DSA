# Given two distinct words startWord and targetWord, and a list denoting wordList 
# of unique words of equal lengths. Find the length of the shortest transformation
#  sequence from startWord to targetWord.
# Keep the following conditions in mind:

#     A word can only consist of lowercase characters.
#     Only one letter can be changed in each transformation.
#     Each transformed word must exist in the wordList including the targetWord.
#     startWord may or may not be part of the wordList.

# The second part of this problem can be found here.


# Example 1:

# Input:
# wordList = {"des","der","dfr","dgt","dfs"}
# startWord = "der", targetWord= "dfs",
# Output:
# 3
# Explanation:
# The length of the smallest transformation
# sequence from "der" to "dfs" is 3
# i,e "der" -> "dfr" -> "dfs".

# Example 2:

# Input:
# wordList = {"geek", "gefk"}
# startWord = "gedk", targetWord= "geek", 
# Output:
# 2
# Explanation:
# gedk -> geek

# Example 3:

# Input: 
# wordList = {"poon", "plee", "same", "poie","plea","plie","poin"}
# startWord = "toon", targetWord= "plea",
# Output: 7 
# Explanation:
# toon -> poon -> poin -> poie -> plie -> plee -> plea 

class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		#Code here
       wordList.append(startWord)
       queue=[]
       res=""
       r=0
       c=0
       while(startWord != targetWord):  
           for j in wordList:
               queue.append(j)
               s=queue.pop(0)
               ctr=0


               for i in range(len(startWord)):
                       if startWord[i]==s[i]:
                           ctr=ctr+1
               if ctr==len(startWord)-1:
                       wordList.remove(startWord)
                       res=j               
                       break       
               else:
                   ctr=0
           c=c+1        
           startWord=j   
       
       return (c+1)	

# TIme - O(26 * n1 * n2 * w)
# n1 - length of wordd
# n2 = for string compare
# w = no of words

########################################################################################

# https://www.youtube.com/watch?v=ZVJ3asMoZ18

import string
class Solution:
	def wordLadderLength(self, beginWord, endWord, wordList):
		#Code here
        st = set(wordList)
        queue = [[beginWord, 1]]
        
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for letter in string.ascii_lowercase: # [a-z]
                    if word[:i] + letter + word[i+1:] in st:
                        temp = word[:i] + letter + word[i+1:]
                        st.remove(temp)
                        queue.append([temp, length+1])
        return 0	


# Time : O(26NL^2)
# Space : O(N)
# Given a string S, the task is to count number of subsequences of the form aibjck,
#  where i >= 1, j >=1 and k >= 1.

# Note: 
# 1. Two subsequences are considered different if the set of array indexes picked
#  for the 2 subsequences are different.
# 2.  For large test cases, the output value will be too large, return the answer
#  MODULO 10^9+7

 

# Example 1:

# Input:
# S = "abbc"
# Output: 3
# Explanation: Subsequences are abc, abc and abbc.


# Example 2:

# Input:
# S = "abcabc"
# Output: 7
# Explanation: Subsequences are abc, abc,
# abbc, aabc abcc, abc and abc.

class Solution:
    def fun(self,s):
        # code here
           c=0
           bc=0
           abc=0
           l=len(s)
           for i in range(l-1,-1,-1):
               if s[i]=='c':
                   c=2*c+1
               elif s[i]=='b':
                   bc=2*bc+c
               elif s[i]=='a':
                   abc=2*abc+bc
           return abc%(1000000007)



# https://www.youtube.com/watch?v=IV9pbZsi5cc           
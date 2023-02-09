# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

def generateParenthesis(self, n):
    res = []
    self.dfs(n, n, "", res)
    return res
        
def dfs(self, leftRemain, rightRemain, path, res):
    if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
        return  # backtracking
    if leftRemain == 0 and rightRemain == 0:
        res.append(path)
        return 
    self.dfs(leftRemain-1, rightRemain, path+"(", res)
    self.dfs(leftRemain, rightRemain-1, path+")", res)

# TC -> 2 ^(2n)
# SC -> 2 ^(2n)

# https://leetcode.com/problems/generate-parentheses/solutions/1599246/python-with-detailed-explanation-faster-than-96-54-recursive-iterative-backtracking/?orderBy=most_votes&languageTags=python    

# Recursive

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """        
        out = []
        def back_track(par='', left=0,right=0):
            #base case --> if we generate parthenis with len 2*n we hit our goal
            if len(par) == 2*n:
                out.append(par)            
            if left < n: # if we still have less opened bracket than the allowed n value --> we can still open more
                back_track(par+'(', left+1,right)
            if right < left: # we can only close the opened brackets
                back_track(par+')', left, right+1)
                
        back_track()
        return out

# Iterative

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        out = []
        stack = []
        stack.append(['(',1,0])
        while stack:
            val, left, right = stack.pop()
            if len(val) == 2*n:
                out.append(val)                
            if left < n:
                stack.append([val+'(', left+1,right])
            if right < left:
                stack.append([val+')', left, right+1])                
        return out
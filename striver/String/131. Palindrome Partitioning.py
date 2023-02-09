# Given a string s, partition s such that every substring of the partition is a palindrome. 
# Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:

# Input: s = "a"
# Output: [["a"]]

# In the backtracking algorithm, we recursively traverse over the string in depth-first search fashion.
#  For each recursive call, the beginning index of the string is given as start\text{start}start.

# Iteratively generate all possible substrings beginning at start\text{start}start index. 
# The end\text{end}end index increments from start\text{start}start till the end of the string.

# For each of the substring generated, check if it is a palindrome.

# If the substring is a palindrome, the substring is a potential candidate. Add substring to the 
# currentList\text{currentList}currentList and perform a depth-first search on the remaining substring.
#  If current substring ends at index end\text{end}end, end+1\text{end}+1end+1 becomes the start\text{start}start
#  index for the next recursive call.

# Backtrack if start\text{start}start index is greater than or equal to the string length and add the 
# currentList\text{currentList}currentList to the result.


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start_ind, end_ind):
            while start_ind <= end_ind:
                if s[start_ind] != s[end_ind]: return False
                start_ind += 1
                end_ind -=1
            return True
        
        def dfs( start , res , curr):
            if start >= len(s):
                res.append(curr[:])
                return
            for end in range(start , len(s)):
                if isPalindrome(start , end):
                    curr.append(s[start : end + 1])
                    dfs(end+1 , res , curr)
                    curr.pop()
        res = []
        dfs(0 , res ,[])
        return res
              

# O-> 2^n * n
# O(N)  where NNN is the length of the string sss. This space will be used to store the recursion stack.
#  For s = aaa, the maximum depth of the recursive call stack is 3 which is equivalent to NNN.
# #########################################################
# Dp Solution

# This approach uses a similar Backtracking algorithm as discussed in Approach 1. But, the previous approach performs one extra iteration to determine if a given substring is a palindrome or not. Here, we are repeatedly iterating over the same substring multiple times and the result is always the same. There are Overlapping Subproblems and we could further optimize the approach by using dynamic programming to determine if a string is a palindrome in constant time. Let's understand the algorithm in detail.

# Algorithm

# A given string sss starting at index start\text{start}start and ending at index end\text{end}end is a palindrome if following conditions are satisfied :

#     The characters at start\text{start}start and end\text{end}end indexes are equal.
#     The substring starting at index start+1\text{start}+1start+1 and ending at index end−1\text{end}-1end−1 is a palindrome.

# img

# Let NNN be the length of the string. To determine if a substring starting at index start\text{start}start and ending at index end\text{end}end is a palindrome or not, we use a 2 Dimensional array dp\text{dp}dp of size N⋅NN \cdot NN⋅N where,

# dp[start][end]=true\text{dp[start][end]} = \text{true}dp[start][end]=true , if the substring beginning at index start\text{start}start and ending at index end\text{end}end is a palindrome.

# Otherwise, dp[start][end] ==false\text{dp[start][end] }== \text{false}dp[start][end] ==false.

# Also, we must update the dp\text{dp}dp array, if we find that the current string is a palindrome.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        dp = [[False for k in range(length)] for k in range(length)]
        ret = []
        self.dfs(ret, s, 0, [], dp)
        
        return ret
        
        
    def dfs(self, ret, s, start, currentList, dp):
        if start >= len(s):
            ret.append(list(currentList))
        
        for end in range(start, len(s)):
            if s[end] == s[start] and (end - start <= 2 or dp[start+1][end-1]):
                dp[start][end] = True
                currentList.append(s[start:end+1])
                self.dfs(ret, s, end + 1, currentList, dp)
                currentList.pop()
              
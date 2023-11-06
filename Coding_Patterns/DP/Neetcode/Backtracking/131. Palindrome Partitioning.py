# Given a string s, partition s such that every
# substring
#  of the partition is a
# palindrome
# . Return all possible palindrome partitioning of s.


# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start_ind, end_ind):
            while start_ind <= end_ind:
                if s[start_ind] != s[end_ind]:
                    return False
                start_ind += 1
                end_ind -= 1
            return True

        def dfs(start, res, curr):
            if start >= len(s):
                res.append(curr[:])
                return
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    curr.append(s[start: end + 1])
                    dfs(end+1, res, curr)
                    curr.pop()
        res = []
        dfs(0, res, [])
        return res

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                     '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        def dfs(i  , curr):
            if len(curr) == len(digits):
                res.append(curr[:])
                return            
            for c in digit_map[digits[i]]:
                dfs(i + 1 , curr + c)
        
        dfs(0 , "")
        return res

# O( n * 4 ^ n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                     '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for i in range(len(digits)):
            new_result = []
            for prev in result:
                for l in digit_map[digits[i]]:
                    new_result.append(prev+l)
            result = new_result
        return result

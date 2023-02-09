# Given a string containing digits from 2-9 inclusive, return all possible letter 
# combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
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
###################################################################################################

# https://www.interviewbit.com/blog/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
 
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
 
        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
 
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
 
                path.append(letter)
 
                backtrack(index + 1, path)
 
                path.pop()
 
        combinations = []
        backtrack(0, [])
        return combinations

# Time Complexity: O(4^N * N), where N is the length of a digit string
# Space Complexity: O(N)
# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

# Example 1:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# Example 2:

# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# Example 3:

# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = { num for num in nums}

        def backtrack(i , curr):
            if i == len(nums):
                res = "".join(curr)
                return None if res in strSet else res
            
            # when current element is 0
            res = backtrack(i + 1 , curr)
            if res:
                return res
                
            # when current element is 1
            curr[i] = "1"
            res = backtrack( i + 1  , curr)
            if res:
                return res

        return backtrack(0  , [ "0" for i in nums])      

        
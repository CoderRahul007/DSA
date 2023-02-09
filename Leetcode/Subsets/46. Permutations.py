# Given an array nums of distinct integers, return all the possible permutations.
#  You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]

# https://leetcode.com/problems/permutations/solutions/993970/python-4-approaches-visuals-time-complexity-analysis/?orderBy=most_votes&languageTags=python&topicTags=backtracking

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = [([])]
        res = []
        
        while stack:
            comb = stack.pop()
            if len(comb) == len(nums):
                res.append(comb)
                continue
            for n in range(0, len(nums)):
                if nums[n] not in comb:
                    stack.append((comb + [nums[n]]))
        return res
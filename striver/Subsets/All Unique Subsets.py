#User function Template for python3
# backtracking
# https://www.youtube.com/watch?v=-eVkq8odxno

################################################################################

#############################################################################
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output            

##################################################################################
# Algo
# We define a backtrack function named backtrack(first, curr) which takes the index of first element to add and a current combination as arguments.

#     If the current combination is done, we add the combination to the final output.

#     Otherwise, we iterate over the indexes i from first to the length of the entire sequence n.

#         Add integer nums[i] into the current combination curr.

#         Proceed to add more integers into the combination : backtrack(i + 1, curr).

#         Backtrack by removing nums[i] from curr.


# https://leetcode.com/problems/subsets/solution/
def subsets(nums):
    ans = []
    nums.sort()
    def backtrack(i , subs):
        if i == len(nums):
            ans.append(subs[:])
            return
        subs.append(nums[i])
        backtrack(i+1 , subs)
        subs.pop()

        # when there are duplicates
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i+=1

        backtrack(i+1, subs)

    backtrack(0, [])
    return res
# O -> n*2^n    
####################################################################################
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        cur = []
        nums.sort()
        
        def backtrack(start):
            output.append(cur.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                backtrack(i+1)
                cur.pop()
            
        backtrack(0)
        return output
##################################################################################

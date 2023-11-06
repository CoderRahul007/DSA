# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]



# The root node represents an empty curr []. From the root, every node's curr represents the path taken from the root. The nodes at depth nums.length represent the answer permutations (the leaf nodes).

# Solving this problem is equivalent to "traversing" this tree. The easiest way to perform the traversal is by using recursion and passing curr as an argument.

# Think of each call to the recursive function as being a node in the tree. In each call, we need to iterate over the numbers that haven't been used yet (not currently in curr).

# For each num that isn't already in curr, we add it to curr and then make a recursive call passing curr. Modifying curr and making a recursive call is equivalent to "traversing" to a child node in the tree.

# When we return from a function call, it's equivalent to moving back up the tree (exactly like in a DFS). When we moved from a parent to a child, we added an element to curr. When we move from a child back to its parent, we need to remove the element we added from curr. This is the "backtracking" step.

# Algorithm

# Initialize an answer array ans and an array curr to build permutations with.
# Create a backtrack function that takes curr as an argument:
# If curr.length == nums.length, add a copy of curr to ans and return.
# Iterate over nums. For each num, if num is not in curr, do the following:
# Add num to curr and call backtrack(curr), then remove num from curr.
# Call backtrack with an initially empty curr.
# Return ans.
# Note that we are essentially implementing a DFS traversal of an imaginary tree. The children of a node are all the numbers that haven't been used yet.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perm = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
        
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
            
        ans = []
        backtrack([])
        return ans

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = [([])]
        res = []
        
        while stack:
            comb = stack.pop()
            if len(comb) == len(nums):
                res.append(comb)
                continue
            for n in range(len(nums)):
                if nums[n] not in comb:
                    stack.append((comb + [nums[n]]))
        return res

# Given n as the length of nums,

# Time complexity, what you should say in an interview: O(n⋅n!)

# Finding permutations is a well-studied problem in combinatorics. Given a set of length n, the number of permutations is n! (n factorial). There are nnn options for the first number, n - 1 for the second, and so on.

# For each of the n! permutations, we need O(n) work to copy curr into the answer. This gives us O(n⋅n!)
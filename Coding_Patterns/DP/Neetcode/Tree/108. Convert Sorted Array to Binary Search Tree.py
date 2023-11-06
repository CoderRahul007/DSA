# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

# Example 1:

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

class Solution:
    def sortedArrayToBST(self, nums):
        def recur(start  , end):
            if start > end: # base case so that None is added to the leaf nodes
                return None
            
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = recur(start , mid - 1)
            node.right = recur(mid + 1 , end)
            return node

        return recur(0 , len(nums)-1)            

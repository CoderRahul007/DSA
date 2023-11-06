# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root , l , r):
            if not root:
                return True
            if not root.left and not root.right:
                return l < root.val < r
            return l < root.val < r and bst(root.left , l , root.val) and bst(root.right  , root.val , r)

        low = float("-inf")
        high = float("inf")
        return bst(root, low, high )                        

# O(n)
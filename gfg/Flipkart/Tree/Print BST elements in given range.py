def inorder(root , res , low , high):
    if not root:
        return 
    inorder(root.left , res , low , high)
    if root.data >= low  and root.data <= high:
        res.append(root.data)
    inorder(root.right , res , low , high)
    
class Solution:
    def printNearNodes(self, root, low, high):
        #code here.
        res = []
        inorder(root , res , low , high)
        return res

# Given a Binary Search Tree and a range [low, high]. Find all the numbers in the BST that lie in the given range.
# Note: Element greater than or equal to root go to the right side.

# Example 1:

# Input:
#        17
#      /    \
#     4     18
#   /   \
#  2     9 
# l = 4, h = 24
# Output: 4 9 17 18 

# Example 2:

# Input:
#        16
#      /    \
#     7     20
#   /   \
#  1    10
# l = 13, h = 23
# Output: 16 20 

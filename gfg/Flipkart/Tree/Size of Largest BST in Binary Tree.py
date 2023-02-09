# Given a binary tree. Find the size of its largest subtree that is a Binary Search Tree.
# Note: Here Size is equal to the number of nodes in the subtree.

# Example 1:

# Input:
#         1
#       /   \
#      4     4
#    /   \
#   6     8
# Output: 1
# Explanation: There's no sub-tree with size
# greater than 1 which forms a BST. All the
# leaf Nodes are the BSTs with size equal
# to 1.

# Example 2:

# Input: 6 6 3 N 2 9 3 N 8 8 2
#             6
#         /       \
#        6         3
#         \      /   \
#          2    9     3
#           \  /  \
#           8 8    2 
# Output: 2
# Explanation: The following sub-tree is a
# BST of size 2: 
#        2
#     /    \ 
#    N      8import math

# https://www.youtube.com/watch?v=X0oXMdtUDwo
class myNode:
    def __init__(self, minn, maxn, sizen):
        self.maxn = maxn
        self.minn = minn
        self.sizen = sizen
        
class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def postOrder(self, root):
        if not root:
            return myNode(math.inf, -math.inf, 0)
        # postorder
        leftch = self.postOrder(root.left)
        rightch = self.postOrder(root.right)

        if leftch.maxn < root.data and rightch.minn > root.data:
            return myNode(min(leftch.minn, root.data), max(root.data, rightch.maxn), 1 + rightch.sizen + leftch.sizen)

        else:
            return myNode(-math.inf, math.inf, max(rightch.sizen, leftch.sizen))
    def largestBst(self, root):
        #code here
        x = self.postOrder(root)
        return x.sizen

# The key observation here is that if a subtree is a BST
#  then all nodes in its subtree will also be a BST.
#   So, we will recurse on the binary tree in a bottom-up 
#   manner and use the information of the left subtree and 
#   right subtree to store the information for the current subtree.
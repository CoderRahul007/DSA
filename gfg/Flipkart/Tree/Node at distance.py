# Given a Binary Tree and a positive integer k. 
# The task is to count all distinct nodes that are
#  distance k from a leaf node. A node is at k distance 
# from a leaf if it is present k levels above the leaf 
# and also, is a direct ancestor of this leaf node. 
# If k is more than the height of Binary Tree, then nothing should be counted.

# Example 1:

# Input:
#         1
#       /   \
#      2     3
#    /  \   /  \
#   4   5  6    7
#           \ 
#           8
# K = 2
# Output: 2
# Explanation: There are only two unique
# nodes that are at a distance of 2 units
# from the leaf node. (node 3 for leaf
# with value 8 and node 1 for leaves with
# values 4, 5 and 7)
# Note that node 2
# isn't considered for leaf with value
# 8 because it isn't a direct ancestor
# of node 8.

# Example 2:

# Input:
#           1
#          /
#         3
#        /
#       5
#     /  \
#    7    8
#          \
#           9
# K = 4
# Output: 1
# Explanation: Only one node is there
# which is at a distance of 4 units
# from the leaf node.(node 1 for leaf
# with value 9) 

def helper(root, k):
    global cnt
    
    if root == None:
        return False
    
    if root.left == None and root.right == None and k == 0:
        return True
    
    return helper(root.left, k-1) or helper(root.right, k-1)
    
def inorder(root , k):
    global cnt
    if not root:
        return
    inorder(root.left  , k)
    if helper(root , k):
        cnt+=1
    inorder(root.right  , k)
    
def printKDistantfromLeaf(root, k):
    #code here
    global cnt
    cnt = 0
    inorder(root , k)
    return cnt
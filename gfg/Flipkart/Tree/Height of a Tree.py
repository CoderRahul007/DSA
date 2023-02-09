# Given a binary tree, find height of it. Height of empty tree is -1,
#  height of tree with one node is 0 and height of below tree is 2. 

# Recursively calculate height of left and right subtrees of a node and assign height to the node as max of the heights of two children plus 1. See below pseudo code and program for details.
# Algorithm: 

#  maxDepth()
# 1. If tree is empty then return -1
# 2. Else
#      (a) Get the max depth of left subtree recursively  i.e., 
#           call maxDepth( tree->left-subtree)
#      (a) Get the max depth of right subtree recursively  i.e., 
#           call maxDepth( tree->right-subtree)
#      (c) Get the max of max depths of left and right 
#           subtrees and add 1 to it for the current node.
#          max_depth = max(max dept of left subtree,  
#                              max depth of right subtree) 
#                              + 1
#      (d) Return max_depth
# See the below diagram for more clarity about execution of the recursive function maxDepth() for above example tree. 

#             maxDepth('1') = max(maxDepth('2'), maxDepth('3')) + 1
#                                = 1 + 1
#                                   /    \
#                                 /         \
#                               /             \
#                             /                 \
#                           /                     \
#                maxDepth('2') = 1                maxDepth('3') = 0
# = max(maxDepth('4'), maxDepth('5')) + 1
# = 1 + 0   = 1         
#                    /    \
#                  /        \
#                /            \
#              /                \
#            /                    \
#  maxDepth('4') = 0     maxDepth('5') = 0 
def maxDepth(node):
    if node is None:
        return 0 
 
    else :
 
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        return max(lDepth, rDepth) + 1
        
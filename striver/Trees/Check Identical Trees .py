#  DFS

# The idea is to use depth-first traversal.
#  Both of the trees will be considered as
#   identical only if their root data is equal and
#    left and right sub-trees are identical. So,
#     we will traverse the tree recursively and check
#      for left subtree as well as right subtree whether 
#      they are identical or not and return false whenever they are not identical.

 
from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree Node class structure
class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
              
        
def identicalTrees(root1, root2):
    #Your code goes here.
    if not root1 and not root2:
        return True
    if root1 and root2 and root1.data == root2.data:
        if identicalTrees(root1.left, root2.left) and identicalTrees(root1.right , root2.right):
            return True
        return False
    return False
        
    
    return False

# Time Complexity

# O(min(M, N)) per test case where M and N are the number of nodes in Binary tree 1 and Binary tree 2 respectively.

# In the worst case, for both the trees, we will be traversing every node once until we find the non-identical nodes.
# Space Complexity
# O(min(H1, H2)) per test case, where H1 and H2 are the heights of the given trees respectively. 

# In the worst case, extra space is required for the recursion stack and at the maximum,
#  the recursion can be called until the minimum height of both trees.

###########################################################################################################
# using BFS
'''
    Time complexity: O( max(M, N) ) 
    Space complexity: O( max(M, N) )
    
    M and N are number of nodes in binary tree 1 and binary tree 2 respectively.
'''


class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
        
def createLevelOrder(root):
    
    # Res will store level order traversal of the tree
    res = []
    
    if root is None:
        res.append(-1)
        return res
    
    # Using queue to implement level order traversal.
    que = []
    
    que.append(root)
    
    res.append(root.data)
    
    while(len(que)>0):
        
        first = que.pop(0)
        
        # Push the left child into queue 
        if first.left!=None:
            que.append(first.left)
            res.append(first.left.data)
            
        else:
            # Push -1 for null node.
            res.append(-1)
            
        # Push the right child into queue    
        if first.right!=None:
            que.append(first.right)
            res.append(first.right.data)
            
        else:
            # Push -1 for null node.
            res.append(-1)
            
    return res
            
            
        
        
def identicalTrees(root1, root2):
    
    arr1 = createLevelOrder(root1)
    
    arr2 = createLevelOrder(root2)
    
    if len(arr1)!=len(arr2):
        return False
    
    for i in range(len(arr1)):
        
        if arr1[i]!=arr2[i]:
            return False
        
    return True


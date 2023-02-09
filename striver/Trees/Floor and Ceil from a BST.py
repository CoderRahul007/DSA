# Given a binary tree and a key(node) value, find the floor and ceil value for that particular key value.

# Floor Value Node: Node with the greatest data lesser than or equal to the key value. 
# Ceil Value Node: Node with the smallest data larger than or equal to the key value.
# For example, Let’s consider the Binary Tree below – 

#           8
#         /   \    
#       4      12
#     /  \    /  \
#    2    6  10   14

# Key: 11  Floor: 10  Ceil: 12
# Key: 1   Floor: -1  Ceil: 2
# Key: 6   Floor: 6   Ceil: 6
# Key: 15  Floor: 14  Ceil: -1
# There are numerous applications where we need to find the floor/ceil value of
#  a key in a binary search tree or sorted array. For example, 
#  consider designing a memory management system in which free nodes are arranged in BST.
#   Find the best fit for the input request.

# Algorithm: 

# Imagine we are moving down the tree, and assume we are root node. 
# The comparison yields three possibilities,

# A) Root data is equal to key. We are done, root data is ceil value.

# B) Root data < key value, certainly the ceil value can't be in left subtree. 
#    Proceed to search on right subtree as reduced problem instance.

# C) Root data > key value, the ceil value may be in left subtree. 
#    We may find a node with is larger data than key value in left subtree, 
#    if not the root itself will be ceil node.
# Implementation: Code for the ceiling value.


# Python program to find ceil of a given value in BST 
  
# A Binary tree node 
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.key = data 
        self.left = None
        self.right = None
  
# Function to find ceil of a given input in BST. If input 
# is more than the max key in BST, return -1 
def ceil(root, inp): 
      
    # Base Case 
    if root == None: 
        return -1
      
    # We found equal key 
    if root.key == inp : 
        return root.key 
      
    # If root's key is smaller, ceil must be in right subtree 
    if root.key < inp: 
        return ceil(root.right, inp) 
      
    # Else, either left subtree or root has the ceil value 
    ceiling = ceil(root.left, inp) 

    return ceiling if ceiling >= inp else root.key 
  
# Driver program to test above function 
root = Node(8) 
  
root.left = Node(4) 
root.right = Node(12) 


# Time Complexity

# O(h),  where ‘h’ is the height of the BST tree.

 

# In the worst case, we may have to travel from the ‘root’ to the deepest leaf node. 
# If a tree is skew then time complexity becomes O( N ). Hence, the overall time complexity is O(h).
# Space Complexity

#  O(h), where ‘h’ is the height of the BST tree.

 

# In the worst case, when the given bst is a skewed tree,  height is equal to ‘N’, i.e.
#  the number of nodes in the tree. Thus the recursion stack will take O(N) space.
#   Hence, the overall space complexity is O(h).


'''
    Time Complexity: O(h)
    Space Complexity: O(h)

    Where 'h' is the height of the tree.
'''

import sys

def floorInBST(root, X):

    # Base Case
    if root is None:
        return sys.maxsize

    # If root.data is equal to 'X'
    if root.data == X:
        return root.data

    # If root -> data is greater than the 'X'
    if root.data > X:
        return floorInBST(root.left, X)

    # Else, the floor may lie in right subtree or may be equal to the root
    floorValue = floorInBST(root.right, X)

    if floorValue <= X:
        return floorValue
    
    else:
        return root.data
    
    
########################################################################################
# Iterative

# 1. If tree is empty, i.e. root is null, 
#    return back to calling function.
# 2. If current node address is not null, perform the following steps : 
#      (a) If current node data matches with the key value - 
#              We have found both our floor and ceil value. 
#              Hence, we return back to calling function.
#     (b) If data in current node is lesser than the key value - 
#             We assign the current node data to the variable keeping
#             track of current floor value and explore the right subtree,
#             as it may contain nodes with values greater than key value.
#     (c) If data in current node is greater than the key value - 
#             We assign the current node data to the variable keeping track
#             of current ceil value and explore the left subtree, as it may
#             contain nodes with values lesser than key value.
# 3. Once we reach null, we return back to the calling function,
#    as we have got our required floor and ceil values for the particular key value.
# Below is the implementation of the above approach:


class Node:
      
    def __init__(self, x):
          
        self.data = x
        self.left = None
        self.right = None
  
# Helper function to find floor and
# ceil of a given key in BST
def floorCeilBSTHelper(root, key):
      
    global floor, ceil
  
    while (root):
        if (root.data == key):
            ceil = root.data
            floor = root.data
            return
        if (key > root.data):
            floor = root.data
            root = root.right
        else: # key < root.data
            ceil = root.data
            root = root.left
  
# Display the floor and ceil of a given 
# key in BST. If key is less than the min
# key in BST, floor will be -1; If key is 
# more than the max key in BST, ceil will be -1;
def floorCeilBST(root, key):
      
    global floor, ceil
  
    # Variables 'floor' and 'ceil' 
    # are passed by reference
    floor = -1
    ceil = -1
  
    floorCeilBSTHelper(root, key)
  
    print(key, floor, ceil)
# Serialization is to store a tree in an array so that it can be later restored and Deserialization
#  is reading tree back from the array. Now your task is to complete the function serialize which stores the tree into an array A[ ] and deSerialize which deserializes the array to the tree and returns it.
# Note: The structure of the tree must be maintained. Multiple nodes can have the same data.

# Example 1:

# Input:
#       1
#     /   \
#    2     3
# Output: 2 1 3

# Example 2:

# Input:
#          10
#        /    \
#       20    30
#     /   \
#    40  60
# Output: 40 20 60 10 30

# https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
# https://www.youtube.com/watch?v=-YbXySKJsX8
def serialize(root, A):
    #code here
    if not root:
        A.append(-1)
        return 
    A.append(root.data)
    serialize(root.left , A)
    serialize(root.right , A)
    #Preorder traversal
#Function to deserialize a list and construct the tree.   
def deSerialize(A):
    #code here
    if A[0] == -1:
        A.pop(0)
        return None
    root = Node(A.pop(0))
    root.left = deSerialize(A)
    root.right = deSerialize(A)
    return root
# Following are some simpler versions of the problem:
# If given Tree is Binary Search Tree? 
# If the given Binary Tree is Binary Search Tree, we can store it by either storing preorder or postorder traversal. In case of Binary Search Trees, only preorder or postorder traversal is sufficient to store structure information. 

# If given Binary Tree is Complete Tree? 
# A Binary Tree is complete if all levels are completely filled except possibly the last level and all nodes of last level are as left as possible (Binary Heaps are complete Binary Tree). For a complete Binary Tree, level order traversal is sufficient to store the tree. We know that the first node is root, next two nodes are nodes of next level, next four nodes are nodes of 2nd level and so on. 

# If given Binary Tree is Full Tree? 
# A full Binary is a Binary Tree where every node has either 0 or 2 children. It is easy to serialize such trees as every internal node has 2 children. We can simply store preorder traversal and store a bit with every node to indicate whether the node is an internal node or a leaf node.

# How to store a general Binary Tree? 
# A simple solution is to store both Inorder and Preorder traversals. This solution requires space twice the size of Binary Tree. 
# We can save space by storing Preorder traversal and a marker for NULL pointers. 

# Let the marker for NULL pointers be '-1'
# Input:
#      12
#     /
#   13
# Output: 12 13 -1 -1 -1

# Input:
#       20
#     /   \
#    8     22 
# Output: 20 8 -1 -1 22 -1 -1 

# Input:
#          20
#        /    
#       8     
#      / \
#     4  12 
#       /  \
#      10  14
# Output: 20 8 4 -1 -1 12 10 -1 -1 14 -1 -1 -1 

# Input:
#           20
#          /    
#         8     
#       /
#     10
#     /
#    5
# Output: 20 8 10 5 -1 -1 -1 -1 -1 

# Input:
#           20
#             \
#              8
#               \   
#                10
#                  \
#                   5   
# Output: 20 -1 8 -1 10 -1 5 -1 -1
# Deserialization can be done by simply reading data from file one by one. 

# Following is the implementation of the above idea. 


# // A C program to demonstrate serialization and deserializa

# OPTIMIZED APPROACH

# A node’s predecessor in a BST is the greatest value present in its left subtree.
#  If the left subtree doesn’t exist, then the predecessor can be one of his ancestors.

 

# Similarly, a node’s successor in a BST is the smallest value present in its right subtree.
#  If the right subtree doesn’t exist, then the successor can be one of his ancestors.

 

# Here is the algorithm:

# We will run a loop until we reach the node given to us.
#     If the value of the current node is smaller than the given node, we will set the predecessor as the current node and move to its right child.
#     Else, we will set the successor as the current node and move to its left child.
# After we reach the given node, we find the maximum value of the left subtree and the minimum value of the right subtree. Then set the values of predecessor and successor, accordingly.

# Time Complexity

# O(N),  where ‘N’ is the number of nodes in the BST.

 

# In the worst case(skewed tree), we will have to traverse all the nodes in the BST.
#  Hence the time complexity will be O(N).
# Space Complexity

# O(1), i.e. we are using constant space.

 

# We are not using any extra space. Hence, the space complexity is constant.
'''

    Time Complexity : O(N)
    Space Complexity : O(1)

    where N is the number of nodes in the BST.
    
'''

def predecessorSuccessor(root, key):

    predecessor = -1
    successor = -1

    # Reach to the key.
    while root.data != key:
        if key > root.data:
            predecessor = root.data
            root = root.right
        
        else:
            successor = root.data
            root = root.left

    
    rightSubtree = root.right

# Similarly, a node’s successor in a BST is the smallest value present in its right subtree.
#  If the right subtree doesn’t exist, then the successor can be one of his ancestors.

    while rightSubtree != None:
        successor = rightSubtree.data
        rightSubtree = rightSubtree.left


    leftSubtree = root.left

# A node’s predecessor in a BST is the greatest value present in its left subtree.
#  If the left subtree doesn’t exist, then the predecessor can be one of his ancestors.

    while leftSubtree != None:
        predecessor = leftSubtree.data
        leftSubtree = leftSubtree.right

    return [predecessor, successor]
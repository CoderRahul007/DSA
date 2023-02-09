# https://www.codingninjas.com/codestudio/problems/flatten-binary-tree-to-linked-list_1112615?topList=striver-sde-sheet-problems&leftPanelTab=0

# Convert to linked list which follows preorder of binary tree
#  Create A New Linked List

#     A brute approach to solve this problem is by iterating over the tree in the pre-order fashion.
#     While traversing, store the values of the nodes in a list.
#     Create the required linked list using the stored values.

# Time Complexity

# O(N), where N is the number of nodes in the tree.


# We are visiting every node of the tree once. Hence, the overall time complexity is O(N).
# Space Complexity

# O(N), where N is the number of nodes in the tree.

 

# O(N) extra space is required for creating a new linked list. Hence, overall space complexity is O(N).


'''
    Time Complexity - O(N)
    Space Complexity - O(N)

    Where N is the number of nodes in the Binary Tree.
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def preOrderTraversal(root, preOrder):
    if (root == None):
        return

    preOrder.append(root.data)

    preOrderTraversal(root.left, preOrder)
    preOrderTraversal(root.right, preOrder)


def flattenBinaryTree(root):
    preOrder = []
    # Find the pre-order traversal of the tree and store it in a list.
    preOrderTraversal(root, preOrder)

    # Create a new linked list from the stored values.
    head = root

    for i in range(1, len(preOrder)):
        root.right = TreeNode(preOrder[i])
        root = root.right
    
    return head

############################################################################################################
# Recursion

'''
    Time Complexity - O(N)
    Space Complexity - O(N)

    Where N is the number of nodes in the Binary Tree.
'''


def flattenBinaryTreeHelper(currentNode, lastNode):
    if (currentNode == None):
        # Base Condition
        return lastNode

    if (lastNode != None):
        # Set currentNode as the right child of the lastNode.
        lastNode.right = currentNode

    # Store the left and right child of the currentNode in temporary variables.
    left = currentNode.left
    right = currentNode.right

    # Set the left and right pointers of currentNode to NULL.
    currentNode.left = currentNode.right = None

    newLastNode = flattenBinaryTreeHelper(left, currentNode)

    newLastNode = flattenBinaryTreeHelper(right, newLastNode)

    return newLastNode


def flattenBinaryTree(root):
    head = root

    flattenBinaryTreeHelper(root, None)

    return head

######################################################################################################

# Using Constant Extra Space

# This approach is similar to the previous recursive approach.
# The idea is to iteratively traverse the tree.
# While exploring the current node we place its right subtree (of the current node) at
# the correct position in the tree (i.e. make it the right child of the rightmost node in the
# left subtree, pre-order predecessor) and make the left subtree the new right subtree of the current node.
# This way we can also avoid keeping track of the last node of the linked list.
 
# Below is the detailed algorithm:  

#     Let 'CURRENTNODE' store the node presently being explored.
#     We start by exploring the root node. So, initialize 'CURRENTNODE' with the root node.
#     Repeat the following steps until 'CURRENTNODE' becomes NULL:
#         If the current node has a left child:
#             Find the rightmost node present in the left subtree and make the right subtree of
#             the current node as its right child.
#             Make the left subtree of the current node as the new right subtree.
#             Set the left child of the current node is NULL.
#         Set 'CURRENTNODE' to 'CURRENTNODE'’s right child.
#     Return the head of the linked list.

# Time Complexity

# O(N), where N is the number of nodes in the tree.

# Even though it may seem that we are iterating over the left subtree for every node,
# as we make the left subtree the new right subtree of the current node, we don't traverse 
# these nodes (present in the left subtree) again. So, we visit every node of the tree at most twice,
# once during the traversal and once to find the correct position for the right subtree. 
# Hence, the overall time complexity is O(2*N) = O(N).
# Space Complexity

# O(1)

'''
    Time Complexity - O(N)
    Space Complexity - O(1)

    Where N is the number of nodes in the Binary Tree.
'''
# https://www.youtube.com/watch?v=sWf7k1x9XR4

def flattenBinaryTree(root):
    currentNode = root
    while (currentNode != None):

        if currentNode.left != None:

            # Place the right subtree at its correct position (according to the linked list).
            # To do this, find the rightmost node present in the left subtree.
            predecessor = currentNode.left

            while (predecessor.right != None):
                predecessor = predecessor.right

            # Make the right subtree of the current node as right child of "predecessor".
            predecessor.right = currentNode.right

            # Make the left subtree of the current node as the new right subtree.
            currentNode.right = currentNode.left

            currentNode.left = None

        # Set the right child of the node as the current node.
        currentNode = currentNode.right

    return root
 
# https://www.codingninjas.com/codestudio/problems/validate-bst_799483?topList=striver-sde-sheet-problems&leftPanelTab=0\

# condition root.left.data <= root.data <= root.right.data


#  Approach 1

#     For each node, store the minimum and maximum value allowed for that node.
#     Initially, for the root node as all the integer values are allowed,
#      the minimum value would be -10^9 and the maximum value should be 10^9.
#       Here we can also use built-in INT_MIN and INT_MAX constants.
#     If the value of that node is not in the bounded range of minimum and maximum value, then return false.
#     For the left subtree of a node with data ‘x’, update the maximum value to ‘x’.
#     For the right subtree of a node with data ‘x’, update the minimum value to ‘x’.
#     This will make sure every node in the left subtree will be less than or equal to x 
#     and every node in the right subtree will be greater than or equal to x.
#     Check this for each node of the tree, if every node is in the range then the tree is a binary search tree.

# Time Complexity

# O(n), where n is the number of nodes in the binary tree.

# We are recursively traversing through all the nodes of the tree.
# Space Complexity

# O(n), Stack space for recursive calls of n nodes of the binary tree.


'''

    Time Complexity : O(N)
    Space Complexity : O(N).

    Where N denotes number of nodes in the binary tree

'''

import queue
import sys

sys.setrecursionlimit(10 ** 6)


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def helper(root, minn, maxx):

    ##An empty tree is a BST
    if root == None:
        return True

    #False if this node violates the min/max constraint
    if (root.data < minn or root.data > maxx):
        return False

    #Otherwise check the subtrees recursively, modifying the min or max constraint
    leftSearch = helper(root.left, minn, root.data)
    rightSearch = helper(root.right, root.data, maxx)

    return leftSearch and rightSearch


def validateBST(root):
    return helper(root, -1 * sys.maxsize, sys.maxsize)


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)



    if length <= 0 or levelorder[0] == -1:
        return None

    root = BinaryTreeNode(levelorder[index])
    index += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():

        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelorder[index]
        index += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


t = int(sys.stdin.readline().strip())
while t > 0:

    li = list(map(int, sys.stdin.readline().strip().split(" ")))
    root = buildLevelTree(li)
    if (validateBST(root)):
        print('true')
    else:
        print('false')
    t = t - 1



########################################################################################
# Inorder Traversal

#     If an inorder traversal is performed on a binary search tree, then the elements are in ascending order.
#     While performing the traversal, keep track of the previous node and the current node.
#     If the previous node is greater than the current node, then the binary tree is definitely not a binary search tree.
#     For all nodes, if the previous node is smaller than the current node,
#      then the traversal is in ascending order, return true.

# Time Complexity

# O(n), where n is the number of nodes in the binary tree.

# We are recursively traversing through all the nodes of the tree.
# Space Complexity

# O(n), Stack space for recursive calls of n nodes of the binary tree.



'''
    Time Complexity : O(N)
    Space Complexity : O(N).
    Where N denotes number of nodes in the binary tree

'''


import queue
import sys
sys.setrecursionlimit(10**6)

class BinaryTreeNode:


    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Helper Function

def helper(root, prev):

    #Traverse the tree in inorder fashion
    #Keep track of previous node
    if root is not None:

        if(helper(root.left, prev)) is False:  #Check left subtree
            return False

        if(prev.data != -1 and root.data < prev.data): #Traversal not in ascending order
            return False

        prev.data = root.data

        return helper(root.right, prev)  #Check right subtree

    return True


# Main Function
def validateBST(root):

    prev = BinaryTreeNode(-1)

    return helper(root, prev)


# Building the tree
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root




t = int(sys.stdin.readline().strip())


while t > 0:

    li = list(map(int, sys.stdin.readline().strip().split(" ")))
    root = buildLevelTree(li)
    if (validateBST(root)):
        print('true')
    else:
        print('false')
    t = t - 1


# The key observation here is that if a subtree is a BST then all nodes in
#  its subtree will also be a BST. So, we will recurse on the binary tree
#   in a bottom-up manner and use the information of the left subtree and 
#   right subtree to store the information for the current subtree.

###################################################################################
# Brute Force
'''
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    
    where N is the total number of nodes in the binary tree.
'''

def isBST(root, min, max):
    if root == None:
        return True

    if root.data < min or root.data > max:
        return False

    return isBST(root.left, min, root.data - 1) and isBST(root.right, root.data + 1, max)


def size(root):
    if root == None:
        return 0
    
    return 1 + size(root.left) + size(root.right)


def largestBST(root):
    
    # Current Subtree is BST.
    if isBST(root, -1e9, 1e9) == True:
        return size(root)
    
    # Find largest BST in left and right subtrees.
    return max(largestBST(root.left), largestBST(root.right))


######################################################################################################
'''
    Time Complexity: O(N)
    Space Complexity: O(N)
    
    where N is the total number of nodes in the binary tree.
'''


class info:
    def __init__(self):
        self.isValid = True
        self.size = 0
        self.min = 1e9
        self.max = -1e9

    def __del__(self):
        del self

#postorder
def maxSize(currNode, maxBST):

    if currNode == None:
        newInfo = info()
        return newInfo


    # Information of left and right subtrees.
    left = maxSize(currNode.left, maxBST)
    right = maxSize(currNode.right, maxBST)


    currInfo = info()

    # Size of current subtree.
    currInfo.size = left.size + right.size + 1
    
    # Left and Right subtrees must be BST.
    currInfo.isValid = left.isValid & right.isValid
    
    # Current subtree must form a BST.
    currInfo.isValid &= (currNode.data > left.max)
    currInfo.isValid &= (currNode.data < right.min)
    
    # Updating min and max for current subtree.
    currInfo.min = min(min(left.min, right.min), currNode.data)
    currInfo.max = max(max(left.max, right.max), currNode.data)


    if currInfo.isValid == True:
        maxBST[0] = max(maxBST[0], currInfo.size)

    return currInfo


def largestBST(root):
    
    # Passing 'maxBST' by reference.
    maxBST = [0]
    maxSize(root, maxBST)

    return maxBST[0]
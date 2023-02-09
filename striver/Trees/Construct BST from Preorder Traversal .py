'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the tree
'''

from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def util(preOrder, preIndex, startRange, endRange):

    # If the preIndex is greater the length of the array return None.
    if preIndex[0] > len(preOrder):
        return None

    currNode = preOrder[preIndex[0]]

    # If the current node lies inside the range then process the node.
    if currNode > startRange and currNode < endRange:
        root = TreeNode(currNode)

        # Increase the index by 1.
        preIndex[0] += 1

        # If left node exists process left.
        if preIndex[0] < len(preOrder):
            root.left = util(preOrder, preIndex, startRange, currNode)

        # If right node exists process right.
        if preIndex[0] < len(preOrder):
            root.right = util(preOrder, preIndex, currNode , endRange)

        # Return the root.
        return root

    # If node was not processed return None.
    return None


def preOrderTree(preOrder: List[int]) -> TreeNode:

    preIndex = [0]

    # Return the util function.
    return util(preOrder, preIndex, float("-infinity"), float("infinity"))
###########################################################################################

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        intMax = float('inf')
        intMin = -float('inf')
        
		# Gets the current index where the program is at
        def getPreorderIndex():
            return bstFromPreorderHelper.bstFromPreorderIndex
		
		# increments index by 1
        def setNextPreorderNextIndex():
            bstFromPreorderHelper.bstFromPreorderIndex += 1

        def bstFromPreorderHelper(preorderArray, valueAtIndex, _min, _max, size):
            # check if we have any index left to process
            if getPreorderIndex() >= size:
                return None

            node = None

            # check if the value is in range _min and _max
            # root index will always be in the initial range if intMin and intMaz

            if _min < valueAtIndex and valueAtIndex < _max:
                # create a tree node
                node = TreeNode(valueAtIndex)

                # now let's increment the index
                setNextPreorderNextIndex()

                # check if we are still in bounds with array index
                # if yes, all the values between intMin and value at index will be part of left sub-tree
                # because they will be smaller
                if getPreorderIndex() < size:
                    node.left = bstFromPreorderHelper(preorderArray, 
                                                        valueAtIndex=preorderArray[getPreorderIndex()],
                                                        _min=_min, _max=valueAtIndex, size=size)

                # and all the value between value at index and intMax will be part of right sub-tree
                # because they will be greater than value at index
                if getPreorderIndex() < size:
                    node.right = bstFromPreorderHelper(preorderArray, 
                                                        valueAtIndex=preorderArray[getPreorderIndex()],
                                                        _min=valueAtIndex, _max=_max, size=size)

            return node
        
        # static variable
        bstFromPreorderHelper.bstFromPreorderIndex = 0
        return bstFromPreorderHelper(preorder, preorder[0], intMin, intMax, len(preorder))
#############################################################################################

# Iterative Method

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        # insertion method
        def insert(root, node):
            # pointer movement
            flag = True
            while flag:
                flag = False
                # move left
                while root.left and node.val < root.val:
                    root = root.left
                    flag = True
                # move right
                while root.right and node.val > root.val:
                    root = root.right
                    flag = True
            
            # insertion at correct place
            if node.val < root.val:
                root.left = node
            else:
                root.right = node
        
        # creating a root
        root = TreeNode(preorder[0])
        
        for i in range(1, len(preorder)):
            insert(root, TreeNode(preorder[i]))
        
        return root
"""
Tc: O(n*logn) | logn/h for insertion
Sc: O(1)
"""


##############################################################################################
'''
    Time Complexity: O(N^2)
    Space Complexity: O(N^2)

    Where N is the number nodes in the tree
'''

from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Utility function to get the the tree from preOrder traversal
def util(preOrder: List[int]):

    # If the length of the preOrder traversal is 0 return None
    if not len(preOrder):
        return None

    # Set the root as the first element of the preOrder traversal
    root = TreeNode(preOrder[0])

    # All the nodes smaller than the root will go in the left subtree
    leftPreOrder = [num for num in preOrder[1:] if num < preOrder[0]]

    # All the nodes smaller than the root will go in the right subtree
    rightPreOrder = [num for num in preOrder[1:] if num > preOrder[0]]

    # Call the method on left and right subtree of the root
    root.left = util(leftPreOrder)
    root.right = util(rightPreOrder)

    # Return the root
    return root


def preOrderTree(preOrder: List[int]) -> TreeNode:

    # Return the util function
    return util(preOrder)

# Time Complexity

# O(N^2), Where ‘N’ is the number of nodes in the tree.

 

# We are iterating over each element in the preorder array, and for each element, 
# we are dividing the array into two subarrays, which will cost O(N^2) time. 
# Hence the final time complexity is O(N^2).
# Space Complexity

# O(N^2), Where ‘N’ is the number of nodes in the tree.

 

# The recursion stack will take O(N) space. For each recursive call,
#  we make two arrays that. will take O(N) space each. Hence the overall space complexity is O(N^2).
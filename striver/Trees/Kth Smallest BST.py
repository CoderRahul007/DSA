class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        ans = float('inf')
        def inorderTraversal(node):
            nonlocal count, ans
            if node:
                inorderTraversal(node.left)
                count -= 1
                if count == 0:
                    ans = node.val
                
                inorderTraversal(node.right)
                
        inorderTraversal(root)
        return ans
        
##########################################################################3
'''
    Time Complexity : O(N)
    Space Complexity : O(N)

    Where 'N' is the number of nodes in the given binary search tree.
'''

nodes = []

def inorder(root):
    global nodes

    if (root == None):
        
        #  Base case.
        return

    #  Recur for the left subtree.
    inorder(root.left)

    #  Store the current node value in "nodes".
    nodes.append(root.data)

    #  Recur for the right subtree.
    inorder(root.right)

def kthSmallest(root, k):
    
    global nodes

    #  To store the inorder traversal of the BST.
    nodes = []

    inorder(root)

    return nodes[k - 1]


#######################################################################################

from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure
   
    class   TreeNode :
        def __init__(self, data) :
            self.data = data
            self.left = None
            self.right = None

        def __del__(self):
            if self.left:
                del self.left
            if self.right:
                del self.right

'''
def inorder(root, visCount, k):
    if root == None:
        return -1
     # Recurse over left subtree.    
    left = inorder(root.left, visCount, k)
    
    if left != -1:
        return left
    
    visCount[0] += 1

    if visCount[0] == k:
        return root.data
   
     # Recurse over right subtree.
    right = inorder(root.right, visCount, k)
    
    return right
    

def kthSmallest(root, k):
    
    global nodes

    #  To store the inorder traversal of the BST.
    visCount = [0]

    return inorder(root, visCount, k)  



#########################################################################################
'''
    Time Complexity : O(N)
    Space Complexity : O(N)

    Where 'N' is the number of nodes in the given binary search tree.
'''

def kthSmallest(root, k):
    
    #  To store the nodes of the tree.
    st = []

    while True:
        while (root != None):
            
            #  Push the root node in the stack.
            st.append(root)

            root = root.left

        root = st.pop()

        if (k == 1):
            return root.data

        #  Update the 'k'
        k = k - 1

        root = root.right

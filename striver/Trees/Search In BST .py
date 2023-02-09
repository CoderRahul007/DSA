from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the Binary Tree node structure:

	class BinaryTreeNode :
	    def __init__(self, data) :
	        self.data = data
	        self.left = None
	        self.right = None

'''

def searchInBST(root, x):
	# Write your code here.
    if not root:
        return False
    elif root.data == x:
        return True
    elif root.data < x:
        return searchInBST(root.right , x)
    elif root.data > x:
        return searchInBST(root.left , x)
    

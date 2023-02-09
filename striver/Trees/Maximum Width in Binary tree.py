'''
    Time Complexity : O(N)
    Space Complexity : O(N)

    Where 'N' is the number of nodes in the given binary tree.
'''

from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def getMaxWidth(root):

    # Write your code here.
    if root is None:
        return 0
    q = []
    q.append(root)
    mx = -1
    while len(q) > 0:
        curr = len(q)
        mx = max(curr , mx)
        
        while curr > 0:
            temp = q[0]
            q.pop(0)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            curr-=1
    return mx
        
        
        
        
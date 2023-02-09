from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)


#   Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def getLevelOrder(root):

    #   Write your code here
    if not root:
        return []
    
    q = []
    q.append(root)
    ans = []
    
    while len(q) > 0 :
        temp = q.pop(0)
        ans.append(temp.val)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return ans

# On and On
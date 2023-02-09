
'''

    Time complexity: O(N*log(N)) 
    Space complexity: O(N)

    Where ‘N’ is the number of nodes present in the binary tree.

'''

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

#for every vertical line only first member will be the top view from left to right thats why we are chcecking in mp
def getTopView(root):
    # Write your code here.
    ans = []
    q = []
    q.append([root , 0])
    mp = {}    
    while len(q) >0 :
        node , level = q.pop(0)
        if level not in mp and node is not None:
                mp[level] = node.val               
        if node and node.left is not None:            
            q.append([node.left , level-1])
        if node and node.right is not None:
            q.append([node.right , level+1])
    for i in sorted(mp.keys()):
        ans.append(mp.get(i))
    return ans
            

# Taking input.
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root

# Printing the tree nodes.
def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# Main.
T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = getTopView(root)
    printAns(ans)
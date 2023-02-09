
# Using queue

# The idea is to store the level order of the tree in the queue.
#  Also, taking the horizontal distances from the root as the key in the map,
#  we will update the value, which is the node corresponding to the horizontal distance, whenever a new node is accessed.

# Take an ordered map and a queue. The ordered map will help to store the nodes in the left to right order.
# Push the root and the horizontal distance(which is 0 for the root) using the pair data structure, in the queue.
# While the queue is not empty, perform the below steps:
#     a. Store the front element of the queue, which will be a node and the horizontal distance of
#        at node in a variable ‘TEMP’.
#     b. Pop the front element.
#     c. Put the dequeued tree node in the map having the corresponding horizontal distance as the key.
#        If the key is already present in the map, update its value with the current dequeued tree node.
#     d. If the dequeued node has a left child, push it to the queue along with the horizontal distance
#        of the dequeued node - 1.
#     e. If the dequeued node has a right child, push it to the queue along with the horizontal distance of
#        the dequeued node + 1.
# Traverse the map and keep storing the values of each key in a vector.
# Finally, return the vector which will be our required nodes in the bottom view of the binary tree.

# Time Complexity

# O(N*log(N)), where ‘N’ is the number of nodes in the binary tree.


# We iterate through all the nodes of the binary tree and the insertion
# in the ordered map takes time of the order ‘log(N)’.
# Space Complexity

# O(N), where ‘N’ is the number of nodes in the binary tree.

# A queue of size ‘N’ is used.


'''

    Time complexity: O(N*log(N))
    Space complexity: O(N)

    Where ‘N’ is the number of nodes present in the binary tree.

'''

from sys import stdin, setrecursionlimit
import queue
import sys
from collections import OrderedDict
setrecursionlimit(10**6)


# Following is the structure used to represent the Binary Tree Node.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Pair:

    def __init__(self, root, level):
        self.root = root
        self.level = level


def bottomView(root):

    ans = []

    mp = OrderedDict()

    q = []

    p1 = Pair(root, 0)
    q.append(p1)

    while len(q) > 0:
        p = q.pop(0)

        mp[p.level] = p.root

        if p.root.left is not None:
            q.append(Pair(p.root.left, p.level - 1))

        if p.root.right is not None:
            q.append(Pair(p.root.right, p.level + 1))

    bottomViewList = []

    for key in mp.keys():
        bottomViewList.append(key)

    bottomViewList.sort()

    for i in bottomViewList:
        ans.append(mp.get(i).data)

    return ans

# vertical lines

# Taking level-order input using fast I/O method.


def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main.
t = int(input())
while t:
    root = takeInput()
    answer = bottomView(root)
    print(*answer)
    t = t - 1


###################################################################################################################
#  Using recursion and map.

# Create a map where the key is the horizontal distance and the value is a pair(a,b)
# where ’a’ is the node and ‘b’ is the level number or the height of the node.
# On traversing the tree, if the current calculated horizontal distance is not
# present in the map, add it. Otherwise, compare the height of the previously-stored value
#  at that key with the current one. If the height of the new node is greater, update the value in the map.

# Start with the root as the current tree node, 0 as the horizontal distance, and 0 as the height.
# If the current horizontal distance is not present in the map, add it.
#  The key will be the horizontal distance and the value will be a pair of the node and the height of the node(the level number).
# If the current horizontal distance is already present in the map,
#  compare the height of the previously-stored value at that key with the current one.
#  If the height of the new node is greater, update the value in the map.
# Recur for left subtree with the left child of the current node, ‘HEIGHT’+1,
#  horizontal distance of the current node-1 (because of the left child).
# Recur for the right subtree with the right child of the current node, ‘HEIGHT’ + 1,
# the horizontal distance of the current node+1 (because of the right child).
# Traverse the map and keep storing the values of each key in a vector.
# Finally, return the vector which will be our required nodes in the bottom view of the binary tree.

# Time Complexity

# O(N*log(N)), where ‘N’ is the number of nodes in the binary tree.

# We iterate through all the nodes of the binary tree and the insertion
# and searching in the ordered map takes time of the order ‘log(N)’.
# Space Complexity

# O(N), where ‘N’ is the number of nodes in the binary tree.


'''

    Time complexity: O(N*log(N)) 
    Space complexity: O(N)

    Where ‘N’ is the number of nodes present in the binary tree.

'''

setrecursionlimit(10**6)


# Following is the structure used to represent the Binary Tree Node.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Pair:

    def __init__(self, root, level):
        self.root = root
        self.level = level


def bottomView(root):

    horizontalDistance = 0
    ans = []

    mp = OrderedDict()

    q = []

    p1 = Pair(root, 0)
    q.append(p1)

    while len(q) > 0:
        p = q.pop(0)

        mp[p.level] = p.root

        if p.root.left is not None:
            q.append(Pair(p.root.left, p.level - 1))

        if p.root.right is not None:
            q.append(Pair(p.root.right, p.level + 1))

    bottomViewList = []

    for key in mp.keys():
        bottomViewList.append(key)

    bottomViewList.sort()

    for i in bottomViewList:
        # at last only single element is there for particular level
        ans.append(mp.get(i).data)

    return ans


#############################################################################################
def print_bottom_of_binary_tree(root):
    d = dict()

    printBottomViewUtil(root, d, 0, 0)
    for i in sorted(d.keys()): #logn
        print(d[i][0], end=" ")


def bottomview(root, d, hd, level):
    if root is None:
        return

    if hd in d:
        if level >= d[hd][1]:
            d[hd] = [root.data, level]
    else:
        d[hd] = [root.data, level]
         
    bottomview(root.left, d, hd - 1,level + 1)
    bottomview(root.right, d, hd + 1,level + 1)

# Time Complexity: O(N) where N is the number of nodes of the binary tree.
# Space Complexity: O(N), as a map is used.

    
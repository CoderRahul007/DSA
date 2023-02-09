###################################################################################################
# Python3 program to find the maximum depth of tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node


def maxDepth(node):
    if node is None:
        return -1

    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

    return max(lDepth, rDepth) + 1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Height of tree is %d" % (maxDepth(root)))

# On On


####################################################################################################
# We can use level order traversal to find height without recursion.
# The idea is to traverse level by level. Whenever move down to a level,
#  increment height by 1 (height is initialized as 0). Count number of nodes at each level,
#  stop traversing when the count of nodes at the next level is 0.

# Following is a detailed algorithm to find level order traversal using a queue.

# Create a queue.
# Push root into the queue.
# height = 0
# nodeCount = 0 // Number of nodes in the current level.

# // If the number of nodes in the queue is 0, it implies
# // that all the levels of the tree have been parsed. So,
# // return the height. Otherwise count the number of nodes
# // in the current level and push the children of all the
# // nodes in the current level to the queue.

# Loop
#     nodeCount = size of queue

#     // If the number of nodes at this level is 0, return height

#     if nodeCount is 0
#         return Height;
#     else
#         increase Height

#         // Remove nodes of this level and add nodes of
#         // next level
#     while (nodeCount > 0)
#         push its children to queue
#         pop node from front
#         decrease nodeCount
#        // At this point, queue has nodes of next level
# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Following is the implementation of the above algorithm.


# Program to find height of tree by Iteration Method

# A binary tree node
class Node:

    # Constructor to create new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Iterative method to find height of Binary Tree


def treeHeight(root):

    # Base Case
    if root is None:
        return 0

    # Create a empty queue for level order traversal
    q = []

    # Enqueue Root and Initialize Height
    q.append(root)
    height = 0

    while(True):

        # nodeCount(queue size) indicates number of nodes
        # at current level
        nodeCount = len(q)
        if nodeCount == 0:
            return height

        height += 1

        # Dequeue all nodes of current level and Enqueue
        # all nodes of next level
        while(nodeCount > 0):
            node = q[0]
            q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

            nodeCount -= 1


# Driver program to test above function
# Let us create binary tree shown in above diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Time Complexity: O(n) where n is the number of nodes in a given binary tree.
# Space Complexity: O(n) where n is the number of nodes in a given binary tree.


# Queue Approach

# The idea here is to use a breadth-first search i.e. BFS along with the queue.

# We use an array to store nodes in current level if the level is even then we
#  will add elements of the array in reverse order otherwise we will add elements of the array in the same order. 

# Steps :

#     Declare an empty array answer to store zigzag traversal.
#     Declare an empty queue and push root to it and declare a boolean variable 
#       reverseOrder which will tell us whether we should include nodes in current level 
#           in the original order or reverse order.
#     Initialize reverseOrder as false.
#     Run a loop until the queue is not empty and do:
#         Size of queue denoted by variable size i.e the number of nodes in the current level.
#         Create an array to store elements of the current level, say currentLevelNodes.
#         Run a loop until nodes in the current level are greater than zero and add all its 
#           nodes data to currentLevelNodes
#         Push left and right child of current level nodes to queue for next-level iteration
#         If reverseOrder is false then add elements of currentLevelNodes to answer, 
#           else add elements of currentLevelnodes to answer in reverse order.
#         Change reverseOrder to false if it is true and vice-versa for the next level.

# 5. At last, return the answer. 
# Time Complexity

# O(N), where N is the total number of nodes in the given binary tree.

# In the worst case, we are visiting each node exactly once.Hence the overall time complexity will be O(N).
# Space Complexity

# O(N), where N is the total number of nodes in the given binary tree.

# In the worst case, we are using a queue that requires additional O(N) space.
#    So the overall space complexity will be O(N).


'''
    Time Complexity  : O(N)
    Space Complexity : O(N)

    Where N is the total number of nodes in the binary tree.
'''

# BinaryTreeNode class definition
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zigZagTraversal(root):
    # Declare an empty array answer to store zigzag traversal
    answer = []

    # Base Case
    if root == None:
        return answer

    # Declare an empty queue and push root to it
    queue = []
    queue.append(root)

    # Initialize reverseOrder as false
    revereOrder = False
    while len(queue):
        # Size of queue denotes number of nodes in current level
        size = len(queue)
        #  Declare an array of size to store elements of current level
        currentLevelNodes = []
        # Run a loop until nodes in the current level are greater than zero and add all its nodes data to currentLevelNodes
        for i in range(size):
            # Pop front node from the queue
            frontNode = queue[0]
            del queue[0]
            # Add data of node of current level node
            currentLevelNodes.append(frontNode.data)

            # Push left and right child of current level nodes to queue for next
            # Level iteration
            if frontNode.left:
                queue.append(frontNode.left)
            if frontNode.right:
                queue.append(frontNode.right)

        # If reverse order is true then add data of nodes from left to right
        # Else add data of nodes in reverse order i.e. right to left
        for i in range(size):
            if revereOrder == False:
                answer.append(currentLevelNodes[i])
            else:
                answer.append(currentLevelNodes[size-i-1])
                
        # Change reverseOrder to false if it is true and vice-versa for the next level
        revereOrder ^= True

    # Return the final answer
    return answer

###################################################################################################
# Using Deque
'''
    Time Complexity  : O(N)
    Space Complexity : O(N)

    Where N is the total number of nodes in the binary tree.
'''

from collections import deque


# BinaryTreeNode class definition
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zigZagTraversal(root):
    # Declare an empty array answer to store zigzag traversal
    answer = []

    # Base Case
    if root == None:
        return answer

    # Declare an empty dequeu and push root to it
    d = deque()
    d.append(root)

    # Declare a variable level to get current level and initialize it to 1
    level = 1
    while len(d):
        # Size of deque denotes number of nodes in current level
        size = len(d)

        # Run a loop until nodes in the current level are greater than zero
        for i in range(size):
            if level % 2 == 1:
                # Pop front node from the dequeu and add that data to the answer
                backNode = d[0]
                del d[0]
                answer.append(backNode.data)

                # Push left and right child of current level nodes to deque
                if backNode.left:
                    d.append(backNode.left)
                if backNode.right:
                    d.append(backNode.right)
            # If current level is even
            else:
                # Pop back node from deque and add its data to answer
                backNode = d[-1]
                del d[-1]
                answer.append(backNode.data)

                # Push left and right child of current level nodes to deque
                if backNode.right:
                    d.appendleft(backNode.right)
                if backNode.left:
                    d.appendleft(backNode.left)
        # Increment level by 1
        level += 1

    # Return the final answer
    return answer

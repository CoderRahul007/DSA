# Level Order Traversal Approach

# The idea is to do a level order traversal and for each level of the binary tree include 
# the leftmost node in the answer. The steps are as follows:

# Define a queue let’s say as “level” for doing level order traversal and an array “leftView”
#  for storing the nodes of the left view of the given binary tree.
# Push the root of the given tree into the ”level”.
# We will keep doing the following operations until “level” does not become empty:
#     Get the size of the queue, i.e. the total number of nodes at the current level.
#      Also declare a variable “leftMostNode” to store the left most node of the current level.
#     Visit all the nodes one by one which are at the current level and store the value of 
#     the first node(i.e. the leftmost node) of the current level in “leftMostNode”.
#      Push their left and right child into the queue if they exist.
#     Insert the value of “leftMostNode” in “leftView”.
# In the end, “leftView” will contain all the nodes which are possible to see from the
# left side of the given binary tree. So return the “leftView”.

# Time Complexity

# O(N), where N is the total number of nodes in the binary tree.

 

# We are using the level order traversal, in which there will be ‘N’ push and ‘N’ pop operations,
#  where push and pop operation will take constant time for the queue data structure.
#  Thus, the total overall time complexity will be O(N).
# Space Complexity

# O(N), where N is the total number of nodes in the binary tree.

 

# We are storing the value of the leftmost nodes in the answer. So in the worst case when
# the binary tree is skewed, there will be a total of ‘N’ nodes to store because in that
# case, all the tree nodes are visible from the left side of the given binary tree.
# Also, for doing level order traversal, we are using a queue that can have a maximum 
# of ‘N/2’ nodes in the case of a complete binary tree. Thus, the total overall space complexity is O(N).


'''
	Time Complexity - O(N)
	Space Complexity - O(N)

	Where N is the number of nodes in the Binary Tree.
'''


# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLeftView(root):

	#    For storing the left view.
	leftView = []

	if (root == None):
		return leftView
	
	#    Queue for doing level order traversal.
	level = []

	#    append the root in the queue.
	level.append(root)
	leftMostNode = None

	while (len(level) != 0):
	
		#    Get the size of the current level.
		queueSize = len(level)

		#    Traverse all nodes of the current level.
		for i in range(queueSize):
		
			#    Pop the node from the front of the queue.
			curr = level[0]
			level.pop(0)

			#    Store the left most node of the current level.
			if (i == 0):
				leftMostNode = curr.data

			#    append the left child into the queue.
			if (curr.left != None):
				level.append(curr.left)

			#    append the right child into the queue.
			if (curr.right != None):
				level.append(curr.right)

		#    Store the left most node of the current level in the array.
		leftView.append(leftMostNode)
	
	#    Return the left view of the given binary tree.
	return leftView
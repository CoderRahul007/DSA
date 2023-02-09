# https://www.geeksforgeeks.org/calculate-height-of-binary-tree-using-inorder-and-level-order-traversal/

##################################################################################################################################

# Queue Solution

#     The first element of the Level order Traversal is necessarily the root of the binary tree.
#     The nodes which appear left of the root in the inorder traversal are necessarily in the left subtree,
#      and those which appear in the right are in the right subtree of the right subtree.
#     We can make use of the fact that the nodes of a subtree of the binary tree will form a continuous segment in the inorder array.
#     We can maintain a queue with each element in a queue containing three integers, namely the height of the
#      current subtree, the starting index, and the ending index of the subtree in the inorder array.
#     Then the algorithm is:
#         We will initially push (0, 0, ‘N’ - 1) in the queue.
#         We will start traversing the level order array.
#         When we are at index ‘i’ in the level order array we will pop out the front element of the queue.
#             Let that popped-out element be ('HEIGHT', ‘LEFTINDEX’, ‘RIGHTINDEX’).
#             We will start iterating from the ‘LEFTINDEX’ to ‘RIGHTINDEX’ of the inorder array and 
#             find the index of element ‘LEVELORDER[i]’ in the inorder array. Let that index be ‘j’.
#             If ('j' - 1) is greater than equal to leftIndex, we will push ('HEIGHT' + 1, ‘LEFTINDEX’, ‘j’ - 1) into the queue.
#             Similarly, if ('j' + 1) is less than equal to rightIndex we will push ('HEIGHT' + 1, ‘j’ + 1, 'RIGHTINDEX') into the queue.
#         The maximum height encountered in this process will be the height of the binary tree.

# Time Complexity

# O(N^2), where N denotes the number of nodes of the binary tree.

 

# As we are iterating over the complete level order traversal and for each node, 
# we are finding its position in the inorder traversal, so the time complexity will be O(N^2).
# Space Complexity

# O(N), where N denotes the number of nodes in the binary tree.

 

# As the last layer can have at most N/2 nodes(in case of a complete binary tree), the maximum number of nodes in the queue at any time will be N/2. 

'''
    Time Complexity: O(N^2)
    Space Complexity: O(N)

    Where N is the total number of nodes in the binary tree.
'''

import sys
sys.setrecursionlimit(10**7)

from queue import Queue

class Node:

	# Height stores the height of the current subtree
	height = 0
	leftIndex = -1
	rightIndex = -1


def heightOfTheTree(inorder, levelOrder, N):	
	q = Queue()

	init = Node()

	init.height = 0
	init.leftIndex = 0
	init.rightIndex = N - 1

	q.put(init)

	maxHeight = 0

	for i in range(N):
		curr = levelOrder[i] #first will be root

		now = q.get()

		currPos = 0

		''' 
            Iterating from leftIndex to rightIndex to find the position of
			leveOrder[i] in the inorder array. 
        '''  
		for j in range(now.leftIndex, now.rightIndex + 1):
			if levelOrder[i] == inorder[j]:
				currPos = j
		
		# There is a left child present.
		if currPos > now.leftIndex:
			newNode = Node()

			# Height will increase by 1 as we are descending 1 level downwards in the tree.
			newNode.height = now.height + 1

			maxHeight = max(maxHeight, newNode.height)

			# New borders of the left subtree in the inorder array.
			newNode.leftIndex = now.leftIndex
			newNode.rightIndex = currPos - 1

			q.put(newNode)		

		# There is a right child present.
		if currPos < now.rightIndex:
			newNode = Node()

			newNode.height = now.height + 1

			maxHeight = max(maxHeight, newNode.height)

			# New borders of the right subtree in the inorder array.
			newNode.leftIndex = currPos + 1
			newNode.rightIndex = now.rightIndex

			q.put(newNode)


	return maxHeight

#####################################################################################################################################
# Queue and Precomputation

#     The N^2 approach can be further optimized by storing the position of node ‘i’ in the inorder
#      array so that we can save time on searching for the position.
#     We can declare an auxiliary array ‘POS’ of size ‘N’ with each element storing the index of node ‘i’, 
#     so that we can get the position of a node in an inorder array in constant time.
#     We can follow the same previous algorithm with one modification-
#         Instead of iterating from ‘LEFTINDEX’ to ‘RIGHTINDEX’ to find the position of ‘LEVELORDER[i]’,
#          we can directly query the required position from the ‘POS’ array.

# Time Complexity

# O(N), where N denotes the number of nodes of the binary tree.

 

# As we are iterating over the complete level order traversal the time complexity will be O(N). 
# The time taken to access an element in pos is O(1).
# Space Complexity

# O(N), where N denotes the number of nodes of the binary tree.

# As the last layer can have at most N/2 nodes(in case of a complete binary tree), 
# the maximum number of nodes in the queue at any time will be N/2. The size of the ‘pos’ array is also N + 1.

'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the total number of nodes in the binary tree.
'''

import sys
sys.setrecursionlimit(10**7)

from queue import Queue

class Node:
	# Height stores the height of the current subtree.
	height = 0
	leftIndex = -1
	rightIndex = -1

def heightOfTheTree(inorder, levelOrder, N):
	
	q = Queue()

	init = Node()

	init.height = 0
	init.leftIndex = 0
	init.rightIndex = N - 1

	q.put(init)
      
	pos = [0] * (N + 1)

	for i in range(N):
		pos[inorder[i]] = i

	maxHeight = 0

	for i in range(N):
		curr = levelOrder[i]

		now = q.get()

		# Position of levelOrder[i] in the inorder array. 
		currPos = pos[levelOrder[i]]
		
		# There is a left child present.
		if currPos > now.leftIndex:
			newNode = Node()

			# Height will increase by 1 as we are descending 1 level downwards in the tree.
			newNode.height = now.height + 1

			maxHeight = max(maxHeight, newNode.height)

			# New borders of the left subtree in the inorder array.
			newNode.leftIndex = now.leftIndex
			newNode.rightIndex = currPos - 1

			q.put(newNode)
		

		# There is a right child present.
		if currPos < now.rightIndex:
			newNode = Node()

			newNode.height = now.height + 1

			maxHeight = max(maxHeight, newNode.height)

			# New borders of the right subtree in the inorder array.
			newNode.leftIndex = currPos + 1
			newNode.rightIndex = now.rightIndex

			q.put(newNode)

	return maxHeight

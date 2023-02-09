# Given a Binary tree and a sum S, print all the paths, starting from root, that sums upto the given sum.
# Note that this problem is different from root to leaf paths. Here path doesn’t need to end on a leaf node.

# Examples:  

# Input : 
# Input : sum = 8, 
#         Root of tree
#          1
#        /   \
#      20      3
#            /    \
#          4       15    
#         /  \     /  \
#        6    7   8    9           
# Output :
# Path: 1 3 4

# Input : sum = 38,
#         Root of tree
#           10
#        /     \
#      28       13
#            /     \
#          14       15
#         /   \     /  \
#        21   22   23   24
# Output : Path found: 10 28 
#         Path found: 10 13 15

# Recommended Practice
# Paths from root with a specified sum
# Try It!

# For this problem, preorder traversal is best suited as we have to add up a key value as we land on that node.
# We start from the root and start traversing by preorder traversal, adding key value to the sum_so_far and checking whether it is equal to the required sum. 
# Also, as tree node doesn’t have a pointer pointing to its parent, we have to explicitly save from where we have moved. We use a vector path to store the path for this.
# Every node in this path contributes to the sum_so_far. 

# Python3 program to Print all the
# paths from root, with a specified
# sum in Binary tree
	
# Binary Tree Node
""" utility that allocates a newNode
with the given key """
class newNode:

	# Construct to create a newNode
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# This function prints all paths
# that have sum k
def printPathsUtil(curr_node, sum,
				sum_so_far, path):

	# empty node
	if (not curr_node) :
		return
	sum_so_far += curr_node.key
	
	# add current node to the path
	path.append(curr_node.key)

	# print the required path
	if (sum_so_far == sum ) :
	
		print("Path found:", end = " ")
		for i in range(len(path)):
			print(path[i], end = " ")

		print()
	
	# if left child exists
	if (curr_node.left != None) :
		printPathsUtil(curr_node.left, sum,
					sum_so_far, path)

	# if right child exists
	if (curr_node.right != None) :
		printPathsUtil(curr_node.right, sum,
					sum_so_far, path)

	# Remove the current element
	# from the path
	path.pop(-1)

# A wrapper over printKPathUtil()
def printPaths(root, sum):

	path = []
	printPathsUtil(root, sum, 0, path)

# Driver Code
if __name__ == '__main__':

	""" 10
	/	 \
	28	 13
		/	 \
		14	 15
		/ \	 / \
	21 22 23 24"""
	root = newNode(10)
	root.left = newNode(28)
	root.right = newNode(13)

	root.right.left = newNode(14)
	root.right.right = newNode(15)

	root.right.left.left = newNode(21)
	root.right.left.right = newNode(22)
	root.right.right.left = newNode(23)
	root.right.right.right = newNode(24)

	sum = 38

	printPaths(root, sum)


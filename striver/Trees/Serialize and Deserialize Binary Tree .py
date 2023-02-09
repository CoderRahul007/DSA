# Level order Traversal Approach

# The idea is to store the level order traversal of the given binary tree to serialize the tree. 
# But since only storing the level order traversal cannot uniquely determine the structure of
#  the binary tree, we will insert -1 in place of NULL nodes so that we can determine the structure 
# of the binary tree uniquely when we deserialize the binary tree.

 

# We will store the serialized binary tree in a string, let’s say “serialized”. 
# Also, we will use ‘,’ as a separator to separate the value of different nodes 
# in the string because then we can distinguish that nodes 12 and 1,2 are different.

# The steps to serialize the binary tree are as follows:


# Define a queue; let’s say “level”.
# Push the root of the given binary tree into the queue (“level”).
# Now we will perform the following operations until the queue (“level”) does not become empty:
#     Pop the node from the front of the “level’, let’s say this node is “curr”.
#     If “curr” is not null, then append the value of “curr” to “serialized”, 
#     also append ‘,’ after this so that we can distinguish between values of different nodes.
#         Also, we will push the left and right children of “curr” into the “level”.
#     Otherwise if “curr” is null, then append “-1,” to “serialized”.
# Return the “serialized” string.

 

# To deserialize the tree, we will read the values in the “serialized” string one by one 
# and then create the binary tree in a level order manner.

# The steps to deserialize the binary tree are as follows:


# Define a queue; let’s say “level”.
# Read the value of the first node from the “serialized”, if this value is equal to -1,
#  return a null node. Otherwise, create a new TreeNode, let’s say “root” with this value,
#  and push this node into the “level”.
# Now we will perform the following operations until “level” does not become empty:
#     Pop the node at the front of “level’, let’s say this node is “curr”.
#     Read the next two values from the “serialized” string. These will be the values 
#     of the left and the right child nodes of “curr”. Let’s say the two values are “leftChild” and 
#     “rightChild” respectively.
#     If “leftChild” is not equal to -1, then create a new TreeNode with the value “leftChild” and make this new node the left child of “curr” and push this node into “level”.
#     If “rightChild” is not equal to -1, then create a new TreeNode with the value “rightChild” and make this new node the right child of “curr” and push this node into “level”.
# Return the root node.

# Time Complexity

# O(N), where N is the total number of nodes in the binary tree.

# We are doing level order traversal for serializing the string which will visit
# each node of the given binary tree exactly once. Thus the total time complexity will be O(N).
# Space Complexity

# O(N), where N is the total number of nodes in the binary tree.

 

# We are storing the value of all nodes in the “serialized” string which will take O(N) space. 
# Also, for doing level order traversal, we are using a queue that can have a maximum of ‘N / 2’ 
# nodes in the case of a complete binary tree. Thus, the total space complexity is O(N).

'''
	Time Complexity - O(N)
	Space Complexity - O(N)

	Where N is the number of nodes in the Binary Tree.
'''

class TreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def serializeTree(root):

	# Intialize serialized as an empty string
	serialized = ""

	# Queue for level order traversal
	level = [root]

	while len(level) != 0:
	
		# Pop the Node at the front
		curr = level.pop(0)
		

		# If the current node is not null.
		if (curr != None):
		
			# Add the value of the curr node to the serialized string.
			serialized += str(curr.data)
			serialized += ','

			# Push the left and the right child nodes in the queue.
			level.append(curr.left)
			level.append(curr.right)

		#    If the current node is null
		else:
		
			#    Add -1 to the serialized string.
			serialized += "-1,"

	#    Return the serialized binary tree.
	return serialized

def deserializeTree(serialized):

	#    Pointer for reading elements from the serialized binary tree.
	ptr = 0
	firstVal = ""
	
	#    Read the first value from the string.
	while (ptr < len(serialized) and serialized[ptr] != ','):
	
		firstVal += serialized[ptr]
		ptr += 1

	ptr += 1
	val = int(firstVal)

	#    If the first value if -1 then return null.
	if (val == -1):
		return None

	#    Create a new root node.
	root = TreeNode(val)

	#    Queue for level order traversal.
	#    Push the root node into the queue.
	level = [root]

	while (len(level) != 0):
	
		#    Pop the front node from the queue.
		curr = level[0]
		level.pop(0)

		leftChild = ""

		#    Read the value of the left child.
		while (ptr < len(serialized) and serialized[ptr] != ','):
		
			leftChild += serialized[ptr]
			ptr += 1
		
		ptr += 1
		rightChild = ""

		#    Read the value of the right child.
		while (ptr < len(serialized) and serialized[ptr] != ','):
		
			rightChild += serialized[ptr]
			ptr += 1
		
		ptr += 1

		leftChildValue = int(leftChild)
		rightChildValue = int(rightChild);

		#    If the left child node is not null
		if (leftChildValue != -1):
		
			#    Create new left child node.
			leftNode = TreeNode(leftChildValue)
			curr.left = leftNode

			#    Push the left child into the queue.
			level.append(curr.left)
		
		#    If the right child is not null
		if (rightChildValue != -1):
		
			#    Create new right child node.
			rightNode = TreeNode(rightChildValue)
			curr.right = rightNode

			#    Push the right child into the queue.
			level.append(curr.right)

	#    Return the root of deserialized the binary tree.
	return root

####################################################################################################3

# Serialization is to store a tree in an array so that it can be later restored and Deserialization
#  is reading tree back from the array. Now your task is to complete the function serialize which stores the tree into an array A[ ] and deSerialize which deserializes the array to the tree and returns it.
# Note: The structure of the tree must be maintained. Multiple nodes can have the same data.

# Example 1:

# Input:
#       1
#     /   \
#    2     3
# Output: 2 1 3

# Example 2:

# Input:
#          10
#        /    \
#       20    30
#     /   \
#    40  60
# Output: 40 20 60 10 30

# https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
# https://www.youtube.com/watch?v=-YbXySKJsX8
def serialize(root, A):
    #code here
    if not root:
        A.append(-1)
        return 
    A.append(root.data)
    serialize(root.left , A)
    serialize(root.right , A)
    #Preorder traversal
#Function to deserialize a list and construct the tree.   
def deSerialize(A):
    #code here
    if A[0] == -1:
        A.pop(0)
        return None
    root = Node(A.pop(0))
    root.left = deSerialize(A)
    root.right = deSerialize(A)
    return root
# Following are some simpler versions of the problem:
# If given Tree is Binary Search Tree? 
# If the given Binary Tree is Binary Search Tree, we can store it by either storing preorder or postorder traversal. In case of Binary Search Trees, only preorder or postorder traversal is sufficient to store structure information. 

# If given Binary Tree is Complete Tree? 
# A Binary Tree is complete if all levels are completely filled except possibly the last level and all nodes of last level are as left as possible (Binary Heaps are complete Binary Tree). For a complete Binary Tree, level order traversal is sufficient to store the tree. We know that the first node is root, next two nodes are nodes of next level, next four nodes are nodes of 2nd level and so on. 

# If given Binary Tree is Full Tree? 
# A full Binary is a Binary Tree where every node has either 0 or 2 children. It is easy to serialize such trees as every internal node has 2 children. We can simply store preorder traversal and store a bit with every node to indicate whether the node is an internal node or a leaf node.

# How to store a general Binary Tree? 
# A simple solution is to store both Inorder and Preorder traversals. This solution requires space twice the size of Binary Tree. 
# We can save space by storing Preorder traversal and a marker for NULL pointers. 

# Let the marker for NULL pointers be '-1'
# Input:
#      12
#     /
#   13
# Output: 12 13 -1 -1 -1

# Input:
#       20
#     /   \
#    8     22 
# Output: 20 8 -1 -1 22 -1 -1 

# Input:
#          20
#        /    
#       8     
#      / \
#     4  12 
#       /  \
#      10  14
# Output: 20 8 4 -1 -1 12 10 -1 -1 14 -1 -1 -1 

# Input:
#           20
#          /    
#         8     
#       /
#     10
#     /
#    5
# Output: 20 8 10 5 -1 -1 -1 -1 -1 

# Input:
#           20
#             \
#              8
#               \   
#                10
#                  \
#                   5   
# Output: 20 -1 8 -1 10 -1 5 -1 -1
# Deserialization can be done by simply reading data from file one by one. 

# Following is the implementation of the above idea. 


# // A C program to demonstrate serialization and deserializa    
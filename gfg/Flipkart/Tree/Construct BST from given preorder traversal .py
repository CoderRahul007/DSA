# Given preorder traversal of a binary search tree, construct the BST.

# For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be the root of the following tree.

#      10
#    /   \
#   5     40
#  /  \      \
# 1    7      50

# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/

# Method 1 ( O(n2) time complexity ) 
# The first element of preorder traversal is always root. We first construct the root. Then we find the index of the first element which is greater than the root. Let the index be ‘i’. The values between root and ‘i’ will be part of the left subtree, and the values between ‘i'(inclusive) and ‘n-1’ will be part of the right subtree. Divide given pre[] at index “i” and recur for left and right sub-trees. 

# For example in {10, 5, 1, 7, 40, 50}, 10 is the first element, so we make it root. Now we look for the first element greater than 10, we find 40. So we know the structure of BST is as following. 

#              10
#            /    \
#           /      \
#   {5, 1, 7}       {40, 50}
# We recursively follow above steps for subarrays {5, 1, 7} and {40, 50}, and get the complete tree. 
# A O(n^2) Python3 program for
# construction of BST from preorder traversal

# A binary tree node


class Node():

	# A constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


# constructTreeUtil.preIndex is a static variable of
# function constructTreeUtil

# Function to get the value of static variable
# constructTreeUtil.preIndex
def getPreIndex():
	return constructTreeUtil.preIndex

# Function to increment the value of static variable
# constructTreeUtil.preIndex


def incrementPreIndex():
	constructTreeUtil.preIndex += 1

# A recurseive function to construct Full from pre[].
# preIndex is used to keep track of index in pre[[].


def constructTreeUtil(pre, low, high):

		# Base Case
	if(low > high):
		return None

	# The first node in preorder traversal is root. So take
	# the node at preIndex from pre[] and make it root,
	# and increment preIndex
	root = Node(pre[getPreIndex()])
	incrementPreIndex()

	# If the current subarray has onlye one element,
	# no need to recur
	if low == high:
		return root

	r_root = -1

	# Search for the first element greater than root
	for i in range(low, high+1):
		if (pre[i] > root.data):
			r_root = i
			break

	# If no elements are greater than the current root,
	# all elements are left children
	# so assign root appropriately
	if r_root == -1:
		r_root = getPreIndex() + (high - low)

	# Use the index of element found in preorder to divide
	# preorder array in two parts. Left subtree and right
	# subtree
	root.left = constructTreeUtil(pre, getPreIndex(), r_root-1)

	root.right = constructTreeUtil(pre, r_root, high)

	return root

# The main function to construct BST from given preorder
# traversal. This function mailny uses constructTreeUtil()


def constructTree(pre):
	size = len(pre)
	constructTreeUtil.preIndex = 0
	return constructTreeUtil(pre, 0, size-1)


def printInorder(root):
	if root is None:
		return
	printInorder(root.left)
	print (root.data,end=' ')
	printInorder(root.right)


# Driver code
pre = [10, 5, 1, 7, 40, 50]

root = constructTree(pre)
print ("Inorder traversal of the constructed tree:")
printInorder(root)
###########################################################################################
# Recursive
# Construct a BST from given pre-order traversal
# for example if the given traversal is {10, 5, 1, 7, 40, 50},
# then the output should be the root of the following tree.
# 	10
# / \
# 5	 40
# / \	 \
# 1 7	 50 

# class Node {
# 	int data;
# 	Node left, right;
# 	Node(int data)
# 	{
# 		this.data = data;
# 		this.left = this.right = null;
# 	}
# }

# class CreateBSTFromPreorder {
# 	private static Node node;

# 	// This will create the BST
# 	public static Node createNode(Node node, int data)
# 	{
# 		if (node == null)
# 			node = new Node(data);

# 		if (node.data > data)
# 			node.left = createNode(node.left, data);
# 		if (node.data < data)
# 			node.right = createNode(node.right, data);

# 		return node;
# 	}

# 	// A wrapper function of createNode
# 	public static void create(int data)
# 	{
# 		node = createNode(node, data);
# 	}
# 	// A function to print BST in inorder
# 	public static void inorderRec(Node root)
# 	{
# 		if (root != null) {
# 			inorderRec(root.left);
# 			System.out.println(root.data);
# 			inorderRec(root.right);
# 		}
# 	}

# 	// Driver Code
# 	public static void main(String[] args)
# 	{
# 		int[] nodeData = { 10, 5, 1, 7, 40, 50 };

# 		for (int i = 0; i < nodeData.length; i++) {
# 			create(nodeData[i]);
# 		}
# 		inorderRec(node);
# 	}
# }


# Method 2 ( O(n) time complexity ) 
# The idea used here is inspired by method 3 of this post. The trick is to set a range
#  {min .. max} for every node. Initialize the range as {INT_MIN .. INT_MAX}. 
# The first node will definitely be in range, so create a root node. 
# To construct the left subtree, set the range as {INT_MIN …root->data}. 
# If a value is in the range {INT_MIN .. root->data}, the values are part of the left subtree. 
# To construct the right subtree, set the range as {root->data..max .. INT_MAX}. 

# Below is the implementation of the above idea:

# A O(n) program for construction of BST from preorder traversal

INT_MIN = -float("inf")
INT_MAX = float("inf")

# A Binary tree node


class Node:

	# Constructor to created a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Methods to get and set the value of static variable
# constructTreeUtil.preIndex for function construcTreeUtil()


def getPreIndex():
	return constructTreeUtil.preIndex


def incrementPreIndex():
	constructTreeUtil.preIndex += 1

# A recursive function to construct BST from pre[].
# preIndex is used to keep track of index in pre[]


def constructTreeUtil(pre, key, mini, maxi, size):

	# Base Case
	if(getPreIndex() >= size):
		return None

	root = None

	# If current element of pre[] is in range, then
	# only it is part of current subtree
	if(key > mini and key < maxi):

		# Allocate memory for root of this subtree
		# and increment constructTreeUtil.preIndex
		root = Node(key)
		incrementPreIndex()

		if(getPreIndex() < size):

			# Construct the subtree under root
			# All nodes which are in range {min.. key} will
			# go in left subtree, and first such node will
			# be root of left subtree
			root.left = constructTreeUtil(pre,
										pre[getPreIndex()],
										mini, key, size)
		if(getPreIndex() < size):

			# All nodes which are in range{key..max} will
			# go to right subtree, and first such node will
			# be root of right subtree
			root.right = constructTreeUtil(pre,
										pre[getPreIndex()],
										key, maxi, size)

	return root

# This is the main function to construct BST from given
# preorder traversal. This function mainly uses
# constructTreeUtil()


def constructTree(pre):
	constructTreeUtil.preIndex = 0
	size = len(pre)
	return constructTreeUtil(pre, pre[0], INT_MIN, INT_MAX, size)


# A utility function to print inorder traversal of Binary Tree
def printInorder(node):

	if node is None:
		return
	printInorder(node.left)
	print (node.data,end=" ")
	printInorder(node.right)


# Driver code
pre = [10, 5, 1, 7, 40, 50]

# Function call
root = constructTree(pre)

print ("Inorder traversal of the constructed tree: ")
printInorder(root)

###############################################################################
#logn
# Iterative
def post_order(pre, size):
    #code here
    root = Node(pre[0])
    cur = None
    for i in range(1 , len(pre)):
        cur = root
        while True:
            if cur.data > pre[i]:
                if cur.left == None:
                    cur.left = Node(pre[i])
                    break
                else:
                    cur = cur.left
            else:
                if cur.right == None:
                    cur.right = Node(pre[i])
                    break
                else:
                    cur = cur.right
    return root
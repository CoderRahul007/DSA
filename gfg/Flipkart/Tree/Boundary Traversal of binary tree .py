# We break the problem in 3 parts: 
# 1. Print the left boundary in top-down manner. 
# 2. Print all leaf nodes from left to right, which can again be sub-divided into two sub-parts: 
# …..2.1 Print all leaf nodes of left sub-tree from left to right. 
# …..2.2 Print all leaf nodes of right subtree from left to right. 
# 3. Print the right boundary in bottom-up manner.
# We need to take care of one thing that nodes are not printed again. e.g. The left most node is also the leaf node of the tree.
# Based on the above cases, below is the implementation:

# Python3 program for binary traversal of binary tree

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# A simple function to print leaf nodes of a Binary Tree
def printLeaves(root):
	if(root):
		printLeaves(root.left)
		
		# Print it if it is a leaf node
		if root.left is None and root.right is None:
			print(root.data)

		printLeaves(root.right)

# A function to print all left boundary nodes, except a
# leaf node. Print the nodes in TOP DOWN manner
def printBoundaryLeft(root):
	
	if(root):
		if (root.left):
			
			# to ensure top down order, print the node
			# before calling itself for left subtree
			print(root.data)
			printBoundaryLeft(root.left)
		
		elif(root.right):
			print (root.data)
			printBoundaryLeft(root.right)
		
		# do nothing if it is a leaf node, this way we
		# avoid duplicates in output


# A function to print all right boundary nodes, except
# a leaf node. Print the nodes in BOTTOM UP manner
def printBoundaryRight(root):
	
	if(root):
		if (root.right):
			# to ensure bottom up order, first call for
			# right subtree, then print this node
			printBoundaryRight(root.right)
			print(root.data)
		
		elif(root.left):
			printBoundaryRight(root.left)
			print(root.data)

		# do nothing if it is a leaf node, this way we
		# avoid duplicates in output


# A function to do boundary traversal of a given binary tree
def printBoundary(root):
	if (root):
		print(root.data)
		
		# Print the left boundary in top-down manner
		printBoundaryLeft(root.left)

		# Print all leaf nodes
		printLeaves(root.left)
		printLeaves(root.right)

		# Print the right boundary in bottom-up manner
		printBoundaryRight(root.right)


# Driver program to test above function
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printBoundary(root)

#################################################################################################
## 2nd Solution##
def isLeaf(root):
    return not root.left and not root.right

def addLeftBoundary(root , res):
    cur = root.left
    while cur:
        if not isLeaf(cur):
            res.append(cur.data)
        if cur.left:
            cur = cur.left
        else:
            cur = cur.right


def addRightBoundary(root , res):
    cur = root.right
    tmp = []
    while cur:
        if not isLeaf(cur):
            tmp.append(cur.data)
        if cur.right:
            cur = cur.right
        else:
            cur = cur.left
    tmp = tmp[::-1]
    for i in tmp:
        res.append(i)
    
 

def addLeaves(root  , res):
    if isLeaf(root):
        res.append(root.data)
        return
    if root.left:
        addLeaves(root.left , res)
    if root.right:
        addLeaves(root.right , res)
    
    

   
class Solution:
    def printBoundaryView(self, root):
        # Code here
        ans = []
        if not isLeaf(root):
            ans.append(root.data)
        addLeftBoundary(root , ans)
        addLeaves(root , ans)
        addRightBoundary(root , ans)
        return ans
# Output:

# The Boundary Traversal is : 1 2 3 4 5 6 10 11 9 8 7 

# Time Complexity: O(N).

# Reason: The time complexity will be O(H) + O(H) + O(N) which is ≈ O(N)

# Space Complexity: O(N)

# Reason: Space is needed for the recursion stack while adding leaves. In the worst case (skewed tree), space complexity can be O(N).


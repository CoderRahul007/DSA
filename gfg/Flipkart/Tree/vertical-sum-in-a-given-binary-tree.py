# Python3 program to find Vertical Sum in
# a given Binary Tree

# Node definition
class newNode:
	
	def __init__(self, data):
		
		self.left = None
		self.right = None
		self.data = data
		
# Traverses the tree in in-order form and
# populates a hashMap that contains the
# vertical sum
def verticalSumUtil(root, hd, Map):

	# Base case
	if(root == None):
		return
	
	# Recur for left subtree
	verticalSumUtil(root.left, hd - 1, Map)

	# Add val of current node to
	# map entry of corresponding hd
	if(hd in Map.keys()):
		Map[hd] = Map[hd] + root.data
	else:
		Map[hd] = root.data
		
	# Recur for right subtree
	verticalSumUtil(root.right, hd + 1, Map)
	
# Function to find vertical_sum
def verticalSum(root):

	# a dictionary to store sum of
	# nodes for each horizontal distance
	Map = {}
	
	# Populate the dictionary
	verticalSumUtil(root, 0, Map);

	# Prints the values stored
	# by VerticalSumUtil()
	for i,j in Map.items():
		print(i, "=", j, end = ", ")
	
# Driver Code
if __name__ == "__main__":
	
	'''	 Create the following Binary Tree
			1
			/ \
		2	 3
		/ \	 / \
		4 5 6 7
	'''
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(4)
	root.left.right = newNode(5)
	root.right.left = newNode(6)
	root.right.right = newNode(7)
	
	print("Following are the values of vertical "
		"sums with the positions of the "
		"columns with respect to root")
	
	verticalSum(root)
# O(nlogn)


#################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        

def verticalSum(root, distance):
    
    if root is None:
        return None
        
    try:
        hashMap[distance] = hashMap[distance] + root.data
    except:
        hashMap[distance] = root.data
        
    verticalSum(root.left, distance-1)
    verticalSum(root.right, distance+1)
        
if __name__ == '__main__':
    hashMap = dict()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    response = verticalSum(root, 0)
    
    max = 0
    
    for k, v in hashMap.items():
        print(k, v)
        if v > max:
            max = v
                
    print("Vertical sum: ", max)
	
#######################################
# Using Linked List
# Python program to find vertical sum in a given Binary Tree
# Python3 program of space optimized
# solution to find vertical sum of
# binary tree.

# Tree node structure
class TNode:
	
	def __init__(self, key):
		
		self.key = key
		self.left = None
		self.right = None

# Doubly linked list structure
class LLNode:
	
	def __init__(self, key):
		
		self.key = key
		self.prev = None
		self.next = None

# Function that creates Linked list and store
# vertical sum in it.
def verticalSumDLLUtil(root: TNode,
					sumNode: LLNode) -> None:

	# Update sum of current line by adding
	# value of current tree node.
	sumNode.key = sumNode.key + root.key

	# Recursive call to left subtree.
	if (root.left):
		if (sumNode.prev == None):
			sumNode.prev = LLNode(0)
			sumNode.prev.next = sumNode

		verticalSumDLLUtil(root.left,
						sumNode.prev)

	# Recursive call to right subtree.
	if (root.right):
		if (sumNode.next == None):
			sumNode.next = LLNode(0)
			sumNode.next.prev = sumNode

		verticalSumDLLUtil(root.right,
						sumNode.next)

# Function to print vertical sum of Tree.
# It uses verticalSumDLLUtil() to calculate sum.
def verticalSumDLL(root: TNode) -> None:

	# Create Linked list node for
	# line passing through root.
	sumNode = LLNode(0)

	# Compute vertical sum of different lines.
	verticalSumDLLUtil(root, sumNode)

	# Make doubly linked list pointer point
	# to first node in list.
	while (sumNode.prev != None):
		sumNode = sumNode.prev

	# Print vertical sum of different lines
	# of binary tree.
	while (sumNode != None):
		print(sumNode.key, end = " ")
		sumNode = sumNode.next

# Driver code
if __name__ == "__main__":
	
	'''
				1
				/ \
			/ \
			2	 3
			/ \ / \
			/ \ / \
		4 5 6 7
	'''
	root = TNode(1)
	root.left = TNode(2)
	root.right = TNode(3)
	root.left.left = TNode(4)
	root.left.right = TNode(5)
	root.right.left = TNode(6)
	root.right.right = TNode(7)
	
	print("Vertical Sums are")
	
	verticalSumDLL(root)

################
# We have discussed Hashing Based Solution in Set 1. Hashing based solution requires a Hash Table to be maintained. We know that hashing requires more space than the number of entries in it. In this post, Doubly Linked List based solution is discussed. The solution discussed here requires only n nodes of linked list where n is total number of vertical lines in binary tree. Below is algorithm. 

# verticalSumDLL(root)
# 1)  Create a node of doubly linked list node 
#     with value 0. Let the node be llnode.
# 2)  verticalSumDLL(root, llnode)

# verticalSumDLL(tnode, llnode)
# 1) Add current node's data to its vertical line
#         llnode.data = llnode.data + tnode.data;
# 2) Recursively process left subtree
#     If left child is not empty
#    if (tnode.left != null)
#    {
#       if (llnode.prev == null)
#       {
#           llnode.prev = new LLNode(0);
#           llnode.prev.next = llnode;
#       }
#       verticalSumDLLUtil(tnode.left, llnode.prev);
#    }
# 3)  Recursively process right subtree
#    if (tnode.right != null)
#    {
#       if (llnode.next == null)
#       {
#           llnode.next = new LLNode(0);
#           llnode.next.prev = llnode;
#       }
#       verticalSumDLLUtil(tnode.right, llnode.next);
#    }


# printVerticalNodes
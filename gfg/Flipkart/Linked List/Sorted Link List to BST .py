# Method 1 (Simple) 
# Following is a simple algorithm where we first find the middle node of the list and make it the root of the tree to be constructed. 
 

# 1) Get the Middle of the linked list and make it root.
# 2) Recursively do same for the left half and right half.
#        a) Get the middle of the left half and make it left child of the root
#           created in step 1.
#        b) Get the middle of right half and make it the right child of the
#           root created in step 1.
# Time complexity: O(nLogn) where n is the number of nodes in Linked List.
# Method 2 (Tricky) 
# Method 1 constructs the tree from root to leaves. 
# In this method, we construct from leaves to root.
#  The idea is to insert nodes in BST in the same order as
#  they appear in Linked List so that the tree can be constructed 
# in O(n) time complexity. We first count the number of nodes in the
#  given Linked List. Let the count be n. After counting nodes, 
# we take left n/2 nodes and recursively construct the left subtree.
#  After left subtree is constructed, we allocate memory for root and 
# link the left subtree with root. Finally, we recursively construct the right subtree and link it with root. 
# While constructing the BST, we also keep moving the list head pointer 
# to next so that we have the appropriate pointer in each recursive call.

# https://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/
class Solution:
    def sortedListToBST(self, head):
        #code here
        if head is None:
            return None
        if head.next is None:
            return TNode(head.data)
        fast = head
        slow = head
        prev = LNode(None)
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        
        root = TNode(slow.data)
        prev.next = None # so that it will create a left linked list with last pointing to None
        root.left = self.sortedListToBST(head)
        if slow.next:
            root.right = self.sortedListToBST(slow.next)
        return root

#  O(nLogn) where n is the number of nodes in Linked List.        

# O(n) solution

# Python3 implementation of above approach

# Link list node
class LNode :
	def __init__(self):
		self.data = None
		self.next = None

# A Binary Tree node
class TNode :
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None

head = None

# This function counts the number of
# nodes in Linked List and then calls
# sortedListToBSTRecur() to construct BST
def sortedListToBST():
	global head
	
	# Count the number of nodes in Linked List
	n = countLNodes(head)

	# Construct BST
	return sortedListToBSTRecur(n)

# The main function that constructs
# balanced BST and returns root of it.
# head -. Pointer to pointer to
# head node of linked list n -. No.
# of nodes in Linked List
def sortedListToBSTRecur( n) :
	global head
	
	# Base Case
	if (n <= 0) :
		return None

	# Recursively construct the left subtree
	left = sortedListToBSTRecur( int(n/2))

	# Allocate memory for root, and
	# link the above constructed left
	# subtree with root
	root = newNode((head).data)
	root.left = left

	# Change head pointer of Linked List
	# for parent recursive calls
	head = (head).next

	# Recursively construct the right
	# subtree and link it with root
	# The number of nodes in right subtree
	# is total nodes - nodes in
	# left subtree - 1 (for root) which is n-n/2-1
	root.right = sortedListToBSTRecur( n - int(n/2) - 1)

	return root

# UTILITY FUNCTIONS

# A utility function that returns
# count of nodes in a given Linked List
def countLNodes(head) :

	count = 0
	temp = head
	while(temp != None):
	
		temp = temp.next
		count = count + 1
	
	return count

# Function to insert a node
#at the beginning of the linked list
def push(head, new_data) :

	# allocate node
	new_node = LNode()
	
	# put in the data
	new_node.data = new_data

	# link the old list off the new node
	new_node.next = (head)

	# move the head to point to the new node
	(head) = new_node
	return head


# Function to print nodes in a given linked list
def printList(node):

	while(node != None):
	
		print( node.data ,end= " ")
		node = node.next
	
# Helper function that allocates a new node with the
# given data and None left and right pointers.
def newNode(data) :

	node = TNode()
	node.data = data
	node.left = None
	node.right = None

	return node

# A utility function to
# print preorder traversal of BST
def preOrder( node) :

	if (node == None) :
		return
	print(node.data, end = " " )
	preOrder(node.left)
	preOrder(node.right)

# Driver code

# Start with the empty list
head = None

# Let us create a sorted linked list to test the functions
# Created linked list will be 1.2.3.4.5.6.7
head = push(head, 7)
head = push(head, 6)
head = push(head, 5)
head = push(head, 4)
head = push(head, 3)
head = push(head, 2)
head = push(head, 1)

print("Given Linked List " )
printList(head)

# Convert List to BST
root = sortedListToBST()
print("\nPreOrder Traversal of constructed BST ")
preOrder(root)

# This code is contributed by Arnab Kundu


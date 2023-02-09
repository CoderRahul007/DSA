
# Binary Tree Approach

# The heap property is satisfied by the heap data structure. And follows the properties of a complete binary tree.
#  Heap property is as follows, which we have used all over the approach:-

# Each parent element is smaller than its child elements.

# The complete binary tree, as we all know, is a tree with every level filled and all nodes as far left as feasible. 
# It's possible that the last level of the binary tree is empty and unfilled. 

#  You're probably wondering what the heap property is.

# Every node of the tree is given a key value or weight in the heap data structure.

# Now, the key value of the root node is compared with the values of children's nodes, and then the tree is arranged
#  into two categories, respectively i.e., max Heap or min-heap. This data structure is used as a sorting algorithm to
#  sort the elements in a list and an array. This sorting algorithm can be used in data structures like order statistics, 
# priority queues, Dijkstra's algorithm, or Prim's algo. Heapify refers to creating a heap data structure using a binary tree. 
# To create the Min-Heap, the heapify process is used. For complete binary tree the left child in an array is 2*i+1 and the right
#  child is 2*i+2 if the current node index is ‘i’ in the array. For the index ‘i’ the parent of it is (i-1)/2.

# Now to create min-heap following steps are used:-

# left ( k )

#     Return 2*k+1.

# right ( k )

#     Return 2*k+2.

# parent ( k )

#     Return ( k-1 ) / 2.

# Heapify ( heap, k)

#     Find the left child of the node.
#     Find the right child of the node.
#     Find the smallest element between the current node and its children.
#     Check if the left child is the smallest.
#     Check if the right node is smallest than the previous smallest.
#     If the smallest element is not in the current node.
#     We have to heapify the Heap to take that element to the top.
#         Swap the values of the current node and the smallest node value.
#         Call the heapify function on the smallest value node which now contains the value of the parent node.

# insert( heap, val )

#     Insert a val in the heap.
#     The function contains heap array, val to inserted.
#     Insert the val at the end of the heap.
#     If there is more than 1 node in the Heap.
#     MinHeapify the heap by checking the val at its parent node.
#     Also, do it until the heap property is not satisfied.
#     while( i != 0 and heap[parent(i)] > heap[i]):
#         Swap the value of the current node with its parent.
#         Check the same if the parent element of the current element is satisfying the heap property.
#         i = parent(i)

# extractMin( heap )

#     Check if the current node is the only node in the heap.
#         Return heap[0].
#     Take out the min value and remove it from the heap.
#     Put the last node on the top of the heap. So that we can heapify from the root node till the last children.
#     Decrease the size of heap as the minimum element is removed.
#     Heapify the heap to satisfy the heap property.

# minHeap ( N, Q )

#     Define minHeap function which takes the size of Queries and Queries as Input.
#     Returns an array of outputs depending on the queries.
#     Define a heap array to store elements.
#     Define an array that stores the min elements.
#     For each query in the array Q.
#     If the query is of type 1 then insert the value in the heap.
#     Else take min element from the heap and append it in the ans.
#     Return the ans array.

# Time Complexity

# O( N * log( N )), Where ‘N’ is the number of queries.


#  We are iterating over each query which is ‘N’ and for each insert or 
# remove we do heapify operation where we each time go to child or parent 
# which is at its double or half of the current position respectively and 
# at max, we will go to the height of the tree which is log ( N ).

# Hence the time complexity will be O( N * log( N )).
# Space Complexity

# O( N ), Where ‘N’ is the number of queries.
 

# We are creating a heap array of size ‘N’.

# Hence the space complexity will be O( N ).

"""
    Time complexity: O( N * log( N ) )
    Space complexity: O( N )

    Where N is the size of heap array.
"""


# Python3 implementation of Min Heap

import sys

class MinHeap:

	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.size = 0
		self.Heap = [0]*(self.maxsize + 1)
		self.Heap[0] = -1 * sys.maxsize
		self.FRONT = 1

	# Function to return the position of
	# parent for the node currently
	# at pos
	def parent(self, pos):
		return pos//2

	# Function to return the position of
	# the left child for the node currently
	# at pos
	def leftChild(self, pos):
		return 2 * pos

	# Function to return the position of
	# the right child for the node currently
	# at pos
	def rightChild(self, pos):
		return (2 * pos) + 1

	# Function that returns true if the passed
	# node is a leaf node
	def isLeaf(self, pos):
		return pos*2 > self.size

	# Function to swap two nodes of the heap
	def swap(self, fpos, spos):
		self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

	# Function to heapify the node at pos
	def minHeapify(self, pos):

		# If the node is a non-leaf node and greater
		# than any of its child
		if not self.isLeaf(pos):
			if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
			self.Heap[pos] > self.Heap[self.rightChild(pos)]):

				# Swap with the left child and heapify
				# the left child
				if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
					self.swap(pos, self.leftChild(pos))
					self.minHeapify(self.leftChild(pos))

				# Swap with the right child and heapify
				# the right child
				else:
					self.swap(pos, self.rightChild(pos))
					self.minHeapify(self.rightChild(pos))

	# Function to insert a node into the heap
	def insert(self, element):
		if self.size >= self.maxsize :
			return
		self.size+= 1
		self.Heap[self.size] = element

		current = self.size

		while self.Heap[current] < self.Heap[self.parent(current)]:
			self.swap(current, self.parent(current))
			current = self.parent(current)

	# Function to print the contents of the heap
	def Print(self):
		for i in range(1, (self.size//2)+1):
			print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
								str(self.Heap[2 * i])+" RIGHT CHILD : "+
								str(self.Heap[2 * i + 1]))

	# Function to build the min heap using
	# the minHeapify function
	def minHeap(self):

		for pos in range(self.size//2, 0, -1):
			self.minHeapify(pos)

	# Function to remove and return the minimum
	# element from the heap
	def remove(self):

		popped = self.Heap[self.FRONT]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size-= 1
		self.minHeapify(self.FRONT)
		return popped

# Driver Code
if __name__ == "__main__":
	
	print('The minHeap is ')
	minHeap = MinHeap(15)
	minHeap.insert(5)
	minHeap.insert(3)
	minHeap.insert(17)
	minHeap.insert(10)
	minHeap.insert(84)
	minHeap.insert(19)
	minHeap.insert(6)
	minHeap.insert(22)
	minHeap.insert(9)
	minHeap.minHeap()

	minHeap.Print()
	print("The Min val is " + str(minHeap.remove()))

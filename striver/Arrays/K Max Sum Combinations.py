
# Using Heap

# In this approach, instead of exploring all the possible sum combinations, 
# we will only use the sum-combinations that can be the possible candidates for the ‘K’ max sum combinations. 

 

# The idea is to sort both arrays and insert the possible candidates of max sum combinations 
# into the max-heap. We will also use a set to make sure that we are using a sum-combination 
# only once. Now, we will keep removing the max element(max sum combination) and keep inserting
#  the next possible candidate in the max heap until we get ‘K’ max sum combinations. We will also
#   store the indices corresponding to the value so that we will be able to get the next possible candidate pair. 

 

# The Steps are as follows :

 

# Sort both the arrays/lists, array/list ‘A’ and array/list ‘B’.
# Create a max-heap to store the sum combinations along with the indices of the elements 
# from both arrays/lists ‘A’ and ‘B’ which make up the sum. The max heap is ordered by the
#  sum, the max sum will be the root of the heap.
# Initialize the heap with the maximum possible sum combination i.e ('A[N – 1]' + ‘B[N – 1]’
#  where ‘N’ is the size of array) and with the indices of elements from both the arrays 
# ('N' – 1, 'N' – 1) because this will be maximum sum possible pair sum. The tuple inside 
# the max heap will be ('A[N-1]' + 'B[N – 1]', ('N' – 1, ‘N’ – 1)). The max heap is ordered
#  by the first value i.e sum of both elements.
# Create an array/list ‘result’ of size ‘K’ that will store the ‘K’ max sum combinations.
# We will keep processing the below steps until we do not get ‘K’ sum combinations.
#     Remove the root of the max-heap to get the current largest sum and along with the indices 
# of the element that make up the sum. Let the tuple be (sum, ('i', ‘j’)).
#         Add the ‘sum’ to the output array ‘RESULT’.
#         If the indices ('i' – 1, ‘j’) and ('i', ‘j’ – 1) are valid and not present in the set, 
# insert ('A[i – 1]' + ‘B[j]’, ('i' – 1, ‘j’)) and ('A[i]' + ‘B[j – 1]’,('i', ‘j’ – 1)) into the 
# max heap. This will make sure that the sum combinations are not redundant.
#         Insert the indices ('i' – 1, ‘j’) and ('i', ‘j’ – 1) into the set.
# Finally, return the output array ‘RESULT’.

# Time Complexity

# O(N * log(N)), Where ‘N’ is the number of elements in the array.

 

# Since we are sorting the given arrays/lists which takes O(N * log(N)) time. Then, we are
#  using a max-heap which, in the worst case, can contain ‘N’ elements. The operations on 
# heap will require O(N * log(N)) time. The look-up in the set can be done in log(N) time. 
# Thus, the time complexity will be O(N * log(N)). 
# Space Complexity

# O(N), Where ‘N’ is the number of elements in the given arrays/lists.

 

# Since we are using a max-heap and a set. In the worst case, the total additional space will be O(N). Thus, the space complexity will be O(N).


"""
    Time Complexity: O(N * log(N))
    Space Complexity: O(N)

    Where 'N' is the number of elements the given arrays.
"""

import heapq

def kMaxSumCombination(a, b, n, k):
	# Sorting the arrays.
	a.sort()
	b.sort()
	
	# Using a max-heap.
	maxHeap = []
	heapq.heapify(maxHeap)
	maxHeap.append((-a[n-1] - b[n-1], n - 1, n - 1))
	
	# Using a set.
	mySet = set() 
	mySet.add((n - 1, n - 1))
	
	# Output array to store the K max sum combinations.
	result = []
	
	while(k > 0):
		# Remove the root of the max heap.
		sum, x, y = heapq.heappop(maxHeap)
		# sum, x, y = lst[0], lst[1], lst[2]
		
		# Add the sum to the output array.
		result.append(-sum)
		
		# Check if the indices (x-1, y) are present in the set.
		if((x - 1, y) not in mySet):
			maxHeap.append((-a[x - 1] - b[y], x - 1, y))
			mySet.add((x - 1, y))
		
		# Check if the indices (x, y-1) are present in the set.
		if((x, y - 1) not in mySet):
			maxHeap.append((-a[x] - b[y - 1], x, y - 1))
			mySet.add((x, y - 1))

		heapq.heapify(maxHeap)
		k -= 1
	
	# Return the output array.
	return result
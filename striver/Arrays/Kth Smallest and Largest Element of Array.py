### Using Heap
'''
    Time complexity: O(N + K * logN)
    Space complexity: O(N)

    Where ‘N’ is the size of the given array and K is given integer.
'''

from queue import PriorityQueue


def kthSmallLarge(arr, n, k):
    # Build Min-Heap from the given array.
    minHeap = PriorityQueue()
    for val in arr:
        minHeap.put(val)

    # Pop from Min-Heap exactly K-1 times
    for i in range(1, k):
        x = minHeap.get()

    # Build Max-Heap from the given array.
    maxHeap = PriorityQueue()
    for val in arr:
        # Inserting the val with negative priority because 'maxHeap' is max heap
        maxHeap.put((-val, val))

    # Pop from Max-Heap exactly K-1 times
    for i in range(1, k):
        maxHeap.get()

    result = [minHeap.get(), maxHeap.get()[1]]

    return result

##############################################################################################
# Using Quick Select

# QuickSelect

# Quickselect is a selection algorithm to find the Kth smallest element in an unordered list. 
# It is related to the Quicksort sorting algorithm.  Like Quicksort, In Quickselect we also have a sub-procedure called a partition. 
# In partition algorithm, we select some index as the pivot and in linear time we rearrange the list in such a way, that element at pivot reach to
#  the index where it should be if this list is sorted in ascending order, and all the elements smaller than it should be on its left side and element greater
#  than it should be on its right side.

# Here is an algorithm that performs a partition in a given array ‘Arr’ about the element Arr[pivotIndex] and in the range between ‘left’ and ‘right’

 

#     Initialize a variable ‘pivotValue’ := Arr[pivotIndex].
#     Swap Arr[pivotIndex] with Arr[right].
#     Initialize a variable ‘current’: = left.
#     Run a loop where ‘i’ ranges from left to right-1 and in each iteration do the following.
#         If Arr[i] < ‘pivotValue’ then swap ‘Arr[current]’ with ‘Arr[i]’ and increment ‘current’ by 1.
#     Swap Arr[right] with Arr[current].
#     Return current.

 

# In quicksort, we recursively sort both branches (i.e left and right side of index return by partition),
#  leading to best-case O(n log n) time. However, when doing the selection, we already know which partition our
#  desired element lies in, since the pivot is in its final sorted position, with all those preceding it in an unsorted 
# order and all those following it in an unsorted order. Therefore, a single recursive call locates the desired element 
# in the correct partition, and we build upon this for quickselect. 

# The recursive algorithm for Quickselect using sub-procedure partition is as follows.

 

#     Let define a function quickselect(Arr, left, right, K) where left and right is the leftmost and rightmost index of the window that can have Kth smallest element in the array ‘Arr’.
#     If left == right  return Arr[left].
#     Select a ‘pivotIndex’ between ‘left’ and ‘right’.
#  In order to ensure the linear time complexity of Quickselect,
#  we should choose ‘pivotIndex’ that has a median element of the array, 
# This can be done by using the Median of medians algorithm.  For simplicity here we randomly select pivotIndex.
#     Call sub-procedure partition and assign value return by it to the variable ‘partitionIndex’
#     If ‘partitionIndex’ is greater than or equal to ‘K’  then recursively call this function by assigning ‘right’:= ‘partitionIndex’-1.
#     If ‘partitionIndex’ is smaller than ‘K-1’  then recursively call this function by assigning ‘left’:= ‘partitionIndex’+1.
#     Otherwise return Arr[pivotIndex].

# This problem can be solved using Quickselect as follow -:

 

# Algorithm

#     Create an array ‘result’ of size 2.
#     Find the Kth smallest element of the array ‘Arr’ using Quickselect and assign it to result[0].
#     Find the (N-K+1)th smallest element of the array ‘Arr’ using Quickselect and assign it to result[1].
#     Return ‘result’

# Time Complexity

# O(N), where  ‘N’ is the size of the given array.

 

# Quickselect can be implemented in O(N) time if we always choose median as a pivot. The median divides array elements in two equal halves after partition,  and in the next recursive call we consider only one half. Since partition takes linear time, So for an array of size N quickselect should take time of order.

# N + N/2 + N/4 + N/8 …. = O(N)

# If we randomly select pivot then the worst case occurs when after partitioning ‘pivotIndex’ is always the last index of range. In that case com
# Space Complexity

# O(1)

 

# Quickselect algorithm uses constant space.

'''
    Time complexity: O(N)
    Space complexity: O(1)

    Where ‘N’ is the size of the given array and K is given integer.
'''

import random

# Standard partition process of QuickSort(). 
# It considers the last element as pivot 
# and moves all smaller element to left of 
# it and greater elements to right
def partition(arr, l, r):
      
    x = arr[r]
    i = l
    for j in range(l, r):
          
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
              
    arr[i], arr[r] = arr[r], arr[i]
    return i
def kthSmallest(arr, l, r, k):
  
    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):
  
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)
  
        # if position is same as k
        if (index - l == k - 1):
            return arr[index]
  
        # If position is more, recur 
        # for left subarray 
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)
  
        # Else recur for right subarray 
        return kthSmallest(arr, index + 1, r, 
                            k - index + l - 1)
    print("Index out of bound")
  
# Driver Code
arr = [ 10, 4, 5, 8, 6, 11, 26 ]
n = len(arr)
k = 3
print("K-th smallest element is ", end = "")
print(kthSmallest(arr, 0, n - 1, k))


############################################################################################

def partition(arr, left, right, pivotIndex):
    pivotValue = arr[pivotIndex]

    # Bring pivot element at the end of range.
    arr[right], arr[pivotIndex] = arr[pivotIndex], arr[right]

    current = left

    for i in range(left, right):
        if (arr[i] < pivotValue):

            arr[i], arr[current] = arr[current], arr[i]
            current += 1

    arr[current], arr[right] = arr[right], arr[current]

    return current


def quickSelect(arr, left, right, k):
    if (left == right):
        # Size of array is 1.
        return arr[left]

    # Note we can select Median as pivot to guaranteed O(N) complexity always.
    pivotIndex = left + int(random.random()) % (right-left+1)

    partitionIndex = partition(arr, left, right, pivotIndex)

    if (partitionIndex >= k):
        # Recur for left subarray
        return quickSelect(arr, left, partitionIndex-1, k)

    if (partitionIndex < (k-1)):
        # Recur for right subarray.
        return quickSelect(arr, partitionIndex+1, right, k)

    return arr[partitionIndex]


def kthSmallLarge(arr, n, k):
    result = [0, 0]
    # Kth smallest element
    result[0] = quickSelect(arr, 0, n-1, k)

    # Kth largest element
    result[1] = quickSelect(arr, 0, n-1, n-k+1)

    return result
    

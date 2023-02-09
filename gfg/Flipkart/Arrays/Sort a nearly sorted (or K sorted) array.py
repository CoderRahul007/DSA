# Given an array of n elements, where each element is at most k away from its target position, 
# devise an algorithm that sorts in O(n log k) time. For example,
#  let us consider k is 2, an element at index 7 in the sorted array,
#   can be at indexes 5, 6, 7, 8, 9 in the given array.

# Examples: 

# Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
#             k = 3 
# Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

# Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
#             k = 4
# Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}

from heapq import heappop, heappush, heapify
class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,arr,n,k):
        
        heap = arr[:k + 1]
     
        heapify(heap)
     
        
        target_index = 0
        for i in range(k + 1, n):
            arr[target_index] = heappop(heap)
            heappush(heap, arr[i])
            target_index += 1
     
        while heap:
            arr[target_index] = heappop(heap)
            target_index += 1
        return arr


# We can sort such arrays more efficiently with the help of Heap data structure.
#  Following is the detailed process that uses Heap. 
# 1) Create a Min Heap of size k+1 with first k+1 elements. 
# This will take O(k) time (See this GFact) 
# 2) One by one remove min element from heap, put it in result array, 
# and add a new element to heap from remaining elements.
# Removing an element and adding a new element to min heap will take log k time. 
# So overall complexity will be O(k) + O((n-k) * log(k)).
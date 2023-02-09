'''
    Time Complexity: O((N * K) * log(K)) 
    Space Complexity: O(N * K)

    Where N is the total number of elements in all the arrays, and K is the number of arrays.
'''

# Time Complexity

# O((N * K) * log(K)), Where ‘K’ is the number of arrays and ‘N’ is the average number of elements in every array. 

# We are using the min-heap of size K. Due to the insertion and the removal of elements in the heap, 
# the final complexity of this approach is O(K * N * log(K)).
# Space Complexity

# O(N * K), where ‘K’ is the number of arrays and ‘N’ is the average number of elements in every array.

# Since we are using a min-heap of size K arrays for the average N elements present in every array, 
# therefore, the space complexity of the approach is O(N * K).


import heapq

def mergeKSortedArrays(kArrays, k):
    
    result = []
    
    # Create a min heap to store atmost k heap nodes at a time.
    minHeap = []
    
    for i in range(len(kArrays)):
        
        heapq.heappush( minHeap, (kArrays[i][0], i, 0) )
        
    while len(minHeap) > 0:
        
        # Remove the minimum element from the heap.
        curr = heapq.heappop(minHeap)
        
        # i is the array number and j is the index of the removed element in the ith array.
        i = curr[1]
        j = curr[2]
        
        # Add the removed element to the output array.
        result.append(curr[0])
        
        # If the next element of the extracted element exists, add it to the heap.
        if j + 1 < len(kArrays[i]):
            
            heapq.heappush( minHeap, (kArrays[i][j + 1], i, j + 1) )
    
            
    # Return the output array.        
    return result
        
    

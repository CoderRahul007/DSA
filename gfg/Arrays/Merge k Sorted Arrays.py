from heapq import heappush, heappop
def mergeKArrays(A):
    pq = []
    output = []
    for i in range(len(A)):
        heappush( pq, (A[i][0], i, 0) )
    while len(pq) != 0:
        (a, b, c) = heappop(pq)
        i = b
        j = c
        output.append(a)
        if j + 1 < len(A[i]):
            heappush(pq, (A[i][j + 1], i, j + 1))
    return output


# An efficient solution is to use heap data structure.
#  The time complexity of heap based solution is O(N Log k).  Space O(k)
#  where N is count of all elements

# Create an output array.
# Create a min heap of size k and insert 1st element in all the arrays into the heap
# Repeat following steps while priority queue is not empty.
# Remove minimum element from heap (minimum is always at root) and store it in output array.
# Insert next element from the array from which the element is extracted. If the array doesn’t have any more elements,
#  then do nothing.



from heapq import heappush, heappop , heapify

# https://medium.com/kode-shaft/find-median-from-data-stream-ffbf44c63b22
# code

import math

minHeap = []

heapify(minHeap)

maxHeap=[]

heapify(maxHeap)

def insertHeaps(num):
	heappush(maxHeap, -num)			 ### Pushing negative element to obtain a minHeap for
	heappush(minHeap, -heappop(maxHeap)) ### the negative counterpart

	if len(minHeap) > len(maxHeap):
		heappush(maxHeap,-heappop(minHeap))
	
def getMedian():
	if len(minHeap)!= len(maxHeap):
		return -maxHeap[0]
	else:
		return (minHeap[0]- maxHeap[0])/2


if __name__== '__main__':
	A= [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
	n= len(A)
	for i in range(n):
		insertHeaps(A[i])
		print(math.floor(getMedian()))

class MedianFinder:

    def __init__(self):
        self.heap1 = [] # heap1, a max heap
        self.heap2 = []  # heap2, a min heap

    def addNum(self, num: int) -> None:
        
        if len(self.heap1) == 0:
            heappush(self.heap1, -num)
            return
        
        if len(self.heap1) > len(self.heap2):
            heappush(self.heap1, -num)
            num_poped = -heappop(self.heap1)
            heappush(self.heap2, num_poped)
            return
        
        if len(self.heap1) == len(self.heap2):
            heappush(self.heap2, num)
            num_poped = heappop(self.heap2)
            heappush(self.heap1, -num_poped)
            return

    def findMedian(self) -> float:

        if len(self.heap1) == len(self.heap2):
            left = -1 * self.heap1[0]
            right = self.heap2[0]
            return (left + right) / 2.0
        if len(self.heap1) > len(self.heap2):
            return self.heap1[0] * -1

# The idea is to use a max heap and a min-heap. Max heap is used to store the smaller half of the number and the min-heap is used to store the larger half of the numbers.

# Algorithm

# If the current element to be added is less than the maximum element of the max heap, then add this to the max heap.
# If the difference between the size of the max and min heap becomes greater than 1, the top element of the max heap is removed and added to the min-heap.
# If the current element to be added is greater than the maximum element of the min-heap, then add this to the min-heap.
# If the difference between the size of the max and min heap becomes greater than 1, the top element of the min-heap is removed and added to the max heap.            

# After processing an incoming element, the number of elements in heaps differs utmost by 1 element.
#  When both heaps contain the same number of elements, we pick the average of heaps root data as effective median.
#  When the heaps are not balanced, we select effective median from the root of the heap containing more elements.

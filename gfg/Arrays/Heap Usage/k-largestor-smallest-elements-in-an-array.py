import heapq

# using maxheap
class Solution:
	def kLargest( arr, n, k):
            heapq._heapify_max(arr) # Using Heapify	O(N)
            l = []
            for i in range(k):
                l.append(heapq._heappop_max(arr)) # O(k*log(n))
            return l

# using Minheap      
from heapq import heappush,heappop      

def solve( A, k):
        if(k == len(A)):
            return A
        pq = []
        for i in range(k):
            heappush(pq,A[i])

        for i in range(k,len(A)): # ((n-k)*logk)

            if(A[i]>pq[0]):

                heappop(pq)
                heappush(pq,A[i])
        ans=[]
        while(len(pq)!=0):
            ans.append(pq[0])
            heappop(pq)
        return ans[::-1]

# Fastest        

def solve( arr, k):
    n=len(arr)
    heap=arr[:k]
    heapq.heapify(heap)

    for i in range(k,n): # ((n-k)*logk)
        if heap[0]<arr[i]:
            heapq.heapreplace(heap,arr[i])
            # another way of below operation
            # heappop(heap)
            # heappush(heap,A[i])            
    return heap

# lightest 

def solve( A, k):
        import heapq as hp

        hp.heapify(A)
        for i in range(len(A)-k):
            hp.heappop(A) 
        return A
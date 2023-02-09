# Contributed By
# Mutiur Rehman khan
# |Level 1
# PriorityQueue

# This problem can also be solved using min-heaps where the root element is always the minimum element 
# in the whole tree. As heaps are theoretical data structures, we will use priority_queues which are
#  implemented using heaps only.
# We know that when we add an element to the priority queue, the minimum(or the maximum)  element in 
# the current queue automatically comes at the top (which is called heapify in heaps). We can use this 
# property to efficiently store the numbers as well as return the kth largest number.
# We can initialize the queue with the initial pool of numbers and use the queue as min-heap.
# Initially, as the size of the queue is ‘k’ the top element will be the kth largest element of the pool.
# When reading numbers at runtime i.e reading integers from the stream, we can add the integer to the queue, 
# and if the size of the queue becomes greater than k, we pop the top element from the queue and then return
#  the top element.
# The top element was removed because: let us assume that the added element is greater than equal to the 
# current kth largest element, now we don’t need the current kth largest and any number that is less than 
# the current kth largest number, because the next kth largest will surely be one of the numbers which are 
# greater than the current kth largest.
# If the added element is less than the current kth largest, then this number will surely come at the top 
# of the queue and we don’t need this number as the previous kth largest is still the kth largest number 
# in the current pool.

# Time Complexity

# O(N * log(K)), where ‘N’ is the maximum number of integers we are reading at run time and ‘K’ is the 
# order of the required number in sorted order.

 

# To insert an element into the queue of size N takes logN time, and as per the approach, 
# the maximum size of the queue will be equal to ‘K’.
# Space Complexity

# O(N), where ‘N’ is the maximum number of integers we are reading at run time.

# As priority queue Is being used to store the elements of the array Therefor, overall space complexity will be O(N)

'''
    Time Complexity : O(N * log(K))
    Space Complexity : O(N)

    Where 'N' is the maximum number of integers read at runtime
    and 'K' is the required order of number in sorted order.
'''

from sys import stdin

import heapq

class KthLargest:
        
    def __init__(self,k,arr):
        
        self.size=k
        self.pq = []
        heapq.heapify(self.pq)
        
        for it in arr:
            heapq.heappush(self.pq,it)
            
            if len(self.pq)>self.size:

                '''
                    Remove the top element from the queue
                    as soon as its size becomes greater than k.
                '''
                heapq.heappop(self.pq)
            
    def add(self,num):
        
            heapq.heappush(self.pq,num)
            
            if len(self.pq)>self.size:
                heapq.heappop(self.pq)
    
    def getKthLargest(self):

        ''' 
            The kth largest element will always
            be at the top of the queue.
        '''
        return self.pq[0]
       
# Main.
q,k = map(int,input().split(" "))

arr=list(map(int, stdin.readline().rstrip().split(" ")))

ob=KthLargest(k,arr)

for i in range(q):
    ip = list(map(int, stdin.readline().rstrip().split(" ")))

    # Ip[0] is 1 definitely.
    if len(ip) == 2: 

        # Add the value at ip[1] in the pool and sort it.
        ob.add(ip[1]) 

    # Means ip[0] is 2 definitely.    
    else:

        # Returns/prints the kth largest no.
        print(ob.getKthLargest()) 



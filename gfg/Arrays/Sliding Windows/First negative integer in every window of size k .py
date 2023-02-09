# Given an array A[] of size N and a positive integer K,
#  find the first negative integer for each and every window(contiguous subarray) of size K.

 

# Example 1:

# Input : 
# N = 5
# A[] = {-8, 2, 3, -6, 10}
# K = 2
# Output : 
# -8 0 -6 -6
# Explanation :
# First negative integer for each window of size k
# {-8, 2} = -8
# {2, 3} = 0 (does not contain a negative integer)
# {3, -6} = -6
# {-6, 10} = -6

from queue import Queue

def printFirstNegativeInteger( A, N, K):
    # code here
    ans = [0]* (N-K+1)
    idx = 0
    
    
    q = Queue()
    for i in range(K):
        if A[i] < 0:
            q.put(i)
    
    start = 0
    end = K-1            
    
    while end < N:
        if not q.empty():
            currIndex = q.queue[0]
            ans[idx] = A[currIndex]

            # If first element of window is negative.
            if(start == currIndex):
                # It will not be present in further window.
                q.get()

        # Move window forward.
        start += 1
        end += 1
        idx += 1

        # Insert element in queue, if negative.
        if(end < N and A[end] < 0):
            q.put(end)
    return ans


# If we process every window of length ‘K’ with the help of a sliding window, 
# we can think of this problem as pushing negative elements into a window of length ‘K’ 
# from behind and removing them from the front which is the basic principle of a Queue.
#  Also, before each insertion and deletion, we have to report the front element (first negative) of the window. 

 
# The only difference that we have here is that we also have positive integers in our array.
#  So, while we slide our window of length ‘K’ in our array, we only insert negative elements into our Queue. 
# If the Queue is empty at any point, then we don’t have any negative element in our current window.
# Here, is the complete algorithm:

 

#     Declare an array ‘ANS’ of size (N - K + 1) i.e. total windows in the array, to store our answer.
#     Declare a queue.
#     Insert the negative elements of the first window (starting from index 0) into the queue.
#     Initialize ‘start’ to 0 and ‘end’ to ‘K’-1. These variables represent the start and end indexes of our sliding window.
#     Loop ‘end’ < ‘N’.
#         If the queue is empty, update the first negative for the current window as 0 and continue.
#         Else
#             Initialize ‘currIndex’ to the front element of Queue.
#             Update the first negative element for this window as ARR[currIndex].
#             If ‘start’ == ‘currIndex’, then this element will not be present in further windows, so pop it from the Queue.
#         Increment ‘start’ and ‘end’ by 1.
#         Insert ARR[end] into the Queue, if ARR[end] is negative.
#     Return ‘ANS’.

# Time Complexity

# O(N), where ‘N’ is the size of the array.

# In the worst-case scenario, when every element is negative in the array,
#  each element will get pushed and popped into the Queue at most once. Hence, the complexity is linear.
# Space Complexity

# O(K), where ‘K’ is the length of the window.

# In the worst-case, the size of the Queue will expand at most ‘K’. 
# This happens when there is a subarray of length ‘K’ or more with all negative elements.


def firstNegative(arr, n, k):
    ans = [0] * (n - k + 1)
    idx = 0
    firstNegIndex = 0
    # Traversing for every window's end.
    for end in range(k - 1, n):
        while(firstNegIndex < end and (firstNegIndex <= end - k or arr[firstNegIndex] >= 0)):
            firstNegIndex += 1
        # If we found a negative.
        if(arr[firstNegIndex] < 0):
            ans[idx] = arr[firstNegIndex]
        # Else it's already 0.
        idx += 1
    return ans


# Two Pointers

# The idea here is to use Two pointers, one for the ‘end’ of the window and one 
# for the ‘index’ of the first negative element inside the window.

 

# Here, is the complete algorithm:

 

#     Declare an array ‘ANS’ of size (N - K + 1) i.e. total windows in the array, to store our answer.
#     Initialize ‘firstNegIndex’ to 0 and ‘end’ to K-1.
#     Loop till ‘end’ < N
#         Increment ‘firstNegIndex’ by 1 until we find a negative element or we are out of the window.
#         If there is no negative element in the window. Update 0 in ‘ANS’.
#         Else, Update ARR[firstNegIndex] in ‘ANS’ for the current window.
#     Return ‘ANS’.

# Time Complexity

# O(N), where ‘N’ is the size of the array.

 

# In the worst-case scenario, when every element is negative in the array,
#  each element will get pushed and popped into the Queue at most once. Hence, the complexity is linear.
# Space Complexity

# O(1), i.e. constant space complexity.
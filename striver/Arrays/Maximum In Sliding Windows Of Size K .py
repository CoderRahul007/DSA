# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(k)



from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        res = []
        left = 0
        
        q = deque()
        
        for right in range(n):
            while q and arr[right] > arr[q[-1]]: # For every element, the previous
        # smaller elements are useless
        # so remove them from q
                q.pop()
            q.append(right)
            
            # Remove the elements which are out of this window
            if left > q[0]: # if left index is greater than the max item index
                q.popleft()
            
            if right-left+1 == k:
                res.append(arr[q[0]])
                left+=1
        return res
#######################################################################
# TUF approach
def maxSlidingKWin(arr , k):
    dq = deque()
    ans = []
    for i in range(len(arr)):

        if len(dq) > 0 and dq[0] <= i-k : # remove out of bounds element
            dq.popleft()

        while len(dq) > 0 and arr[dq[-1]] <= arr[i] : # remove smaller element
            dq.pop()

        dq.append(i)
        
        if i >= k-1:    # if window size reach add 
            ans.append(arr[dq[0]])
    return ans
########################################################################
# Another Approach
'''
    Time Complexity = O(N)
    Space Complexity = O(N)

    Where N is the number of elements in the given array/list.
'''

from collections import deque


def slidingWindowMaximum(nums, k):
    n = len(nums)
    result = []

    # Create a Double Ended Queue of capacity K.
    window = deque()

    # For the first window
    for i in range(k):
        # For every element, the previous smaller elements are of no use so remove them from q.
        while len(window) and nums[i] >= nums[window[-1]]:
            window.pop()

        # Add new element at rear of queue.
        window.append(i)

    # For rest of the elements from nums[k] to nums[n-1]
    for i in range(k, n):
        # The element at the front of the queue is the largest element of previous window, so add it to the result.
        result.append(nums[window[0]])

        # Remove the elements which are out of this window
        while len(window) and window[0] <= i - k:
            window.popleft()

        # Remove all elements smaller than the currently being added element.
        while len(window) and nums[i] >= nums[window[-1]]:
            window.pop()

        window.append(i)

    # Add the maximum element of the last window.
    result.append(nums[window[0]])

    # Return the final answer
    return result

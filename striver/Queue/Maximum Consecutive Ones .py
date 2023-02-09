# Problem Statement
# Given a binary array 'ARR' of size 'N', your task is to find the longest sequence of continuous 1’s that can be
#  formed by replacing at-most 'K' zeroes by ones.
#  Return the length of this longest sequence of continuous 1’s.


#######################################################################
#  Queue based approach

# The idea is to iterate the whole array and push the indices having value as zero of the subarray considered in a queue. 
# Keep on iterating the array until the size of the queue is less than ‘K’. When the size of the queue becomes equal to ‘K’,
# update the starting index of the subarray under consideration and pop an element from the queue and push the value of current
#  index in the queue. Check at every step for maximum size.

 

# Algorithm : 

#     Loop over the array and keep a mark of the starting index of the subarray under consideration and take an empty queue.
#     If the value at current index of array is 0, check the size of the queue:
#     a. If the size of the queue is less than ‘K’, push the index.
#     b. Else update the value of the starting index as the next index present at the front of the queue, pop the front value of 
#       the queue and push the current index at the back.
#     At every step update the length of the longest subarray of 1’s found so far, print this value at the end.

# Time Complexity

# O(N), where ‘N’ is the number of elements in the array.

 

# The array is iterated once. So, time complexity will be O(N).
# Space Complexity

# O(K), where ‘K’ is the maximum number of replacements that can be done. 

 

# The maximum size of the queue at any point of time can be ‘K’. Thus, the final space complexity is O(K).
'''
	Time complexity: O(N)
	Space complexity: O(K)

	where 'N' is the total number of elements in the array and 'K' is the maximum number of 
    replacements allowed from 0 to 1.
'''

from collections import deque

def longestSubSeg(arr, n, k):

    # Starting index of array under consideration.
    l = 0
    max_len = 0
    q = deque()
    # To store current size of the queue.
    size = 0

    # r decides current ending point, i.e. the right pointer.
    for r in range(n):
        if (arr[r] == 0):
            q.append(r)
            size += 1

        # Updating queue when its size becomes greater than k.
        if (size > k):
            # Updating starting index of array under consideration.
            l = q.popleft() + 1
            size -= 1

        max_len = max(max_len, r - l + 1)

    return max_len


###########################################################################
# We have to choose longest consecutive sequence of 1s with atmost k zeros 
# (k zeros can be flipped to 1). We can use a sliding window approach for this 
# since the problem is nothing but finding the longest window with atmost k zeros.

# We can maintain two pointers l (left-most window index) and r (right-most window index).
#  We have following possible scenarios -

# nums[r] == 0 : We will try to include this in our window. Here we have two subcases:

# k != 0: We can just include nums[r] in current window and extend it. We will also decrement
#  k denoting a zero has been picked in the current window
# k == 0: Our window already contains maximum zeros (k) allowed. So, we need to shrink our
#  window size from the left till a zero is removed from the other end. Then we can pick nums[r]
#  in our window & extend it. k won't change since we have popped a zero from left and picked one from right.
# nums[r] == 1: We can simply pick this element and extend our window.

# We will keep updating ans to hold the maximum of window size at any point in time and finally return it.

# 1 1 0 0 1 0 0 0 0 0  , k = 3
def longestOnes(self, nums: List[int], k: int) -> int:
	n, ans, l = len(nums), 0, 0
	for r in range(n):
		if nums[r] == 0:                       # try to pick current 0
			if k == 0:                         # if window already picked k zeros, pop 1 from left and pick this
				while nums[l] != 0 : 
                    l += 1
				l += 1 # move away from that left most 0
			else :
                k-= 1                       # otherwise pick it and decrement k
		ans = max(ans, r - l + 1)              # update ans as max window size till now
	return ans

# Another one

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        end = 0
        res = 0
        zero_count = 0
        while end < len(A):
            if A[end] == 1:
                end += 1
                res = max(res, end - start)
            else:
                if zero_count < K:
                    end += 1
                    zero_count += 1
                    res = max(res, end - start)
                else: # zero_count >= K:
                    while start <= end and zero_count >= K:
                        if A[start] == 0:
                            zero_count -= 1
                        start += 1
        return res
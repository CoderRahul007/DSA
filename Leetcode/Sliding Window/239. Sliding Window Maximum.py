# You are given an array of integers nums, there is a sliding window of size k
#  which is moving from the very left of the array to the very right. You can only 
# see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# https://leetcode.com/problems/sliding-window-maximum/solutions/871317/clear-thinking-process-with-picture-brute-force-to-mono-deque-python-java-javascript/?orderBy=most_votes&languageTags=python

# Monotonic deque
# Here we introduce an interesting data structure. It's a deque with an

# interesting property - the elements in the deque from head to tail are in decreasing order (hence the name monotonic).

# To achieve this property, we modify the push operation so that

# Before we push an element into the deque, we first pop everything smaller than it out of the deque.

# This enforces the decreasing order

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque() # stores *indices* # decreasing deque 
        res = []
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur: # everything smaller than cur is popped
                q.pop() # popping from right

            q.append(i)
            # remove first element if it's outside the window
            if q[0] == i - k:
                q.popleft()
            # if window has k elements add to results 
            # (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

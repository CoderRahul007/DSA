# Given an array and an integer K, find the maximum for each 
# and every contiguous subarray of size k.

# Examples : 

# Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3 
# Output: 3 3 4 5 5 5 6
# Explanation: 
# Maximum of 1, 2, 3 is 3
# Maximum of 2, 3, 1 is 3
# Maximum of 3, 1, 4 is 4
# Maximum of 1, 4, 5 is 5
# Maximum of 4, 5, 2 is 5 
# Maximum of 5, 2, 3 is 5
# Maximum of 2, 3, 6 is 6

# Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4 
# Output: 10 10 10 15 15 90 90
# Explanation:
# Maximum of first 4 elements is 10, similarly for next 4 
# elements (i.e from index 1 to 4) is 10, So the sequence 
# generated is 10 10 10 15 15 90 90

#  https://www.youtube.com/watch?v=TCHSXAu5pls

# Number of Subarrays N-K+1

# for brute force Time O(k*(N-k))

from collections import deque


def maxofSubarrays(nums , k):
      # T/S: O(n)
        res, left = [], 0
        q = deque()
        for right in range(len(nums)):
            # pop smaller vals from q to maintain it strictly non-increasing
            while q and nums[right] > nums[q[-1]]:  # if found right index is greater than stored in q then this right will be max so pop from queu
                q.pop()
            q.append(right) 
                       
            if left > q[0]:  # remove first element if it's outside the window
                q.popleft()
                
            # window is size k
            if right - left + 1 == k:
                res.append(nums[q[0]])
                left += 1
        return res

N = 9
K = 3
arr = [1, 2, 3, 1, 4, 5 ,2 ,3 ,6]
print(maxofSubarrays(arr , K))
# https://www.geeksforgeeks.org/find-smallest-range-containing-elements-from-k-lists/

# Given K sorted lists of integers, KSortedArray[] of size N each. 
# The task is to find the smallest range that includes at least one 
# element from each of the K lists. If more than one such range's are found, return the first such range found.

# Example 1:

# Input:
# N = 5, K = 3
# KSortedArray[][] = {{1 3 5 7 9},
#                     {0 2 4 6 8},
#                     {2 3 5 7 11}}
# Output: 1 2
# Explanation: K = 3
# A:[1 3 5 7 9]
# B:[0 2 4 6 8]
# C:[2 3 5 7 11]
# Smallest range is formed by number 1
# present in first list and 2 is present
# in both 2nd and 3rd list.

# Example 2:

# Input:
# N = 4, K = 3
# KSortedArray[][] = {{1 2 3 4},
#                     {5 6 7 8},
#                     {9 10 11 12}}
# Output: 4 9


#####################################################################################################
# Sliding Windows
def smallestRange(self, nums: List[List[int]]) -> List[int]:
        allNums = []
        ht = {}
        for i, nums_ in enumerate(nums):
            ht[i] = 0
            for n in nums_:
                allNums.append((n, i))
        
        allNums.sort(key=lambda x:x[0])
        
        minRange = 1000000
        count = len(nums)
        i = 0
        a = 0
        b = 0
        for j in range(len(allNums)):
            x, y = allNums[j]
            # x is the value
            # y is in the list index
            if ht[y] == 0:
                count -= 1
            ht[y] += 1
            while count == 0:
                x1, y1 = allNums[i]
                if x - x1 < minRange:
                    a, b = x1, x
                    minRange = x - x1
                if ht[y1] == 1:
                    count += 1
                ht[y1] -= 1
                i += 1
            
        return [a, b]    
########################################################################################
from collections import defaultdict
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        d = []
        k = len(nums)
        count = defaultdict(int)
        for i, lst in enumerate(nums):
            for e in lst:
                d.append([e,i])
        d.sort()
        res = []
        left = 0
        for right, e in enumerate(d):
            count[e[1]] += 1
            while len(count) == k:
                if not res or d[right][0]-d[left][0] < res[1]-res[0]:
                    res = [d[left][0],d[right][0]]
                if count[d[left][1]] > 1:
                    count[d[left][1]] -= 1
                    left += 1
                else:
                    break
        return res
###############################################################################################
# Heap Solution
# Efficient approach: The approach remains the same but the time complexity
#  can be reduced by using min-heap or priority queue. Min heap can be used to 
#  find the maximum and minimum value in logarithmic time or log k time instead 
#  of linear time. Rest of the approach remains the same. 

# Algorithm: 
# create a Min heap to store k elements, one from each array and a variable 
# minrange initialized to a maximum value and also keep a variable max to store the maximum integer.
# Initially put the first element of each element from each list and store the maximum value in max.
# Repeat the following steps until at least one list exhausts : 
# To find the minimum value or min, use the top or root of the Min heap which is the minimum element.
# Now update the minrange if current (max-min) is less than minrange.
# remove the top or root element from priority queue and insert the next
#  element from the list which contains the min element and update the max with the new element inserted.


# Complexity Analysis: 
# Time complexity : O(n * k *log k). 
# To find the maximum and minimum in a Min Heap of length k 
# the time required is O(log k), and to traverse all the k arrays
#  of length n (in the worst case), the time complexity is O(n*k), then the total time complexity is O(n * k *log k).
# Space complexity: O(k). 
# The priority queue will store k elements so the space complexity of O(k)

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        maximum = -math.inf
        
        low = -math.inf
        high = math.inf
        
        # insert first value for each list
        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            maximum = max(maximum, arr[0])
            
        while True:
            minimum, i, j = heapq.heappop(heap)
            
            """
            take example lists:
            [1,2,3]
            [4,5,6]
            [7,8,9]
            
            The min heap will be [1,4,7].
            1 is extracted, and the 7 was recorded as the max at the time it's put in.
            4 is naturally included between the current min and current max.
            The answer would temporarily be recorded as [1,7] until a better range is found.
            The final answer for the above example is [3,7] after extracting 1, 2, and 3.
            """
            if high - low > maximum - minimum:
                high = maximum
                low = minimum
                
            # iterate to next item in list
            j += 1
            if j >= len(nums[i]):
                break
            
            # place new item in min heap and record a possible new maximum
            num = nums[i][j]
            heapq.heappush(heap, (num, i, j))
            maximum = max(maximum, num)
                
        return low, high                        
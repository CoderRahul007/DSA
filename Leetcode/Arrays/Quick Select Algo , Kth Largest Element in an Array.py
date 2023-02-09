# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.


# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        priority_queue = nums[:k]

        # this will place the smallest element of the array at zeroth position.
        heapq.heapify(priority_queue)

        for x in nums[k:]:
            # this line will push the element x in the heap which we made
            heapq.heappush(priority_queue, x)

            heapq.heappop(priority_queue)
            # this line will pop the zeroth element from the array.

        return priority_queue[0]

# https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/1019513/python-quickselect-average-o-n-explained/

#############################################################################
# Quick Select recursive


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p + 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
                
        return quickSelect(0, len(nums) - 1)

##################################################################################
# Iterative

# We are going to discuss Quick Select, because it is easier to code:

# First, we need to choose so-called pivot and partition element of nums into 3 parts:
# elements, smaller than pivot, equal to pivot and bigger than pivot.
# (sometimes two groups enough: less and more or equal)
# Next step is to see how many elements we have in each group: if k <= L, where L is size of left,
#  than we can be sure that we need to look into the left part. If k > L + M, where M is size of mid group,
#  than we can be sure, that we need to look into the right part. Finally,
#  if none of these two condition holds, we need to look in the mid part,
#  but because all elements there are equal, we can immedietly return mid[0].
# Complexity: time complexity is O(n) in average, because on each time we reduce
# searching range approximately 2 times. This is not strict proof, for more details
# you can do some googling. Space complexity is O(n) as well.


class Solution:

    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)-1
        k = len(nums)-k
        while l <= r:
            mid = self.randomized_partition(nums, l, r)
            print(mid, k)
            if mid < k:
                l = mid + 1
            elif mid > k:
                r = mid - 1
            else:
                return nums[mid]
        return -1

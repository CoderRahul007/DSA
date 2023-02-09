# Given two integer arrays nums1 and nums2, return an array of their intersection.
#  Each element in the result must appear as many times as it shows in both arrays 
# and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# Two Pointer Method #########################################################################
# TC - n log n
class Solution(object):
    def intersect(self, nums1, nums2):
        n1, n2, res = sorted(nums1), sorted(nums2), []
        p1 = p2 = 0
        while p1 < len(n1) and p2 < len(n2):
            if n1[p1] < n2[p2]:
                p1 += 1
            elif n2[p2] < n1[p1]:
                p2 += 1
            else:
                res.append(n1[p1])
                p1 += 1
                p2 += 1
        return res



###################################################################################
# Dictionary

class Solution(object):
    def intersect(self, nums1, nums2):

        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res
# https://leetcode.com/problems/first-missing-positive/solutions/2154663/4-approaches-brute-force-to-optimized-solutions/?languageTags=python&topicTags=binary-search

from collections import Counter


def firstMissingPositive(self, nums: List[int]) -> int:
    length = len(nums)
    for i in range(1, length+1):
        if i not in nums:
            return i
    return length + 1

# O(N^2)
#######################################################################


def firstMissingPositive(self, nums: List[int]) -> int:
    length = len(nums)
    frequencyDict = Counter(nums)
    for i in range(1, length+2):
        if i not in frequencyDict:
            return i
    return nums[-1] + 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        Hashset = set(nums)
        for i in range(1, len(nums)+1):   
            if i not in Hashset:
                return i
            else:
                continue
        return len(nums) + 1
        
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        val = 1
        while val in nums: 
            val = val + 1
        return val
        
                
# O(N)
# O(N)

####################################################

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i  in range(len(nums)):
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
import collections

class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

######################################################################

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

#######################################################################3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = -1
        c = 0
        for i in range(len(nums)):
            if c == 0:
                major = nums[i]
                c = 1
                continue
            if nums[i] == major:
                c +=1
            else:
                c-=1
        c = 0
        for i in range(len(nums)):
            if nums[i] == major:
                c += 1
        if c > len(nums)//2:
            return major
        return -1
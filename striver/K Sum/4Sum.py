'''

	Time Complexity: O(N^3)
	Space Complexity: O(1)

	Where N is the number of elements in the array.
	
'''

class Solution(object):
  def threeSum(self, nums, target):
    results = []
    nums.sort()
    for i in range(len(nums)-2):
      l = i + 1; r = len(nums) - 1
      t = target - nums[i]
      if i == 0 or nums[i] != nums[i-1]:
        while l < r:
          s = nums[l] + nums[r]
          if s == t:
            results.append([nums[i], nums[l], nums[r]])
            while l < r and nums[l] == nums[l+1]: l += 1
            while l < r and nums[r] == nums[r-1]: r -= 1
            l += 1; r -=1
          elif s < t:
            l += 1
          else:
            r -= 1

    return results

  def fourSum(self, nums, target):
    results = []
    nums.sort()
    for i in range(len(nums)-3):
      if i == 0 or nums[i] != nums[i-1]:
        threeResult = self.threeSum(nums[i+1:], target-nums[i])
        for item in threeResult:
          results.append([nums[i]] + item)
    return results


#################################################################################
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:       
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                # two sum problem solution
                new_target = target - (nums[i] + nums[j])
                start = j+1
                end = n-1
                while end > start:
                    if(nums[start] + nums[end] == new_target):
                        ans.add((nums[i], nums[j], nums[start], nums[end]))
                        end -= 1
                        start += 1
                    elif nums[start] + nums[end] > new_target:
                        end -= 1
                    else:
                        start += 1
        return ans

# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

 

# Example 1:

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# Example 2:

# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1 , earn2 = 0 , 0
        #  e1 e2   currEarn
        # [1 , 2 , 3]
        for i in range(len(nums)):
            currEarn = nums[i] * count[nums[i]] # total profit count of nums * nums
            if i > 0 and nums[i] ==  nums[i-1] + 1: # if previous is nums - 1
                # temp = earn2
                # earn2 = max(currEarn + earn1, earn2) we have to take the maximum , since we cant use both currEarn and earn2 
                                    # earn1 is previous of earn2 and we can add it to currEarn or just have the earn2
                # earn1 = temp
                #include currEarn
                include = currEarn + earn1
                #exclude currEarn
                exclude = earn2
                earn1  , earn2 = earn2  , max( include , exclude)
            else:
                # temp = earn2
                # earn2 = max(currEarn + earn2, earn2)
                # earn1 = temp
                #include currEarn
                include = currEarn + earn2
                #exclude currEarn
                exclude = earn2
                earn1  , earn2 = earn2  , max( include , exclude)
        return earn2

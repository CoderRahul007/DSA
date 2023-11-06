# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.
class Solution:
    def search(self, nums, target):
        l,r=(0,len(nums)-1)
        while l<r:
            mid=l+(r-l)//2
            if nums[mid] == target: # to search if target is mid
                print("returning Mid",mid)
                return mid
            if nums[l]<=nums[mid]: # to check if nums[l:mid] is increasing order
                if nums[l]<=target<nums[mid]: # if target is in nums[l:mid] then right is mid
                    r=mid-1
                    print('1st condition if part- R',r)
                else:
                    l=mid+1 # else left is one highr than mid
                    print('1st condition Else part-L',l)
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                    print('2nd condition if part-L',l)
                else:
                    r=mid-1
                    print('2nd condition else part- R',r)
        return l if l!=len(nums) and nums[l] == target else -1

print(Solution().search([4,5,6,7,0,1,2],4))
print('-----------------------')
print(Solution().search([4,5,6,7,0,1,2],5))
print('-----------------------------')
print(Solution().search([4,5,6,7,0,1,2],6))
print('-----------------------------')
print(Solution().search([4,5,6,7,0,1,2],7))
print('-----------------------------')
print(Solution().search([4,5,6,7,0,1,2],0))
print('-----------------------------')
print(Solution().search([4,5,6,7,0,1,2],1))
print('-----------------------------')
print(Solution().search([4,5,6,7,0,1,2],2))
print('-----------------------------')
print(Solution().search([4,5,6,7,0,1,2],3))
print('-----------------------------')
print(Solution().search([4,5,6,7,0,1,2],9))
print('-----------------------------')
print(Solution().search([4,5,6,7,0,1,2],10))

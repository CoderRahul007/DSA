#  First if the length of list is 1 then because of (2) we return 0.
#   At this point we have at least 2 elements in list. Second, since A[-1] = -inf, 
#   if A[0] > A[1] then we return 0 (A[0] can be counted as peak). Also, since A[len(A)] = -inf if A[-1] > A[-2] 
#   then last element of list is peak. At this point we know that our list has at least three elements and fist element
#    is smaller than the second and the last element is smaller the one previous to it (A[0] < A[1] .......... A[-2] > A[-1], 
#    (3) if you find it difficult to understand this part, imagine, in a coordinate plane that a line starts going up and
#     finishes going down, we know for sure that at some point it should turn down). WLOG we take the middle element and 
#     check if it is peak (if yes, we are done). If it is not peak, then we have either A[mid-1] < A[mid] ...... A[-2] > A[-1] 
#     or A[0]<A[1] .... A[mid-1] > A[mid]
#     both of which are same as (3)
class Solution:
    def findPeakElement(self, nums):
        l=len(nums)
        if l==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return l-1
        left ,right= 0,l-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            else:
                if nums[mid]< nums[mid+1]:
                    left=mid+1
                elif nums[mid] > nums[mid+1]:
                    right=mid-1
# think like in coordiante system we have to find the peak where it starts descend 
print(Solution().findPeakElement([1,2,3,4,5,6,7]))
print('-----------------')
print(Solution().findPeakElement([3,2,4]))
print('-----------------')
print(Solution().findPeakElement([-1,-99]))
print('-----------------')
print(Solution().findPeakElement([0,1]))
print('-----------------')
print(Solution().findPeakElement([7,6,5,4,9,100]))
        
        
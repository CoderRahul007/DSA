# Problem Statement
# You are given an array/list ARR consisting of N integers. Your task is to find all the distinct
#  triplets present in the array which adds up to a given number K.
# An array is said to have a triplet {ARR[i], ARR[j], ARR[k]} with sum = 'K' if there exists
#  three indices i, j and k such that i!=j, j!=k and i!=j and ARR[i] + ARR[j] + ARR[k] = 'K'.
# Note:

# 1. You can return the list of values in any order. For example, if a valid triplet is {1, 2, -3}, 
# then {2, -3, 1}, {-3, 2, 1} etc is also valid triplet. Also, the ordering of different triplets can 
# be random i.e if there are more than one valid triplets, you can return them in any order.
# 2. The elements in the array need not be distinct.
# 3. If no such triplet is present in the array, then return an empty list, and the output printed for 
# such a test case will be "-1".

###############################################################################################################

#  Two pointers

#  Sort the array in non-decreasing order because after the array is sorted, we don’t have to process
#  the same elements multiple times and hence we don’t have to explicitly keep track for distinct triplets.
#  The other advantage of sorting the array is that if we have some value and we require a greater value,
#  we know we have to look in only a single direction.
#     Now since we want triplets such that x + y + z = ‘K’, we have x+ y =  ‘K’ - z and now we can fix z as
#  arr[i]. So we want to find the sum of two numbers x and y as ‘K’ - arr[i] in the array.
#     Let us assume that we are the ith index of the array and initialise variable target to ‘K’ - ‘ARR[i]’.
#     So now we just need to find two elements x, y such that target = x + y.
#     We will use two pointers, one will start from i+1, and the other will start from the end of the array.
#     Let the two pointers be ‘FRONT’ and ‘BACK’, where ‘FRONT’ = i + 1 and ‘BACK’ = n - 1. Let ‘SUM’ = x + y,
#  where x = ‘ARR[FRONT]’ and y = ‘ARR[BACK]’. We have to find the triplets such that ‘TARGET’ = ‘SUM’.
#     While ‘FRONT’ < ‘BACK’, there will be 3 cases:
#         if ('SUM' < ‘TARGET’), we will have to increase the sum and hence increment front pointer as we have 
# sorted the array and to increase the sum, the greater element will always be present after the front index.
#         Else if ('SUM' > ‘TARGET’), we will have to decrease the sum and hence decrease the ‘BACK’ pointer. 
# The reason for this is exactly similar to the above point
#         Else print the triplet and since we want distinct triplets,  do the following.
#             Increment the front pointer until ‘ARR[FRONT]’ = x and ‘FRONT’ < ‘BACK’.
#             Decrement the back pointer until ‘ARR[BACK]’ = y and ‘FRONT’ < ‘BACK’.
#     While ‘ARR[i]’ = ‘ARR[i+1]’, keep on incrementing i, this will automatically ensure that we are only
#  finding distinct triplets.

# Time Complexity

# O(N ^ 2),  where N is the number of elements in the array.


# For every possible candidate for target, we can find if there are valid X and Y in O(N) time. Thus the complexity will be O(N ^ 2).
# Space Complexity

# O(1), as we are using constant extra space.

#####################################################################################################

# Using Hash Set
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)
################################################################################################################
'''

	Time Complexity: O(N^2)
	Space Complexity: O(1)

	Where N is the number of elements in the array.
	
'''

from sys import stdin, stdout, setrecursionlimit

def findTriplets(arr, n, k):
    ans = list()
    # Sorting the arraylist.
    arr = sorted(arr)

    i = 0
    while i < n - 1:
        target = k-arr[i]
        front, back = i + 1, n - 1
        while front < back:
            sum = arr[front] + arr[back]
            # Finding answer which starts from arr[i].
            if sum < target:
                front += 1

            elif sum > target:
                back -= 1

            else:
                x, y = arr[front], arr[back]
                ans.append([arr[i], x, y])
                # Incrementing front pointer until we reach a different number.
                while front < back and arr[front] == x:
                    front += 1
                # Decrementing last pointer until we reach a different number.
                while front < back and arr[back] == y:
                    back -= 1
                    
	# Ensuring that we don't encounter duplicate values for arr[i].
        while i + 1 < n and arr[i] == arr[i + 1]:
            i += 1

        i += 1
    return ans


#######################################################################################################

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []        # Triples
        n = len(nums)   # Length of the list
        nums.sort()     # We need to sort the list first!
        
        for i in range(n-2):
            
            # Since the list is sorted, if nums[i] > 0, then all 
            # nums[j] with j > i are positive as well, and we cannot
            # have three positive numbers sum up to 0. Return immediately.
            if nums[i] > 0:
                break
                
            # The nums[i] == nums[i-1] condition helps us avoid duplicates.
            # E.g., given [-1, -1, 0, 0, 1], when i = 0, we see [-1, 0, 1]
            # works. Now at i = 1, since nums[1] == -1 == nums[0], we avoid
            # this iteration and thus avoid duplicates. The i > 0 condition
            # is to avoid negative index, i.e., when i = 0, nums[i-1] = nums[-1]
            # and you don't want to skip this iteration when nums[0] == nums[-1]
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Classic two pointer solution
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: # sum too small, move left ptr
                    l += 1
                elif s > 0: # sum too large, move right ptr
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # we need to skip elements that are identical to our
                    # current solution, otherwise we would have duplicated triples
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
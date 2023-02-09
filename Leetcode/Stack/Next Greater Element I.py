# The next greater element of some element x in an array is the first greater element
# that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2,
# where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
#  and determine the next greater element of nums2[j] in nums2. If there is no next
#   greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next
# greater element as described above.


# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


#######################################################################################

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res_list = []

        for num1 in nums1:
            for num2 in nums2:
                if num2 == num1:
                    current_index = nums2.index(num2)
                    if current_index == len(nums2) - 1:  # last element
                        res_list.append(-1)
                        break
                    else:
                        for i in range(current_index + 1, len(nums2)):
                            if nums2[i] > num1:
                                res_list.append(nums2[i])
                                break
                            elif i == len(nums2)-1:
                                res_list.append(-1)

        return res_list

# O(n^2)

###########################################################################################


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        dic = {}
        # for inp nums1 = [2,4], nums2 = [1,2,3,4]

        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()  # top = 1 , top = 2 , top = 3
                dic[top] = num  # { 1 : 2  , 2: 3  , 3: 4}
            # stack = [1] , stack = [2] , stack = [3] , stack = [4]
            stack.append(num)

        res = []
        for num in nums1:
            if num in dic.keys():
                res.append(dic[num])
            else:
                res.append(-1)

        return res

# O(n)
# O(n)

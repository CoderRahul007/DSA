##############################################################
# Good Solution


import Find_min_in_rotated_sorted_array


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:  # left subarray
                if nums[0] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            else: # right subarrays
                if nums[mid] < target <= nums[-1]:
                    left = mid+1
                else:
                    right = mid-1
        return -1


#####################################################


def find_element(arr, ele):

    minElement = Find_min_in_rotated_sorted_array.findMin(arr)

    f1 = binary_search(arr, 0, minElement-1, ele)
    f2 = binary_search(arr, minElement + 1, len(arr)-1, ele)

    if f1 != -1:
        return f1
    elif f2 != -1:
        return f2
    else:
        return -1


def binary_search(arr, start, end, ele):
    while start <= end:
        m = start + (end - start) // 2
        if arr[m] == ele:
            return m
        elif arr[m] < ele:
            end = m-1
        else:
            start = m+1
    return -1

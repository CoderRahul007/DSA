# https://algo.monster/problems/min_in_rotated_sorted_array
from typing import List


def findMin(nums):
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r - l)//2
            if nums[m] > nums[r]:  # finding the [ 18 , 17 , 16 , 2 , 3 , 5] finding 18  , 17 , 16
                # biggest element in the array and marking them and moving the l
                l = m+1
            else:
                r = m  # preserving the mid and setting as right dont have to go beyond this since it will be less than that
        return nums[l]
    

#
#######################################################


def find_min_rotated(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2
        # if <= last element, then belongs to lower half
        if arr[mid] <= arr[-1]:  # mid is less than equal to last element
            boundary_index = mid # found first element less than the last element
            right = mid - 1 # no need to go for more
        else:
            # if >= last element, then belongs to  higher half
            left = mid + 1 # [ 18 , 17 , 16 , 2 , 3 , 5] finding 18  , 17 , 16

    return boundary_index


#############################################
# Not Good Algo

def find_min_rotated_sec(arr):
    left, right = 0, len(arr) - 1
    N = len(arr)
    if arr[right] >= arr[0]:  # array sorted
        return arr[0]

    while left <= right:
        mid = left + (right - left) // 2
        next = (mid + 1) % N
        prev = (mid + N - 1) % N
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:  # mid <= prev element
            return arr[mid]
        elif arr[mid] >= arr[0]:
            left = mid + 1
        else:
            right = mid - 1
    return 0

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        # nums1 is exhausted so n-1 elements are there as m+n-1 => m = 0 => n-1
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1        
            
        
        
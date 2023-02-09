def getMedian(A, B, n, m) :
 
    i = 0 
    j = 0 
    m1, m2 = -1, -1
 
    if((m + n) % 2 == 1) :   
        for count in range(((n + m) // 2) + 1) :       
            if(i != n and j != m) :           
                if A[i] > B[j] :
                    m1 = B[j]
                    j += 1
                else :
                    m1 = A[i]
                    i += 1           
            elif(i < n) :           
                m1 = A[i]
                i += 1
          
            # for case when j<m,
            else :           
                m1 = B[j]
                j += 1       
        return m1
     
    else :
        for count in range(((n + m) // 2) + 1) :        
            m2 = m1
            if(i != n and j != m) :       
                if A[i] > B[j] :
                    m1 = B[j]
                    j += 1
                else :
                    m1 = A[i]
                    i += 1           
            elif(i < n) :           
                m1 = A[i]
                i += 1
             
            # for case when j<m,
            else :           
                m1 = B[j]
                j += 1       
        return (m1 + m2)//2

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
    l1 = len(nums1)
    l2 = len(nums2)

    if l1 > l2:
        small = nums2
        large = nums1

    elif l1 <= l2:
        small = nums1
        large = nums2

    sl = len(small)
    hl = len(large)
    l = 0
    h = sl

    while l <= h:

        mx = (l + h) //2
        my = (sl + hl + 1) //2 -mx

        maxleftx = -sys.maxsize if mx == 0 else small[mx-1]
        minrightx = sys.maxsize if mx == sl else small[mx]
        maxlefty = -sys.maxsize if my == 0 else large[my-1]
        minrighty = sys.maxsize if my == hl else large[my]
        
        if maxleftx <= minrighty and maxlefty <= minrightx:
            if (sl + hl) %2 ==0:
                avg = min( minrighty, minrightx ) + max( maxlefty, maxleftx )
                return float(avg/2)
            else:
                return max( maxleftx , maxlefty )

        elif maxlefty > minrightx:
            l = mx + 1
        else:
            h = mx - 1
    return 1.0
        

def findMedianSortedArrays(nums1: List[int], nums2: List[int]):
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
        

    lo, hi = 0, len(nums1) - 1
    while True:
        med1 = (lo + hi) // 2 # searching in shorter array
        med2 = (len(nums1) + len(nums2) + 1) // 2 - med1   # 1 add bcz it plays well with odd and even total len of arr
        
        left1 = -float('inf') if med1 < 0 else nums1[med1]
        right1 = float('inf') if med1 + 1 >= len(nums1) else nums1[med1 + 1]
        left2 = -float('inf') if med2 < 0 else nums2[med2]
        right2 = float('inf') if med2 + 1 >= len(nums2) else nums2[med2 + 1]
        
        if left1 > right2:
            hi = med1 if hi != 0 else med1 - 1
        elif left2 > right1:
            lo = med1 + 1
        else:
            break
    
    if all_len % 2 == 1: # if odd
        return max(left1, left2)
    else: # if even
        return (max(left1, left2) + min(right1, right2)) / 2


# Why do we need that len(nums1) <= len(nums2)? (third line in code)

# if len(nums1) > len(nums2):
#     return self.findMedianSortedArrays(nums2, nums1)

# because if the length of nums1 is greater than the length of nums2,
#  and we go to the left in binary search, it may turn out that the second nums2 doesn't have enough elements to fill left_size, example:

# nums1 = [2, 3, 4, 5, 6, 7, 8]
# nums2 = [1]

# First if left1 > right2? -> 5 > 1? -> Yes! -> hi = med1
# left_size = 4, nums1 median index is 1 (and that's 2 elements in the left part for nums1), 
# but nums2 has only 1 element!!! That is, 2 + 1 = 3, and 3 < 4 (left_size), and here our code breaks. Therefore it is necessary that the first list is less than the second!!!

# Time Complexity - O(log(min(m, n))), Space Complexity - O(1)
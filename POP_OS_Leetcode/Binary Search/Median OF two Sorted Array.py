#  Try every cut in binary search way. Making sure every left part is smaller than the right part and the median is around the parition 
	#  which mean:  When you cut first array at i then you cut second array 
	#  at (m + n + 1)/2-i. Now try to find the i where a[i-1] <= b[j] 
	#  and b[j-1] <= a[i]. So this i is partition around the median.
    # Time: O(log(min(m, n))), Space: O(1)
#     /* https://www.youtube.com/watch?v=LPFhl65R7ww
#       2      4
#       L      R
#     x1 x2| x3 x4 x5 x6    
#     y1 y2  y3 y4 y5 |y6 y7 y8
#            5            3
#     Our Goal: Do the binary search on the combined array such that, each size of the array is the same and Lmax_x <= Rmin_y && Lmax_y <= Rmin_x
#     e.x in this example, Left = 2 + 5 = 7, Right = 4 + 3 = 7
#     x2 <= y6 && y5 <= x3
#     1. partitionX = (lo + hi)/2;
#        partitionY = (x + y + 1)/2 - partitionX;  (x/y:指的是分别俩array的长度)
#     2.Found:Lmax_x <= Rmin_y && Lmax_y <= Rmin_x
#     else if Lmax_x > Rmin_y
#         move towards left in X
#     else move towards right in X
#     3. avg = avg(max(x2,y5), min(x3, y6)) - even len
#        avg = max(x2,y5) - odd len
#     */
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1=len(nums1)
        l2=len(nums2)
        if l1>l2:
            small=nums2
            large=nums1
        elif l1<=l2:
            small=nums1
            large=nums2
        sl=len(small)
        hl=len(large)
        l=0
        h=sl
        while l<=h:
            mx=(l+h)//2
            my=(sl+hl+1)//2 -mx
            maxleftx=-sys.maxsize if mx==0 else small[mx-1]
            minrightx=sys.maxsize if mx==sl else small[mx]
            maxlefty=-sys.maxsize if my==0 else large[my-1]
            minrighty=sys.maxsize if my==hl else large[my]
            
            if maxleftx<= minrighty and maxlefty<=minrightx:
                if (sl+hl)%2==0:
                    avg=min(minrighty,minrightx)+max(maxlefty,maxleftx)
                    return float(avg/2)
                else:
                    return max(maxleftx,maxlefty)
            elif maxlefty>minrightx:
                l=mx+1
            else:
                h=mx-1
        return 1.0
        
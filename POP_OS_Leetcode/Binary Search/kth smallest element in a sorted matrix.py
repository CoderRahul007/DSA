# Given a n x n matrix where each of the rows and columns are sorted in ascending order, 
# find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.

# class Solution:
#     def lessThanM(self,row,m):
#         l=0
#         r=len(row)
#         while l<r:
#             mid=l+(-l+r)//2
#             if row[mid]>m:
#                 r=mid
#             else:
#                 l=mid+1
#         return l
#      def kthSmallest(self, A, k):    
#         l=A[0][0]
#         h=A[-1][-1]
#         while l<h:
#             m=l+(h-l)//2
#             tot=0
#             for row in A:
#                 tot+=self.lessThanM(row,m)
#             if tot >=k:
#                 h=m
#             else:
#                 l=m+1
#         return l
import bisect
class Solution:
    def kthSmallest(self, A, k):    
        l=A[0][0]
        h=A[-1][-1]
        while l<h:
            m=l+(h-l)//2
            tot=0
            for row in A:
                tot+=bisect.bisect_right(row,m)
                print('M',m)
                print(bisect.bisect_right(row,m))
                print('total',tot)
            if tot >=k:
                h=m
            else:
                l=m+1
            print('l',l,'H',h)
        return l
s=Solution()
matrix = [
      [12, 13, 15],
   [ 1,  5,  9],
   [10, 11, 13],
 
]
k = 8
print(s.kthSmallest(matrix,k))
print('------------------------------')
print(s.kthSmallest([[1,2],[1,3]],4))

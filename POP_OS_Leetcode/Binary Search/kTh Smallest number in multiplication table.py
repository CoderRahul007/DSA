# Let's do the binary search for the answer A\text{A}A.

# Say enough(x) is true if and only if there are k\text{k}k or more values in the multiplication table that are 
# less than or equal to x\text{x}x. Colloquially, enough describes whether x\text{x}x is large enough to be the 
# kthk^{th}kth value in the multiplication table.

# Then (for our answer A\text{A}A), whenever \text{x ≥ A}, enough(x) is True; and whenever x < A\text{x < A}x < A,
#  enough(x) is False.

# In our binary search, our loop invariant is enough(hi) = True. At the beginning, enough(m*n) = True,
#  and whenever hi is set, it is set to a value that is "enough" (enough(mi) = True).
#  That means hi will be the lowest such value at the end of our binary search.

# This leaves us with the task of counting how many values are less than or equal to x\text{x}x.
#  For each of m\text{m}m rows, the ithi^{th}ith row looks like [i, 2*i, 3*i, ..., n*i]
# \text{[i, 2*i, 3*i, ..., n*i]}[i, 2*i, 3*i, ..., n*i]. The largest possible \text{k*i ≤ x} 
# that could appear is k = x // i\text{k = x // i}k = x // i. However, if x\text{x}x is really big,
#  then perhaps k > n\text{k > n}k > n, so in total there are
#  min(k, n) = min(x // i, n)\text{min(k, n) = min(x // i, n)}min(k, n) = min(x // i, n) values in that row
#  that are less than or equal to x\text{x}x.

# After we have the count of how many values in the table are less than or equal to x\text{x}x,
#  by the definition of enough(x), we want to know if that count is greater than or equal to k\text{k}k.
# Input: m = 3, n = 3, k = 5
# Output: 
# Explanation: 
# The Multiplication Table:
# 1	2	3 -->n
# 2	4	6
# 3	6	9
# ^
# |
# m
# The 5-th smallest number is 3 (1, 2, 2, 3, 3).
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def search(mid,m,n):
            c=0
            print(1,mid,m,n)
            for i in range(1,m+1):
                print(c)
                c+=min(n,mid//i)
                print(c)
            
            return c
        l=1
        r=m*n
        while l<=r:
            mid=(l+r)//2
            s=search(mid,m,n)
            print('s',s)
            if s<k:
                l=mid+1
            else:
                r=mid-1
        return l

s=Solution()
print(s.findKthNumber(3,3,5))
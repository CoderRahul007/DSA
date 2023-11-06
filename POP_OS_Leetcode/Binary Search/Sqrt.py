class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        h=x
        while l<=h:
            m=(l+h)//2
            sq=m*m
            if sq ==x:
                return m
            elif sq >x:
                h=m-1
            elif sq<x:
                l=m+1
        return (h,l)
# The int result will always be h part of the interval        
print(Solution().mySqrt(97))
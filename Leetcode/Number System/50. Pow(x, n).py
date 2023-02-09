class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1/x
        res = 1.0
        while n != 0:
            if n % 2 != 0:  # at last n will be 1 so res will multiply x
                res *= x
            x *= x
            n = n >> 1
        return res

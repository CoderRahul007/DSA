class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        h = x
        while l <= h:
            m = (l+h)>>1
            sq = m * m
            if sq == x:
                return m
            elif sq > x:
                h = m-1
            else:
                l = m+1
    # If x is not a perfect square, ans won't be returned above, and `lo` will become > than `hi`, and the loop will
    # terminate.
    # In these cases answer will be = `lo-1` = `hi`, because the loop terminated because of two possible cases:
    # Either:
    # `mid_sq < x` (=> mid < sqrt(x)), `lo = mid + 1` executed, and `lo` became > than `hi` => int(sqrt(x)) = lo-1 = hi
    # Or:
    # `mid_sq > x` (=> mid > sqrt(x)), `hi = mid - 1` executed, and `hi` became < than `lo` => int(sqrt(x)) = hi = lo-1
        return lo-1  # or hi
        
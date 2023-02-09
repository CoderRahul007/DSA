class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        p = 0
        for i in range(1 , len(prices)):
            if prices[i] < m:
                m = prices[i]
            p = max( p ,  prices[i] - m)
        return p
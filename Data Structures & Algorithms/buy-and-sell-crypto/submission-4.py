class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        p = prices[0]

        for i in range(0, len(prices)):
            if prices[i] < p:
                p = prices[i]
            
            res = max(res, (prices[i] - p))
        
        return res
            
            
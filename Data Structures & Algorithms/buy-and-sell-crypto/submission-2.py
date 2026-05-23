class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_price = prices[0]

        for i in range(1, len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            
            res = max(res, (prices[i] - buy_price))
        
        return res


        
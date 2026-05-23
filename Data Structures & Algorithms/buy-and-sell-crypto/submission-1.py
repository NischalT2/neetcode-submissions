class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_price = prices[0]

        for i in prices[1:]:
            if buy_price > i:
                buy_price = i
            
            res = max(res, i - buy_price)

        return res

        
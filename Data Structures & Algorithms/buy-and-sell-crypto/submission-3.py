class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        p = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < p:
                p = prices[i]
            else:
                curr_profit = prices[i] - p
                res = max(curr_profit, res)
        
        return res
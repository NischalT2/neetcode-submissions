class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for p in range(1, len(prices)):
            curr_profit = prices[p] - buy
            profit = max(profit, curr_profit)

            if prices[p] < buy:
                buy = prices[p]
        
        return profit
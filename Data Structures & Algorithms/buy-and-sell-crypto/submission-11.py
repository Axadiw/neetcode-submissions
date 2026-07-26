class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        lowest_index = 0
        profit = 0

        for r in range(n):
            profit = max(profit,prices[r] - prices[lowest_index])
            lowest_index = r if prices[r] < prices[lowest_index] else lowest_index

        return profit





        

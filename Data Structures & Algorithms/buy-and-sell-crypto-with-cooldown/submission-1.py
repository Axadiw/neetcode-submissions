class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}
        def dfs(day, buy_date):
            if (day,buy_date) in cache:
                return cache[(day,buy_date)]
            if day >= len(prices):
                return 0
            
            if buy_date >= 0:
                profit = prices[day] - prices[buy_date]
                res = max(dfs(day+1,buy_date), profit + dfs(day+2,-1))
            else:
                res = max(dfs(day+1,buy_date), dfs(day+1,day))
            
            cache[(day,buy_date)] = res
            return res
        
        return dfs(0,-1)
        
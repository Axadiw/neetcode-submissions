class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        def dfs(i, expiration):
            if (i,expiration) in cache:
                return cache[(i, expiration)]
            if i>=len(days):
                return 0
            
            current_day = days[i]
            if expiration > current_day:
                cache[(i, expiration)] = dfs(i+1,expiration)
                return cache[(i, expiration)]
            
            cache[(i, expiration)] = min(costs[0] + dfs(i+1, current_day + 1),
                        costs[1] + dfs(i+1, current_day + 7),
                        costs[2] + dfs(i+1, current_day + 30))
            return cache[(i, expiration)]
        return dfs(0,-1)
        
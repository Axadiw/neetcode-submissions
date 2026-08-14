class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}
        def dfs(remaining, coins_i):
            if (remaining, coins_i) in cache:
                return cache[(remaining, coins_i)]
                
            if remaining < 0:
                cache[(remaining, coins_i)] = 0
                return cache[(remaining, coins_i)]
            if remaining == 0:
                cache[(remaining, coins_i)] = 1
                return cache[(remaining, coins_i)]
            
            ret = 0
            for i in range(coins_i,len(coins)):
                coin = coins[i]
                ret += dfs(remaining-coin, i)

            cache[(remaining, coins_i)] = ret
            return ret
        
        return dfs(amount,0)
        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def helper(i):
            if i in cache:
                return cache[i]

            if i > amount:
                return sys.maxsize
            if i == amount:
                return 0
            
            min_value = sys.maxsize
            for coin in coins:
                min_value = min(min_value,helper(i+coin) + 1)
            
            cache[i] = min_value
            return min_value
            
        ret = helper(0)
        return ret if ret != sys.maxsize else -1
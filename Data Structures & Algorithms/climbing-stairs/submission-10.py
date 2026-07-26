# top down
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(step):
            if step in cache:
                return cache[step]

            if step == 0:                
                cache[step] = 1
                return 1
            if step <= 0:
                cache[step] = 0
                return cache[step]
            
            cache[step] = helper(step - 1) + helper(step - 2)
            return cache[step]
        
        return helper(n)

        
        
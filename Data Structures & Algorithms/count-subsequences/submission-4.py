class Solution:
    def numDistinct(self, s: str, t: str) -> int:      
        cache = {}      
        def dfs(si, ti):
            if (si,ti) in cache:
                return cache[(si,ti)]
            if ti >= len(t):
                cache[(si,ti)] = 1
                return cache[(si,ti)]
            
            if si >= len(s):
                cache[(si,ti)] = 0
                return cache[(si,ti)]

            if s[si] == t[ti]:
                cache[(si,ti)] = dfs(si+1,ti+1) + dfs(si+1,ti)
                return cache[(si,ti)]
            
            cache[(si,ti)] = dfs(si+1, ti)
            return cache[(si,ti)]
        
        return dfs(0,0)
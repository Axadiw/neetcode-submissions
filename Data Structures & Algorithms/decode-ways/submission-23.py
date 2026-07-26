class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1

        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            
            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0

            r1 = dfs(i+1)
            r2 = 0
            if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) < 7)):
                r2 = dfs(i+2)
            cache[i] = r1 + r2
            return cache[i]
        
        return dfs(0)

# 12 # 2
# 226 # 3
# 06 # 0
# 10 # 1
# 27 # 1
# 2101 # 1
# 01 # 0        
        
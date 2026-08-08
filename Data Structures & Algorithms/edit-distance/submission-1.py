class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i1,i2):
            if (i1,i2) in cache:
                return cache[(i1,i2)]
            # print(f"analyzing i1: {i1} i2: {i2}")
            if i1 >= len(word1) or i2 >= len(word2):
                # print(f"reached end")
                cache[(i1,i2)] = abs((len(word1)-i1) - (len(word2)-i2))
                return cache[(i1,i2)]

            if word1[i1] == word2[i2]:
                cache[(i1,i2)] = dfs(i1+1,i2+1)
                return cache[(i1,i2)]
                
            cache[(i1,i2)] = 1 + min(dfs(i1+1,i2+1),dfs(i1,i2+1),dfs(i1+1,i2))
            return cache[(i1,i2)]
        
        return dfs(0,0)

        
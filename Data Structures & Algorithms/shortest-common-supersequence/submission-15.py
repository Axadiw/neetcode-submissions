class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        sys.setrecursionlimit(3000)
        cache = {}
        def dfs(i1,i2):
            if (i1,i2) in cache:
                return cache[(i1,i2)]
            if i1 >= len(str1):
                return len(str2) - i2
                
            if i2 >= len(str2):
                return len(str1) - i1

            if str1[i1] == str2[i2]:
                res = 1 + dfs(i1+1,i2+1)
            else:
                res = 1 + min(dfs(i1+1,i2),dfs(i1,i2+1))
            
            cache[(i1,i2)] = res
            return res
        
        i1 = 0
        i2 = 0
        res = ""
        while i1<len(str1) and i2<len(str2):
            if str1[i1] == str2[i2]:
                res += str1[i1]
                i1+=1
                i2+=1
            elif dfs(i1+1,i2) <= dfs(i1,i2+1):
                res += str1[i1]
                i1 +=1
            else:
                res += str2[i2]
                i2 +=1

        return res + str1[i1:] + str2[i2:]
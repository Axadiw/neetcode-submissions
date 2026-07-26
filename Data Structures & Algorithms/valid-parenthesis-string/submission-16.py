class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        cache = {}
        def dfs(i, counter):
            if (i,counter) in cache:
                return cache[(i,counter)]
            if i ==  n:
                success = counter == 0
                cache[(i,counter)] = success
                return success
            
            if counter < 0:
                cache[(i,counter)] = False
                return False
            
            success = False
            if s[i] == '*':
                if dfs(i+1,counter+1):
                   success = True
                elif dfs(i+1,counter-1):
                   success = True
                elif dfs(i+1,counter):
                   success = True
            else:
                success = dfs(i+1,counter + 1 if s[i] == '(' else counter - 1)
            
            cache[(i,counter)] = success
            return success
            

        return dfs(0,0)
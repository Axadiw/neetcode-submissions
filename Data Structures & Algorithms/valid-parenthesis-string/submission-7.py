class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        cache = {}
        def dfs(i, counter):
            repr = f'{i}_{counter}'
            if repr in cache:
                return cache[repr]
            if i ==  n:
                # print(f"counter: {counter} s[i]: {s[i]}")
                success = counter == 0
                cache[repr] = success
                return success
            
            if counter < 0:
                cache[repr] = False
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
            
            cache[repr] = success
            return success
            

        return dfs(0,0)
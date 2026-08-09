class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        t1 = t2 = t3 = 0
        cache = {}
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(t1,t2):
            t3 = t1+t2
            
            # print(f"analyzing {t1} {t2} {t3}")
            repr = (t1,t2)
            if repr in cache:
                return cache[repr]
            
            if t3 == len(s3): 
                # print(f"True 1")
                cache[repr] = True
                return cache[repr]                               
            
            if t1 < len(s1) and s1[t1] == s3[t3]:                
                if dfs(t1+1,t2):
                    # print(f"True 2")                    
                    cache[repr] = True
                    return cache[repr]
            if t2 < len(s2) and s2[t2] == s3[t3]:                
                if dfs(t1,t2+1):
                    # print(f"True 3")
                    cache[repr] = True
                    return cache[repr]
            if not(t1 < len(s1) and s1[t1] == s3[t3] and t2 < len(s2) and s2[t2] == s3[t3]):
                # print(f"False 4")
                cache[repr] = False
                return cache[repr]
        
            # print(f"False 5")
            # print(f"Sad failure at the end")
            cache[repr] = False
            return cache[repr]

        return dfs(0,0)

        
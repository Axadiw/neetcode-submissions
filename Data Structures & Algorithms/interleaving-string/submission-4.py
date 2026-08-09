class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        t1 = t2 = t3 = 0
        cache = {}
        def dfs(t1,t2,t3):
            # print(f"analyzing {t1} {t2} {t3}")
            repr = (t1,t2,t3)
            if repr in cache:
                return cache[repr]
            if t3 == len(s3):
                # print(f"reached end of s3")
                if t2 == len(s2) and t1 == len(s1):
                    # print(f"reached end of s1 and s2 - success")
                    cache[repr] = True
                    return cache[repr]
                # print(f"not reached end of s1 and s2 - failuje")                    
                cache[repr] = False
                return cache[repr]
            
            if t1 < len(s1):
                if s1[t1] == s3[t3]:
                    # print(f"s1[t1] matches s3[t3] {s1[t1]} == {s3[t3]}")
                    if dfs(t1+1,t2,t3+1):
                        # print(f"Success 1")
                        cache[repr] = True
                        return cache[repr]
            
            
            if t2 < len(s2):
                if s2[t2] == s3[t3]:
                    # print(f"s2[t2] matches s3[t3] {s2[t2]} == {s3[t3]}")
                    if dfs(t1,t2+1,t3+1):
                        # print(f"Success 2")
                        cache[repr] = True
                        return cache[repr]
            
            if t1 < len(s1) and t2 < len(s2):
                if s1[t1] != s3[t3] and s2[t2] != s3[t3]:
                    # print(f"s1[t1] and s2[t2] dont match s3[t3] {s1[t1]} and {s2[t2]} != {s3[t3]}")
                    if dfs(t1+1,t2+1,t3):
                        # print(f"Success 3")
                        cache[repr] = True
                        return cache[repr]
                
            # print(f"Sad failure at the end")
            cache[repr] = False
            return cache[repr]

        return dfs(0,0,0)

        
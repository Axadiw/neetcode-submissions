class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # print(f"n = {n}")
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]            
                
            if i >= n-1:
                return 0
            


            min_val = n
            for j in range(i+1,i+nums[i]+1):
                min_val = min(min_val,1 + dfs(j))
            
            cache[i] = min_val
            return min_val

        
        return dfs(0)
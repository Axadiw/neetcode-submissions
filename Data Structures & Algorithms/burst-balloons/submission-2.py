class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        def dfs(l,r):
            if (l,r) in cache:
                return cache[(l,r)]
            if l + 1 >= r:
                return 0
            
            ret_val = 0
            for i in range(l + 1, r):
                a = nums[l] * nums[i] * nums[r]
                ret_val = max(ret_val, a + dfs(l, i) + dfs(i, r))
            cache[(l,r)] = ret_val
            return ret_val

        return dfs(0, len(nums) - 1)
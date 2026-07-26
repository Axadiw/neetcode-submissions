class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = [0] * (len(nums)+1)
        for i in range(len(cache)):
            cache[i] = {}
        def helper(i, curr):
            if curr in cache[i]:
                return cache[i][curr]
            if i == len(nums):
                return 1 if curr == target else 0 
            
            cache[i][curr] = helper(i+1,curr+nums[i]) + helper(i+1,curr-nums[i])
            return cache[i][curr]
            

        return helper(0,0)
        
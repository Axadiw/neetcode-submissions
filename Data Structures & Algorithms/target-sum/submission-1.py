class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def helper(i, curr):
            if i == len(nums):
                # print(curr)
                return 1 if curr == target else 0 
            
            val = helper(i+1,curr+nums[i]) + helper(i+1,curr-nums[i])
            return val
            

        return helper(0,0)
        
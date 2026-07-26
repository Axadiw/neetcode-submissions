class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0],nums[1])

        i = 2
        while i<len(nums):
            res[i] = max(nums[i]+res[i-2], res[i-1])
            i+=1
        return res[-1]
        
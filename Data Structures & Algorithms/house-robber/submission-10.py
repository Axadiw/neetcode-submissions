class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        cache = {}
        rev = nums.reverse()
        def helper(i,n):
            if i < 2:
                return n[i]
            
            if i in cache:
                return cache[i]

            cache[i] = max(helper(i-1,n), helper(i-2,n)+n[i])
            return cache[i]
        
        return max(helper(len(nums)-1,nums),helper(len(nums)-1, rev))
        